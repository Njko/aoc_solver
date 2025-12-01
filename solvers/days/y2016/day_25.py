from itertools import count

from solvers.solver import Solver


class Day25Solver(Solver):
    def _run_assembunny(self, initial_a, instructions):
        registers = {'a': initial_a, 'b': 0, 'c': 0, 'd': 0}
        pc = 0
        expected_output = 0
        output_count = 0

        max_instructions = 100000
        executed_instructions = 0

        while pc < len(instructions) and executed_instructions < max_instructions:
            if output_count >= 12:  # Check for a reasonable number of outputs
                return True

            parts = instructions[pc]
            cmd, args = parts[0], parts[1:]
            executed_instructions += 1

            if cmd == 'cpy':
                val_str, reg = args
                if reg in registers:
                    val = registers[val_str] if val_str in registers else int(val_str)
                    registers[reg] = val
                pc += 1
            elif cmd == 'inc':
                if args[0] in registers:
                    registers[args[0]] += 1
                pc += 1
            elif cmd == 'dec':
                if args[0] in registers:
                    registers[args[0]] -= 1
                pc += 1
            elif cmd == 'jnz':
                val_str, jump_str = args
                val = registers[val_str] if val_str in registers else int(val_str)
                if val != 0:
                    jump = registers[jump_str] if jump_str in registers else int(jump_str)
                    pc += jump
                else:
                    pc += 1
            elif cmd == 'out':
                val_str = args[0]
                val = registers[val_str] if val_str in registers else int(val_str)
                if val == expected_output:
                    output_count += 1
                    expected_output = 1 - expected_output
                else:
                    return False
                pc += 1
        
        return False

    def part1(self):
        instructions = [line.split() for line in self.input_data.strip().split('\n')]
        for a in count(1):
            if self._run_assembunny(a, instructions):
                return a

    def part2(self):
        return "There is no part two for day 25!"
