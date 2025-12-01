from aoc_agent.solver import Solver

class DaySolver(Solver):
    def part1(self) -> "str | int":
        nice_count = 0
        for s in self.lines:
            if self.is_nice_part1(s):
                nice_count += 1
        return nice_count

    def is_nice_part1(self, s: str) -> bool:
        # Rule 1: At least 3 vowels
        vowels = sum(1 for c in s if c in 'aeiou')
        if vowels < 3:
            return False
            
        # Rule 2: At least one letter twice in a row
        has_double = False
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                has_double = True
                break
        if not has_double:
            return False
            
        # Rule 3: No forbidden strings
        for forbidden in ['ab', 'cd', 'pq', 'xy']:
            if forbidden in s:
                return False
                
        return True

    def part2(self) -> "str | int":
        nice_count = 0
        for s in self.lines:
            if self.is_nice_part2(s):
                nice_count += 1
        return nice_count
        
    def is_nice_part2(self, s: str) -> bool:
        # Rule 1: Pair appears twice without overlapping
        has_pair = False
        for i in range(len(s) - 1):
            pair = s[i:i+2]
            if s.count(pair) >= 2:
                # Check for overlap: e.g. "aaa" has "aa" twice but they overlap.
                # But s.count() counts non-overlapping occurrences? No, wait.
                # "aaa".count("aa") is 1 in Python.
                # Wait, "aaaa".count("aa") is 2.
                # So s.count() is actually what we want?
                # "aaa" -> "aa" at 0, "aa" at 1. Overlap.
                # Python's count() returns non-overlapping occurrences.
                # So "aaa".count("aa") is 1.
                # "aaaa".count("aa") is 2.
                # So if count >= 2, it's satisfied.
                has_pair = True
                break
        if not has_pair:
            return False
            
        # Rule 2: Repeat with one between
        has_repeat = False
        for i in range(len(s) - 2):
            if s[i] == s[i+2]:
                has_repeat = True
                break
        if not has_repeat:
            return False
            
        return True
