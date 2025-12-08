from solvers.days.y2025.day_09 import Day09Solver
from solvers.storage import storage

try:
    data = storage.load_input(2025, 9)
    solver = Day09Solver(data)
    coords = solver.coordinates
    
    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]
    
    print(f"Count: {len(coords)}")
    print(f"X Range: {min(xs)} - {max(xs)}")
    print(f"Y Range: {min(ys)} - {max(ys)}")
    
except Exception as e:
    print(f"Error: {e}")
