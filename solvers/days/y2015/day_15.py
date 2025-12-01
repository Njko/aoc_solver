from aoc_agent.solver import Solver
import re
import math

class DaySolver(Solver):
    def parse(self):
        ingredients = []
        for line in self.lines:
            # Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
            match = re.search(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)", line)
            if match:
                ingredients.append(list(map(int, match.group(2, 3, 4, 5, 6))))
        return ingredients

    def score(self, ingredients, amounts):
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        
        for i, amount in enumerate(amounts):
            capacity += amount * ingredients[i][0]
            durability += amount * ingredients[i][1]
            flavor += amount * ingredients[i][2]
            texture += amount * ingredients[i][3]
            
        if capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0:
            return 0
            
        return capacity * durability * flavor * texture

    def calories(self, ingredients, amounts):
        cal = 0
        for i, amount in enumerate(amounts):
            cal += amount * ingredients[i][4]
        return cal

    def partitions(self, n, k):
        # Generate all ways to sum to n with k parts
        if k == 1:
            yield (n,)
            return
        
        for i in range(n + 1):
            for p in self.partitions(n - i, k - 1):
                yield (i,) + p

    def part1(self) -> "str | int":
        ingredients = self.parse()
        k = len(ingredients)
        max_score = 0
        
        for amounts in self.partitions(100, k):
            s = self.score(ingredients, amounts)
            max_score = max(max_score, s)
            
        return max_score

    def part2(self) -> "str | int":
        ingredients = self.parse()
        k = len(ingredients)
        max_score = 0
        
        for amounts in self.partitions(100, k):
            if self.calories(ingredients, amounts) == 500:
                s = self.score(ingredients, amounts)
                max_score = max(max_score, s)
                
        return max_score
