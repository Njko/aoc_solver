from solvers.solver import Solver

class Day01Solver(Solver):
    def part1(self) -> "str | int":
        total = 0
        lines = self.input_data.strip().split('\n')
        for line in lines:
            if not line.strip():
                continue
            total += int(line)
        return total

    def part2(self) -> "str | int":
        current_freq = 0
        seen_freqs = {0}
        lines = self.input_data.strip().split('\n')
        changes = []
        for line in lines:
            if line.strip():
                changes.append(int(line))
        
        if not changes:
            return 0

        while True:
            for delta in changes:
                current_freq += delta
                if current_freq in seen_freqs:
                    return current_freq
                seen_freqs.add(current_freq)
