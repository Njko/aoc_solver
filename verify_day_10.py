from solvers.days.y2025.day_10 import Day10Solver
from solvers.storage import storage

def test_part1():
    example = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
    
    solver = Day10Solver(example)
    result = solver.part1()
    print(f"Example Part 1 Result: {result}")
    assert result == 7, f"Expected 7, got {result}"

def test_part2():
    example = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
    
    solver = Day10Solver(example)
    result = solver.part2()
    print(f"Example Part 2 Result: {result}")
    assert result == 33, f"Expected 33, got {result}"

if __name__ == "__main__":
    test_part1()
    test_part2()
    
    # Load real input
    try:
        real_input = storage.load_input(2025, 10)
        solver = Day10Solver(real_input)
        print(f"Real Part 1 Result: {solver.part1()}")
        print(f"Real Part 2 Result: {solver.part2()}")
    except Exception as e:
        print(f"Could not run on real input: {e}")
