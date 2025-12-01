from itertools import combinations
from collections import deque
from solvers.solver import Solver
import re


class Day11Solver(Solver):
    def _parse_input(self, input_data):
        items = {}
        item_idx = 0
        initial_state = [set() for _ in range(4)]

        for i, line in enumerate(input_data.strip().split('\n')):
            for generator in re.findall(r'(\w+) generator', line):
                if generator not in items:
                    items[generator] = item_idx
                    item_idx += 1
                initial_state[i].add((items[generator], 'g'))
            for microchip in re.findall(r'(\w+)-compatible microchip', line):
                if microchip not in items:
                    items[microchip] = item_idx
                    item_idx += 1
                initial_state[i].add((items[microchip], 'm'))
        
        self.num_items = len(items)
        return tuple(frozenset(s) for s in initial_state)

    def _is_valid(self, floor):
        generators = {item[0] for item in floor if item[1] == 'g'}
        microchips = {item[0] for item in floor if item[1] == 'm'}
        
        if not generators or not microchips:
            return True
            
        # If there are generators, any microchip present must have its generator present.
        return microchips.issubset(generators)

    def _get_state_representation(self, elevator_floor, floors):
        # Canonical representation of the state to reduce state space.
        # The identity of the pairs doesn't matter, only their relative positions.
        pairs = sorted([
            (
                next(f_idx for f_idx, f in enumerate(floors) if (p_idx, 'm') in f),
                next(f_idx for f_idx, f in enumerate(floors) if (p_idx, 'g') in f)
            )
            for p_idx in range(self.num_items)
        ])
        return (elevator_floor, tuple(pairs))

    def _solve(self, initial_floors):
        initial_state = (0, initial_floors)
        
        queue = deque([(initial_state, 0)])
        
        initial_repr = self._get_state_representation(0, initial_floors)
        visited = {initial_repr}

        while queue:
            (elevator_floor, floors), steps = queue.popleft()

            if elevator_floor == 3 and all(len(f) == 0 for f in floors[:3]):
                 return steps

            # Try moving up or down
            for move in [1, -1]:
                next_floor_idx = elevator_floor + move
                if 0 <= next_floor_idx < 4:
                    current_floor_items = list(floors[elevator_floor])
                    
                    # Move 1 or 2 items
                    for num_to_move in [1, 2]:
                        if len(current_floor_items) < num_to_move:
                            continue
                        
                        for items_to_move in combinations(current_floor_items, num_to_move):
                            new_floors = list(floors)
                            
                            new_current_floor = set(new_floors[elevator_floor])
                            new_next_floor = set(new_floors[next_floor_idx])

                            for item in items_to_move:
                                new_current_floor.remove(item)
                                new_next_floor.add(item)

                            if self._is_valid(new_current_floor) and self._is_valid(new_next_floor):
                                new_floors[elevator_floor] = frozenset(new_current_floor)
                                new_floors[next_floor_idx] = frozenset(new_next_floor)
                                
                                new_floors_tuple = tuple(new_floors)
                                
                                new_repr = self._get_state_representation(next_floor_idx, new_floors_tuple)

                                if new_repr not in visited:
                                    visited.add(new_repr)
                                    new_state = (next_floor_idx, new_floors_tuple)
                                    queue.append((new_state, steps + 1))
        return -1

    def part1(self):
        initial_floors = self._parse_input(self.input_data)
        return self._solve(initial_floors)

    def part2(self):
        initial_floors_list = list(self._parse_input(self.input_data))
        
        # Add elerium and dilithium items
        elerium_idx = self.num_items
        dilithium_idx = self.num_items + 1
        self.num_items += 2

        new_first_floor = set(initial_floors_list[0])
        new_first_floor.add((elerium_idx, 'g'))
        new_first_floor.add((elerium_idx, 'm'))
        new_first_floor.add((dilithium_idx, 'g'))
        new_first_floor.add((dilithium_idx, 'm'))
        
        initial_floors_list[0] = frozenset(new_first_floor)
        
        return self._solve(tuple(initial_floors_list))
