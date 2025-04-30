import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        prog="year_crossover_analytics",
        description="Year Crossover Analytics — detect and report cross-year trades"
    )
    parser.add_argument("--max-threads", type=int, default=4,
                        help="Maximum concurrent worker threads")
    return parser.parse_args()
