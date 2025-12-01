from collections import deque
from solvers.solver import Solver


class Day13Solver(Solver):
    def _is_wall(self, x, y, favorite_number):
        if x < 0 or y < 0:
            return True
        val = x*x + 3*x + 2*x*y + y + y*y + favorite_number
        return bin(val).count('1') % 2 != 0

    def part1(self):
        favorite_number = int(self.input_data)
        start = (1, 1)
        target = (31, 39)
        
        queue = deque([(start, 0)])
        visited = {start}
        
        while queue:
            (x, y), steps = queue.popleft()
            
            if (x, y) == target:
                return steps
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and not self._is_wall(nx, ny, favorite_number):
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))
        return -1

    def part2(self):
        favorite_number = int(self.input_data)
        start = (1, 1)
        
        queue = deque([(start, 0)])
        visited = {start}
        
        # Count locations reachable in at most 50 steps
        count = 1 # Starting location
        
        while queue:
            (x, y), steps = queue.popleft()
            
            if steps >= 50:
                continue
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and not self._is_wall(nx, ny, favorite_number):
                    visited.add((nx, ny))
                    count += 1
                    queue.append(((nx, ny), steps + 1))
        return count
