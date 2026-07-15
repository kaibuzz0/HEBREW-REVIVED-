#!/usr/bin/env python3
"""
Hebrew Text Processor
Combines: Gematria, Resonance, Morphology
"""

import json
from pathlib import Path

class HebrewTextProcessor:
    """Main processor for Hebrew biblical text"""
    
    def __init__(self):
        self.gematria = GematriaCalculator()
        self.resonance = ResonanceEngine()
        self.morphology = HebrewMorphology()
    
    def analyze_word(self, word: str) -> dict:
        """Full analysis of a Hebrew word"""
        return {
            'original': word,
            'gematria': self.gematria.all_methods(word),
            'resonance': self.resonance.decode_word(word).__dict__,
            'morphology': self.morphology.parse_word(word).__dict__
        }
    
    def analyze_verse(self, words: list) -> dict:
        """Analyze a full verse"""
        return {
            'word_count': len(words),
            'total_gematria': sum(self.gematria.calculate(w) for w in words),
            'words': [self.analyze_word(w) for w in words]
        }
    
    def generate_report(self, text: str, output_file: str):
        """Generate JSON report"""
        words = text.split()
        analysis = self.analyze_verse(words)
        
        with open(output_file, 'w') as f:
            json.dump(analysis, f, indent=2, ensure_ascii=False)
        
        return analysis

# Import the other classes
import sys
sys.path.insert(0, '/root/hebrew-repo')

from gematria_calculator import GematriaCalculator
from resonance_decoder import ResonanceEngine

# Hebrew Morphology placeholder
class HebrewMorphology:
    def parse_word(self, word: str):
        # Simplified morphology
        class Result:
            def __init__(self, word):
                self.surface = word
                self.root = word[:3] if len(word) >= 3 else word
                self.pos = "unknown"
                self.parsing = "needs_full_parser"
        return Result(word)

if __name__ == "__main__":
    processor = HebrewTextProcessor()
    
    # Analyze Genesis 1:1
    genesis_1_1 = ["בְּרֵאשִׁית", "בָּרָא", "אֱלֹהִים", "אֵת", 
                   "הַשָּׁמַיִם", "וְאֵת", "הָאָרֶץ"]
    
    print("Hebrew Text Processor - Genesis 1:1 Analysis")
    print("=" * 60)
    
    for word in genesis_1_1:
        analysis = processor.analyze_word(word)
        print(f"\n{word}")
        print(f"  Gematria: {analysis['gematria']['standard']}")
        print(f"  Seeds: {analysis['resonance']['seed_sequence']}")
        print(f"  Root: {analysis['morphology']['root']}")