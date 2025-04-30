import time
from pathlib import Path
from typing import Optional

import pandas as pd

from source.core.features.mt5_report import Mt5Report
from source.core.models.worker_signals import WorkerSignals


class Analyzer:
    def __init__(self, signals: WorkerSignals, base_path: Path, result_path: Path):
        self.signals = signals
        self.base_path = base_path
        self.result_path = result_path
        self.data_path = base_path / 'DataBase (don\'t change)'

        self.mt5 = Mt5Report()

    def process(self, report_path: Path, connect_path: Optional[Path] = None):
        self.signals.log.emit(f"🔍 Processing report: {report_path.name}")
        if connect_path:
            self.signals.log.emit(f"🔗 Using connection data: {connect_path.name}")

        for p in self._main_progression(report_path, connect_path):
            self.signals.progress.emit(p)

    def _main_progression(self, report_path: Path, connect_path: Optional[Path] = None):
        total_steps = 5
        self.signals.log.emit('☑️ Read details in the report file')
        details = self.mt5.get_symbol_name(report_path)
        symbol = details['symbol'].split('-', 1)[0]
        yield 1 / total_steps * 100

        self.signals.log.emit('☑️ Read data from report file')
        data = self._load_excel_data(symbol)
        self.mt5.set_contract_size(data['contract_size'])
        yield 2 / total_steps * 100

        self.signals.log.emit('✅ Merging Orders and Deals in Report file')
        self.signals.sub_format.emit(f"Detect Trades %p%")
        report, _ = self.mt5.get_file_via_path_with_gui(report_path, connect_path, self.signals.sub_progress)
        yield 3 / total_steps * 100

        self.signals.log.emit('☑️ Starting trade analysis')
        result = self._analyze_data(report)
        yield 4 / total_steps * 100

        self.signals.log.emit('☑️ Store Results in file')
        if len(result) != 0:
            self._save_to_excel(result, symbol)
        yield 5 / total_steps * 100

    def _load_excel_data(self, symbol: str) -> dict:
        df = pd.read_excel(self.data_path / 'DataBase for margin and commision.xlsx')
        for _, row in df.iterrows():
            if row['symbol'] == symbol:
                return {
                    'margin': row['Margin for 1 LOT(usd)'],
                    'contract_size': row['Contract Size'],
                    'commission': row['Commision for 1 Lot for in/out loop (usd)'],
                    'risk': row['Risk Free Rate'],
                    'point': row['Point'],
                }
        raise RuntimeError(f'❌ No margin or commission data found for symbol: {symbol}')

    def _analyze_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df['OpenYear'] = df['OpenTime'].dt.year
        df['CloseYear'] = df['CloseTime'].dt.year

        # Combine open and close events with year
        open_events = df[['OpenTime']].copy()
        open_events['Year'] = open_events['OpenTime'].dt.year
        open_events['Timestamp'] = open_events['OpenTime']

        close_events = df[['CloseTime']].copy()
        close_events['Year'] = close_events['CloseTime'].dt.year
        close_events['Timestamp'] = close_events['CloseTime']

        events = pd.concat([open_events[['Year', 'Timestamp']], close_events[['Year', 'Timestamp']]])
        first_event_per_year = (
            events.groupby('Year')['Timestamp']
            .min()
            .reset_index()
            .rename(columns={'Year': 'CloseYear', 'Timestamp': 'YearBoundary'})
        )

        # Merge boundary into main DataFrame by CloseYear
        df = df.merge(first_event_per_year, on='CloseYear', how='left')

        # Filter: Opened in previous year, closed before year's first activity
        flagged = df[(df['OpenYear'] < df['CloseYear']) & (df['CloseTime'] > df['YearBoundary'])].copy()

        if flagged.empty:
            self.signals.log.emit("✅ No cross-year anomalies detected.")
        else:
            self.signals.log.emit(
                f"⚠️ Detected {len(flagged)} cross-year violations based on earliest yearly activity.")

        return flagged

    def _save_to_excel(self, result: pd.DataFrame, symbol: str):
        for col in ['OpenTime', 'CloseTime', 'YearBoundary']:
            if col in result.columns:
                result[col] = pd.to_datetime(result[col], errors='coerce').dt.strftime('%Y.%m.%d %H:%M:%S')
        output_path = self.result_path / f"{symbol}_CrossYear_{len(result)}Records_{int(time.time())}.csv"
        result.to_csv(output_path, index=False)
        self.signals.log.emit(f"📁 Result saved to: {output_path}")
