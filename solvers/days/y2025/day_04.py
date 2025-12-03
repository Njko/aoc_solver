from solvers.solver import Solver

class Day04Solver(Solver):
    def part1(self) -> "str | int":
        grid = [list(line) for line in self.input_data.strip().split('\n')]
        rows = len(grid)
        cols = len(grid[0])
        accessible_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    neighbors = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols:
                                if grid[nr][nc] == '@':
                                    neighbors += 1
                    
                    if neighbors < 4:
                        accessible_count += 1
                        
        return accessible_count

    def part2(self) -> "str | int":
        grid = [list(line) for line in self.input_data.strip().split('\n')]
        rows = len(grid)
        cols = len(grid[0])
        total_removed = 0
        
        while True:
            to_remove = []
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == '@':
                        neighbors = 0
                        for dr in [-1, 0, 1]:
                            for dc in [-1, 0, 1]:
                                if dr == 0 and dc == 0:
                                    continue
                                nr, nc = r + dr, c + dc
                                if 0 <= nr < rows and 0 <= nc < cols:
                                    if grid[nr][nc] == '@':
                                        neighbors += 1
                        
                        if neighbors < 4:
                            to_remove.append((r, c))
            
            if not to_remove:
                break
                
            total_removed += len(to_remove)
            for r, c in to_remove:
                grid[r][c] = '.' # Mark as removed (using '.' or 'x' doesn't matter as long as it's not '@')
                
        return total_removed
