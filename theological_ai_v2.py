#!/usr/bin/env python3
"""
AI THEOLOGICAL ANALYZER v2.0
Automated pattern detection and insight generation
Connects to pattern miner for intelligent analysis
"""

import sys
import json
from typing import Dict, List, Optional
from dataclasses import dataclass

sys.path.insert(0, '/root/hebrew-repo')

from import_torah_complete_v2 import TORAH_COMPLETE
from import_genesis_chapter_1_full import GENESIS_1_FULL
from gematria_calculator import GematriaCalculator
from resonance_decoder import ResonanceEngine

@dataclass
class AIInsight:
    """Structured AI-generated insight"""
    insight_type: str
    reference: str
    observation: str
    significance: str
    confidence: float  # 0.0 to 1.0
    related_passages: List[str]

class TheologicalAIAnalyzer:
    """Advanced AI for theological analysis"""
    
    def __init__(self):
        self.gem = GematriaCalculator()
        self.res = ResonanceEngine()
        self.insights = []
        
    def analyze_numerical_significance(self, verse_ref: str, hebrew: str) -> Optional[AIInsight]:
        """AI analysis of numerical patterns"""
        gem = self.gem.calculate(hebrew)
        katan = self.gem.calculate(hebrew, "katan")
        
        insights = []
        
        # Check for significant numbers
        if gem % 26 == 0:
            insights.append(f"Divisible by 26 (YHWH = 26) - suggests divine presence marker")
        if gem % 13 == 0:
            insights.append(f"Divisible by 13 - covenant/love pattern")
        if gem % 7 == 0:
            insights.append(f"Divisible by 7 - creation/completion pattern")
        
        # Check katan value
        if katan == 13:
            insights.append(f"Katan value 13 - oneness/unity theme")
        if katan == 7:
            insights.append(f"Katan value 7 - spiritual perfection")
        
        if insights:
            return AIInsight(
                insight_type="numerical_significance",
                reference=verse_ref,
                observation=f"Gematria: {gem}, Katan: {katan}",
                significance="; ".join(insights),
                confidence=0.85,
                related_passages=["Find verses with similar numerical patterns"]
            )
        return None
    
    def analyze_seed_patterns(self, verse_ref: str, hebrew: str) -> Optional[AIInsight]:
        """AI analysis of 8 seeds patterns"""
        all_seeds = set()
        for word in hebrew.split()[:5]:
            decoded = self.res.decode_word(word)
            all_seeds.update(decoded.seeds)
        
        if not all_seeds:
            return None
        
        seed_meanings = {
            "NA": "creation/divine initiation",
            "HA": "life/breath/spirit",
            "GE": "manifestation/touch",
            "OR": "light/illumination",
            "RI": "alignment/turning",
            "VO": "voice/sound/word",
            "EL": "power/seal",
            "AM": "embodiment/faithfulness"
        }
        
        themes = [seed_meanings.get(s, s) for s in all_seeds]
        
        return AIInsight(
            insight_type="seed_resonance",
            reference=verse_ref,
            observation=f"Seeds detected: {', '.join(all_seeds)}",
            significance=f"Theological themes: {', '.join(themes)}",
            confidence=0.80,
            related_passages=["Find verses with similar seed patterns"]
        )
    
    def analyze_creation_themes(self, verse_num: int, themes: List[str]) -> Optional[AIInsight]:
        """AI analysis of Genesis 1 themes"""
        theme_connections = {
            "light": "First act of creation - light precedes luminaries",
            "separation": "Fundamental creative act - ordering from chaos",
            "naming": "Authority and relationship - God names and defines",
            "life": "Biological creation - plants, animals, humanity",
            "image": "Humanity as divine reflection - covenant partners",
            "speech": "Creation by word - power of divine speech"
        }
        
        insights = []
        for theme in themes:
            if theme in theme_connections:
                insights.append(f"{theme}: {theme_connections[theme]}")
        
        if insights:
            return AIInsight(
                insight_type="creation_theology",
                reference=f"Genesis 1:{verse_num}",
                observation=f"Themes: {', '.join(themes[:3])}",
                significance="; ".join(insights),
                confidence=0.90,
                related_passages=["John 1:1-4 (Logos creation)", "Colossians 1:15-17 (Christ as firstborn)"]
            )
        return None
    
    def generate_cross_references(self, book: str, chapter: int, themes: List[str]) -> AIInsight:
        """Generate AI cross-references"""
        cross_refs = []
        
        # Pattern matching for cross-references
        if "creation" in themes:
            cross_refs.extend(["Psalm 19:1-4", "Isaiah 42:5", "John 1:1-3"])
        if "light" in themes:
            cross_refs.extend(["Isaiah 9:2", "Matthew 4:16", "John 8:12"])
        if "image" in themes or "humanity" in themes:
            cross_refs.extend(["Psalm 8:4-6", "Ephesians 4:24", "Colossians 3:10"])
        if "covenant" in themes:
            cross_refs.extend(["Genesis 15:18", "Exodus 19:5", "Jeremiah 31:31"])
        if "sacrifice" in themes:
            cross_refs.extend(["Leviticus 16", "Isaiah 53", "Hebrews 9"])
        
        return AIInsight(
            insight_type="cross_references",
            reference=f"{book} {chapter}",
            observation=f"Themes: {', '.join(themes[:3])}",
            significance=f"Parallel passages: {', '.join(cross_refs[:5])}",
            confidence=0.75,
            related_passages=cross_refs[:5]
        )
    
    def analyze_book_structure(self, book_name: str) -> AIInsight:
        """Analyze structural patterns in a book"""
        book = TORAH_COMPLETE.get(book_name)
        if not book:
            return None
        
        verse_count = len(book["key_verses"])
        
        structural_notes = {
            "Genesis": "Primeval history → Patriarchs → Israel's formation",
            "Exodus": "Slavery → Deliverance → Sinai Covenant → Tabernacle",
            "Leviticus": "Sacrifice → Priesthood → Holiness Code",
            "Numbers": "Organization → Wilderness → Preparation",
            "Deuteronomy": "Retrospective → Covenant renewal → Transition"
        }
        
        return AIInsight(
            insight_type="book_structure",
            reference=book_name,
            observation=f"{book['chapters']} chapters, {verse_count} key verses analyzed",
            significance=structural_notes.get(book_name, "Standard narrative structure"),
            confidence=0.95,
            related_passages=["See book outline in translation layers"]
        )
    
    def generate_comprehensive_report(self) -> Dict:
        """Generate complete AI analysis report"""
        print("="*70)
        print("AI THEOLOGICAL ANALYZER v2.0")
        print("Automated Insight Generation")
        print("="*70)
        
        insights = []
        
        # Analyze Genesis 1
        print("\n🤖 Analyzing Genesis 1...")
        for verse_num, data in sorted(GENESIS_1_FULL.items()):
            hebrew = data["hebrew"]
            verse_ref = f"Genesis 1:{verse_num}"
            
            # Numerical analysis
            insight = self.analyze_numerical_significance(verse_ref, hebrew)
            if insight:
                insights.append(insight)
            
            # Seed analysis
            insight = self.analyze_seed_patterns(verse_ref, hebrew)
            if insight:
                insights.append(insight)
            
            # Creation themes
            insight = self.analyze_creation_themes(verse_num, data["themes"])
            if insight:
                insights.append(insight)
            
            # Cross-references
            insight = self.generate_cross_references("Genesis", verse_num, data["themes"])
            insights.append(insight)
        
        # Analyze each book structure
        print("🤖 Analyzing book structures...")
        for book_name in TORAH_COMPLETE.keys():
            insight = self.analyze_book_structure(book_name)
            if insight:
                insights.append(insight)
        
        # Generate report
        report = {
            "generated_insights": len(insights),
            "by_type": {},
            "high_confidence": [],
            "all_insights": []
        }
        
        for insight in insights:
            # Group by type
            if insight.insight_type not in report["by_type"]:
                report["by_type"][insight.insight_type] = []
            report["by_type"][insight.insight_type].append({
                "reference": insight.reference,
                "significance": insight.significance,
                "confidence": insight.confidence
            })
            
            # High confidence insights
            if insight.confidence >= 0.85:
                report["high_confidence"].append({
                    "type": insight.insight_type,
                    "reference": insight.reference,
                    "insight": insight.significance[:100] + "..." if len(insight.significance) > 100 else insight.significance
                })
            
            report["all_insights"].append({
                "type": insight.insight_type,
                "reference": insight.reference,
                "observation": insight.observation,
                "significance": insight.significance,
                "confidence": insight.confidence,
                "related": insight.related_passages
            })
        
        return report
    
    def export_report(self, filename="/root/hebrew-repo/ai_insights_v2.json"):
        """Export AI analysis"""
        report = self.generate_comprehensive_report()
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Print summary
        print("\n" + "="*70)
        print("AI ANALYSIS COMPLETE")
        print("="*70)
        print(f"\nTotal insights generated: {report['generated_insights']}")
        print(f"\nBy category:")
        for insight_type, items in report["by_type"].items():
            print(f"  {insight_type}: {len(items)}")
        print(f"\nHigh confidence insights (>85%): {len(report['high_confidence'])}")
        
        print(f"\n✅ Report exported to {filename}")

if __name__ == "__main__":
    ai = TheologicalAIAnalyzer()
    ai.export_report()