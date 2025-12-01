from aoc_agent.solver import Solver
import hashlib

class DaySolver(Solver):
    def part1(self) -> "str | int":
        key = self.input_data.strip()
        i = 0
        while True:
            s = f"{key}{i}"
            h = hashlib.md5(s.encode()).hexdigest()
            if h.startswith("00000"):
                return i
            i += 1

    def part2(self) -> "str | int":
        key = self.input_data.strip()
        i = 0
        while True:
            s = f"{key}{i}"
            h = hashlib.md5(s.encode()).hexdigest()
            if h.startswith("000000"):
                return i
            i += 1
