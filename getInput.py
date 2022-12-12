import requests
import os
from dotenv import load_dotenv

# get session from .env file
load_dotenv()
SESSION = os.getenv("SESSION")


# Get the input from the user
day = input("Enter the day: ")

# Get the input from the website
url = f"https://adventofcode.com/2022/day/{day}/input"

# Get the input from the website
r = requests.get(url, cookies={"session": SESSION}, timeout=10)

# Check if the input is available
if "before it unlocks" in r.text:
    print("The input is not available yet")
    exit()

# Check if day folder exists, if not create it
if not os.path.exists(f"day{day}"):
    os.mkdir(f"day{day}")    
    with open(f"day{day}/main.py", "w", encoding="ascii") as f:
        f.write("")

# Save the input to a file
with open(f"day{day}/input.txt", "w", encoding="ascii") as f:
    f.write(r.text)


