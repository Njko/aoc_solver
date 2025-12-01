import hashlib
import re
from solvers.solver import Solver


class Day14Solver(Solver):
    def __init__(self, input_data):
        super().__init__(input_data)
        self.hashes = {}

    def _get_hash(self, salt, index, stretch=False):
        if (index, stretch) in self.hashes:
            return self.hashes[(index, stretch)]
        
        h = hashlib.md5(f"{salt}{index}".encode()).hexdigest()
        if stretch:
            for _ in range(2016):
                h = hashlib.md5(h.encode()).hexdigest()
        
        self.hashes[(index, stretch)] = h
        return h

    def _find_keys(self, salt, stretch=False):
        keys = []
        index = 0
        while len(keys) < 64:
            h = self._get_hash(salt, index, stretch)
            if match := re.search(r'(.)\1\1', h):
                char = match.group(1)
                five_char_pattern = char * 5
                for i in range(1, 1001):
                    next_h = self._get_hash(salt, index + i, stretch)
                    if five_char_pattern in next_h:
                        keys.append(index)
                        break
            index += 1
        return keys

    def part1(self):
        salt = self.input_data.strip()
        self.hashes = {}
        keys = self._find_keys(salt, stretch=False)
        return keys[-1]

    def part2(self):
        salt = self.input_data.strip()
        self.hashes = {}
        keys = self._find_keys(salt, stretch=True)
        return keys[-1]
