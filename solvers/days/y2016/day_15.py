from solvers.solver import Solver
import re


class Day15Solver(Solver):
    def __init__(self, input_data: str):
        super().__init__(input_data)
        self.discs = self._parse_discs(self.input_data)

    def _parse_discs(self, raw_input):
        discs = []
        for line in raw_input.splitlines():
            match = re.match(
                r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).",
                line,
            )
            if match:
                groups = match.groups()
                num_positions = int(groups[1])
                start_pos = int(groups[2])
                discs.append((num_positions, start_pos))
        return discs

    def _check_time(self, time, discs):
        for i, (num_positions, start_pos) in enumerate(discs):
            disc_num = i + 1
            if (start_pos + time + disc_num) % num_positions != 0:
                return False
        return True

    def part1(self):
        time = 0
        while True:
            if self._check_time(time, self.discs):
                return time
            time += 1

    def part2(self):
        discs_part_2 = self.discs + [(11, 0)]
        time = 0
        while True:
            if self._check_time(time, discs_part_2):
                return time
            time += 1

