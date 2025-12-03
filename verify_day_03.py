from solvers.days.y2025.day_03 import Day03Solver

class MockSolver(Day03Solver):
    def __init__(self, input_data):
        self.input_data = input_data
        self.lines = input_data.strip().split('\n')

def test_example():
    input_data = """
987654321111111
811111111111119
234234234234278
818181911112111
"""
    solver = MockSolver(input_data)
    result = solver.part1()
    print(f"Part 1 Result: {result}")
    expected = 357
    if result == expected:
        print("Part 1 Verification PASSED")
    else:
        print(f"Part 1 Verification FAILED. Expected {expected}, got {result}")

    result_p2 = solver.part2()
    print(f"Part 2 Result: {result_p2}")
    expected_p2 = 3121910778619
    if result_p2 == expected_p2:
        print("Part 2 Verification PASSED")
    else:
        print(f"Part 2 Verification FAILED. Expected {expected_p2}, got {result_p2}")

if __name__ == "__main__":
    test_example()
