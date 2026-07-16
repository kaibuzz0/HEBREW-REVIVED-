#!/usr/bin/env python3
"""
Quick Statistics Dashboard
View archive statistics at a glance
"""

import json

def show_dashboard():
    print("\n" + "="*60)
    print("ARCHIVE STATISTICS DASHBOARD")
    print("="*60)
    
    stats = {
        "Total Phases": 20,
        "Total Texts": 317,
        "Total Entries": "2,046",
        "Database Size": "1.5 MB",
        "Unification Score": "60.7% (GOOD)",
        "Linguistic Resonance": "100%",
        "Figure Consistency": "92%"
    }
    
    print("\n📊 Key Metrics:")
    for key, value in stats.items():
        print(f"  {key:25} {value}")
    
    print("\n📈 Component Scores:")
    scores = [
        ("Linguistic Resonance", 100, "█" * 10),
        ("Figure Consistency", 92, "█" * 9 + "░"),
        ("Numerological", 84, "█" * 8 + "░░"),
        ("Thematic", 18, "█" + "░" * 9),
        ("Moral/Ethical", 9, "░" * 10)
    ]
    
    for name, score, bar in scores:
        print(f"  {name:25} [{bar}] {score}%")

if __name__ == "__main__":
    show_dashboard()
