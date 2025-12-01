import argparse
import importlib
import sys
from datetime import datetime
from .config import config
from .client import client
from .storage import storage

def get_solver_module(year: int, day: int):
    # Try year-specific module first
    try:
        return importlib.import_module(f"aoc_agent.days.y{year}.day_{day:02d}")
    except ImportError:
        pass
        
    # Fallback to legacy flat structure
    try:
        return importlib.import_module(f"aoc_agent.days.day_{day:02d}")
    except ImportError:
        return None

def cmd_solve(args):
    year = args.year
    day = args.day
    
    # 1. Get Input
    input_data = storage.load_input(year, day)
    if not input_data:
        print(f"Input for Day {day} {year} not found in cache. Downloading...")
        config.validate()
        if config.session_cookie:
            try:
                input_data = client.get_input(year, day)
                storage.save_input(year, day, input_data)
                print("Input downloaded and cached.")
            except Exception as e:
                print(f"Failed to download input: {e}")
                return
        else:
            print("Cannot download input without session cookie.")
            return

    # 2. Load Solver
    module = get_solver_module(year, day)
    if not module:
        print(f"No solver found for Day {day} {year}")
        return
    
    if not hasattr(module, "DaySolver"):
        print(f"Module aoc_agent.days.day_{day:02d} does not have a DaySolver class.")
        return

    # 3. Solve
    solver = module.DaySolver(input_data)
    solver.solve()

def cmd_fetch(args):
    year = args.year
    day = args.day
    
    print(f"Fetching data for Day {day} {year}...")
    config.validate()
    if not config.session_cookie:
        print("Error: AOC_SESSION not set.")
        return

    try:
        # Fetch Input
        if not storage.load_input(year, day):
            data = client.get_input(year, day)
            storage.save_input(year, day, data)
            print("Input downloaded.")
        else:
            print("Input already cached.")

        # Fetch Problem
        if not storage.load_problem(year, day):
            data = client.get_problem(year, day)
            storage.save_problem(year, day, data)
            print("Problem description downloaded.")
        else:
            print("Problem description already cached.")

    except Exception as e:
        print(f"Error fetching data: {e}")

def main():
    parser = argparse.ArgumentParser(description="Advent of Code Agent")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Solve Command
    solve_parser = subparsers.add_parser("solve", help="Run solution for a specific day")
    solve_parser.add_argument("--day", "-d", type=int, required=True, help="Day number (1-25)")
    solve_parser.add_argument("--year", "-y", type=int, default=datetime.now().year, help="Year (default: current year)")
    solve_parser.set_defaults(func=cmd_solve)

    # Fetch Command
    fetch_parser = subparsers.add_parser("fetch", help="Download input and problem description")
    fetch_parser.add_argument("--day", "-d", type=int, required=True, help="Day number (1-25)")
    fetch_parser.add_argument("--year", "-y", type=int, default=datetime.now().year, help="Year (default: current year)")
    fetch_parser.set_defaults(func=cmd_fetch)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
