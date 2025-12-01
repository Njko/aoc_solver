from aoc_agent.solver import Solver
from itertools import permutations

class DaySolver(Solver):
    def parse(self):
        distances = {}
        locations = set()
        
        for line in self.lines:
            parts = line.split(" = ")
            dist = int(parts[1])
            locs = parts[0].split(" to ")
            src, dst = locs[0], locs[1]
            
            distances[(src, dst)] = dist
            distances[(dst, src)] = dist
            locations.add(src)
            locations.add(dst)
            
        return distances, locations

    def part1(self) -> "str | int":
        distances, locations = self.parse()
        min_dist = float('inf')
        
        for path in permutations(locations):
            current_dist = 0
            valid = True
            for i in range(len(path) - 1):
                if (path[i], path[i+1]) in distances:
                    current_dist += distances[(path[i], path[i+1])]
                else:
                    valid = False
                    break
            
            if valid:
                min_dist = min(min_dist, current_dist)
                
        return min_dist

    def part2(self) -> "str | int":
        distances, locations = self.parse()
        max_dist = 0
        
        for path in permutations(locations):
            current_dist = 0
            valid = True
            for i in range(len(path) - 1):
                if (path[i], path[i+1]) in distances:
                    current_dist += distances[(path[i], path[i+1])]
                else:
                    valid = False
                    break
            
            if valid:
                max_dist = max(max_dist, current_dist)
                
        return max_dist
