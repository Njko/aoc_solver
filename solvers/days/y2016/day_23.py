from solvers.solver import Solver


class Day23Solver(Solver):
    def _run_assembunny(self, instructions_str, initial_registers):
        instructions = [line.split() for line in instructions_str.strip().split('\n')]
        registers = initial_registers.copy()
        pc = 0

        while pc < len(instructions):
            parts = instructions[pc]
            cmd, args = parts[0], parts[1:]

            # Optimization for multiplication loop
            if pc + 5 < len(instructions) and \
               instructions[pc][0] == 'cpy' and \
               instructions[pc+1][0] == 'inc' and \
               instructions[pc+2][0] == 'dec' and \
               instructions[pc+3][0] == 'jnz' and \
               instructions[pc+4][0] == 'dec' and \
               instructions[pc+5][0] == 'jnz':
                
                # cpy b c
                # inc a
                # dec c
                # jnz c -2
                # dec d
                # jnz d -5
                
                b_reg = instructions[pc][1]
                a_reg = instructions[pc+1][1]
                d_reg = instructions[pc+4][1]

                if b_reg in registers and d_reg in registers:
                    b_val = registers[b_reg]
                    d_val = registers[d_reg]
                    registers[a_reg] += b_val * d_val
                    registers[instructions[pc+2][1]] = 0
                    registers[d_reg] = 0
                    pc += 6
                    continue

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
                jump = registers[jump_str] if jump_str in registers else int(jump_str)
                if val != 0:
                    pc += jump
                else:
                    pc += 1
            elif cmd == 'tgl':
                offset_str = args[0]
                offset = registers[offset_str] if offset_str in registers else int(offset_str)
                target_pc = pc + offset
                
                if 0 <= target_pc < len(instructions):
                    target_instr = instructions[target_pc]
                    if len(target_instr) == 2: # one-arg
                        target_instr[0] = 'dec' if target_instr[0] == 'inc' else 'inc'
                    elif len(target_instr) == 3: # two-arg
                        target_instr[0] = 'cpy' if target_instr[0] == 'jnz' else 'jnz'
                pc += 1
        
        return registers['a']

    def part1(self):
        initial_registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
        return self._run_assembunny(self.input_data, initial_registers)

    def part2(self):
        # Part 2 is essentially calculating 12! + (some large number)
        # The assembunny code for part 2 with a=12 is very slow.
        # The code calculates a factorial and adds a product.
        # The relevant part of the code is:
        # cpy a d
        # cpy 0 a
        # cpy b c
        # inc a
        # dec c
        # jnz c -2
        # dec d
        # jnz d -5
        # This is a multiplication loop: a += b * d
        # The initial value of 'a' is 12. The code calculates 12!
        # Then it adds the product of two numbers from the input.
        # Let's analyze the input to find those numbers.
        # The last two lines are often `cpy X Y` `inc Z` or similar.
        # Looking at a typical input, it's `cpy 75 c` and `cpy 78 d` (example)
        # So the result is 12! + 75 * 78
        # Let's find those numbers from the input.
        lines = self.input_data.strip().split('\n')
        # This is a heuristic based on the common structure of this puzzle's input.
        # The multiplication is `c * d` which is added to `a`.
        # The values of c and d are set by instructions like `cpy 75 c`.
        # Let's find them.
        c_val = 0
        d_val = 0
        for line in lines:
            if line.startswith("cpy "):
                parts = line.split()
                if parts[2] == 'c':
                    try:
                        c_val = int(parts[1])
                    except ValueError:
                        pass # It's a register
                if parts[2] == 'd':
                    try:
                        d_val = int(parts[1])
                    except ValueError:
                        pass
        
        # The code calculates 12! + (c_val * d_val)
        # This is a common pattern for this puzzle.
        # Let's find the actual values from the input.
        # The instructions are `cpy 75 c` and `jnz 78 d` in my sample, but it's `cpy 78 d` effectively.
        # The code is complex, but the result is factorial.
        # Let's assume the optimization in the interpreter handles it.
        initial_registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
        return self._run_assembunny(self.input_data, initial_registers)
