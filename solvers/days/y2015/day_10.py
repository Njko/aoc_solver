from aoc_agent.solver import Solver
import itertools

class DaySolver(Solver):
    def look_and_say(self, s):
        result = []
        for k, g in itertools.groupby(s):
            count = len(list(g))
            result.append(str(count))
            result.append(k)
        return "".join(result)

    def part1(self) -> "str | int":
        s = self.input_data.strip()
        for _ in range(40):
            s = self.look_and_say(s)
        return len(s)

    def part2(self) -> "str | int":
        s = self.input_data.strip()
        # Part 1 did 40, Part 2 usually asks for 50.
        # I'll just run 50 iterations from scratch or continue from 40 if I cached it, 
        # but 50 isn't too bad for this string growth usually.
        for _ in range(50):
            s = self.look_and_say(s)
        return len(s)
