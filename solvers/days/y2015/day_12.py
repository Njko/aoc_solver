from aoc_agent.solver import Solver
import json
import re

class DaySolver(Solver):
    def part1(self) -> "str | int":
        # Just find all numbers with regex
        return sum(map(int, re.findall(r"-?\d+", self.input_data)))

    def part2(self) -> "str | int":
        data = json.loads(self.input_data)
        return self.sum_ignoring_red(data)

    def sum_ignoring_red(self, obj):
        if isinstance(obj, int):
            return obj
        elif isinstance(obj, list):
            return sum(self.sum_ignoring_red(x) for x in obj)
        elif isinstance(obj, dict):
            if "red" in obj.values():
                return 0
            return sum(self.sum_ignoring_red(x) for x in obj.values())
        else:
            return 0
