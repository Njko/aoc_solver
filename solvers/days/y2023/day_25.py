import collections
import random
import collections
import random
from aoc_agent.solver import Solver

class DaySolver(Solver):
    """
    Solves Day 25: Snowverload
    
    Approach:
    - Part 1: Find the minimum cut of size 3 in the graph to split it into two components.
      - Use a randomized Max-Flow Min-Cut approach (Edmonds-Karp with BFS).
      - Pick a fixed source node `s` and a random target node `t`.
      - Compute max flow between `s` and `t`.
      - If max flow is 3, the min-cut is found. The reachable nodes from `s` in the residual graph form one component.
      - Calculate the product of the sizes of the two components.
    - Part 2: There is no Part 2 for Day 25 (just a "Push the Button" victory lap).
    """
    def part1(self) -> "str | int":
        # Build Graph
        adj = collections.defaultdict(set)
        nodes = set()
        
        for line in self.lines:
            if not line.strip():
                continue
            parts = line.split(":")
            u = parts[0].strip()
            nodes.add(u)
            vs = parts[1].strip().split()
            for v in vs:
                v = v.strip()
                nodes.add(v)
                adj[u].add(v)
                adj[v].add(u)
        
        nodes_list = list(nodes)
        total_nodes = len(nodes_list)
        
        # We need to find a cut of size 3.
        # We pick a fixed source 's' and try random sinks 't'.
        # If s and t are on different sides of the cut, max_flow(s, t) will be 3.
        
        s = nodes_list[0]
        
        while True:
            t = random.choice(nodes_list)
            if s == t:
                continue
            
            # Compute Max Flow using Edmonds-Karp (BFS for augmenting paths)
            # Since capacities are 1, we just find edge-disjoint paths.
            
            # Residual graph: copy of adj (since undirected, we treat as directed both ways with cap 1)
            # Actually, simpler: maintain used edges.
            # But for min-cut, we need the residual graph.
            
            # Let's implement a clean Max Flow on unit capacity graph
            flow = 0
            # Residual capacity: (u, v) -> 1 if edge exists.
            # We can use a dict of dicts for residual.
            residual = collections.defaultdict(lambda: collections.defaultdict(int))
            for u in adj:
                for v in adj[u]:
                    residual[u][v] = 1
            
            while True:
                # BFS to find path s -> t with capacity > 0
                queue = collections.deque([s])
                parent = {s: None}
                path_found = False
                
                while queue:
                    u = queue.popleft()
                    if u == t:
                        path_found = True
                        break
                    
                    for v in residual[u]:
                        if residual[u][v] > 0 and v not in parent:
                            parent[v] = u
                            queue.append(v)
                
                if not path_found:
                    break
                
                # Augment flow
                flow += 1
                curr = t
                while curr != s:
                    prev = parent[curr]
                    residual[prev][curr] -= 1
                    residual[curr][prev] += 1
                    curr = prev
            
            if flow == 3:
                # Found the cut!
                # The partition is the set of nodes reachable from s in the residual graph
                visited = set()
                queue = collections.deque([s])
                visited.add(s)
                
                while queue:
                    u = queue.popleft()
                    for v in residual[u]:
                        if residual[u][v] > 0 and v not in visited:
                            visited.add(v)
                            queue.append(v)
                
                size1 = len(visited)
                size2 = total_nodes - size1
                return size1 * size2
            
            # If flow > 3, s and t are in the same component. Try another t.

    def part2(self) -> "str | int":
        return "Merry Christmas!"
