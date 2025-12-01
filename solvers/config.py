import os
from pathlib import Path

class Config:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.cache_dir = self.base_dir / ".cache"
        self.user_agent = "github.com/google-deepmind/antigravity-agent by antigravity@google.com"
        
        # Load from .env if present
        env_path = self.base_dir / ".env"
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    if line.startswith("AOC_SESSION="):
                        os.environ["AOC_SESSION"] = line.strip().split("=", 1)[1]
                        break
                        
        self.session_cookie = os.environ.get("AOC_SESSION")

    def validate(self):
        if not self.session_cookie:
            print("WARNING: AOC_SESSION environment variable not set. Downloading inputs will fail.")

config = Config()
