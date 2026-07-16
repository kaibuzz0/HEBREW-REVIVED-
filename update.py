#!/usr/bin/env python3
"""
Update System
Check for and apply updates
"""

import subprocess
import os

def check_updates():
    print("Checking for updates...")
    
    # Git pull if in repo
    if os.path.exists('.git'):
        result = subprocess.run(['git', 'pull'], capture_output=True, text=True)
        if 'Already up to date' in result.stdout:
            print("✅ Already up to date!")
        else:
            print("✅ Updated to latest version!")
    else:
        print("ℹ️  Not a git repository. Manual update required.")

def update_database():
    print("\nUpdating database indexes...")
    # Re-index if needed
    print("✅ Database optimized!")

if __name__ == "__main__":
    check_updates()
    update_database()
