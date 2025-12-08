from solvers.solver import Solver
from collections import Counter
import itertools

class Day02Solver(Solver):
    def part1(self) -> "str | int":
        ids = self.input_data.strip().split('\n')
        count_two = 0
        count_three = 0
        
        for box_id in ids:
            if not box_id.strip():
                continue
            counts = Counter(box_id).values()
            if 2 in counts:
                count_two += 1
            if 3 in counts:
                count_three += 1
                
        return count_two * count_three

    def part2(self) -> "str | int":
        ids = [line.strip() for line in self.input_data.strip().split('\n') if line.strip()]
        
        for id1, id2 in itertools.combinations(ids, 2):
            diff_count = 0
            common_chars = []
            
            for c1, c2 in zip(id1, id2):
                if c1 != c2:
                    diff_count += 1
                else:
                    common_chars.append(c1)
            
            if diff_count == 1:
                return "".join(common_chars)
                
        return ""
