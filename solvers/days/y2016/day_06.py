from collections import Counter
from solvers.solver import Solver


class Day06Solver(Solver):
    def _get_message(self, input_data, most_common=True):
        lines = input_data.strip().split('\n')
        if not lines:
            return ""
        
        num_cols = len(lines[0])
        columns = ['' for _ in range(num_cols)]
        
        for line in lines:
            for i, char in enumerate(line):
                columns[i] += char
        
        message = ""
        for col in columns:
            counts = Counter(col)
            if most_common:
                message += counts.most_common(1)[0][0]
            else:
                message += counts.most_common()[-1][0]
        
        return message

    def part1(self):
        return self._get_message(self.input_data, most_common=True)

    def part2(self):
        return self._get_message(self.input_data, most_common=False)
