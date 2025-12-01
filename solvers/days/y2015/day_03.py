from aoc_agent.solver import Solver

class DaySolver(Solver):
    def part1(self) -> "str | int":
        x, y = 0, 0
        visited = {(0, 0)}
        
        for move in self.input_data:
            if move == '^': y += 1
            elif move == 'v': y -= 1
            elif move == '>': x += 1
            elif move == '<': x -= 1
            visited.add((x, y))
            
        return len(visited)

    def part2(self) -> "str | int":
        santa_x, santa_y = 0, 0
        robo_x, robo_y = 0, 0
        visited = {(0, 0)}
        
        for i, move in enumerate(self.input_data):
            if i % 2 == 0:
                # Santa moves
                if move == '^': santa_y += 1
                elif move == 'v': santa_y -= 1
                elif move == '>': santa_x += 1
                elif move == '<': santa_x -= 1
                visited.add((santa_x, santa_y))
            else:
                # Robo-Santa moves
                if move == '^': robo_y += 1
                elif move == 'v': robo_y -= 1
                elif move == '>': robo_x += 1
                elif move == '<': robo_x -= 1
                visited.add((robo_x, robo_y))
                
        return len(visited)
