#!/usr/bin/env python3
"""
System Validator
Check if everything is working correctly
"""

import os

def validate():
    print("\n" + "="*60)
    print("SYSTEM VALIDATION")
    print("="*60)
    
    checks = [
        ("Database exists", "data/complete_bible.db"),
        ("HTML presentation", "COMPLETE_BIBLE_ARCHIVE.html"),
        ("README", "README.md"),
        ("Search system", "tools/search_system.py"),
        ("Menu", "menu.py")
    ]
    
    all_ok = True
    for name, path in checks:
        exists = os.path.exists(path)
        status = "✅" if exists else "❌"
        print(f"  {status} {name:30} {path}")
        if not exists:
            all_ok = False
    
    if all_ok:
        print("\n✅ All systems operational!")
    else:
        print("\n⚠️  Some components missing")
    
    return all_ok

if __name__ == "__main__":
    validate()
