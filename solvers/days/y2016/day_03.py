from solvers.solver import Solver


class Day03Solver(Solver):
    def _is_valid_triangle(self, sides):
        a, b, c = sorted(sides)
        return a + b > c

    def part1(self):
        count = 0
        for line in self.input_data.strip().split('\n'):
            sides = [int(s) for s in line.split()]
            if self._is_valid_triangle(sides):
                count += 1
        return count

    def part2(self):
        lines = self.input_data.strip().split('\n')
        numbers = []
        for line in lines:
            numbers.append([int(s) for s in line.split()])
        
        count = 0
        for i in range(0, len(numbers), 3):
            for j in range(3):
                triangle = (numbers[i][j], numbers[i+1][j], numbers[i+2][j])
                if self._is_valid_triangle(triangle):
                    count += 1
        return count
