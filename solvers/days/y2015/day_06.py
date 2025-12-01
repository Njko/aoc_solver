from aoc_agent.solver import Solver
import re

class DaySolver(Solver):
    def part1(self) -> "str | int":
        grid = [[False for _ in range(1000)] for _ in range(1000)]
        
        for line in self.lines:
            match = re.search(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", line)
            if not match: continue
            
            action = match.group(1)
            x1, y1, x2, y2 = map(int, match.group(2, 3, 4, 5))
            
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if action == "turn on":
                        grid[x][y] = True
                    elif action == "turn off":
                        grid[x][y] = False
                    elif action == "toggle":
                        grid[x][y] = not grid[x][y]
                        
        count = sum(sum(row) for row in grid)
        return count

    def part2(self) -> "str | int":
        grid = [[0 for _ in range(1000)] for _ in range(1000)]
        
        for line in self.lines:
            match = re.search(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", line)
            if not match: continue
            
            action = match.group(1)
            x1, y1, x2, y2 = map(int, match.group(2, 3, 4, 5))
            
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if action == "turn on":
                        grid[x][y] += 1
                    elif action == "turn off":
                        grid[x][y] = max(0, grid[x][y] - 1)
                    elif action == "toggle":
                        grid[x][y] += 2
                        
        total_brightness = sum(sum(row) for row in grid)
        return total_brightness
