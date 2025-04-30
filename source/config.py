import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(
        prog="year_crossover_analytics",
        description="Analyze trades that cross over calendar years"
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging"
    )

    parser.add_argument(
        "--max-threads",
        type=int,
        default=4,
        help="Maximum number of worker threads"
    )

    return parser.parse_args()
