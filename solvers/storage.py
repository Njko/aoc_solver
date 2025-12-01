import os
from pathlib import Path
from .config import config

class Storage:
    def __init__(self):
        self.cache_dir = config.cache_dir
        self.cache_dir.mkdir(exist_ok=True)

    def _get_path(self, year: int, day: int, filename: str) -> Path:
        year_dir = self.cache_dir / str(year)
        year_dir.mkdir(exist_ok=True)
        return year_dir / f"day_{day:02d}_{filename}"

    def save_input(self, year: int, day: int, data: str):
        path = self._get_path(year, day, "input.txt")
        path.write_text(data)

    def load_input(self, year: int, day: int) -> "str | None":
        path = self._get_path(year, day, "input.txt")
        if path.exists():
            return path.read_text()
        return None

    def save_problem(self, year: int, day: int, data: str):
        path = self._get_path(year, day, "problem.md")
        path.write_text(data)
    
    def load_problem(self, year: int, day: int) -> "str | None":
        path = self._get_path(year, day, "problem.md")
        if path.exists():
            return path.read_text()
        return None

storage = Storage()
