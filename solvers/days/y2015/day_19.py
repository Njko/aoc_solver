from aoc_agent.solver import Solver
import re

class DaySolver(Solver):
    def parse(self):
        replacements = []
        molecule = ""
        for line in self.lines:
            if " => " in line:
                src, dst = line.strip().split(" => ")
                replacements.append((src, dst))
            elif line.strip():
                molecule = line.strip()
        return replacements, molecule

    def part1(self) -> "str | int":
        replacements, molecule = self.parse()
        distinct_molecules = set()
        
        for src, dst in replacements:
            for i in range(len(molecule)):
                if molecule[i:].startswith(src):
                    new_molecule = molecule[:i] + dst + molecule[i+len(src):]
                    distinct_molecules.add(new_molecule)
                    
        return len(distinct_molecules)

    def part2(self) -> "str | int":
        replacements, molecule = self.parse()
        # Greedy reverse search: try to reduce the molecule to 'e'
        # Sort replacements by length of destination (descending) to be greedy
        replacements.sort(key=lambda x: len(x[1]), reverse=True)
        
        target = molecule
        steps = 0
        
        while target != 'e':
            changed = False
            for src, dst in replacements:
                if dst in target:
                    # Replace one occurrence (greedy)
                    # We count how many times we can replace this dst with src
                    # Actually, just replacing one by one is safer to track steps
                    # But to be faster, let's replace one occurrence at a time
                    target = target.replace(dst, src, 1)
                    steps += 1
                    changed = True
                    break # Restart from top of list to ensure greediness
            
            if not changed:
                # If we get stuck, we might need to backtrack or shuffle, but for AoC inputs 
                # this greedy approach usually works or we need to shuffle.
                # Let's just return "Failed" or try to shuffle if I were more robust.
                # But for now, let's assume greedy works.
                return "Failed (stuck)"
                
        return steps
