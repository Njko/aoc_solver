from solvers.days.y2018.day_02 import Day02Solver

def test_day02():
    # Part 1 Example
    example_p1 = """abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab"""
    solver = Day02Solver(example_p1)
    result_p1 = solver.part1()
    print(f"Example Part 1 Result: {result_p1}")
    assert result_p1 == 12, f"Expected 12, got {result_p1}"

    # Part 2 Example
    example_p2 = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""
    solver = Day02Solver(example_p2)
    result_p2 = solver.part2()
    print(f"Example Part 2 Result: {result_p2}")
    assert result_p2 == "fgij", f"Expected fgij, got {result_p2}"

if __name__ == "__main__":
    test_day02()
    
    # Run on real input
    from solvers.storage import storage
    try:
        real_input = storage.load_input(2018, 2)
        solver = Day02Solver(real_input)
        print(f"Real Part 1 Result: {solver.part1()}")
        print(f"Real Part 2 Result: {solver.part2()}")
    except Exception as e:
        print(f"Could not run on real input: {e}")
