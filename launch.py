#!/usr/bin/env python3
"""
Bible Archive Launcher
Works on Linux, macOS, and Windows
"""

import platform
import subprocess
import sys

def launch():
    system = platform.system()
    print(f"Detected OS: {system}")
    
    if system == "Windows":
        # Windows-specific launch
        subprocess.run(["python", "menu.py"])
    else:
        # Unix-like (Linux/macOS)
        subprocess.run(["python3", "menu.py"])

if __name__ == "__main__":
    launch()
