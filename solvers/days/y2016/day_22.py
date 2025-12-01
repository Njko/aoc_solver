import re
from itertools import permutations
from collections import deque
from solvers.solver import Solver


class Day22Solver(Solver):
    def _parse_nodes(self):
        nodes = {}
        for line in self.input_data.strip().split('\n')[2:]:
            match = re.match(r'/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+\d+%', line)
            x, y, size, used, avail = map(int, match.groups())
            nodes[(x, y)] = {'size': size, 'used': used, 'avail': avail}
        return nodes

    def part1(self):
        nodes = self._parse_nodes()
        node_list = list(nodes.items())
        viable_pairs = 0
        
        for (ax, ay), a in node_list:
            if a['used'] == 0:
                continue
            for (bx, by), b in node_list:
                if (ax, ay) == (bx, by):
                    continue
                if a['used'] <= b['avail']:
                    viable_pairs += 1
        return viable_pairs

    def part2(self):
        nodes = self._parse_nodes()
        
        # Find grid dimensions
        max_x = max(x for x, y in nodes.keys())
        max_y = max(y for x, y in nodes.keys())
        
        # Find the empty node
        empty_node = None
        for (x, y), node in nodes.items():
            if node['used'] == 0:
                empty_node = (x, y)
                break
        
        # Identify walls (nodes too big to move data into)
        # Heuristic: if a node's used space is larger than the empty node's size, it's a wall.
        empty_size = nodes[empty_node]['size']
        walls = {pos for pos, node in nodes.items() if node['used'] > empty_size}

        # BFS to find shortest path for empty slot to get next to the goal data
        
        # We want to move the empty slot to (max_x - 1, 0)
        target_empty_pos = (max_x - 1, 0)
        
        queue = deque([(empty_node, 0)])
        visited = {empty_node}
        
        steps_to_move_empty = 0
        while queue:
            pos, steps = queue.popleft()
            if pos == target_empty_pos:
                steps_to_move_empty = steps
                break
            
            x, y = pos
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= max_x and 0 <= ny <= max_y and (nx, ny) not in visited and (nx, ny) not in walls:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))

        # Once the empty slot is at (max_x - 1, 0), the goal data is at (max_x, 0).
        # To move the goal data one step left, it takes 5 moves:
        # 1. Move empty slot U, R, R, D, L around the goal data.
        # This sequence moves the goal data one step left, and the empty slot is again to its left.
        # It takes (max_x - 1) such sequences to move the data to (1, 0).
        # Then 1 more move to get it to (0, 0).
        
        # Total moves = (steps to get empty to (max_x-1, 0)) + 1 (to swap with goal) + (max_x-1)*5
        
        # The logic is:
        # 1. Move the empty space to be adjacent to the goal data.
        # 2. The goal data is at (max_x, 0). We need to move it to (0,0).
        #    To move it one step left, we need to move the empty space around it.
        #    If empty is at (x-1, y) and goal is at (x,y), we do:
        #    - empty up to (x-1, y-1)
        #    - empty right to (x, y-1)
        #    - empty down to (x,y) -- this is the old goal spot
        #    - goal data left to (x-1, y)
        #    - empty from (x,y) down to (x, y+1)
        #    - empty left to (x-1, y+1)
        #    This is complex. A simpler view:
        #    To move data from (x,y) to (x-1,y), the empty slot must be at (x-1,y).
        #    The swap takes 1 move. Then the empty slot is at (x,y).
        #    To get it back to (x-2,y) to repeat the process, it takes moves.
        #    The pattern is: move data left (1), move empty U, L, L, D (4) = 5 moves per step.
        
        # Let's re-verify the logic.
        # Path for empty slot to get to (max_x - 1, 0)
        # Then, one move to swap empty with goal data. Empty is at (max_x, 0).
        # Now, to move goal data from (max_x-1, 0) to (max_x-2, 0), we need empty at (max_x-2, 0).
        # Path for empty from (max_x, 0) to (max_x-2, 0):
        # (max_x, 0) -> (max_x, 1) -> (max_x-1, 1) -> (max_x-2, 1) -> (max_x-2, 0) -- 4 moves.
        # Then 1 move to swap. Total 5 moves per step left.
        
        # So, total = steps_to_move_empty + 1 (first swap) + (max_x - 1) * 5
        # The target is (max_x, 0), we want to move it to (0,0).
        # It needs to move max_x-1 steps to the left.
        # The final move is from (1,0) to (0,0).
        
        return steps_to_move_empty + 1 + (max_x - 1) * 5
