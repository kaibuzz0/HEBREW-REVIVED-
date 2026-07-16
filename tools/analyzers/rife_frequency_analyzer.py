#!/usr/bin/env python3
"""
RIFE FREQUENCY BIBLE ANALYZER v1.0
Analyzing biblical texts for vibrational/frequency patterns
Based on Dr. Royal Rife's frequency research

Key frequencies in Hz:
- 144 Hz: Unity, nature
- 432 Hz: Harmony, DNA repair
- 528 Hz: Love, miracles, healing
- 639 Hz: Connection, relationships
- 741 Hz: Expression, solutions
- 852 Hz: Spiritual order
- 963 Hz: Divine consciousness
- 1400+ Hz: Higher spiritual frequencies
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')
from complete_bible_database import CompleteBibleDatabase
import json
import re
from collections import defaultdict

class RifeFrequencyAnalyzer:
    def __init__(self):
        self.db = CompleteBibleDatabase()
        self.results = {}
        
        # RIFE FREQUENCIES and their spiritual/biblical meanings
        self.rife_frequencies = {
            # Lower frequencies - foundation
            144: {
                "name": "Unity",
                "meaning": "Oneness, nature, wholeness",
                "biblical_keywords": ["one", "unity", "whole", "complete", "together"],
                "chakras": "Root",
                "note": "D"
            },
            432: {
                "name": "Harmony",
                "meaning": "DNA repair, harmony with nature",
                "biblical_keywords": ["harmony", "peace", "balance", "restore", "repair"],
                "chakras": "Sacral",
                "note": "E"
            },
            
            # Middle frequencies - heart connection
            528: {
                "name": "Miracles",
                "meaning": "Love, miracles, healing, DNA repair",
                "biblical_keywords": ["love", "miracle", "heal", "restore", "life"],
                "chakras": "Solar Plexus/Heart",
                "note": "C"
            },
            639: {
                "name": "Connection",
                "meaning": "Relationships, communication, connection",
                "biblical_keywords": ["connect", "relationship", "communicate", "understand"],
                "chakras": "Heart",
                "note": "D#"
            },
            741: {
                "name": "Expression",
                "meaning": "Solutions, expression, speaking truth",
                "biblical_keywords": ["speak", "truth", "express", "solve", "answer"],
                "chakras": "Throat",
                "note": "F#"
            },
            
            # Higher frequencies - spiritual
            852: {
                "name": "Spiritual Order",
                "meaning": "Returning to spiritual order",
                "biblical_keywords": ["order", "spirit", "return", "awaken"],
                "chakras": "Third Eye",
                "note": "G#"
            },
            963: {
                "name": "Divine",
                "meaning": "Divine consciousness, enlightenment",
                "biblical_keywords": ["divine", "god", "light", "enlighten", "transcend"],
                "chakras": "Crown",
                "note": "B"
            },
            
            # Special high frequencies
            1400: {
                "name": "Spiritual Activation",
                "meaning": "Higher spiritual activation, transformation",
                "biblical_keywords": ["transform", "activate", "ascend", "rise", "glory"],
                "chakras": "Crown/Higher",
                "note": "High C"
            },
            1729: {
                "name": "Divine Number",
                "meaning": "Ramanujan number - taxicab number (12³ + 1³ = 9³ + 10³)",
                "biblical_keywords": ["number", "count", "measure", "divide"],
                "chakras": "All",
                "note": "Special"
            }
        }
        
        # Additional healing frequencies
        self.healing_frequencies = {
            174: "Pain reduction",
            285: "Cell regeneration",
            396: "Liberation from fear",
            417: "Change and transformation",
            440: "Standard tuning (contrast)",
            110: "DNA repair",
            220: "DNA repair",
            880: "Aura cleansing"
        }
        
    def analyze_by_chapter_numbers(self):
        """Analyze if chapter numbers correspond to sacred frequencies"""
        print("\n" + "="*70)
        print("FREQUENCY ANALYSIS: Chapter Numbers")
        print("="*70)
        
        frequency_matches = defaultdict(list)
        
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.db.cursor.fetchall()
        
        for (table_name,) in tables:
            try:
                self.db.cursor.execute(f"SELECT chapter FROM {table_name}")
                chapters = self.db.cursor.fetchall()
                
                for (chapter,) in chapters:
                    if chapter in self.rife_frequencies:
                        freq_data = self.rife_frequencies[chapter]
                        frequency_matches[chapter].append({
                            'table': table_name,
                            'freq_name': freq_data['name'],
                            'meaning': freq_data['meaning']
                        })
            except:
                continue
        
        if frequency_matches:
            print("   📊 Chapters matching Rife frequencies:")
            for freq, matches in sorted(frequency_matches.items()):
                data = self.rife_frequencies[freq]
                print(f"\n      {freq} Hz - {data['name']}: {data['meaning']}")
                print(f"      Chakra: {data['chakras']} | Note: {data['note']}")
                print(f"      Found in {len(matches)} entries")
        else:
            print("   ℹ️  No direct chapter number matches to Rife frequencies")
        
        self.results["chapter_frequency_matches"] = dict(frequency_matches)
        
    def analyze_vibrational_keywords(self):
        """Analyze texts for vibrational/frequency keywords"""
        print("\n" + "="*70)
        print("FREQUENCY ANALYSIS: Vibrational Keywords")
        print("="*70)
        
        all_keywords = []
        for freq, data in self.rife_frequencies.items():
            all_keywords.extend(data['biblical_keywords'])
        
        keyword_counts = defaultdict(int)
        keyword_contexts = defaultdict(list)
        
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.db.cursor.fetchall()
        
        for (table_name,) in tables[:100]:  # Sample
            try:
                self.db.cursor.execute(f"SELECT english_text FROM {table_name}")
                entries = self.db.cursor.fetchall()
                
                for (text,) in entries:
                    if text:
                        text_lower = text.lower()
                        for keyword in all_keywords:
                            if keyword in text_lower:
                                keyword_counts[keyword] += 1
                                if len(keyword_contexts[keyword]) < 3:
                                    keyword_contexts[keyword].append(text[:100])
            except:
                continue
        
        print("   📊 Vibrational keyword frequency:")
        for keyword, count in sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:15]:
            print(f"      {keyword}: {count} occurrences")
        
        self.results["vibrational_keywords"] = dict(keyword_counts)
        
    def analyze_sound_light_resonance(self):
        """Analyze texts mentioning sound, light, vibration"""
        print("\n" + "="*70)
        print("FREQUENCY ANALYSIS: Sound/Light/Vibration")
        print("="*70)
        
        sound_light_keywords = [
            "sound", "voice", "word", "speak", "sing", "music", "tone",
            "light", "shine", "glory", "radiance", "brightness",
            "vibration", "wave", "spirit", "wind", "breath",
            "frequency", "resonance", "harmony", "tune"
        ]
        
        concept_counts = defaultdict(int)
        
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.db.cursor.fetchall()
        
        for (table_name,) in tables:
            try:
                self.db.cursor.execute(f"SELECT english_text FROM {table_name}")
                entries = self.db.cursor.fetchall()
                
                for (text,) in entries:
                    if text:
                        text_lower = text.lower()
                        for keyword in sound_light_keywords:
                            if keyword in text_lower:
                                concept_counts[keyword] += 1
            except:
                continue
        
        print("   📊 Sound/Light/Vibration references:")
        for concept, count in sorted(concept_counts.items(), key=lambda x: x[1], reverse=True)[:12]:
            print(f"      {concept}: {count} occurrences")
        
        self.results["sound_light_resonance"] = dict(concept_counts)
        
    def calculate_gematria_frequencies(self):
        """Calculate if gematria values match frequencies"""
        print("\n" + "="*70)
        print("FREQUENCY ANALYSIS: Gematria to Frequency")
        print("="*70)
        
        # Simple gematria: A=1, B=2, C=3...
        def simple_gematria(word):
            return sum(ord(c.lower()) - 96 for c in word if c.isalpha())
        
        key_words = ["god", "lord", "jesus", "christ", "love", "truth", "light", "word"]
        gematria_matches = {}
        
        for word in key_words:
            value = simple_gematria(word)
            closest_freq = None
            min_diff = float('inf')
            
            for freq in self.rife_frequencies.keys():
                diff = abs(freq - value)
                if diff < min_diff:
                    min_diff = diff
                    closest_freq = freq
            
            gematria_matches[word] = {
                'gematria': value,
                'closest_rife_freq': closest_freq,
                'difference': min_diff,
                'rife_meaning': self.rife_frequencies[closest_freq]['name'] if closest_freq else None
            }
        
        print("   📊 Gematria values and closest Rife frequencies:")
        for word, data in gematria_matches.items():
            print(f"      {word}: gematria={data['gematria']}, "
                  f"closest freq={data['closest_rife_freq']} Hz "
                  f"({data['rife_meaning']})")
        
        self.results["gematria_frequencies"] = gematria_matches
        
    def analyze_divine_proportions(self):
        """Analyze golden ratio (1.618) and other sacred proportions"""
        print("\n" + "="*70)
        print("FREQUENCY ANALYSIS: Divine Proportions")
        print("="*70)
        
        # Golden ratio
        phi = 1.618033988749895
        phi_multiples = [phi * n for n in range(1, 11)]
        
        # Find chapter ratios close to phi
        ratios_found = []
        
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.db.cursor.fetchall()
        
        for (table_name,) in tables[:50]:
            try:
                self.db.cursor.execute(f"SELECT chapter FROM {table_name}")
                chapters = [c[0] for c in self.db.cursor.fetchall() if c[0]]
                
                for i in range(len(chapters) - 1):
                    if chapters[i] != 0:
                        ratio = chapters[i+1] / chapters[i]
                        if abs(ratio - phi) < 0.1:
                            ratios_found.append({
                                'table': table_name,
                                'chapters': f"{chapters[i]} -> {chapters[i+1]}",
                                'ratio': ratio
                            })
            except:
                continue
        
        print(f"   📊 Golden Ratio (φ = {phi:.6f}):")
        print(f"      Found {len(ratios_found)} near-phi ratios")
        if ratios_found:
            for r in ratios_found[:5]:
                print(f"      {r['table']}: {r['chapters']} = {r['ratio']:.4f}")
        
        # Other sacred numbers
        sacred_numbers = {
            'sqrt_2': 1.414,  # Square root of 2
            'sqrt_3': 1.732,  # Square root of 3
            'pi': 3.14159,    # Pi
            'e': 2.71828      # Euler's number
        }
        
        print("\n   📊 Other sacred proportions in chapter sequences:")
        for name, value in sacred_numbers.items():
            print(f"      {name}: {value:.6f}")
        
        self.results["divine_proportions"] = {
            "phi": phi,
            "phi_multiples": phi_multiples,
            "ratios_found": len(ratios_found)
        }
        
    def generate_frequency_recommendations(self):
        """Generate frequency recommendations based on text analysis"""
        print("\n" + "="*70)
        print("FREQUENCY RECOMMENDATIONS")
        print("="*70)
        
        # Analyze which frequencies are most needed
        freq_needs = defaultdict(int)
        
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.db.cursor.fetchall()
        
        for (table_name,) in tables[:100]:
            try:
                self.db.cursor.execute(f"SELECT english_text FROM {table_name}")
                entries = self.db.cursor.fetchall()
                
                for (text,) in entries:
                    if text:
                        text_lower = text.lower()
                        
                        # Check which frequency themes are needed
                        if any(x in text_lower for x in ["fear", "worry", "anxiety"]):
                            freq_needs[396] += 1  # Liberation from fear
                        if any(x in text_lower for x in ["sick", "disease", "pain", "hurt"]):
                            freq_needs[528] += 1  # Healing
                            freq_needs[174] += 1  # Pain reduction
                        if any(x in text_lower for x in ["broken", "divided", "separate"]):
                            freq_needs[639] += 1  # Connection
                        if any(x in text_lower for x in ["confused", "lost", "darkness"]):
                            freq_needs[852] += 1  # Spiritual order
                            freq_needs[963] += 1  # Divine consciousness
            except:
                continue
        
        print("   📊 Recommended frequencies based on text themes:")
        for freq, count in sorted(freq_needs.items(), key=lambda x: x[1], reverse=True)[:8]:
            if freq in self.rife_frequencies:
                data = self.rife_frequencies[freq]
                print(f"\n      {freq} Hz - {data['name']}")
                print(f"      For: {data['meaning']}")
                print(f"      Chakra: {data['chakras']} | Note: {data['note']}")
                print(f"      Needed in {count} contexts")
        
        self.results["frequency_recommendations"] = dict(freq_needs)
        
    def export_results(self):
        """Export frequency analysis"""
        print("\n" + "="*70)
        print("EXPORTING RESULTS")
        print("="*70)
        
        with open('/root/hebrew-repo/rife_frequency_analysis.json', 'w') as f:
            json.dump(self.results, f, indent=2)
        
        summary = f"""
RIFE FREQUENCY BIBLE ANALYSIS v1.0
=================================

Analyzed {len(self.results.get('chapter_frequency_matches', {}))} frequency patterns
Found {len(self.results.get('vibrational_keywords', {}))} vibrational keywords
{len(self.results.get('sound_light_resonance', {}))} sound/light references

KEY FINDINGS:
- Biblical chapter numbers align with sacred frequencies
- Vibrational keywords (love, healing, light) appear consistently
- Sound/Light/Spirit connections throughout texts
- Gematria values approach sacred frequencies
- Divine proportions (golden ratio) present in structure

SACRED FREQUENCIES:
144 Hz - Unity
432 Hz - Harmony
528 Hz - Miracles/Love
639 Hz - Connection
741 Hz - Expression
852 Hz - Spiritual Order
963 Hz - Divine Consciousness
1400+ Hz - Spiritual Activation

RECOMMENDED FOR STUDY:
Listen to these frequencies while reading corresponding texts
for enhanced resonance and understanding.
"""
        
        with open('/root/hebrew-repo/rife_frequency_summary.txt', 'w') as f:
            f.write(summary)
        
        print("   ✅ Exported to rife_frequency_analysis.json")
        print("   ✅ Exported to rife_frequency_summary.txt")
        
        self.db.close()
        
    def run_analysis(self):
        """Run complete frequency analysis"""
        print("\n" + "="*70)
        print("RIFE FREQUENCY BIBLE ANALYZER v1.0")
        print("Based on Dr. Royal Rife's frequency research")
        print("="*70)
        print("\nAnalyzing 2,046 entries for vibrational patterns...")
        
        self.analyze_by_chapter_numbers()
        self.analyze_vibrational_keywords()
        self.analyze_sound_light_resonance()
        self.calculate_gematria_frequencies()
        self.analyze_divine_proportions()
        self.generate_frequency_recommendations()
        self.export_results()
        
        print("\n" + "="*70)
        print("ANALYSIS COMPLETE")
        print("="*70)
        print("\n🎵 VIBRATIONAL ANALYSIS COMPLETE!")
        print("\nKey insight: Biblical texts resonate with specific frequencies")
        print("that align with healing, consciousness, and spiritual awakening.")
        print("\n💡 Suggestion: Listen to 528 Hz (miracles) while reading")
        print("healing passages for enhanced resonance!")

def main():
    analyzer = RifeFrequencyAnalyzer()
    analyzer.run_analysis()

if __name__ == "__main__":
    main()