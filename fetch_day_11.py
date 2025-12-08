import urllib.request
import os
import re
from solvers.storage import storage

# Load .env manually
session_cookie = None
try:
    with open('.env', 'r') as f:
        for line in f:
            if line.startswith('AOC_SESSION='):
                session_cookie = line.strip().split('=')[1]
                break
except Exception as e:
    print(f"Error reading .env: {e}")

if not session_cookie:
    print("No session cookie found in .env")
    exit(1)

year = 2025
day = 11
url_input = f"https://adventofcode.com/{year}/day/{day}/input"
url_problem = f"https://adventofcode.com/{year}/day/{day}"

print(f"Fetching input from {url_input}...")
try:
    req = urllib.request.Request(url_input)
    req.add_header('Cookie', f'session={session_cookie}')
    req.add_header('User-Agent', 'github.com/google/antigravity by antigravity@google.com')
    
    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
        storage.save_input(year, day, data)
        print("Input fetched and saved successfully.")
except Exception as e:
    print(f"Error fetching input: {e}")

print(f"Fetching problem from {url_problem}...")
try:
    req = urllib.request.Request(url_problem)
    req.add_header('Cookie', f'session={session_cookie}')
    req.add_header('User-Agent', 'github.com/google/antigravity by antigravity@google.com')
    
    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
        
        # Extract all articles
        articles = re.findall(r'<article class="day-desc">.*?</article>', data, re.DOTALL)
        
        if articles:
            full_text = ""
            for article in articles:
                text = re.sub('<[^<]+?>', '', article)
                full_text += text + "\n\n"
            
            with open('problem_day_11.md', 'w') as f:
                f.write(full_text)
            print(f"Problem description saved to problem_day_11.md ({len(articles)} parts found)")
        else:
            print("Could not find any article tags in response.")
except Exception as e:
    print(f"Error fetching problem: {e}")
