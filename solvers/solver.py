from abc import ABC, abstractmethod

class Solver(ABC):
    def __init__(self, input_data: str):
        self.input_data = input_data.strip()
        self.lines = self.input_data.splitlines()

    @abstractmethod
    def part1(self) -> "str | int":
        pass

    @abstractmethod
    def part2(self) -> "str | int":
        pass

    def solve(self):
        print("--- Part 1 ---")
        try:
            p1 = self.part1()
            print(p1)
        except NotImplementedError:
            print("Not implemented")
        
        print("\n--- Part 2 ---")
        try:
            p2 = self.part2()
            print(p2)
        except NotImplementedError:
            print("Not implemented")
