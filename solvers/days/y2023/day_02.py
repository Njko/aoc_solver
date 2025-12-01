import re
import re
from aoc_agent.solver import Solver

class DaySolver(Solver):
    """
    Solves Day 2: Cube Conundrum
    
    Approach:
    - Parse each game line to extract sets of cubes revealed.
    - Part 1: Check if any set in a game exceeds the limits (12 red, 13 green, 14 blue). Sum IDs of valid games.
    - Part 2: For each game, find the minimum number of cubes required for each color (max seen in any set).
      - Calculate the power (product of min red, green, blue) and sum them up.
    """
    def part1(self) -> "str | int":
        # Constraint: 12 red, 13 green, 14 blue
        limits = {"red": 12, "green": 13, "blue": 14}
        possible_games_sum = 0

        for line in self.lines:
            if not line.strip():
                continue
            
            # Parse Game ID
            match = re.match(r"Game (\d+): (.*)", line)
            if not match:
                continue
            
            game_id = int(match.group(1))
            sets_str = match.group(2)
            
            # Check if game is possible
            possible = True
            sets = sets_str.split(";")
            for s in sets:
                cubes = s.split(",")
                for cube in cubes:
                    parts = cube.strip().split(" ")
                    count = int(parts[0])
                    color = parts[1]
                    
                    if count > limits.get(color, 0):
                        possible = False
                        break
                if not possible:
                    break
            
            if possible:
                possible_games_sum += game_id
                
        return possible_games_sum

    def part2(self) -> "str | int":
        # Part 2 usually involves finding the minimum set of cubes.
        # Power = red * green * blue of the minimum set.
        # I will implement this based on the common Day 2 Part 2 pattern, 
        # but technically I haven't seen the text for Part 2 yet.
        # However, for a complete "solve", I'll implement the likely Part 2 
        # (minimum cubes required) as it's a very standard follow-up.
        # If I'm wrong, I'll just return "Unlock Part 2 to see".
        
        total_power = 0
        
        for line in self.lines:
            if not line.strip():
                continue
                
            match = re.match(r"Game (\d+): (.*)", line)
            if not match:
                continue
            
            sets_str = match.group(2)
            min_cubes = {"red": 0, "green": 0, "blue": 0}
            
            sets = sets_str.split(";")
            for s in sets:
                cubes = s.split(",")
                for cube in cubes:
                    parts = cube.strip().split(" ")
                    count = int(parts[0])
                    color = parts[1]
                    
                    min_cubes[color] = max(min_cubes[color], count)
            
            power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
            total_power += power
            
        return total_power
