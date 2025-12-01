from aoc_agent.solver import Solver
import re

class DaySolver(Solver):
    def parse(self):
        sues = {}
        for line in self.lines:
            # Sue 1: goldfish: 6, trees: 9, akitas: 0
            match = re.match(r"Sue (\d+): (.*)", line)
            if match:
                num = int(match.group(1))
                props_str = match.group(2)
                props = {}
                for p in props_str.split(", "):
                    k, v = p.split(": ")
                    props[k] = int(v)
                sues[num] = props
        return sues

    def part1(self) -> "str | int":
        target = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1
        }
        
        sues = self.parse()
        
        for num, props in sues.items():
            match = True
            for k, v in props.items():
                if target[k] != v:
                    match = False
                    break
            if match:
                return num
        return -1

    def part2(self) -> "str | int":
        target = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1
        }
        
        sues = self.parse()
        
        for num, props in sues.items():
            match = True
            for k, v in props.items():
                if k in ["cats", "trees"]:
                    if v <= target[k]:
                        match = False
                        break
                elif k in ["pomeranians", "goldfish"]:
                    if v >= target[k]:
                        match = False
                        break
                else:
                    if target[k] != v:
                        match = False
                        break
            if match:
                return num
        return -1
