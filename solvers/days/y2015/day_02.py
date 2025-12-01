from aoc_agent.solver import Solver

class DaySolver(Solver):
    def part1(self) -> "str | int":
        total_paper = 0
        for line in self.lines:
            l, w, h = map(int, line.split('x'))
            sides = [l*w, w*h, h*l]
            surface_area = 2 * sum(sides)
            slack = min(sides)
            total_paper += surface_area + slack
        return total_paper

    def part2(self) -> "str | int":
        # Part 2 is likely ribbon, but I'll wait or implement if I know it.
        # Ribbon: smallest perimeter + volume
        # I'll implement it just in case, or leave it.
        # Let's check if I can just implement it.
        # If the user hasn't unlocked it, they won't see the description, but the code will be ready.
        total_ribbon = 0
        for line in self.lines:
            l, w, h = map(int, line.split('x'))
            dims = sorted([l, w, h])
            wrap = 2 * (dims[0] + dims[1])
            bow = l * w * h
            total_ribbon += wrap + bow
        return total_ribbon
