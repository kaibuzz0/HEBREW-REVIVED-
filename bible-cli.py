#!/usr/bin/env python3
"""
Command Line Interface
Quick commands for power users
"""

import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Bible Archive CLI')
    parser.add_argument('command', choices=['search', 'stats', 'export', 'validate'])
    parser.add_argument('--query', '-q', help='Search query')
    
    args = parser.parse_args()
    
    if args.command == 'search':
        print(f"Searching for: {args.query}")
        # Import and run search
        import search_system
    elif args.command == 'stats':
        import dashboard
        dashboard.show_dashboard()
    elif args.command == 'export':
        print("Export options: csv, json, html")
    elif args.command == 'validate':
        import validate
        validate.validate()

if __name__ == "__main__":
    main()
