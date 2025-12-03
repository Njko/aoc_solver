from solvers.days.y2025.day_04 import Day04Solver

def test_part1():
    example_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    
    solver = Day04Solver(example_input)
    result = solver.part1()
    print(f"Example Part 1 Result: {result}")
    assert result == 13, f"Expected 13, got {result}"

    
    # Part 2 Example
    solver = Day04Solver(example_input)
    result_part2 = solver.part2()
    print(f"Example Part 2 Result: {result_part2}")
    assert result_part2 == 43, f"Expected 43, got {result_part2}"

if __name__ == "__main__":
    test_part1()
    
    # Run on real input
    from solvers.storage import storage
    try:
        real_input = storage.load_input(2025, 4)
        solver = Day04Solver(real_input)
        print(f"Real Part 1 Result: {solver.part1()}")
        print(f"Real Part 2 Result: {solver.part2()}")
    except Exception as e:
        print(f"Could not run on real input: {e}")
