from aoc_agent.solver import Solver
from itertools import permutations

class DaySolver(Solver):
    def parse(self):
        happiness = {}
        people = set()
        
        for line in self.lines:
            parts = line.strip().split()
            # Alice would gain 54 happiness units by sitting next to Bob.
            p1 = parts[0]
            p2 = parts[-1][:-1] # remove dot
            amount = int(parts[3])
            if parts[2] == "lose":
                amount = -amount
                
            happiness[(p1, p2)] = amount
            people.add(p1)
            
        return happiness, people

    def calculate_happiness(self, arrangement, happiness):
        total = 0
        n = len(arrangement)
        for i in range(n):
            p1 = arrangement[i]
            p2 = arrangement[(i + 1) % n]
            
            total += happiness.get((p1, p2), 0)
            total += happiness.get((p2, p1), 0)
        return total

    def part1(self) -> "str | int":
        happiness, people = self.parse()
        max_happiness = float('-inf')
        
        # permutations of people.
        # Since it's circular, we can fix one person to reduce search space (n-1)!
        fixed_person = list(people)[0]
        others = [p for p in people if p != fixed_person]
        
        for p in permutations(others):
            arrangement = [fixed_person] + list(p)
            h = self.calculate_happiness(arrangement, happiness)
            max_happiness = max(max_happiness, h)
            
        return max_happiness

    def part2(self) -> "str | int":
        happiness, people = self.parse()
        
        # Add "Me"
        me = "Me"
        for p in people:
            happiness[(me, p)] = 0
            happiness[(p, me)] = 0
        people.add(me)
        
        max_happiness = float('-inf')
        
        fixed_person = list(people)[0]
        others = [p for p in people if p != fixed_person]
        
        for p in permutations(others):
            arrangement = [fixed_person] + list(p)
            h = self.calculate_happiness(arrangement, happiness)
            max_happiness = max(max_happiness, h)
            
        return max_happiness
