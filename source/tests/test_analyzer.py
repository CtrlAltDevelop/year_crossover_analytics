import pandas as pd
from ..core.analyzer import Analyzer


def make_csv(path, rows):
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)


def test_cross_year_detection(tmp_path):
    # Create two small CSVs
    rows1 = [
        {'ticket': 'A', 'time_open': '2023-12-31 23:50', 'time_close': '2024-01-01 00:10', 'profit': 10},
    ]
    file1 = tmp_path / "r1.csv"; make_csv(file1, rows1)
    file2 = tmp_path / "r2.csv"; make_csv(file2, [])

    analyzer = Analyzer(str(file1), str(file2))
    report = list(analyzer.process())
    # Last message should flag trade A
    assert any("FLAG" in msg for _, _, msg in report)
