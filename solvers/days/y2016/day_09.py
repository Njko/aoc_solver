import re
from solvers.solver import Solver


class Day09Solver(Solver):
    def _decompress(self, data, recursive=False):
        length = 0
        i = 0
        while i < len(data):
            if data[i] == '(':
                match = re.match(r'\((\d+)x(\d+)\)', data[i:])
                char_count, repeat = map(int, match.groups())
                marker_len = match.end()
                i += marker_len
                
                sub_data = data[i:i+char_count]
                if recursive:
                    sub_len = self._decompress(sub_data, recursive=True)
                else:
                    sub_len = len(sub_data)
                
                length += sub_len * repeat
                i += char_count
            else:
                length += 1
                i += 1
        return length

    def part1(self):
        data = "".join(self.input_data.strip().split())
        return self._decompress(data, recursive=False)

    def part2(self):
        data = "".join(self.input_data.strip().split())
        return self._decompress(data, recursive=True)
