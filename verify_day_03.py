from solvers.days.y2017.day_03 import Day03Solver

def test_day03():
    # Part 1 Examples
    examples_p1 = [
        ("1", 0),
        ("12", 3),
        ("23", 2),
        ("1024", 31)
    ]
    
    for inp, expected in examples_p1:
        solver = Day03Solver(inp)
        result = solver.part1()
        print(f"Part 1 Input: {inp}, Expected: {expected}, Got: {result}")
        assert result == expected, f"Part 1 Failed for {inp}"

    # Part 2 Examples (Manual check based on sequence)
    # 1, 1, 2, 4, 5, 10, 11, 23, 25...
    examples_p2 = [
        ("1", 2),
        ("2", 4),
        ("4", 5),
        ("5", 10)
    ]
    
    for inp, expected in examples_p2:
        solver = Day03Solver(inp)
        result = solver.part2()
        print(f"Part 2 Input: {inp}, Expected: {expected}, Got: {result}")
        assert result == expected, f"Part 2 Failed for {inp}"

if __name__ == "__main__":
    test_day03()
    
    # Run on real input
    from solvers.storage import storage
    try:
        real_input = storage.load_input(2017, 3)
        solver = Day03Solver(real_input)
        print(f"Real Part 1 Result: {solver.part1()}")
        print(f"Real Part 2 Result: {solver.part2()}")
    except Exception as e:
        print(f"Could not run on real input: {e}")
