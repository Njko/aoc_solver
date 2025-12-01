import re
from solvers.solver import Solver


class Day07Solver(Solver):
    def _has_abba(self, s):
        for i in range(len(s) - 3):
            if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
                return True
        return False

    def part1(self):
        count = 0
        for line in self.input_data.strip().split('\n'):
            parts = re.split(r'[\[\]]', line)
            supernets = parts[::2]
            hypernets = parts[1::2]
            
            if any(self._has_abba(s) for s in supernets) and not any(self._has_abba(h) for h in hypernets):
                count += 1
        return count

    def _get_abas(self, s):
        abas = set()
        for i in range(len(s) - 2):
            if s[i] == s[i+2] and s[i] != s[i+1]:
                abas.add(s[i:i+3])
        return abas

    def part2(self):
        count = 0
        for line in self.input_data.strip().split('\n'):
            parts = re.split(r'[\[\]]', line)
            supernets = parts[::2]
            hypernets = parts[1::2]
            
            abas = set()
            for s in supernets:
                abas.update(self._get_abas(s))
            
            found_ssl = False
            for aba in abas:
                bab = aba[1] + aba[0] + aba[1]
                if any(bab in h for h in hypernets):
                    found_ssl = True
                    break
            if found_ssl:
                count += 1
        return count
