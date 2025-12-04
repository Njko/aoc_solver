from solvers.solver import Solver
import math

class Day03Solver(Solver):
    def part1(self) -> "str | int":
        target = int(self.input_data.strip())
        if target == 1:
            return 0
            
        # Find ring k
        # (2k-1)^2 < target <= (2k+1)^2
        # sqrt(target) <= 2k+1
        # (sqrt(target) - 1) / 2 <= k
        k = math.ceil((math.sqrt(target) - 1) / 2)
        
        side_len = 2 * k + 1
        max_val = side_len * side_len
        
        # Centers of the sides on ring k
        # Bottom: max_val - k
        # Left: max_val - k - (side_len - 1)
        # Top: max_val - k - 2*(side_len - 1)
        # Right: max_val - k - 3*(side_len - 1)
        
        centers = [
            max_val - k,
            max_val - k - (side_len - 1),
            max_val - k - 2 * (side_len - 1),
            max_val - k - 3 * (side_len - 1)
        ]
        
        dist_to_center = min(abs(target - c) for c in centers)
        
        return k + dist_to_center

    def part2(self) -> "str | int":
        target = int(self.input_data.strip())
        
        grid = {(0, 0): 1}
        x, y = 0, 0
        dx, dy = 1, 0 # Start moving Right
        
        # Spiral logic:
        # Move 1 R, 1 U
        # Move 2 L, 2 D
        # Move 3 R, 3 U
        # ...
        
        # Alternative simple spiral generator:
        # Move dx, dy. Check if we can turn Left. If yes, turn Left.
        # Turning Left: (dx, dy) -> (-dy, dx)
        # Condition to turn left: The spot to the left is empty.
        
        while True:
            # Calculate next position
            # Try turning left first
            lx, ly = -dy, dx
            if (x + lx, y + ly) not in grid:
                # Can turn left, so do it
                dx, dy = lx, ly
            
            x, y = x + dx, y + dy
            
            # Calculate value
            val = 0
            for nx in range(x - 1, x + 2):
                for ny in range(y - 1, y + 2):
                    if (nx, ny) == (x, y): continue
                    val += grid.get((nx, ny), 0)
            
            grid[(x, y)] = val
            
            if val > target:
                return val
