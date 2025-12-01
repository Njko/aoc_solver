import hashlib
from solvers.solver import Solver


class Day05Solver(Solver):
    def part1(self):
        door_id = self.input_data.strip()
        password = ""
        index = 0
        while len(password) < 8:
            test_string = f"{door_id}{index}"
            result = hashlib.md5(test_string.encode()).hexdigest()
            if result.startswith("00000"):
                password += result[5]
            index += 1
        return password

    def part2(self):
        door_id = self.input_data.strip()
        password = ['_'] * 8
        index = 0
        found_chars = 0
        
        while found_chars < 8:
            test_string = f"{door_id}{index}"
            result = hashlib.md5(test_string.encode()).hexdigest()
            if result.startswith("00000"):
                position_char = result[5]
                if '0' <= position_char <= '7':
                    position = int(position_char)
                    if password[position] == '_':
                        password[position] = result[6]
                        found_chars += 1
            index += 1
            
        return "".join(password)
