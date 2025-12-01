import argparse
from .config import config
from .client import client
from .storage import storage

def fetch_year(year):
    print(f"Fetching all inputs for year {year}...")
    config.validate()
    if not config.session_cookie:
        print("Error: AOC_SESSION environment variable not set.")
        print("Please set it to your Advent of Code session cookie to download inputs.")
        return

    for day in range(1, 26):
        print(f"Checking Day {day:02d}...")
        if not storage.load_input(year, day):
            try:
                print("  -> Input not found in cache. Downloading...")
                input_data = client.get_input(year, day)
                storage.save_input(year, day, input_data)
                print(f"  -> Input for Day {day:02d} downloaded and cached.")
            except Exception as e:
                print(f"  -> Failed to download input for Day {day:02d}: {e}")
        else:
            print(f"  -> Input for Day {day:02d} already in cache.")

def main():
    parser = argparse.ArgumentParser(description="Fetch all puzzle inputs for a specific year.")
    parser.add_argument("year", type=int, help="The year to fetch inputs for.")
    args = parser.parse_args()
    
    fetch_year(args.year)

if __name__ == "__main__":
    main()
