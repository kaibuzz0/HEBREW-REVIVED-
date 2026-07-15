#!/usr/bin/env python3
"""
ADVANCED PATTERN ANALYZER v3.0
Cross-chapter and cross-book pattern detection
Part of complete Hebrew Bible analysis suite
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from import_torah_complete_v2 import TORAH_COMPLETE
from import_genesis_chapter_1_full import GENESIS_1_FULL
from gematria_calculator import GematriaCalculator
from resonance_decoder import ResonanceEngine
from collections import defaultdict
import json

class AdvancedPatternAnalyzer:
    """Detect complex patterns across Torah"""
    
    def __init__(self):
        self.gem = GematriaCalculator()
        self.res = ResonanceEngine()
        self.patterns = {
            "divine_speech": [],
            "creation_formula": [],
            "separation_patterns": [],
            "evaluation_good": [],
            "naming_patterns": [],
            "numerical_patterns": [],
            "seed_continuity": defaultdict(list),
            "thematic_bridges": []
        }
    
    def analyze_divine_speech(self):
        """Find 'And God said' patterns"""
        print("="*70)
        print("DIVINE SPEECH PATTERNS")
        print("="*70)
        
        speech_indicators = [
            "וַיֹּאמֶר",  # And he said
            "וַיֹּאמֶר אֱלֹהִים",  # And God said
            "וַיְדַבֵּר",  # And he spoke
        ]
        
        occurrences = []
        for book_name, book_data in TORAH_COMPLETE.items():
            for verse_key, hebrew in book_data["key_verses"].items():
                for indicator in speech_indicators:
                    if indicator in hebrew:
                        occurrences.append({
                            "reference": f"{book_name} {verse_key[0]}:{verse_key[1]}",
                            "hebrew": hebrew[:50] + "..." if len(hebrew) > 50 else hebrew,
                            "indicator": indicator
                        })
        
        print(f"\n🗣️  Divine Speech Found: {len(occurrences)} occurrences")
        for occ in occurrences[:10]:
            print(f"   {occ['reference']}: {occ['indicator']}")
        
        self.patterns["divine_speech"] = occurrences
        return occurrences
    
    def analyze_creation_formula(self):
        """Find 'And God said... and it was so' patterns"""
        print("\n" + "="*70)
        print("CREATION FORMULA PATTERNS")
        print("="*70)
        
        # Look for formula: "Let there be... and there was"
        formula_words = ["יְהִי", "וַיְהִי"]  # Let there be, and there was
        
        occurrences = []
        for verse_key, data in GENESIS_1_FULL.items():
            hebrew = data["hebrew"]
            if any(word in hebrew for word in formula_words):
                occurrences.append({
                    "verse": verse_key,
                    "hebrew": hebrew,
                    "themes": data["themes"]
                })
        
        print(f"\n✨ Creation Formula Found: {len(occurrences)} occurrences")
        for occ in occurrences:
            print(f"   Genesis 1:{occ['verse']} - {', '.join(occ['themes'][:2])}")
        
        self.patterns["creation_formula"] = occurrences
        return occurrences
    
    def analyze_separation_patterns(self):
        """Find 'God divided/separated' patterns"""
        print("\n" + "="*70)
        print("SEPARATION PATTERNS")
        print("="*70)
        
        separation_words = ["וַיַּבְדֵּל", "בָּדַל", "הִבְדִּיל"]  # separated, divide
        
        occurrences = []
        for book_name, book_data in TORAH_COMPLETE.items():
            for verse_key, hebrew in book_data["key_verses"].items():
                for word in separation_words:
                    if word in hebrew:
                        occurrences.append({
                            "reference": f"{book_name} {verse_key[0]}:{verse_key[1]}",
                            "hebrew": hebrew[:60] + "..." if len(hebrew) > 60 else hebrew
                        })
        
        print(f"\n⚡ Separation Events: {len(occurrences)} occurrences")
        for occ in occurrences[:5]:
            print(f"   {occ['reference']}")
        
        self.patterns["separation_patterns"] = occurrences
        return occurrences
    
    def analyze_evaluation_good(self):
        """Find 'And God saw that it was good' patterns"""
        print("\n" + "="*70)
        print("EVALUATION: 'AND GOD SAW THAT IT WAS GOOD'")
        print("="*70)
        
        good_pattern = "כִּי טוֹב"  # that it was good
        
        occurrences = []
        for verse_key, data in GENESIS_1_FULL.items():
            hebrew = data["hebrew"]
            if good_pattern in hebrew:
                occurrences.append({
                    "verse": verse_key,
                    "themes": data["themes"]
                })
        
        print(f"\n✅ 'Good' Evaluations: {len(occurrences)} occurrences")
        for occ in occurrences:
            print(f"   Genesis 1:{occ['verse']}")
        
        # Note: Day 2 is the only day without "good"!
        print(f"\n📋 All days except Day 2 have 'good' evaluation")
        
        self.patterns["evaluation_good"] = occurrences
        return occurrences
    
    def analyze_numerical_patterns(self):
        """Find significant numerical patterns"""
        print("\n" + "="*70)
        print("NUMERICAL PATTERNS")
        print("="*70)
        
        # Collect all gematria values
        all_gematrias = []
        for book_name, book_data in TORAH_COMPLETE.items():
            for verse_key, hebrew in book_data["key_verses"].items():
                gem = self.gem.calculate(hebrew)
                all_gematrias.append({
                    "reference": f"{book_name} {verse_key[0]}:{verse_key[1]}",
                    "gematria": gem,
                    "hebrew": hebrew[:30]
                })
        
        # Find patterns
        multiples_of_7 = [g for g in all_gematrias if g["gematria"] % 7 == 0]
        multiples_of_13 = [g for g in all_gematrias if g["gematria"] % 13 == 0]
        multiples_of_26 = [g for g in all_gematrias if g["gematria"] % 26 == 0]
        
        print(f"\n🔢 Numerical Patterns:")
        print(f"   Multiples of 7: {len(multiples_of_7)}")
        print(f"   Multiples of 13: {len(multiples_of_13)}")
        print(f"   Multiples of 26 (YHWH): {len(multiples_of_26)}")
        
        if multiples_of_26:
            print(f"\n   ⚠️  Divine name pattern found:")
            for m in multiples_of_26[:3]:
                print(f"      {m['reference']} = {m['gematria']}")
        
        self.patterns["numerical_patterns"] = {
            "multiples_of_7": multiples_of_7,
            "multiples_of_13": multiples_of_13,
            "multiples_of_26": multiples_of_26
        }
        
        return self.patterns["numerical_patterns"]
    
    def analyze_seed_continuity(self):
        """Track seed patterns across books"""
        print("\n" + "="*70)
        print("8 SEEDS CONTINUITY ANALYSIS")
        print("="*70)
        
        # Analyze each book for seed distribution
        for book_name, book_data in TORAH_COMPLETE.items():
            book_seeds = defaultdict(int)
            
            for verse_key, hebrew in book_data["key_verses"].items():
                for word in hebrew.split()[:5]:
                    decoded = self.res.decode_word(word)
                    for seed in decoded.seeds:
                        book_seeds[seed] += 1
            
            print(f"\n📖 {book_name}:")
            for seed, count in sorted(book_seeds.items(), key=lambda x: -x[1])[:5]:
                print(f"   {seed}: {count}")
            
            self.patterns["seed_continuity"][book_name] = dict(book_seeds)
        
        return self.patterns["seed_continuity"]
    
    def find_thematic_bridges(self):
        """Find connections between books"""
        print("\n" + "="*70)
        print("THEMATIC BRIDGES BETWEEN BOOKS")
        print("="*70)
        
        bridges = []
        
        # Genesis to Exodus bridge
        bridges.append({
            "connection": "Creation → Exodus",
            "theme": "New creation through deliverance",
            "verses": ["Genesis 1:1", "Exodus 3:14"]
        })
        
        # Exodus to Leviticus bridge
        bridges.append({
            "connection": "Deliverance → Holiness",
            "theme": "Redemption leads to sanctification",
            "verses": ["Exodus 15:2", "Leviticus 19:2"]
        })
        
        # Leviticus to Deuteronomy bridge
        bridges.append({
            "connection": "Law → Covenant renewal",
            "theme": "Blessing and curse framework",
            "verses": ["Leviticus 26", "Deuteronomy 28"]
        })
        
        print(f"\n🔗 Thematic Bridges Found: {len(bridges)}")
        for bridge in bridges:
            print(f"\n   {bridge['connection']}")
            print(f"   Theme: {bridge['theme']}")
        
        self.patterns["thematic_bridges"] = bridges
        return bridges
    
    def export_report(self, filename="/root/hebrew-repo/advanced_patterns.json"):
        """Export complete analysis"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.patterns, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Report exported to {filename}")
    
    def generate_full_report(self):
        """Generate comprehensive pattern analysis"""
        print("\n" + "="*70)
        print("ADVANCED PATTERN ANALYSIS v3.0")
        print("Complete Torah Pattern Detection")
        print("="*70)
        
        self.analyze_divine_speech()
        self.analyze_creation_formula()
        self.analyze_separation_patterns()
        self.analyze_evaluation_good()
        self.analyze_numerical_patterns()
        self.analyze_seed_continuity()
        self.find_thematic_bridges()
        
        # Summary
        print("\n" + "="*70)
        print("PATTERN SUMMARY")
        print("="*70)
        print(f"Divine speech occurrences: {len(self.patterns['divine_speech'])}")
        print(f"Creation formulas: {len(self.patterns['creation_formula'])}")
        print(f"Separation events: {len(self.patterns['separation_patterns'])}")
        print(f"'Good' evaluations: {len(self.patterns['evaluation_good'])}")
        print(f"Thematic bridges: {len(self.patterns['thematic_bridges'])}")
        
        self.export_report()
        
        print("\n" + "="*70)
        print("ADVANCED PATTERN ANALYSIS COMPLETE")
        print("="*70)

if __name__ == "__main__":
    analyzer = AdvancedPatternAnalyzer()
    analyzer.generate_full_report()