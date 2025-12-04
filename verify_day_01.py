from solvers.days.y2018.day_01 import Day01Solver

def test_part1():
    examples = [
        ("+1\n-2\n+3\n+1", 3),
        ("+1\n+1\n+1", 3),
        ("+1\n+1\n-2", 0),
        ("-1\n-2\n-3", -6)
    ]
    
    for inp, expected in examples:
        solver = Day01Solver(inp)
        result = solver.part1()
        print(f"Input: {inp.replace(chr(10), ', ')}, Expected: {expected}, Got: {result}")
        assert result == expected, f"Failed for {inp}"

    
    examples_part2 = [
        ("+1\n-1", 0),
        ("+3\n+3\n+4\n-2\n-4", 10),
        ("-6\n+3\n+8\n+5\n-6", 5),
        ("+7\n+7\n-2\n-7\n-4", 14)
    ]
    
    for inp, expected in examples_part2:
        solver = Day01Solver(inp)
        result = solver.part2()
        print(f"Part 2 Input: {inp.replace(chr(10), ', ')}, Expected: {expected}, Got: {result}")
        assert result == expected, f"Part 2 Failed for {inp}"

if __name__ == "__main__":
    test_part1()
    
    # Run on real input
    from solvers.storage import storage
    try:
        real_input = storage.load_input(2018, 1)
        solver = Day01Solver(real_input)
        print(f"Real Part 1 Result: {solver.part1()}")
        print(f"Real Part 2 Result: {solver.part2()}")
    except Exception as e:
        print(f"Could not run on real input: {e}")
