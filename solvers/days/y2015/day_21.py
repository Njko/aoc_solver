from aoc_agent.solver import Solver
from itertools import combinations

class DaySolver(Solver):
    def parse(self):
        boss = {}
        for line in self.lines:
            k, v = line.split(": ")
            boss[k] = int(v)
        return boss

    def simulate(self, my_damage, my_armor, boss_hp, boss_damage, boss_armor):
        my_hp = 100
        
        my_dmg_dealt = max(1, my_damage - boss_armor)
        boss_dmg_dealt = max(1, boss_damage - my_armor)
        
        # Turns to kill boss
        turns_to_kill_boss = (boss_hp + my_dmg_dealt - 1) // my_dmg_dealt
        
        # Turns to kill me
        turns_to_kill_me = (my_hp + boss_dmg_dealt - 1) // boss_dmg_dealt
        
        return turns_to_kill_boss <= turns_to_kill_me

    def get_loadouts(self):
        weapons = [
            (8, 4, 0),
            (10, 5, 0),
            (25, 6, 0),
            (40, 7, 0),
            (74, 8, 0)
        ]
        
        armors = [
            (0, 0, 0), # No armor
            (13, 0, 1),
            (31, 0, 2),
            (53, 0, 3),
            (75, 0, 4),
            (102, 0, 5)
        ]
        
        rings = [
            (0, 0, 0), # No ring 1
            (0, 0, 0), # No ring 2
            (25, 1, 0),
            (50, 2, 0),
            (100, 3, 0),
            (20, 0, 1),
            (40, 0, 2),
            (80, 0, 3)
        ]
        
        for w in weapons:
            for a in armors:
                for r1, r2 in combinations(rings, 2):
                    cost = w[0] + a[0] + r1[0] + r2[0]
                    damage = w[1] + a[1] + r1[1] + r2[1]
                    armor = w[2] + a[2] + r1[2] + r2[2]
                    yield cost, damage, armor

    def part1(self) -> "str | int":
        boss = self.parse()
        min_cost = float('inf')
        
        for cost, damage, armor in self.get_loadouts():
            if self.simulate(damage, armor, boss["Hit Points"], boss["Damage"], boss["Armor"]):
                min_cost = min(min_cost, cost)
                
        return min_cost

    def part2(self) -> "str | int":
        boss = self.parse()
        max_cost = 0
        
        for cost, damage, armor in self.get_loadouts():
            if not self.simulate(damage, armor, boss["Hit Points"], boss["Damage"], boss["Armor"]):
                max_cost = max(max_cost, cost)
                
        return max_cost
