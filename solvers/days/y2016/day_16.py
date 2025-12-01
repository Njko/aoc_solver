from solvers.solver import Solver


class Day16Solver(Solver):
    def __init__(self, input_data: str) -> None:
        super().__init__(input_data)
        self.input = self.input_data.strip()

    def _dragon_curve(self, a: str) -> str:
        b = "".join(["1" if c == "0" else "0" for c in reversed(a)])
        return f"{a}0{b}"

    def _generate_data(self, initial_state: str, length: int) -> str:
        data = initial_state
        while len(data) < length:
            data = self._dragon_curve(data)
        return data[:length]

    def _checksum(self, data: str) -> str:
        checksum = data
        while len(checksum) % 2 == 0:
            new_checksum = ""
            for i in range(0, len(checksum), 2):
                if checksum[i] == checksum[i + 1]:
                    new_checksum += "1"
                else:
                    new_checksum += "0"
            checksum = new_checksum
        return checksum

    def part1(self) -> str:
        disk_length = 272
        data = self._generate_data(self.input, disk_length)
        return self._checksum(data)

    def part2(self) -> str:
        disk_length = 35651584
        data = self._generate_data(self.input, disk_length)
        return self._checksum(data)

