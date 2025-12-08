from solvers.days.y2025.day_11 import Day11Solver
from solvers.storage import storage

def verify_part1():
    print("Verifying Part 1...")
    
    # Example input
    example_input = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""
    solver = Day11Solver(example_input)
    result = solver.part1()
    print(f"Example result: {result}")
    
    expected = 5
    if result == expected:
        print("Example passed!")
    else:
        print(f"Example failed. Expected {expected}, got {result}")
        return

    # Real input
    try:
        real_input = storage.load_input(2025, 11)
        solver_real = Day11Solver(real_input)
        real_result = solver_real.part1()
        print(f"Real input Part 1 result: {real_result}")
    except Exception as e:
        print(f"Could not run on real input: {e}")

def verify_part2():
    print("\nVerifying Part 2...")
    
    # Example input
    example_input = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""
    solver = Day11Solver(example_input)
    result = solver.part2()
    print(f"Example result: {result}")
    
    expected = 2
    if result == expected:
        print("Example passed!")
    else:
        print(f"Example failed. Expected {expected}, got {result}")
        return

    # Real input
    try:
        real_input = storage.load_input(2025, 11)
        solver_real = Day11Solver(real_input)
        real_result = solver_real.part2()
        print(f"Real input Part 2 result: {real_result}")
    except Exception as e:
        print(f"Could not run on real input for Part 2: {e}")

if __name__ == "__main__":
    verify_part1()
    verify_part2()
