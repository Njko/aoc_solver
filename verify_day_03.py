from solvers.days.y2018.day_03 import Day03Solver

def test_day03():
    example = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    
    solver = Day03Solver(example)
    
    # Part 1
    result_p1 = solver.part1()
    print(f"Example Part 1 Result: {result_p1}")
    assert result_p1 == 4, f"Expected 4, got {result_p1}"

    # Part 2
    result_p2 = solver.part2()
    print(f"Example Part 2 Result: {result_p2}")
    assert result_p2 == 3, f"Expected 3, got {result_p2}"

if __name__ == "__main__":
    test_day03()
    
    # Run on real input
    from solvers.storage import storage
    try:
        real_input = storage.load_input(2018, 3)
        solver = Day03Solver(real_input)
        print(f"Real Part 1 Result: {solver.part1()}")
        print(f"Real Part 2 Result: {solver.part2()}")
    except Exception as e:
        print(f"Could not run on real input: {e}")
