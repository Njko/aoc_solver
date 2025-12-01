from collections import deque
from itertools import permutations
from solvers.solver import Solver


class Day24Solver(Solver):
    def __init__(self, input_data):
        super().__init__(input_data)
        self.grid, self.points = self._parse_map(self.input_data)
        self.dists = self._calculate_distances(self.grid, self.points)

    def _parse_map(self, input_data):
        grid = [list(row) for row in input_data.strip().split('\n')]
        points = {}
        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                if char.isdigit():
                    points[int(char)] = (r, c)
        return grid, points

    def _bfs(self, grid, start, end):
        queue = deque([(start, 0)])
        visited = {start}
        while queue:
            (r, c), dist = queue.popleft()
            if (r, c) == end:
                return dist
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if grid[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))
        return float('inf')

    def _calculate_distances(self, grid, points):
        dists = {}
        point_nums = sorted(points.keys())
        for i in range(len(point_nums)):
            for j in range(i + 1, len(point_nums)):
                p1 = point_nums[i]
                p2 = point_nums[j]
                dist = self._bfs(grid, points[p1], points[p2])
                dists[(p1, p2)] = dist
                dists[(p2, p1)] = dist
        return dists

    def part1(self):
        other_points = [p for p in self.points if p != 0]
        min_path = float('inf')
        
        for perm in permutations(other_points):
            path = [0] + list(perm)
            current_dist = 0
            for i in range(len(path) - 1):
                current_dist += self.dists[(path[i], path[i+1])]
            min_path = min(min_path, current_dist)
            
        return min_path

    def part2(self):
        other_points = [p for p in self.points if p != 0]
        min_path = float('inf')
        
        for perm in permutations(other_points):
            path = [0] + list(perm) + [0]
            current_dist = 0
            for i in range(len(path) - 1):
                current_dist += self.dists[(path[i], path[i+1])]
            min_path = min(min_path, current_dist)
            
        return min_path
