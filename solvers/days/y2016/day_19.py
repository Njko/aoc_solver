from solvers.solver import Solver


class Day19Solver(Solver):
    def part1(self):
        num_elves = int(self.input_data)
        # This is a variation of the Josephus problem.
        # The survivor is at position 2L + 1, where N = 2^a + L.
        # A simpler way to calculate this is to find the highest power of 2 less than N,
        # say p. Then the answer is 2 * (N - p) + 1.
        highest_power_of_2 = 1
        while highest_power_of_2 * 2 <= num_elves:
            highest_power_of_2 *= 2
        
        l = num_elves - highest_power_of_2
        return 2 * l + 1

    def part2(self):
        num_elves = int(self.input_data)
        # For the across-the-circle version, the pattern is different.
        # Find the highest power of 3 less than or equal to N, say p.
        # If N = p, the answer is N.
        # If N = p + k where 1 <= k <= p, the answer is k.
        # If N = p + k where p < k < 2p, the answer is p + 2*(k-p).
        
        p = 1
        while p * 3 <= num_elves:
            p *= 3
            
        if num_elves == p:
            return num_elves
        
        if num_elves <= 2 * p:
            return num_elves - p
        else:
            return 2 * num_elves - 3 * p
