from aoc_agent.solver import Solver

class DaySolver(Solver):
    def run_program(self, a_start=0):
        registers = {"a": a_start, "b": 0}
        instructions = [line.strip().replace(",", "") for line in self.lines]
        pc = 0
        
        while 0 <= pc < len(instructions):
            parts = instructions[pc].split()
            op = parts[0]
            
            if op == "hlf":
                registers[parts[1]] //= 2
                pc += 1
            elif op == "tpl":
                registers[parts[1]] *= 3
                pc += 1
            elif op == "inc":
                registers[parts[1]] += 1
                pc += 1
            elif op == "jmp":
                pc += int(parts[1])
            elif op == "jie":
                if registers[parts[1]] % 2 == 0:
                    pc += int(parts[2])
                else:
                    pc += 1
            elif op == "jio":
                if registers[parts[1]] == 1:
                    pc += int(parts[2])
                else:
                    pc += 1
                    
        return registers["b"]

    def part1(self) -> "str | int":
        return self.run_program(a_start=0)

    def part2(self) -> "str | int":
        return self.run_program(a_start=1)
