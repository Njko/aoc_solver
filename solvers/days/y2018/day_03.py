from solvers.solver import Solver
import re
from collections import defaultdict

class Day03Solver(Solver):
    def __init__(self, input_data: str):
        super().__init__(input_data)
        self.claims = self._parse_claims()
        self.grid = defaultdict(int)
        self._populate_grid()

    def _parse_claims(self):
        claims = []
        # Format: #1 @ 1,3: 4x4
        pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
        for line in self.input_data.strip().split('\n'):
            if not line.strip():
                continue
            match = pattern.match(line.strip())
            if match:
                claim_id, x, y, w, h = map(int, match.groups())
                claims.append({
                    'id': claim_id,
                    'x': x,
                    'y': y,
                    'w': w,
                    'h': h
                })
        return claims

    def _populate_grid(self):
        for claim in self.claims:
            for i in range(claim['w']):
                for j in range(claim['h']):
                    self.grid[(claim['x'] + i, claim['y'] + j)] += 1

    def part1(self) -> "str | int":
        return sum(1 for count in self.grid.values() if count >= 2)

    def part2(self) -> "str | int":
        for claim in self.claims:
            overlap = False
            for i in range(claim['w']):
                for j in range(claim['h']):
                    if self.grid[(claim['x'] + i, claim['y'] + j)] > 1:
                        overlap = True
                        break
                if overlap:
                    break
            if not overlap:
                return claim['id']
        return -1
