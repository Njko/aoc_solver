from aoc_agent.solver import Solver

class DaySolver(Solver):
    def increment_password(self, s):
        chars = list(s)
        i = len(chars) - 1
        while i >= 0:
            if chars[i] == 'z':
                chars[i] = 'a'
                i -= 1
            else:
                chars[i] = chr(ord(chars[i]) + 1)
                break
        return "".join(chars)

    def is_valid(self, s):
        # Rule 2: No i, o, l
        if 'i' in s or 'o' in s or 'l' in s:
            return False
            
        # Rule 1: Increasing straight of 3
        has_straight = False
        for i in range(len(s) - 2):
            if ord(s[i+1]) == ord(s[i]) + 1 and ord(s[i+2]) == ord(s[i]) + 2:
                has_straight = True
                break
        if not has_straight:
            return False
            
        # Rule 3: Two different non-overlapping pairs
        pairs = 0
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i+1]:
                pairs += 1
                i += 2
            else:
                i += 1
        if pairs < 2:
            return False
            
        return True

    def next_password(self, s):
        while True:
            s = self.increment_password(s)
            if self.is_valid(s):
                return s

    def part1(self) -> "str | int":
        current = self.input_data.strip()
        return self.next_password(current)

    def part2(self) -> "str | int":
        # Part 2 usually asks for the next one after Part 1
        # I'll calculate Part 1 again (or cache it if I were optimizing, but it's fast enough)
        p1 = self.part1()
        return self.next_password(p1)
