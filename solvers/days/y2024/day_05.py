from aoc_agent.solver import Solver
from functools import cmp_to_key

class DaySolver(Solver):
    """
    Solves Day 5: Print Queue
    
    Approach:
    - Parse ordering rules (X|Y) and updates (lists of pages).
    - Part 1: Check if each update is strictly ordered according to the rules.
      - For every pair of pages in an update, verify they don't violate any rule.
      - Sum the middle page numbers of valid updates.
    - Part 2: Identify invalid updates and reorder them.
      - Use a custom comparator based on the rules to sort the pages.
      - `cmp(a, b)` returns -1 if a|b rule exists, 1 if b|a rule exists.
      - Sum the middle page numbers of the corrected updates.
    """
    def parse(self):
        parts = self.input_data.strip().split("\n\n")
        rules_str = parts[0].strip().splitlines()
        updates_str = parts[1].strip().splitlines()
        
        rules = set()
        for r in rules_str:
            a, b = map(int, r.split("|"))
            rules.add((a, b))
            
        updates = []
        for u in updates_str:
            updates.append(list(map(int, u.split(","))))
            
        return rules, updates

    def is_ordered(self, update, rules):
        # Check every pair in the update
        # A more efficient way: for every rule (a, b), if both a and b are in update,
        # check if index(a) < index(b).
        
        # Map page to index for O(1) lookup
        idx_map = {page: i for i, page in enumerate(update)}
        
        for a, b in rules:
            if a in idx_map and b in idx_map:
                if idx_map[a] > idx_map[b]:
                    return False
        return True

    def part1(self) -> "str | int":
        rules, updates = self.parse()
        total = 0
        
        for update in updates:
            if self.is_ordered(update, rules):
                mid = update[len(update) // 2]
                total += mid
                
        return total

    def part2(self) -> "str | int":
        rules, updates = self.parse()
        total = 0
        
        # Comparator for sorting
        def compare(a, b):
            if (a, b) in rules:
                return -1 # a comes before b
            if (b, a) in rules:
                return 1 # b comes before a
            return 0
            
        for update in updates:
            if not self.is_ordered(update, rules):
                # Sort the update
                sorted_update = sorted(update, key=cmp_to_key(compare))
                mid = sorted_update[len(sorted_update) // 2]
                total += mid
                
        return total
