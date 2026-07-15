#!/usr/bin/env python3
"""
AI THEOLOGICAL INTEGRATION
Connects Hebrew text to LLM for deep theological analysis
"""

import json
import sys
sys.path.insert(0, '/root/hebrew-repo')

from dataclasses import dataclass
from typing import List, Dict, Optional
from gematria_calculator import GematriaCalculator

@dataclass
class AIAnalysisRequest:
    """Request for AI theological analysis"""
    verse_reference: str
    hebrew_text: str
    gematria: int
    seeds: List[str]
    question: str

class TheologicalAI:
    """Simulates AI theological analysis (can integrate with real LLM)"""
    
    THEOLOGICAL_PATTERNS = {
        "creation": {
            "keywords": ["ברא", "אור", "שמים", "ארץ"],
            "themes": ["divine order", "cosmology", "ex nihilo"],
            "christian_parallel": "John 1:1-3 - Logos as agent of creation"
        },
        "covenant": {
            "keywords": ["ברית", "את", "לך"],
            "themes": ["promise", "election", "faithfulness"],
            "christian_parallel": "New Covenant in Christ's blood"
        },
        "sacrifice": {
            "keywords": ["עלה", "זבח", "דם"],
            "themes": ["atonement", "substitution", "worship"],
            "christian_parallel": "Christ as Passover lamb"
        },
        "divine_name": {
            "keywords": ["יהוה", "אלהים", "אהיה"],
            "themes": ["revelation", "presence", "holiness"],
            "christian_parallel": "I AM statements in John"
        }
    }
    
    def __init__(self):
        self.gem = GematriaCalculator()
        self.analysis_history = []
    
    def analyze_verse(self, reference: str, hebrew: str, question: str = "") -> Dict:
        """Perform theological analysis of a verse"""
        
        # Calculate gematria
        gematria = self.gem.calculate(hebrew)
        
        # Detect themes
        detected_themes = self._detect_themes(hebrew)
        
        # Generate analysis (simulated AI)
        analysis = self._generate_analysis(
            reference, hebrew, gematria, detected_themes, question
        )
        
        # Store in history
        self.analysis_history.append({
            "reference": reference,
            "hebrew": hebrew,
            "gematria": gematria,
            "themes": detected_themes,
            "analysis": analysis
        })
        
        return {
            "reference": reference,
            "hebrew": hebrew,
            "gematria": gematria,
            "gematria_katan": self.gem.calculate(hebrew, "katan"),
            "detected_themes": detected_themes,
            "theological_insights": analysis,
            "suggested_cross_references": self._suggest_cross_references(detected_themes),
            "christian_connections": self._christian_connections(detected_themes)
        }
    
    def _detect_themes(self, hebrew: str) -> List[str]:
        """Detect theological themes in Hebrew text"""
        themes = []
        
        for theme_name, theme_data in self.THEOLOGICAL_PATTERNS.items():
            for keyword in theme_data["keywords"]:
                if keyword in hebrew:
                    themes.append(theme_name)
                    break
        
        return themes if themes else ["general"]
    
    def _generate_analysis(self, ref: str, hebrew: str, gem: int, 
                          themes: List[str], question: str) -> Dict:
        """Generate theological analysis"""
        
        insights = []
        
        # Theme-based insights
        for theme in themes:
            if theme in self.THEOLOGICAL_PATTERNS:
                data = self.THEOLOGICAL_PATTERNS[theme]
                insights.append({
                    "theme": theme,
                    "key_concepts": data["themes"],
                    "significance": f"This text relates to {theme} theology"
                })
        
        # Gematria insights
        if gem == 26:
            insights.append({
                "type": "gematria",
                "note": "Gematria equals YHVH (26) - divine name connection"
            })
        elif gem == 86:
            insights.append({
                "type": "gematria", 
                "note": "Gematria equals Elohim (86) - divine title connection"
            })
        
        # Response to question
        question_response = ""
        if question:
            question_response = self._answer_question(hebrew, themes, question)
        
        return {
            "insights": insights,
            "gematria_significance": self._interpret_gematria(gem),
            "question_response": question_response
        }
    
    def _interpret_gematria(self, value: int) -> str:
        """Interpret gematria value theologically"""
        interpretations = {
            13: "Echad (One) - Divine unity",
            26: "YHVH - Personal name of God",
            86: "Elohim - God as Creator",
            111: "Alef (first letter) - Beginning",
            2701: "Genesis 1:1 - Creation formula"
        }
        
        return interpretations.get(value, f"Numerical value: {value}")
    
    def _suggest_cross_references(self, themes: List[str]) -> List[str]:
        """Suggest related biblical passages"""
        refs = []
        
        if "creation" in themes:
            refs.extend(["Psalm 33:6", "John 1:1-3", "Colossians 1:16"])
        if "covenant" in themes:
            refs.extend(["Genesis 15", "Jeremiah 31:31", "Hebrews 8"])
        if "divine_name" in themes:
            refs.extend(["Exodus 6:3", "Isaiah 42:8", "John 8:58"])
        
        return refs
    
    def _christian_connections(self, themes: List[str]) -> List[str]:
        """Find Christian theological connections"""
        connections = []
        
        for theme in themes:
            if theme in self.THEOLOGICAL_PATTERNS:
                conn = self.THEOLOGICAL_PATTERNS[theme].get("christian_parallel")
                if conn:
                    connections.append(conn)
        
        return connections
    
    def _answer_question(self, hebrew: str, themes: List[str], question: str) -> str:
        """Attempt to answer theological question"""
        # Simple keyword matching (real AI would use LLM)
        question_lower = question.lower()
        
        if "meaning" in question_lower:
            return f"The text speaks of {', '.join(themes)}. Key Hebrew words reveal {len(hebrew.split())} conceptual units."
        
        if "god" in question_lower or "divine" in question_lower:
            if "אלהים" in hebrew:
                return "Elohim (God as Creator/Council) is used here, suggesting divine majesty and plurality-in-unity."
            if "יהוה" in hebrew:
                return "The Tetragrammaton (YHVH) indicates personal covenant relationship."
        
        if "christ" in question_lower or "jesus" in question_lower:
            return "Typologically, this prefigures Messiah's work. The numerical patterns may encode christological significance."
        
        return "This requires deeper study of the Hebrew syntax and historical context."
    
    def export_analysis(self, filename: str):
        """Export all analyses to JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.analysis_history, f, indent=2, ensure_ascii=False)
        print(f"✅ Exported {len(self.analysis_history)} analyses to {filename}")

# Example usage
if __name__ == "__main__":
    ai = TheologicalAI()
    
    print("="*70)
    print("AI THEOLOGICAL ANALYSIS SYSTEM")
    print("="*70)
    
    # Analyze key verses
    verses = [
        ("Genesis 1:1", "בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ", "What does this teach about God?"),
        ("Exodus 3:14", "אֶהְיֶה אֲשֶׁר אֶהְיֶה", "What is the significance of the divine name?"),
        ("Deuteronomy 6:4", "שְׁמַע יִשְׂרָאֵל יְהוָה אֱלֹהֵינוּ יְהוָה אֶחָד", "How does this relate to Christian theology?"),
    ]
    
    for ref, hebrew, question in verses:
        print(f"\n📖 {ref}")
        print(f"   Hebrew: {hebrew}")
        
        result = ai.analyze_verse(ref, hebrew, question)
        
        print(f"   Gematria: {result['gematria']} (Katan: {result['gematria_katan']})")
        print(f"   Themes: {', '.join(result['detected_themes'])}")
        
        print(f"   Insights:")
        for insight in result['theological_insights']['insights']:
            if isinstance(insight, dict):
                print(f"     • {insight.get('theme', 'Insight')}: {insight.get('significance', '')}")
        
        if result['christian_connections']:
            print(f"   Christian Connections:")
            for conn in result['christian_connections']:
                print(f"     → {conn}")
        
        print(f"   Q: {question}")
        print(f"   A: {result['theological_insights']['question_response']}")
    
    ai.export_analysis("/root/hebrew-repo/ai_theological_analysis.json")
    
    print("\n" + "="*70)
    print("AI Analysis Complete")
    print("="*70)