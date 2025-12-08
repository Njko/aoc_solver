from solvers.days.y2025.day_05 import Day05Solver

def test_part1():
    example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    solver = Day05Solver(example)
    result = solver.part1()
    print(f"Example Part 1 Result: {result}")
    assert result == 3, f"Expected 3, got {result}"

    # Part 2
    result_p2 = solver.part2()
    print(f"Example Part 2 Result: {result_p2}")
    assert result_p2 == 14, f"Expected 14, got {result_p2}"

if __name__ == "__main__":
    test_part1()
    
    # Run on real input
    from solvers.storage import storage
    try:
        real_input = storage.load_input(2025, 5)
        solver = Day05Solver(real_input)
        print(f"Real Part 1 Result: {solver.part1()}")
        print(f"Real Part 2 Result: {solver.part2()}")
    except Exception as e:
        print(f"Could not run on real input: {e}")
