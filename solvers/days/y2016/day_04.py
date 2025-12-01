import re
from collections import Counter
from solvers.solver import Solver


class Day04Solver(Solver):
    def _parse_room(self, room_string):
        match = re.match(r'(.+)-(\d+)\[(.+)\]', room_string)
        return match.groups()

    def _is_real_room(self, name, checksum):
        name_without_dashes = name.replace('-', '')
        counts = Counter(name_without_dashes)
        
        sorted_chars = sorted(counts.keys(), key=lambda char: (-counts[char], char))
        
        calculated_checksum = "".join(sorted_chars[:5])
        
        return calculated_checksum == checksum

    def _decrypt_name(self, encrypted_name, sector_id):
        decrypted = ""
        for char in encrypted_name:
            if char == '-':
                decrypted += ' '
            else:
                shifted = (ord(char) - ord('a') + sector_id) % 26
                decrypted += chr(ord('a') + shifted)
        return decrypted

    def part1(self):
        total_sector_id = 0
        for line in self.input_data.strip().split('\n'):
            name, sector_id, checksum = self._parse_room(line)
            if self._is_real_room(name, checksum):
                total_sector_id += int(sector_id)
        return total_sector_id

    def part2(self):
        for line in self.input_data.strip().split('\n'):
            name, sector_id_str, checksum = self._parse_room(line)
            if self._is_real_room(name, checksum):
                sector_id = int(sector_id_str)
                decrypted_name = self._decrypt_name(name, sector_id)
                if "northpole object storage" in decrypted_name:
                    return sector_id
        return -1  # Should not be reached
