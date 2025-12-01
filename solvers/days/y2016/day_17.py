import hashlib
from collections import deque
from solvers.solver import Solver


class Day17Solver(Solver):
    def _get_open_doors(self, passcode, path):
        full_str = f"{passcode}{path}"
        h = hashlib.md5(full_str.encode()).hexdigest()[:4]
        doors = []
        # Up, Down, Left, Right
        if h[0] in 'bcdef': doors.append('U')
        if h[1] in 'bcdef': doors.append('D')
        if h[2] in 'bcdef': doors.append('L')
        if h[3] in 'bcdef': doors.append('R')
        return doors

    def part1(self):
        passcode = self.input_data.strip()
        start = (0, 0, "")  # x, y, path
        queue = deque([start])
        
        while queue:
            x, y, path = queue.popleft()
            
            if (x, y) == (3, 3):
                return path
            
            open_doors = self._get_open_doors(passcode, path)
            
            # Up
            if 'U' in open_doors and y > 0:
                queue.append((x, y - 1, path + 'U'))
            # Down
            if 'D' in open_doors and y < 3:
                queue.append((x, y + 1, path + 'D'))
            # Left
            if 'L' in open_doors and x > 0:
                queue.append((x - 1, y, path + 'L'))
            # Right
            if 'R' in open_doors and x < 3:
                queue.append((x + 1, y, path + 'R'))
        return "No path found"

    def part2(self):
        passcode = self.input_data.strip()
        start = (0, 0, "")  # x, y, path
        queue = deque([start])
        longest_path_len = 0
        
        while queue:
            x, y, path = queue.popleft()
            
            if (x, y) == (3, 3):
                longest_path_len = max(longest_path_len, len(path))
                continue

            open_doors = self._get_open_doors(passcode, path)
            
            # Up
            if 'U' in open_doors and y > 0:
                queue.append((x, y - 1, path + 'U'))
            # Down
            if 'D' in open_doors and y < 3:
                queue.append((x, y + 1, path + 'D'))
            # Left
            if 'L' in open_doors and x > 0:
                queue.append((x - 1, y, path + 'L'))
            # Right
            if 'R' in open_doors and x < 3:
                queue.append((x + 1, y, path + 'R'))
                
        return longest_path_len
