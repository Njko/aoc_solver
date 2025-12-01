from aoc_agent.solver import Solver

class DaySolver(Solver):
    def parse(self):
        grid = {}
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line.strip()):
                if char == '#':
                    grid[(x, y)] = True
        return grid, len(self.lines), len(self.lines[0].strip())

    def get_neighbors(self, x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                yield x + dx, y + dy

    def step(self, grid, width, height, corners_stuck=False):
        new_grid = {}
        
        if corners_stuck:
            corners = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]
            for c in corners:
                grid[c] = True

        for y in range(height):
            for x in range(width):
                neighbors_on = 0
                for nx, ny in self.get_neighbors(x, y):
                    if grid.get((nx, ny), False):
                        neighbors_on += 1
                
                is_on = grid.get((x, y), False)
                if is_on:
                    if neighbors_on in [2, 3]:
                        new_grid[(x, y)] = True
                else:
                    if neighbors_on == 3:
                        new_grid[(x, y)] = True
                        
        if corners_stuck:
            corners = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]
            for c in corners:
                new_grid[c] = True
                
        return new_grid

    def part1(self) -> "str | int":
        grid, h, w = self.parse()
        for _ in range(100):
            grid = self.step(grid, w, h)
        return len(grid)

    def part2(self) -> "str | int":
        grid, h, w = self.parse()
        # Initial corners stuck
        corners = [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)]
        for c in corners:
            grid[c] = True
            
        for _ in range(100):
            grid = self.step(grid, w, h, corners_stuck=True)
        return len(grid)
