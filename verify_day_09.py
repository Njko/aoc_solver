from solvers.days.y2025.day_09 import Day09Solver
from solvers.storage import storage

def test_part1():
    example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
    
    solver = Day09Solver(example)
    result = solver.part1()
    print(f"Example Part 1 Result: {result}")
    assert result == 50, f"Expected 50, got {result}"

def test_part2():
    example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
    
    solver = Day09Solver(example)
    result = solver.part2()
    print(f"Example Part 2 Result: {result}")
    assert result == 24, f"Expected 24, got {result}"

if __name__ == "__main__":
    test_part1()
    test_part2()
    
    # Load real input
    try:
        real_input = storage.load_input(2025, 9)
        solver = Day09Solver(real_input)
        print(f"Real Part 1 Result: {solver.part1()}")
        print(f"Real Part 2 Result: {solver.part2()}")
    except Exception as e:
        print(f"Could not run on real input: {e}")
