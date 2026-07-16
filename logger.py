#!/usr/bin/env python3
"""
Activity Logger
Track usage and changes
"""

import json
import datetime
import os

LOG_FILE = 'activity.log'

def log_activity(action, details=""):
    entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        'action': action,
        'details': details
    }
    
    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(entry) + "\n")

def view_log():
    if not os.path.exists(LOG_FILE):
        print("No activity logged yet.")
        return
    
    print("\nRecent Activity:")
    print("-" * 60)
    
    with open(LOG_FILE) as f:
        for line in f.readlines()[-10:]:  # Last 10 entries
            entry = json.loads(line)
            print(f"  {entry['timestamp'][:19]} - {entry['action']}")

if __name__ == "__main__":
    view_log()
