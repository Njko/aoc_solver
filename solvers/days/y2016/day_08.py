import re
from solvers.solver import Solver


class Day08Solver(Solver):
    def __init__(self, input_data=None):
        super().__init__(input_data)
        self.width = 50
        self.height = 6
        self.screen = [['.' for _ in range(self.width)] for _ in range(self.height)]
        self._execute_instructions()

    def _execute_instructions(self):
        for line in self.input_data.strip().split('\n'):
            if match := re.match(r'rect (\d+)x(\d+)', line):
                w, h = map(int, match.groups())
                for y in range(h):
                    for x in range(w):
                        self.screen[y][x] = '#'
            elif match := re.match(r'rotate row y=(\d+) by (\d+)', line):
                row, amount = map(int, match.groups())
                self.screen[row] = self.screen[row][-amount:] + self.screen[row][:-amount]
            elif match := re.match(r'rotate column x=(\d+) by (\d+)', line):
                col, amount = map(int, match.groups())
                column = [self.screen[y][col] for y in range(self.height)]
                column = column[-amount:] + column[:-amount]
                for y in range(self.height):
                    self.screen[y][col] = column[y]

    def part1(self):
        return sum(row.count('#') for row in self.screen)

    def part2(self):
        return "\n" + "\n".join("".join(row) for row in self.screen)