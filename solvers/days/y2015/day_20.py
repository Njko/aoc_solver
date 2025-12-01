from aoc_agent.solver import Solver

class DaySolver(Solver):
    def part1(self) -> "str | int":
        target = int(self.input_data.strip())
        limit = target // 10
        
        houses = [0] * (limit + 1)
        for elf in range(1, limit + 1):
            for house in range(elf, limit + 1, elf):
                houses[house] += elf * 10
            
        for i, presents in enumerate(houses):
            if presents >= target:
                return i
        return -1

    def part2(self) -> "str | int":
        target = int(self.input_data.strip())
        limit = target // 10
        
        houses = [0] * (limit + 1)
        for elf in range(1, limit + 1):
            count = 0
            for house in range(elf, limit + 1, elf):
                houses[house] += elf * 11
                count += 1
                if count == 50:
                    break
            
        for i, presents in enumerate(houses):
            if presents >= target:
                return i
        return -1
