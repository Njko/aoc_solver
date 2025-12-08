from solvers.days.y2025.day_08 import Day08Solver
from solvers.storage import storage

def test_part1():
    example = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
    
    # For the example, the problem says "After making the ten shortest connections... produces 40".
    solver = Day08Solver(example)
    result = solver.part1(limit=10)
    print(f"Example Part 1 Result: {result}")
    assert result == 40, f"Expected 40, got {result}"

    result_p2 = solver.part2()
    print(f"Example Part 2 Result: {result_p2}")
    assert result_p2 == 25272, f"Expected 25272, got {result_p2}"

if __name__ == "__main__":
    test_part1()
    
    # Load real input
    try:
        real_input = storage.load_input(2025, 8)
        solver = Day08Solver(real_input)
        print(f"Real Part 1 Result: {solver.part1()}")
        print(f"Real Part 2 Result: {solver.part2()}")
    except Exception as e:
        print(f"Could not run on real input: {e}")
