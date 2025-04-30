import pandas as pd
from datetime import datetime

class Analyzer:
    def __init__(self, file1: str, file2: str):
        self.file1 = file1
        self.file2 = file2

    def process(self):
        # Phase 1: Read file1
        df1 = pd.read_csv(self.file1)
        n1 = len(df1)
        for i in range(n1):
            phase = int((i / n1) * 33)
            inner = int((i / n1) * 100)
            yield phase, inner, f"Reading file1: {i+1}/{n1}"

        # Phase 2: Read file2
        df2 = pd.read_csv(self.file2)
        n2 = len(df2)
        for i in range(n2):
            phase = 34 + int((i / n2) * 32)
            inner = int((i / n2) * 100)
            yield phase, inner, f"Reading file2: {i+1}/{n2}"

        # Combine and convert
        df = pd.concat([df1, df2], ignore_index=True)
        df['time_open']  = pd.to_datetime(df['time_open'])
        df['time_close'] = pd.to_datetime(df['time_close'])
        df['year_open']  = df['time_open'].dt.year
        df['year_close'] = df['time_close'].dt.year
        cross = df[df['year_open'] != df['year_close']]

        # Phase 3: Analyze
        total = len(cross)
        for idx, (ticket, grp) in enumerate(cross.groupby('ticket')):
            inner = int((idx / total) * 100)
            phase = 67 + int(inner * 0.33)  # scale 0–100 → 67–100
            # Check first close
            first_close = grp['time_close'].min()
            boundary = datetime(grp['year_close'].iloc[0], 1, 1)
            valid = first_close >= boundary
            profit = grp['profit'].sum()
            msg = (f"Ticket {ticket}: first close {first_close.date()} "
                   f"{'OK' if valid else 'FLAG'} (profit {profit:.2f})")
            yield min(phase, 100), inner, msg
