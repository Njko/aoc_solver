import re
from collections import defaultdict
from solvers.solver import Solver


class Day10Solver(Solver):
    def _parse_instructions(self, instructions):
        bots = defaultdict(list)
        rules = {}
        for instruction in instructions:
            if match := re.match(r'value (\d+) goes to bot (\d+)', instruction):
                value, bot_id = map(int, match.groups())
                bots[bot_id].append(value)
            elif match := re.match(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', instruction):
                bot_id, low_type, low_id, high_type, high_id = match.groups()
                rules[int(bot_id)] = (low_type, int(low_id), high_type, int(high_id))
        return bots, rules

    def _run_simulation(self, instructions):
        bots, rules = self._parse_instructions(instructions)
        outputs = defaultdict(list)
        part1_answer = None

        queue = [bot_id for bot_id, chips in bots.items() if len(chips) == 2]
        
        while queue:
            bot_id = queue.pop(0)
            
            low_chip, high_chip = sorted(bots[bot_id])
            bots[bot_id] = []

            if low_chip == 17 and high_chip == 61:
                part1_answer = bot_id

            low_type, low_id, high_type, high_id = rules[bot_id]

            for chip, dest_type, dest_id in [(low_chip, low_type, low_id), (high_chip, high_type, high_id)]:
                if dest_type == 'bot':
                    bots[dest_id].append(chip)
                    if len(bots[dest_id]) == 2:
                        queue.append(dest_id)
                else:
                    outputs[dest_id].append(chip)
        
        return part1_answer, outputs

    def part1(self):
        instructions = self.input_data.strip().split('\n')
        part1_answer, _ = self._run_simulation(instructions)
        return part1_answer

    def part2(self):
        instructions = self.input_data.strip().split('\n')
        _, outputs = self._run_simulation(instructions)
        return outputs[0][0] * outputs[1][0] * outputs[2][0]
