from solvers.solver import Solver


class Day01Solver(Solver):
    def part1(self):
        instructions = [s.strip() for s in self.input_data.split(',')]

        x, y = 0, 0
        # 0: N, 1: E, 2: S, 3: W
        direction = 0
        
        # dx, dy for directions N, E, S, W
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for instruction in instructions:
            turn = instruction[0]
            blocks = int(instruction[1:])

            if turn == 'R':
                direction = (direction + 1) % 4
            elif turn == 'L':
                direction = (direction - 1 + 4) % 4
            
            x += blocks * dx[direction]
            y += blocks * dy[direction]

        return abs(x) + abs(y)

    def part2(self):
        instructions = [s.strip() for s in self.input_data.split(',')]

        x, y = 0, 0
        direction = 0
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        visited = {(0, 0)}

        for instruction in instructions:
            turn = instruction[0]
            blocks = int(instruction[1:])

            if turn == 'R':
                direction = (direction + 1) % 4
            elif turn == 'L':
                direction = (direction - 1 + 4) % 4
            
            for _ in range(blocks):
                x += dx[direction]
                y += dy[direction]
                if (x, y) in visited:
                    return abs(x) + abs(y)
                visited.add((x, y))
        
        return -1 # Should not be reached with puzzle input
