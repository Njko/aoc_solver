from solvers.client import client
from solvers.storage import storage
import sys

year = 2018
day = 2

try:
    print(f"Fetching problem for {year} Day {day}...")
    html = client.get_problem(year, day)
    storage.save_problem(year, day, html)
    print("Problem saved.")

    print(f"Fetching input for {year} Day {day}...")
    input_data = client.get_input(year, day)
    storage.save_input(year, day, input_data)
    print("Input saved.")
except Exception as e:
    print(f"Error: {e}")
