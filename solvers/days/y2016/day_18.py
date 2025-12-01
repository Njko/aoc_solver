from solvers.solver import Solver


class Day18Solver(Solver):
    def _get_next_row(self, row):
        padded_row = '.' + row + '.'
        next_row = ""
        for i in range(len(row)):
            left, center, right = padded_row[i:i+3]
            
            is_trap = (left == '^' and center == '^' and right == '.') or \
                      (center == '^' and right == '^' and left == '.') or \
                      (left == '^' and center == '.' and right == '.') or \
                      (right == '^' and center == '.' and left == '.')
            
            next_row += '^' if is_trap else '.'
        return next_row

    def _count_safe_tiles(self, first_row, num_rows):
        safe_count = first_row.count('.')
        current_row = first_row
        for _ in range(num_rows - 1):
            current_row = self._get_next_row(current_row)
            safe_count += current_row.count('.')
        return safe_count

    def part1(self):
        first_row = self.input_data.strip()
        return self._count_safe_tiles(first_row, 40)

    def part2(self):
        first_row = self.input_data.strip()
        return self._count_safe_tiles(first_row, 400000)
