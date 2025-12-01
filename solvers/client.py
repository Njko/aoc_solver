import urllib.request
import urllib.error
import time
from .config import config

class AocClient:
    def __init__(self):
        self.base_url = "https://adventofcode.com"
        self.last_request_time = 0
        self.min_interval = 1.0 # 1 second between requests, be nice

    def _request(self, path: str) -> str:
        # Throttle
        now = time.time()
        if now - self.last_request_time < self.min_interval:
            time.sleep(self.min_interval - (now - self.last_request_time))
        
        url = f"{self.base_url}{path}"
        req = urllib.request.Request(url)
        req.add_header("User-Agent", config.user_agent)
        req.add_header("Cookie", f"session={config.session_cookie}")
        
        try:
            with urllib.request.urlopen(req) as response:
                self.last_request_time = time.time()
                return response.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            print(f"Error fetching {url}: {e}")
            raise

    def get_input(self, year: int, day: int) -> str:
        return self._request(f"/{year}/day/{day}/input")

    def get_problem(self, year: int, day: int) -> str:
        # Note: This returns HTML. We might want to convert to markdown later, 
        # but for now raw HTML or text extraction is fine.
        # The /day/N page contains the problem description.
        return self._request(f"/{year}/day/{day}")

client = AocClient()
