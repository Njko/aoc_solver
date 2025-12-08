import math
from collections import defaultdict

class Day08Solver:
    def __init__(self, input_data: str):
        self.input_data = input_data.strip()
        self.points = self._parse_input()

    def _parse_input(self):
        points = []
        for line in self.input_data.split('\n'):
            if not line.strip():
                continue
            parts = line.strip().split(',')
            points.append(tuple(map(int, parts)))
        return points

    def _dist(self, p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

    def part1(self, limit=1000) -> "str | int":
        points = self.points
        n = len(points)
        
        # Calculate all pairwise distances
        pairs = []
        for i in range(n):
            for j in range(i + 1, n):
                d = self._dist(points[i], points[j])
                pairs.append((d, i, j))
        
        # Sort by distance
        pairs.sort(key=lambda x: x[0])
        
        # Take top 'limit' pairs
        top_pairs = pairs[:limit]
        
        # Union-Find
        parent = list(range(n))
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False
            
        # Process pairs
        for _, i, j in top_pairs:
            union(i, j)
            
        # Count component sizes
        counts = defaultdict(int)
        for i in range(n):
            counts[find(i)] += 1
            
        # Get top 3 sizes
        sizes = sorted(counts.values(), reverse=True)
        
        if len(sizes) < 3:
            # Handle edge case if fewer than 3 components (unlikely for 1000 points)
            # But for small examples it might happen.
            # Example has 20 points.
            # If < 3 components, just multiply what we have?
            # Problem says "multiply together the sizes of the three largest circuits".
            # If there are fewer than 3, maybe pad with 1? Or 0?
            # Assuming valid input will have >= 3.
            res = 1
            for s in sizes:
                res *= s
            return res
            
        return sizes[0] * sizes[1] * sizes[2]

    def part2(self) -> "str | int":
        points = self.points
        n = len(points)
        
        # Calculate all pairwise distances
        pairs = []
        for i in range(n):
            for j in range(i + 1, n):
                d = self._dist(points[i], points[j])
                pairs.append((d, i, j))
        
        # Sort by distance
        pairs.sort(key=lambda x: x[0])
        
        # Union-Find
        parent = list(range(n))
        num_components = n
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False
            
        # Process pairs until single component
        for _, i, j in pairs:
            if union(i, j):
                num_components -= 1
                if num_components == 1:
                    # Last connection
                    return points[i][0] * points[j][0]
                    
        return 0
