#!/usr/bin/env python3
"""
COMPARATIVE ANALYSIS ENGINE
Hebrew / Greek / Aramaic side-by-side comparison
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from dataclasses import dataclass
from typing import Dict, List, Optional
from gematria_calculator import GematriaCalculator

@dataclass
class ComparativeVerse:
    """A verse in multiple languages"""
    reference: str  # "Genesis 1:1"
    hebrew: str
    greek: str
    aramaic: str
    latin: str
    english: str
    
    # Analysis
    hebrew_gematria: int
    greek_isopsephy: int  # Greek gematria equivalent
    semantic_matches: List[str]  # Words that align across languages

class ComparativeAnalyzer:
    """Analyzes Hebrew text alongside ancient translations"""
    
    # Key verses with known Greek/Aramaic parallels
    COMPARATIVE_DATA = {
        "Genesis 1:1": {
            "hebrew": "בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ",
            "greek": "Ἐν ἀρχῇ ἐποίησεν ὁ θεὸς τὸν οὐρανὸν καὶ τὴν γῆν",
            "aramaic": "בְּקַדְמִין בְּרָא אֱלָהָא יָת שְׁמַיָא וְיָת אַרְעָא",
            "latin": "In principio creavit Deus caelum et terram",
            "english": "In the beginning God created the heavens and the earth"
        },
        "Genesis 1:3": {
            "hebrew": "וַיֹּאמֶר אֱלֹהִים יְהִי אוֹר וַיְהִי אוֹר",
            "greek": "καὶ εἶπεν ὁ θεός Γενηθήτω φῶς καὶ ἐγένετο φῶς",
            "aramaic": "וַאֲמַר אֱלָהָא יְהִי נְהוֹר וַהֲוָה נְהוֹר",
            "latin": "Dixitque Deus: Fiat lux. Et facta est lux",
            "english": "And God said, Let there be light: and there was light"
        },
        "Genesis 1:27": {
            "hebrew": "וַיִּבְרָא אֱלֹהִים אֶת הָאָדָם בְּצַלְמוֹ בְּצֶלֶם אֱלֹהִים בָּרָא אֹתוֹ",
            "greek": "καὶ ἐποίησεν ὁ θεὸς τὸν ἄνθρωπον κατ' εἰκόνα θεοῦ ἐποίησεν αὐτόν",
            "aramaic": "וּבְרָא אֱלָהָא יַת אָדָם בְּצַלְמֵהּ בְּצַלְם אֱלָהָא בְּרָא יָתֵהּ",
            "latin": "Et creavit Deus hominem ad imaginem suam",
            "english": "So God created man in his own image, in the image of God created he him"
        },
        "Exodus 3:14": {
            "hebrew": "אֶהְיֶה אֲשֶׁר אֶהְיֶה",
            "greek": "Ἐγώ εἰμι ὁ ὤν",
            "aramaic": "אֶהְיֶה דְּאֶהְיֶה",
            "latin": "Ego sum qui sum",
            "english": "I AM THAT I AM"
        },
        "Deuteronomy 6:4": {
            "hebrew": "שְׁמַע יִשְׂרָאֵל יְהוָה אֱלֹהֵינוּ יְהוָה אֶחָד",
            "greek": "Ἄκουε, Ἰσραήλ· Κύριος ὁ θεὸς ἡμῶν Κύριος εἷς ἐστιν",
            "aramaic": "שְׁמַע יִשְׂרָאֵל יְיָ אֱלָהֲנָא יְיָ חָד",
            "latin": "Audi, Israel: Dominus Deus noster Dominus unus est",
            "english": "Hear, O Israel: The LORD our God is one LORD"
        }
    }
    
    # Greek letter values (isopsephy)
    GREEK_VALUES = {
        'α': 1, 'β': 2, 'γ': 3, 'δ': 4, 'ε': 5, 'ϛ': 6, 'ζ': 7, 'η': 8, 'θ': 9,
        'ι': 10, 'κ': 20, 'λ': 30, 'μ': 40, 'ν': 50, 'ξ': 60, 'ο': 70, 'π': 80, 'ϟ': 90,
        'ρ': 100, 'σ': 200, 'τ': 300, 'υ': 400, 'φ': 500, 'χ': 600, 'ψ': 700, 'ω': 800, 'ϡ': 900
    }
    
    def __init__(self):
        self.gem = GematriaCalculator()
    
    def greek_isopsephy(self, greek_text: str) -> int:
        """Calculate Greek isopsephy (gematria equivalent)"""
        total = 0
        for char in greek_text.lower():
            if char in self.GREEK_VALUES:
                total += self.GREEK_VALUES[char]
        return total
    
    def compare_translations(self, reference: str) -> Optional[Dict]:
        """Compare all translations for a verse"""
        if reference not in self.COMPARATIVE_DATA:
            return None
        
        data = self.COMPARATIVE_DATA[reference]
        
        # Calculate values
        hebrew_val = self.gem.calculate(data['hebrew'])
        greek_val = self.greek_isopsephy(data['greek'])
        
        # Find numerical relationships
        relationship = self._analyze_relationship(hebrew_val, greek_val)
        
        return {
            'reference': reference,
            'hebrew': data['hebrew'],
            'hebrew_gematria': hebrew_val,
            'greek': data['greek'],
            'greek_isopsephy': greek_val,
            'aramaic': data['aramaic'],
            'latin': data['latin'],
            'english': data['english'],
            'numerical_relationship': relationship,
            'difference': abs(hebrew_val - greek_val),
            'ratio': hebrew_val / greek_val if greek_val > 0 else 0
        }
    
    def _analyze_relationship(self, hebrew: int, greek: int) -> str:
        """Analyze relationship between Hebrew and Greek values"""
        if hebrew == greek:
            return "EXACT_MATCH"
        elif abs(hebrew - greek) < 100:
            return "CLOSE"
        elif hebrew > greek * 2:
            return "HEBREW_DOMINANT"
        elif greek > hebrew * 2:
            return "GREEK_DOMINANT"
        else:
            return "MODERATE"
    
    def generate_comparative_report(self):
        """Generate full comparative analysis report"""
        print("="*70)
        print("COMPARATIVE BIBLICAL ANALYSIS REPORT")
        print("Hebrew | Greek | Aramaic | Latin | English")
        print("="*70)
        
        total_hebrew = 0
        total_greek = 0
        
        for ref in self.COMPARATIVE_DATA.keys():
            result = self.compare_translations(ref)
            if not result:
                continue
            
            total_hebrew += result['hebrew_gematria']
            total_greek += result['greek_isopsephy']
            
            print(f"\n📖 {ref}")
            print(f"   Hebrew:  {result['hebrew'][:50]}...")
            print(f"            Gematria: {result['hebrew_gematria']}")
            print(f"   Greek:   {result['greek'][:50]}...")
            print(f"            Isopsephy: {result['greek_isopsephy']}")
            print(f"   Relationship: {result['numerical_relationship']}")
            print(f"   Ratio H/G: {result['ratio']:.3f}")
            
            if result['difference'] < 500:
                print(f"   ⚠️  Close numerical alignment!")
        
        print("\n" + "="*70)
        print("COMPARATIVE STATISTICS")
        print("="*70)
        print(f"Total Hebrew gematria:   {total_hebrew}")
        print(f"Total Greek isopsephy:   {total_greek}")
        print(f"Overall ratio:           {total_hebrew/total_greek:.3f}")
        print(f"Total difference:        {abs(total_hebrew - total_greek)}")
        
        print("\n" + "="*70)

if __name__ == "__main__":
    analyzer = ComparativeAnalyzer()
    analyzer.generate_comparative_report()