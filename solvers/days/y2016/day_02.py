from solvers.solver import Solver


class Day02Solver(Solver):
    def part1(self):
        lines = self.input_data.strip().split('\n')
        
        keypad = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        
        x, y = 1, 1 # Start at 5
        code = ""
        
        for line in lines:
            for move in line:
                if move == 'U':
                    y = max(0, y - 1)
                elif move == 'D':
                    y = min(2, y + 1)
                elif move == 'L':
                    x = max(0, x - 1)
                elif move == 'R':
                    x = min(2, x + 1)
            code += str(keypad[y][x])
            
        return code

    def part2(self):
        lines = self.input_data.strip().split('\n')
        
        keypad = {
            (2, 0): '1',
            (1, 1): '2', (2, 1): '3', (3, 1): '4',
            (0, 2): '5', (1, 2): '6', (2, 2): '7', (3, 2): '8', (4, 2): '9',
            (1, 3): 'A', (2, 3): 'B', (3, 3): 'C',
            (2, 4): 'D'
        }
        
        x, y = 0, 2 # Start at 5
        code = ""
        
        for line in lines:
            for move in line:
                nx, ny = x, y
                if move == 'U':
                    ny -= 1
                elif move == 'D':
                    ny += 1
                elif move == 'L':
                    nx -= 1
                elif move == 'R':
                    nx += 1
                
                if (nx, ny) in keypad:
                    x, y = nx, ny

            code += keypad[(x, y)]
            
        return code
