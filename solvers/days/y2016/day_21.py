import re
from collections import deque
from solvers.solver import Solver


class Day21Solver(Solver):
    def _scramble(self, s, instructions, unscramble=False):
        password = list(s)
        ops = instructions.strip().split('\n')
        
        if unscramble:
            ops = ops[::-1]

        for op in ops:
            if match := re.match(r'swap position (\d+) with position (\d+)', op):
                x, y = map(int, match.groups())
                password[x], password[y] = password[y], password[x]
            elif match := re.match(r'swap letter (\w) with letter (\w)', op):
                x, y = match.groups()
                ix, iy = password.index(x), password.index(y)
                password[ix], password[iy] = password[iy], password[ix]
            elif match := re.match(r'rotate (left|right) (\d+) steps?', op):
                direction, steps = match.groups()
                steps = int(steps)
                d = deque(password)
                if (direction == 'left' and not unscramble) or (direction == 'right' and unscramble):
                    d.rotate(-steps)
                else:
                    d.rotate(steps)
                password = list(d)
            elif match := re.match(r'rotate based on position of letter (\w)', op):
                letter = match.group(1)
                if unscramble:
                    # This is the tricky part. We need to find the original index.
                    # The forward rotation is right by `rot = 1 + idx + (1 if idx >= 4 else 0)`.
                    # The inverse is a left rotation.
                    # We can pre-calculate the inverse rotations.
                    # new_idx = (old_idx + rot) % 8
                    # 0 -> 1
                    # 1 -> 3
                    # 2 -> 5
                    # 3 -> 7
                    # 4 -> 2 + 4 = 6 -> 10 % 8 = 2
                    # 5 -> 2 + 5 = 7 -> 12 % 8 = 4
                    # 6 -> 2 + 6 = 8 -> 14 % 8 = 6
                    # 7 -> 2 + 7 = 9 -> 16 % 8 = 0
                    #
                    # new_idx: old_idx
                    # 1: 0 (left 1)
                    # 3: 1 (left 2)
                    # 5: 2 (left 3)
                    # 7: 3 (left 4)
                    # 2: 4 (left 6)
                    # 4: 5 (left 7)
                    # 6: 6 (left 8 = 0)
                    # 0: 7 (left 9 = 1)
                    
                    # Let's try a simpler way: test each possible final index
                    # and see what left rotation it corresponds to.
                    current_idx = password.index(letter)
                    
                    # This mapping is fixed for a password of length 8
                    # new_pos: left_rotation_amount
                    unrotate_map = {
                        1: 1, 3: 2, 5: 3, 7: 4,
                        2: 6, 4: 7, 6: 0, 0: 1,
                    }
                    # Wait, the above map is wrong. Let's re-derive.
                    # new_idx = (old_idx + 1 + old_idx + (1 if old_idx >= 4 else 0)) % 8
                    # old | rot | new
                    # 0   | 1   | 1
                    # 1   | 2   | 3
                    # 2   | 3   | 5
                    # 3   | 4   | 7
                    # 4   | 6   | 2
                    # 5   | 7   | 4
                    # 6   | 8   | 6
                    # 7   | 9   | 0
                    #
                    # So, to reverse, if we are at new_idx, what was old_idx?
                    # new_idx: old_idx
                    # 0: 7
                    # 1: 0
                    # 2: 4
                    # 3: 1
                    # 4: 5
                    # 5: 2
                    # 6: 6
                    # 7: 3
                    # This means if current_idx is 0, old_idx was 7.
                    # To get from 0 to 7, we rotate right 7, or left 1.
                    # Let's check: old=7, rot=9, new=(7+9)%8 = 16%8=0. Correct.
                    # if current_idx is 1, old_idx was 0.
                    # To get from 1 to 0, we rotate left 1.
                    # Let's check: old=0, rot=1, new=(0+1)%8=1. Correct.
                    # if current_idx is 2, old_idx was 4.
                    # To get from 2 to 4, we rotate right 2, or left 6.
                    # Let's check: old=4, rot=6, new=(4+6)%8=2. Correct.
                    
                    # The amount of left rotation needed to undo the operation
                    # based on the *current* index of the letter.
                    left_rotations = {
                        0: 1, 1: 1, 2: 6, 3: 2, 4: 7, 5: 3, 6: 0, 7: 4
                    }
                    
                    rot = left_rotations[current_idx]
                    d = deque(password)
                    d.rotate(-rot)
                    password = list(d)
                else:
                    idx = password.index(letter)
                    rotations = 1 + idx + (1 if idx >= 4 else 0)
                    d = deque(password)
                    d.rotate(rotations)
                    password = list(d)
            elif match := re.match(r'reverse positions (\d+) through (\d+)', op):
                x, y = map(int, match.groups())
                sub = password[x:y+1]
                sub.reverse()
                password = password[:x] + sub + password[y+1:]
            elif match := re.match(r'move position (\d+) to position (\d+)', op):
                x, y = map(int, match.groups())
                if unscramble:
                    x, y = y, x
                char = password.pop(x)
                password.insert(y, char)
        
        return "".join(password)

    def part1(self):
        return self._scramble('abcdefgh', self.input_data)

    def part2(self):
        return self._scramble('fbgdceah', self.input_data, unscramble=True)
