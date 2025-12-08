from solvers.days.y2025.day_06 import Day06Solver

def test_part1():
    example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    solver = Day06Solver(example)
    result = solver.part1()
    print(f"Example Part 1 Result: {result}")
    assert result == 4277556, f"Expected 4277556, got {result}"

    result_p2 = solver.part2()
    print(f"Example Part 2 Result: {result_p2}")
    assert result_p2 == 3263827, f"Expected 3263827, got {result_p2}"

if __name__ == "__main__":
    test_part1()
    
    # Run on real input
    from solvers.storage import storage
    try:
        real_input = storage.load_input(2025, 6)
        solver = Day06Solver(real_input)
        print(f"Real Part 1 Result: {solver.part1()}")
        print(f"Real Part 2 Result: {solver.part2()}")
    except Exception as e:
        print(f"Could not run on real input: {e}")
