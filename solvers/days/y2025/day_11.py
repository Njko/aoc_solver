from functools import lru_cache
import re

class Day11Solver:
    def __init__(self, input_data: str):
        self.input_data = input_data.strip()
        self.adj = self._parse_input()

    def _parse_input(self):
        adj = {}
        for line in self.input_data.split('\n'):
            line = line.strip()
            if not line:
                continue
            # Format: 'aaa: you hhh'
            # Note: the problem says "aaa: you hhh" means "aaa has outputs you and hhh"
            # It also says: "Data only ever flows from a device through its outputs"
            # So if line is "src: dst1 dst2", edges are src->dst1, src->dst2
            
            if ':' in line:
                src_part, dst_part = line.split(':')
                src = src_part.strip()
                dsts = dst_part.strip().split()
                if src not in adj:
                    adj[src] = []
                for dst in dsts:
                    adj[src].append(dst)
        return adj

    def _count_paths(self, start_node, end_node):
        # Use simple DFS with memoization (since it's a DAG)
        @lru_cache(maxsize=None)
        def dfs(node):
            if node == end_node:
                return 1
            
            if node not in self.adj:
                return 0
            
            total = 0
            for neighbor in self.adj[node]:
                total += dfs(neighbor)
            return total

        return dfs(start_node)

    def part1(self) -> "str | int":
        # Count paths from 'you' to 'out'
        return self._count_paths('you', 'out')

    def part2(self) -> "str | int":
        # Paths from 'svr' to 'out' passing through BOTH 'dac' and 'fft'.
        # Order 1: svr -> ... -> dac -> ... -> fft -> ... -> out
        # Order 2: svr -> ... -> fft -> ... -> dac -> ... -> out
        
        # Determine paths for Order 1
        p1 = self._count_paths('svr', 'dac') * self._count_paths('dac', 'fft') * self._count_paths('fft', 'out')
        
        # Determine paths for Order 2
        p2 = self._count_paths('svr', 'fft') * self._count_paths('fft', 'dac') * self._count_paths('dac', 'out')
        
        return p1 + p2
