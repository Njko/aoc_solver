import re
import math
from itertools import combinations
from fractions import Fraction
import itertools

class Day10Solver:
    def __init__(self, input_data: str):
        self.input_data = input_data.strip()
        self.machines = self._parse_input()

    def _parse_input(self):
        # Format: [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
        machines = []
        for line in self.input_data.split('\n'):
            line = line.strip()
            if not line:
                continue
            
            # Extract target lights
            lights_match = re.search(r'\[([.#]+)\]', line)
            
            # Extract joltages
            jolt_match = re.search(r'\{([\d,]+)\}', line)
            
            if not lights_match or not jolt_match:
                continue
                
            lights_str = lights_match.group(1)
            target_lights = [1 if c == '#' else 0 for c in lights_str]
            num_lights = len(target_lights)
            
            jolt_str = jolt_match.group(1)
            target_joltages = [int(x) for x in jolt_str.split(',')]
            num_counters = len(target_joltages)
            
            # Extract buttons
            buttons_raw = []
            # Find all (x,y,z) groups
            button_matches = re.finditer(r'\(([\d,]+)\)', line)
            for bm in button_matches:
                indices = [int(x) for x in bm.group(1).split(',')]
                buttons_raw.append(indices)
            
            # Button vectors for Lights (GF2)
            buttons_lights = []
            for indices in buttons_raw:
                vec = [0] * num_lights
                for idx in indices:
                    if 0 <= idx < num_lights:
                        vec[idx] = 1
                buttons_lights.append(vec)
                
            # Button vectors for Joltages (Integer)
            buttons_jolts = []
            for indices in buttons_raw:
                vec = [0] * num_counters
                for idx in indices:
                    if 0 <= idx < num_counters:
                        vec[idx] = 1
                buttons_jolts.append(vec)

            machines.append({
                'target_lights': target_lights,
                'buttons_lights': buttons_lights,
                'num_lights': num_lights,
                'target_joltages': target_joltages,
                'buttons_jolts': buttons_jolts,
                'num_counters': num_counters
            })
        return machines

    def solve_machine_part1(self, machine):
        target = machine['target_lights'] # Vector B
        buttons = machine['buttons_lights'] # Columns of Matrix A
        
        num_rows = machine['num_lights']
        num_cols = len(buttons)
        
        # Build Augmented Matrix [A | B]
        # Rows correspond to lights, Cols to buttons + target
        matrix = []
        for r in range(num_rows):
            row = [b[r] for b in buttons] + [target[r]]
            matrix.append(row)
            
        # Gaussian Elimination over GF(2)
        pivot_row = 0
        pivot_cols = [] # List of pivot column indices
        
        for col in range(num_cols):
            if pivot_row >= num_rows:
                break
                
            # Find row with 1 in this column
            pivot = -1
            for r in range(pivot_row, num_rows):
                if matrix[r][col] == 1:
                    pivot = r
                    break
            
            if pivot == -1:
                continue # No pivot in this column, it's a free variable
                
            # Swap rows
            matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
            pivot_cols.append(col)
            
            # Eliminate other rows
            for r in range(num_rows):
                if r != pivot_row and matrix[r][col] == 1:
                    # XOR row
                    for c in range(col, num_cols + 1):
                        matrix[r][c] ^= matrix[pivot_row][c]
            
            pivot_row += 1
            
        # Check consistency
        for r in range(num_rows):
            if matrix[r][-1] == 1:
                is_zero_row = True
                for c in range(num_cols):
                    if matrix[r][c] == 1:
                        is_zero_row = False
                        break
                if is_zero_row:
                    return float('inf') # No solution
                    
        # Extract solution
        pivots_set = set(pivot_cols)
        free_vars = [c for c in range(num_cols) if c not in pivots_set]
        
        min_weight = float('inf')
        
        # Optimize if too many free vars
        if len(free_vars) > 18:
             # Basic heuristic or just return partial
             pass

        for free_vals in itertools.product([0, 1], repeat=len(free_vars)):
            assignment = [0] * num_cols
            for i, f_idx in enumerate(free_vars):
                assignment[f_idx] = free_vals[i]
            
            # Back-substitution
            for r in range(len(pivot_cols) - 1, -1, -1):
                col = pivot_cols[r]
                val = matrix[r][-1]
                for c in range(col + 1, num_cols):
                    if matrix[r][c] == 1:
                        val ^= assignment[c]
                assignment[col] = val
                
            weight = sum(assignment)
            if weight < min_weight:
                min_weight = weight
                
        return min_weight

    def solve_machine_part2(self, machine):
        # Solve Ax = b for non-negative integers x
        target = machine['target_joltages']
        buttons = machine['buttons_jolts']
        
        num_rows = machine['num_counters']
        num_cols = len(buttons)
        
        # Build Matrix with Fractions
        matrix = []
        for r in range(num_rows):
            row = [Fraction(b[r]) for b in buttons] + [Fraction(target[r])]
            matrix.append(row)
            
        # Gaussian Elimination over Rationals
        pivot_row = 0
        pivot_cols = []
        
        for col in range(num_cols):
            if pivot_row >= num_rows:
                break
            
            pivot = -1
            for r in range(pivot_row, num_rows):
                if matrix[r][col] != 0:
                    pivot = r
                    break
            
            if pivot == -1:
                continue
            
            matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
            pivot_cols.append(col)
            
            # Normalize pivot row
            pivot_val = matrix[pivot_row][col]
            for c in range(col, num_cols + 1):
                matrix[pivot_row][c] /= pivot_val
                
            # Eliminate other rows
            for r in range(num_rows):
                if r != pivot_row and matrix[r][col] != 0:
                    factor = matrix[r][col]
                    for c in range(col, num_cols + 1):
                        matrix[r][c] -= factor * matrix[pivot_row][c]
            
            pivot_row += 1

        # Check consistency
        for r in range(num_rows):
            is_zero_lhs = all(matrix[r][c] == 0 for c in range(num_cols))
            if is_zero_lhs and matrix[r][-1] != 0:
                return float('inf')

        pivots_set = set(pivot_cols)
        free_vars = [c for c in range(num_cols) if c not in pivots_set]
        
        # Pre-compile equations for back-substitution to Integer Math
        # For each pivot col, we have:
        # matrix[r][col] * x_col + sum(matrix[r][k] * x_k) = matrix[r][-1]
        # Since RREF, matrix[r][col] is 1.
        # x_col = matrix[r][-1] - sum(matrix[r][k] * x_k)
        # We only care about k > col. In RREF, non-zero entries are free variables.
        
        # We want to store: x_col = Constant - sum(Coeff_free * x_free)
        # Store as: (Constant_num, Constant_den, List[(Coeff_num, Coeff_den, free_idx)])
        
        # Actually, let's just use raw float for speed if usually precision isn't issue? 
        # No, Fraction is safer. Let's converting to common denominator.
        
        compiled_eqs = []
        # Process pivots in reverse order for dependency? 
        # Actually in RREF, each pivot row is independent of other pivots for the definition!
        # x_p is defined purely by free variables (and constants).
        
        for r in range(len(pivot_cols)):
            col = pivot_cols[r]
            # row r defines x_col
            constant = matrix[r][-1]
            coeffs = []
            for c in range(col + 1, num_cols):
                if matrix[r][c] != 0:
                    coeffs.append((matrix[r][c], c))
            
            # x_col = constant - sum(coeff * x_c)
            # x_c must be a free variable because if it was a pivot, it would be 0 in this row (RREF).
            
            # Optimization: Convert to integer arithmetic
            # Find LCM of denominators
            denoms = [constant.denominator] + [c[0].denominator for c in coeffs]
            lcm = 1
            for d in denoms:
                lcm = math.lcm(lcm, d)
                
            # Scale everything by LCM
            # x_col * LCM = (constant * LCM) - sum((coeff * LCM) * x_free)
            # We need RHS % LCM == 0 and RHS / LCM >= 0
            
            int_const = int(constant * lcm)
            int_coeffs = [(int(c[0] * lcm), c[1]) for c in coeffs]
            compiled_eqs.append((col, lcm, int_const, int_coeffs))

        # Map free var index to assignment index
        free_var_map = {f: i for i, f in enumerate(free_vars)}
        compiled_eqs_mapped = []
        for col, lcm, int_const, int_coeffs in compiled_eqs:
            # Filter int_coeffs to only include free vars (should be all of them)
            mapped_coeffs = []
            for val, f_idx in int_coeffs:
                if f_idx in free_vars:
                    mapped_coeffs.append((val, free_var_map[f_idx]))
            compiled_eqs_mapped.append((col, lcm, int_const, mapped_coeffs))

        min_presses = float('inf')
        
        # Adaptive search limits
        if not free_vars:
             search_limit = 1
        elif len(free_vars) <= 1:
            search_limit = max(max(target), 500) + 10
        elif len(free_vars) <= 3:
            search_limit = 200
        else:
            search_limit = 30
            
        for free_vals in itertools.product(range(search_limit), repeat=len(free_vars)):
            # Check validity
            possible = True
            current_sum = sum(free_vals)
            if current_sum >= min_presses: # Pruning
                continue
                
            pivot_sum = 0
            
            for col, lcm, int_const, mapped_coeffs in compiled_eqs_mapped:
                val = int_const
                for coeff, f_idx_mapped in mapped_coeffs:
                    val -= coeff * free_vals[f_idx_mapped]
                
                # Check divisibility and non-negativity
                if val < 0 or val % lcm != 0:
                    possible = False
                    break
                pivot_sum += val // lcm
                
            if possible:
                total_s = current_sum + pivot_sum
                if total_s < min_presses:
                    min_presses = total_s
        
        if min_presses == float('inf'):
            print(f"Failed to solve machine with {num_cols} cols, {num_rows} rows. Free vars: {len(free_vars)}.")
            
        return min_presses

    def part1(self) -> "str | int":
        total = 0
        for m in self.machines:
            res = self.solve_machine_part1(m)
            if res != float('inf'):
                total += res
        return total

    def part2(self) -> "str | int":
        total = 0
        for m in self.machines:
            res = self.solve_machine_part2(m)
            if res == float('inf'):
                print("No solution for machine in Part 2")
            else:
                total += res
        return total
