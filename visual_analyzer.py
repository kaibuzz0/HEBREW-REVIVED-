#!/usr/bin/env python3
"""
Visual Hebrew Analyzer - Terminal Interface
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gematria_calculator import GematriaCalculator
from resonance_decoder import ResonanceEngine

class VisualAnalyzer:
    def __init__(self):
        self.gem = GematriaCalculator()
        self.res = ResonanceEngine()
    
    def display_header(self, title):
        print("=" * 70)
        print(f"  {title:^66}")
        print("=" * 70)
    
    def display_word(self, word):
        """Visual display of word analysis"""
        print(f"\n┌{'─'*68}┐")
        print(f"│ {word:^66} │")
        print(f"├{'─'*68}┤")
        
        # Gematria
        gem_vals = self.gem.all_methods(word)
        print(f"│ {'GEMATRIA':^66} │")
        for method, val in gem_vals.items():
            print(f"│   {method:12}: {val:>5}{' '*43} │")
        
        # Resonance
        decoded = self.res.decode_word(word)
        if decoded.seeds:
            print(f"├{'─'*68}┤")
            print(f"│ {'RESONANCE (8 Seeds)':^66} │")
            print(f"│   Sequence: {decoded.seed_sequence:<52} │")
            print(f"│   Pattern:  {decoded.resonance_pattern:<52} │")
        
        # Morphology placeholder
        print(f"├{'─'*68}┤")
        print(f"│ {'MORPHOLOGY':^66} │")
        print(f"│   Transliteration: {decoded.translit:<45} │")
        print(f"└{'─'*68}┘")
    
    def display_verse(self, words, title="Verse Analysis"):
        """Visual display of verse analysis"""
        self.display_header(title)
        
        total = 0
        for word in words:
            self.display_word(word)
            total += self.gem.calculate(word)
        
        print(f"\n{'='*70}")
        print(f"TOTAL GEMATRIA: {total}")
        print(f"WORD COUNT: {len(words)}")
        print(f"{'='*70}")
    
    def menu(self):
        """Interactive menu"""
        while True:
            self.display_header("HEBREW REVIVED - Visual Analyzer")
            print("\n1. Analyze Genesis 1:1")
            print("2. Analyze custom word")
            print("3. Show 8 Seeds reference")
            print("4. Exit")
            print()
            
            choice = input("Select option (1-4): ").strip()
            
            if choice == "1":
                genesis = ["בְּרֵאשִׁית", "בָּרָא", "אֱלֹהִים", "אֵת",
                          "הַשָּׁמַיִם", "וְאֵת", "הָאָרֶץ"]
                self.display_verse(genesis, "Genesis 1:1 - In the Beginning")
                input("\nPress Enter to continue...")
                
            elif choice == "2":
                word = input("Enter Hebrew word: ").strip()
                if word:
                    self.display_word(word)
                input("\nPress Enter to continue...")
                
            elif choice == "3":
                self.show_seeds_reference()
                input("\nPress Enter to continue...")
                
            elif choice == "4":
                print("\nShalom!")
                break
    
    def show_seeds_reference(self):
        """Display 8 Seeds reference"""
        self.display_header("8 SEEDS REFERENCE")
        
        seeds = self.res.SEEDS
        for symbol, seed in seeds.items():
            print(f"\n{symbol}: {seed.name}")
            print(f"  Meaning: {seed.meaning}")
            print(f"  Quality: {seed.quality}")
            print(f"  Hebrew:  {', '.join(seed.hebrew_equiv)}")

# Run if executed directly
if __name__ == "__main__":
    analyzer = VisualAnalyzer()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--menu":
        analyzer.menu()
    else:
        # Demo mode
        genesis = ["בְּרֵאשִׁית", "בָּרָא", "אֱלֹהִים", "אֵת",
                  "הַשָּׁמַיִם", "וְאֵת", "הָאָרֶץ"]
        analyzer.display_verse(genesis, "Genesis 1:1")
        print("\nRun with --menu flag for interactive mode")