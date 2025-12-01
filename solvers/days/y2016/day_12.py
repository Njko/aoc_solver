from solvers.solver import Solver


class Day12Solver(Solver):
    def _run_assembunny(self, instructions, initial_registers):
        registers = initial_registers.copy()
        pc = 0

        while pc < len(instructions):
            parts = instructions[pc].split()
            cmd, args = parts[0], parts[1:]

            # Optimization: Detect addition loop
            if (pc + 2 < len(instructions) and
                    cmd == 'inc' and
                    instructions[pc + 1].startswith('dec') and
                    instructions[pc + 2].startswith('jnz')):
                
                inc_parts = instructions[pc].split()
                dec_parts = instructions[pc + 1].split()
                jnz_parts = instructions[pc + 2].split()

                if (len(inc_parts) == 2 and len(dec_parts) == 2 and len(jnz_parts) == 3 and
                        inc_parts[0] == 'inc' and dec_parts[0] == 'dec' and jnz_parts[0] == 'jnz' and
                        dec_parts[1] == jnz_parts[1] and jnz_parts[2] == '-2'):
                    
                    inc_reg = inc_parts[1]
                    dec_reg = dec_parts[1]
                    
                    if registers[dec_reg] != 0:
                        registers[inc_reg] += registers[dec_reg]
                        registers[dec_reg] = 0
                    
                    pc += 3
                    continue
            
            if cmd == 'cpy':
                val_str, reg = args
                val = registers[val_str] if val_str in registers else int(val_str)
                registers[reg] = val
                pc += 1
            elif cmd == 'inc':
                registers[args[0]] += 1
                pc += 1
            elif cmd == 'dec':
                registers[args[0]] -= 1
                pc += 1
            elif cmd == 'jnz':
                val_str, jump_str = args
                val = registers[val_str] if val_str in registers else int(val_str)
                if val != 0:
                    pc += int(jump_str)
                else:
                    pc += 1
        
        return registers['a']

    def part1(self):
        instructions = self.input_data.strip().split('\n')
        initial_registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        return self._run_assembunny(instructions, initial_registers)

    def part2(self):
        instructions = self.input_data.strip().split('\n')
        initial_registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
        return self._run_assembunny(instructions, initial_registers)
