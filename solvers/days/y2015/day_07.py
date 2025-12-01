from aoc_agent.solver import Solver
import functools

class DaySolver(Solver):
    def parse(self):
        connections = {}
        for line in self.lines:
            parts = line.split(" -> ")
            target = parts[1]
            source = parts[0].split()
            connections[target] = source
        return connections

    def solve_wire(self, wire, connections, cache):
        if wire.isdigit():
            return int(wire)
        
        if wire in cache:
            return cache[wire]
        
        source = connections[wire]
        result = 0
        
        if len(source) == 1:
            # Direct assignment or number
            result = self.solve_wire(source[0], connections, cache)
        elif len(source) == 2:
            # NOT operation
            if source[0] == "NOT":
                val = self.solve_wire(source[1], connections, cache)
                result = ~val & 0xFFFF
        elif len(source) == 3:
            # Binary operation
            op = source[1]
            left = self.solve_wire(source[0], connections, cache)
            right = self.solve_wire(source[2], connections, cache)
            
            if op == "AND":
                result = left & right
            elif op == "OR":
                result = left | right
            elif op == "LSHIFT":
                result = (left << right) & 0xFFFF
            elif op == "RSHIFT":
                result = (left >> right) & 0xFFFF
                
        cache[wire] = result
        return result

    def part1(self) -> "str | int":
        connections = self.parse()
        cache = {}
        return self.solve_wire("a", connections, cache)

    def part2(self) -> "str | int":
        connections = self.parse()
        
        # Get signal from 'a' in part 1
        cache1 = {}
        a_val = self.solve_wire("a", connections, cache1)
        
        # Override 'b' with 'a' signal
        connections["b"] = [str(a_val)]
        
        # Reset cache and solve for 'a' again
        cache2 = {}
        return self.solve_wire("a", connections, cache2)
