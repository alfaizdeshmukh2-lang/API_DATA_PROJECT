import json
import os
from datetime import datetime

def save_to_json(filename, data):
    # Create folder if it does not exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def print_section(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
