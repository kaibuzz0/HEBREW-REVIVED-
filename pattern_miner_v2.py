#!/usr/bin/env python3
"""
PATTERN MINING SYSTEM v2.0
Finds connections across all Genesis verses
Part of complete Hebrew Bible analysis suite
"""

import sys
import json
from collections import defaultdict
sys.path.insert(0, '/root/hebrew-repo')

from biblical_database import BiblicalDatabase
from gematria_calculator import GematriaCalculator
from resonance_decoder import ResonanceEngine
from import_genesis_chapter_1_full import GENESIS_1_FULL

class GenesisPatternMiner:
    """Advanced pattern detection for Genesis 1"""
    
    def __init__(self):
        self.gem = GematriaCalculator()
        self.res = ResonanceEngine()
        self.db = BiblicalDatabase()
    
    def find_gematria_patterns(self):
        """Find gematria relationships"""
        print("="*70)
        print("GEMATRIA PATTERN ANALYSIS")
        print("="*70)
        
        results = []
        for verse_num, data in sorted(GENESIS_1_FULL.items()):
            hebrew = data["hebrew"]
            gem = self.gem.calculate(hebrew)
            katan = self.gem.calculate(hebrew, "katan")
            
            results.append({
                "verse": verse_num,
                "gematria": gem,
                "katan": katan,
                "themes": data["themes"]
            })
        
        # Find multiples
        multiples_of_7 = [r for r in results if r["gematria"] % 7 == 0]
        multiples_of_13 = [r for r in results if r["gematria"] % 13 == 0]
        
        print(f"\n🔢 Multiples of 7: {len(multiples_of_7)}")
        for r in multiples_of_7:
            print(f"   Genesis 1:{r['verse']} = {r['gematria']}")
        
        print(f"\n🔢 Multiples of 13: {len(multiples_of_13)}")
        for r in multiples_of_13:
            print(f"   Genesis 1:{r['verse']} = {r['gematria']}")
        
        return results
    
    def find_seed_patterns(self):
        """Find 8-seed patterns across verses"""
        print("\n" + "="*70)
        print("8 SEEDS PATTERN ANALYSIS")
        print("="*70)
        
        all_seeds = defaultdict(list)
        
        for verse_num, data in sorted(GENESIS_1_FULL.items()):
            for word in data["key_words"][:3]:
                decoded = self.res.decode_word(word)
                for seed in decoded.seeds:
                    all_seeds[seed].append(f"1:{verse_num}")
        
        print("\n🌱 Seed Distribution:")
        for seed, verses in sorted(all_seeds.items(), key=lambda x: -len(x[1])):
            print(f"   {seed}: appears in {len(verses)} verses")
            if len(verses) <= 5:
                print(f"      → {', '.join(verses)}")
        
        return dict(all_seeds)
    
    def find_theological_patterns(self):
        """Find theological connections"""
        print("\n" + "="*70)
        print("THEOLOGICAL PATTERN ANALYSIS")
        print("="*70)
        
        patterns = {
            "creation_by_word": [],
            "separation": [],
            "naming": [],
            "evaluation_good": [],
            "creation_of_life": [],
            "humanity": []
        }
        
        for verse_num, data in sorted(GENESIS_1_FULL.items()):
            themes = data["themes"]
            
            if "creation_by_word" in themes or "speech" in themes:
                patterns["creation_by_word"].append(verse_num)
            if "separation" in themes:
                patterns["separation"].append(verse_num)
            if "naming" in themes:
                patterns["naming"].append(verse_num)
            if "evaluation" in themes or "goodness" in themes:
                patterns["evaluation_good"].append(verse_num)
            if "life" in themes or "sea_creatures" in themes or "land_animals" in themes:
                patterns["creation_of_life"].append(verse_num)
            if "humanity" in themes or "image" in themes:
                patterns["humanity"].append(verse_num)
        
        print("\n📖 Theological Patterns:")
        for pattern, verses in patterns.items():
            if verses:
                print(f"   {pattern.replace('_', ' ').title()}: verses {verses}")
        
        return patterns
    
    def find_7_day_structure(self):
        """Analyze 7-day creation structure"""
        print("\n" + "="*70)
        print("7-DAY CREATION STRUCTURE")
        print("="*70)
        
        days = {
            1: ["light"],
            2: ["firmament", "sky", "day_two"],
            3: ["dry_land", "vegetation", "day_three"],
            4: ["luminaries", "calendar", "day_four"],
            5: ["sea_creatures", "birds", "day_five"],
            6: ["land_animals", "humanity", "day_six"],
        }
        
        for day_num, keywords in days.items():
            matching_verses = []
            for v_num, data in GENESIS_1_FULL.items():
                if any(kw in data["themes"] for kw in keywords):
                    matching_verses.append(v_num)
            
            if matching_verses:
                print(f"\n📅 Day {day_num}: Genesis 1:{min(matching_verses)}-{max(matching_verses) if len(matching_verses) > 1 else matching_verses[0]}")
                print(f"   Themes: {', '.join(keywords)}")
        
        return days
    
    def generate_full_report(self):
        """Generate comprehensive pattern report"""
        print("\n" + "="*70)
        print("GENESIS 1: COMPREHENSIVE PATTERN REPORT")
        print("="*70)
        
        gematria_data = self.find_gematria_patterns()
        seed_data = self.find_seed_patterns()
        theological_data = self.find_theological_patterns()
        day_structure = self.find_7_day_structure()
        
        # Summary
        total_gematria = sum(g["gematria"] for g in gematria_data)
        avg_gematria = total_gematria / len(gematria_data)
        
        print("\n" + "="*70)
        print("SUMMARY STATISTICS")
        print("="*70)
        print(f"Total verses analyzed: 16")
        print(f"Total gematria: {total_gematria}")
        print(f"Average gematria: {avg_gematria:.1f}")
        print(f"Unique seeds found: {len(seed_data)}")
        print(f"Theological patterns: {len([p for p in theological_data.values() if p])}")
        
        # Export
        report = {
            "gematria_patterns": gematria_data,
            "seed_patterns": seed_data,
            "theological_patterns": theological_data,
            "day_structure": day_structure,
            "summary": {
                "total_verses": 16,
                "total_gematria": total_gematria,
                "avg_gematria": round(avg_gematria, 1)
            }
        }
        
        with open("/root/hebrew-repo/genesis_1_patterns.json", "w") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Report exported to genesis_1_patterns.json")
        self.db.close()

if __name__ == "__main__":
    miner = GenesisPatternMiner()
    miner.generate_full_report()