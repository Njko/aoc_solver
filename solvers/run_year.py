import argparse
import importlib
import time
from .storage import storage

def run_year(year):
    print(f"--- Running Solvers for Year {year} ---")
    for day in range(1, 26):
        try:
            # Dynamically import the solver module for the given day
            module_name = f"solvers.days.y{year}.day_{day:02d}"
            solver_module = importlib.import_module(module_name)

            # Get the solver class from the module
            solver_class = getattr(solver_module, f"Day{day:02d}Solver")

            # Load the input for the day
            input_data = storage.load_input(year, day)
            if not input_data:
                print(f"\n--- Day {day:02d} ---")
                print("Input not found. Skipping.")
                continue

            # Instantiate the solver and run the solutions
            solver = solver_class(input_data)

            print(f"\n--- Day {day:02d} ---")
            
            # Solve Part 1
            start_time = time.perf_counter()
            part1_result = solver.part1()
            part1_time = (time.perf_counter() - start_time) * 1000
            print(f"Part 1: {part1_result} ({part1_time:.2f} ms)")

            # Solve Part 2
            start_time = time.perf_counter()
            part2_result = solver.part2()
            part2_time = (time.perf_counter() - start_time) * 1000
            print(f"Part 2: {part2_result} ({part2_time:.2f} ms)")

        except ImportError:
            # This will catch days that don't have a solver file
            pass # Silently ignore missing days
        except Exception as e:
            print(f"\n--- Day {day:02d} ---")
            print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Run all solvers for a specific year.")
    parser.add_argument("year", type=int, help="The year to run.")
    args = parser.parse_args()
    
    run_year(args.year)

if __name__ == "__main__":
    main()
