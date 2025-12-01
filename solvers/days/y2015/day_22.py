from aoc_agent.solver import Solver
import heapq

class DaySolver(Solver):
    def parse(self):
        boss = {}
        for line in self.lines:
            k, v = line.split(": ")
            boss[k] = int(v)
        return boss

    def solve_rpg(self, boss_stats, hard_mode=False):
        boss_hp_start = boss_stats["Hit Points"]
        boss_damage = boss_stats["Damage"]
        
        # State: (mana_spent, player_hp, player_mana, boss_hp, shield_timer, poison_timer, recharge_timer, is_player_turn)
        # We prioritize by mana_spent (min-heap)
        queue = [(0, 50, 500, boss_hp_start, 0, 0, 0, True)]
        visited = set()
        
        min_mana = float('inf')
        
        while queue:
            mana_spent, p_hp, p_mana, b_hp, shield, poison, recharge, is_player_turn = heapq.heappop(queue)
            
            # Pruning
            if mana_spent >= min_mana:
                continue
            
            state_key = (p_hp, p_mana, b_hp, shield, poison, recharge, is_player_turn)
            if state_key in visited:
                continue
            visited.add(state_key)
            
            # Hard Mode effect
            if hard_mode and is_player_turn:
                p_hp -= 1
                if p_hp <= 0:
                    continue
            
            # Apply Effects
            armor = 0
            if shield > 0:
                armor = 7
                shield -= 1
            
            if poison > 0:
                b_hp -= 3
                poison -= 1
            
            if recharge > 0:
                p_mana += 101
                recharge -= 1
                
            # Check win/loss after effects
            if b_hp <= 0:
                min_mana = min(min_mana, mana_spent)
                continue
                
            if is_player_turn:
                # Player Turn: Cast a spell
                
                # Magic Missile: 53 mana, 4 damage
                if p_mana >= 53:
                    heapq.heappush(queue, (mana_spent + 53, p_hp, p_mana - 53, b_hp - 4, shield, poison, recharge, False))
                    
                # Drain: 73 mana, 2 damage, 2 heal
                if p_mana >= 73:
                    heapq.heappush(queue, (mana_spent + 73, p_hp + 2, p_mana - 73, b_hp - 2, shield, poison, recharge, False))
                    
                # Shield: 113 mana, 6 turns (if not active)
                if p_mana >= 113 and shield == 0:
                    heapq.heappush(queue, (mana_spent + 113, p_hp, p_mana - 113, b_hp, 6, poison, recharge, False))
                    
                # Poison: 173 mana, 6 turns (if not active)
                if p_mana >= 173 and poison == 0:
                    heapq.heappush(queue, (mana_spent + 173, p_hp, p_mana - 173, b_hp, shield, 6, recharge, False))
                    
                # Recharge: 229 mana, 5 turns (if not active)
                if p_mana >= 229 and recharge == 0:
                    heapq.heappush(queue, (mana_spent + 229, p_hp, p_mana - 229, b_hp, shield, poison, 5, False))
                    
            else:
                # Boss Turn: Attack
                dmg = max(1, boss_damage - armor)
                p_hp -= dmg
                
                if p_hp > 0:
                    heapq.heappush(queue, (mana_spent, p_hp, p_mana, b_hp, shield, poison, recharge, True))
                    
        return min_mana

    def part1(self) -> "str | int":
        boss = self.parse()
        return self.solve_rpg(boss, hard_mode=False)

    def part2(self) -> "str | int":
        boss = self.parse()
        return self.solve_rpg(boss, hard_mode=True)
