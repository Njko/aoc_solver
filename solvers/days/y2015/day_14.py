from aoc_agent.solver import Solver
import re

class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.distance = 0
        self.points = 0
        self.state = "flying"
        self.time_in_state = 0

    def tick(self):
        if self.state == "flying":
            self.distance += self.speed
            self.time_in_state += 1
            if self.time_in_state == self.fly_time:
                self.state = "resting"
                self.time_in_state = 0
        else:
            self.time_in_state += 1
            if self.time_in_state == self.rest_time:
                self.state = "flying"
                self.time_in_state = 0

class DaySolver(Solver):
    def parse(self):
        reindeers = []
        for line in self.lines:
            # Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
            match = re.search(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
            if match:
                name = match.group(1)
                speed = int(match.group(2))
                fly_time = int(match.group(3))
                rest_time = int(match.group(4))
                reindeers.append(Reindeer(name, speed, fly_time, rest_time))
        return reindeers

    def part1(self) -> "str | int":
        reindeers = self.parse()
        time_limit = 2503
        
        # We can calculate distance directly without simulation for Part 1
        max_dist = 0
        for r in reindeers:
            cycle_time = r.fly_time + r.rest_time
            full_cycles = time_limit // cycle_time
            remaining_time = time_limit % cycle_time
            
            dist = full_cycles * r.speed * r.fly_time
            dist += min(remaining_time, r.fly_time) * r.speed
            max_dist = max(max_dist, dist)
            
        return max_dist

    def part2(self) -> "str | int":
        reindeers = self.parse()
        time_limit = 2503
        
        for _ in range(time_limit):
            for r in reindeers:
                r.tick()
            
            max_dist = max(r.distance for r in reindeers)
            for r in reindeers:
                if r.distance == max_dist:
                    r.points += 1
                    
        return max(r.points for r in reindeers)
