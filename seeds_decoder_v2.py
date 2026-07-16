#!/usr/bin/env python3
"""
SEEDS DECODER v2.0 - COMPREHENSIVE UNIFICATION VERIFICATION
Analyzing 1,425 entries for numerology, resonance, alignment, and hidden knowledge
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')
from complete_bible_database import CompleteBibleDatabase
import json
import re
from collections import Counter, defaultdict

class SeedsDecoderV2:
    def __init__(self):
        self.db = CompleteBibleDatabase()
        self.results = {}
        
        # BIBLICAL NUMEROLOGY PATTERNS
        self.divine_numbers = {
            1: "Unity, God",
            2: "Witness, Division",
            3: "Divine, Trinity, Resurrection",
            4: "Creation, World, Cardinal directions",
            5: "Grace, Torah",
            6: "Man, Creation",
            7: "Perfection, Completion, Sabbath",
            8: "New beginning, Covenant",
            10: "Completion, Commandments",
            12: "Government, Tribes, Apostles",
            13: "Rebellion, Babylon",
            14: "Passover, Salvation",
            20: "Distress, Expectancy",
            30: "Priesthood, Blood",
            40: "Testing, Trial, Preparation",
            50: "Pentecost, Jubilee, Freedom",
            70: "Nations, Elders, Completion",
            72: "Disciples, Nations",
            99: "Exclusive, Elect",
            100: "Election, Children of promise",
            120: "Divine appointment, End time",
            144: "12x12, Elect, New Jerusalem",
            153: "Disciples catch, Sons of God",
            200: "Insufficiency",
            300: "Deliverance, Anointing",
            365: "Days of the year, Enoch",
            666: "Mark of beast, Man's number",
            777: "Triple perfection",
            1000: "Divine completeness, Millennium"
        }
        
        # CORE THEMES TO CHECK ALIGNMENT
        self.core_themes = {
            "creation": ["create", "beginning", "formed", "made", "light"],
            "fall": ["fall", "sin", "disobedience", "death", "curse", "expelled"],
            "redemption": ["save", "redeem", "rescue", "deliver", "ransom"],
            "incarnation": ["born", "flesh", "word", "logos", "son", "christ"],
            "sacrifice": ["blood", "cross", "die", "suffer", "atonement", "lamb"],
            "resurrection": ["rise", "alive", "third day", "victory", "overcome death"],
            "ascension": ["ascend", "taken up", "clouds", "heaven"],
            "judgment": ["judge", "reward", "punish", "righteous", "wicked"],
            "kingdom": ["kingdom", "reign", "throne", "rule", "christ"],
            "spirit": ["holy spirit", "ghost", "breath", "wind", "fire"],
            "wisdom": ["wisdom", "knowledge", "understand", "truth", "light"],
            "love": ["love", "beloved", "charity", "compassion", "mercy"],
            "faith": ["faith", "believe", "trust", "hope", "confidence"],
            "law": ["law", "commandment", "statute", "ordinance", "torah"],
            "prophecy": ["prophesy", "vision", "dream", "foretell", "messenger"],
            "apocalypse": ["end", "last days", "tribulation", "antichrist", "second coming"],
            "bridal": ["bride", "marriage", "wedding", "chamber", "union"],
            "ascent": ["ascend", "climb", "up", "heaven", "above"],
            "mystery": ["mystery", "hidden", "secret", "concealed", "reveal"]
        }
        
        # MORAL/ETHICAL PRINCIPLES
        self.moral_principles = {
            "love_enemies": ["love enemy", "love your enemies", "pray for persecutors"],
            "turn_cheek": ["turn cheek", "other cheek", "not resist evil"],
            "give": ["give", "charity", "alms", "poor", "needy"],
            "forgive": ["forgive", "pardon", "release debt", "seventy times seven"],
            "humility": ["humble", "meek", "lowly", "poor in spirit"],
            "purity": ["pure", "clean", "undefiled", "holy", "saints"],
            "truth": ["truth", "true", "faithful", "witness", "amen"],
            "justice": ["justice", "righteous", "just", "equity", "fair"],
            "peace": ["peace", "shalom", "harmony", "unity"],
            "patience": ["patient", "endure", "longsuffering", "persevere"],
            "mercy": ["mercy", "compassion", "kindness", "grace"],
            "repentance": ["repent", "turn", "return", "confess", "sin"]
        }
        
        # KEY CHARACTERS/PERSONS TO TRACK
        self.key_figures = [
            "Adam", "Eve", "Seth", "Enoch", "Noah", "Abraham", "Isaac", "Jacob",
            "Joseph", "Moses", "Aaron", "Joshua", "David", "Solomon", "Isaiah",
            "Jeremiah", "Ezekiel", "Daniel", "Jesus", "Christ", "Mary", "Joseph father",
            "John Baptist", "Peter", "James", "John", "Paul", "Thomas", "Philip",
            "Mary Magdalene", "Sophia", "Logos", "Word", "Son of Man", "Lamb",
            "Antichrist", "Beast", "Dragon", "Serpent", "Devil", "Satan",
            "Michael", "Gabriel", "Raphael", "Uriel", "Metatron", "Melchizedek"
        ]
        
        # EVENTS TO ALIGN
        self.key_events = [
            "creation", "fall", "flood", "covenant", "exodus", "passover",
            "law given", "temple built", "baptism", "temptation", "transfiguration",
            "last supper", "crucifixion", "resurrection", "ascension", "pentecost",
            "judgment", "kingdom come", "new heaven", "new earth"
        ]
        
    def analyze_numerology(self):
        """Analyze numerical patterns across all texts"""
        print("\n" + "="*70)
        print("PASS 1: NUMEROLOGICAL ANALYSIS")
        print("="*70)
        
        # Get all chapter numbers from all tables
        chapter_counts = []
        table_counts = {}
        
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.db.cursor.fetchall()
        
        for (table_name,) in tables:
            try:
                self.db.cursor.execute(f"SELECT chapter FROM {table_name}")
                chapters = self.db.cursor.fetchall()
                if chapters:
                    chapter_nums = [c[0] for c in chapters]
                    chapter_counts.extend(chapter_nums)
                    table_counts[table_name] = len(chapters)
            except:
                continue
        
        # Find patterns
        number_freq = Counter(chapter_counts)
        significant_numbers = {}
        
        for num, meaning in self.divine_numbers.items():
            freq = number_freq.get(num, 0)
            if freq > 0:
                significant_numbers[num] = {
                    "frequency": freq,
                    "meaning": meaning,
                    "significance": "High" if freq > 10 else "Medium" if freq > 5 else "Present"
                }
        
        # Check for multiples
        multiples_7 = sum(1 for n in chapter_counts if n % 7 == 0 and n > 0)
        multiples_12 = sum(1 for n in chapter_counts if n % 12 == 0 and n > 0)
        multiples_40 = sum(1 for n in chapter_counts if n % 40 == 0 and n > 0)
        
        self.results["numerology"] = {
            "significant_numbers_found": significant_numbers,
            "multiples_of_7": multiples_7,
            "multiples_of_12": multiples_12,
            "multiples_of_40": multiples_40,
            "total_chapters_analyzed": len(chapter_counts),
            "unique_numbers": len(set(chapter_counts))
        }
        
        print(f"   📊 Total chapters analyzed: {len(chapter_counts)}")
        print(f"   📊 Unique numbers: {len(set(chapter_counts))}")
        print(f"   📊 Multiples of 7: {multiples_7}")
        print(f"   📊 Multiples of 12: {multiples_12}")
        print(f"   📊 Multiples of 40: {multiples_40}")
        print(f"   📊 Significant biblical numbers found: {len(significant_numbers)}")
        
        return significant_numbers
        
    def analyze_thematic_alignment(self):
        """Check if themes align across all texts"""
        print("\n" + "="*70)
        print("PASS 2: THEMATIC ALIGNMENT")
        print("="*70)
        
        theme_counts = defaultdict(lambda: defaultdict(int))
        theme_tables = defaultdict(set)
        
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.db.cursor.fetchall()
        
        for (table_name,) in tables:
            try:
                self.db.cursor.execute(f"SELECT theme, english_text FROM {table_name}")
                entries = self.db.cursor.fetchall()
                
                for theme, text in entries:
                    text_lower = (text or "").lower()
                    theme_lower = (theme or "").lower()
                    
                    for core_theme, keywords in self.core_themes.items():
                        for keyword in keywords:
                            if keyword in text_lower or keyword in theme_lower:
                                theme_counts[core_theme][table_name] += 1
                                theme_tables[core_theme].add(table_name)
                                break
            except:
                continue
        
        # Calculate alignment score
        total_tables = len(tables)
        theme_coverage = {}
        
        for theme, tables_dict in theme_counts.items():
            coverage = len(tables_dict) / total_tables * 100
            total_mentions = sum(tables_dict.values())
            theme_coverage[theme] = {
                "tables_with_theme": len(tables_dict),
                "total_mentions": total_mentions,
                "coverage_percent": round(coverage, 2)
            }
        
        self.results["thematic_alignment"] = theme_coverage
        
        # Sort by coverage
        sorted_themes = sorted(theme_coverage.items(), 
                              key=lambda x: x[1]["coverage_percent"], 
                              reverse=True)
        
        print("   📊 Top 10 universal themes:")
        for i, (theme, data) in enumerate(sorted_themes[:10], 1):
            print(f"      {i}. {theme}: {data['coverage_percent']}% coverage "
                  f"({data['total_mentions']} mentions)")
        
        avg_coverage = sum(t["coverage_percent"] for t in theme_coverage.values()) / len(theme_coverage)
        print(f"\n   ✅ Average thematic coverage: {avg_coverage:.1f}%")
        
        return theme_coverage
        
    def analyze_moral_alignment(self):
        """Check moral/ethical consistency"""
        print("\n" + "="*70)
        print("PASS 3: MORAL/ETHICAL ALIGNMENT")
        print("="*70)
        
        moral_counts = defaultdict(lambda: defaultdict(int))
        
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.db.cursor.fetchall()
        
        for (table_name,) in tables:
            try:
                self.db.cursor.execute(f"SELECT english_text, theme FROM {table_name}")
                entries = self.db.cursor.fetchall()
                
                for text, theme in entries:
                    text_lower = (text or "").lower()
                    
                    for principle, keywords in self.moral_principles.items():
                        for keyword in keywords:
                            if keyword in text_lower:
                                moral_counts[principle][table_name] += 1
                                break
            except:
                continue
        
        moral_coverage = {}
        total_tables = len(tables)
        
        for principle, tables_dict in moral_counts.items():
            coverage = len(tables_dict) / total_tables * 100
            total_mentions = sum(tables_dict.values())
            moral_coverage[principle] = {
                "tables_with_principle": len(tables_dict),
                "total_mentions": total_mentions,
                "coverage_percent": round(coverage, 2)
            }
        
        self.results["moral_alignment"] = moral_coverage
        
        sorted_morals = sorted(moral_coverage.items(),
                              key=lambda x: x[1]["coverage_percent"],
                              reverse=True)
        
        print("   📊 Moral principle consistency:")
        for i, (principle, data) in enumerate(sorted_morals[:8], 1):
            print(f"      {i}. {principle}: {data['coverage_percent']}% "
                  f"({data['total_mentions']} mentions)")
        
        return moral_coverage
        
    def analyze_figure_alignment(self):
        """Track key figures across texts"""
        print("\n" + "="*70)
        print("PASS 4: FIGURE/CHARACTER ALIGNMENT")
        print("="*70)
        
        figure_counts = defaultdict(lambda: defaultdict(int))
        
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.db.cursor.fetchall()
        
        for (table_name,) in tables:
            try:
                self.db.cursor.execute(f"SELECT english_text FROM {table_name}")
                entries = self.db.cursor.fetchall()
                
                for (text,) in entries:
                    text = text or ""
                    for figure in self.key_figures:
                        if figure.lower() in text.lower():
                            figure_counts[figure][table_name] += 1
            except:
                continue
        
        figure_coverage = {}
        total_tables = len(tables)
        
        for figure, tables_dict in figure_counts.items():
            coverage = len(tables_dict) / total_tables * 100
            total_mentions = sum(tables_dict.values())
            figure_coverage[figure] = {
                "tables_with_figure": len(tables_dict),
                "total_mentions": total_mentions,
                "coverage_percent": round(coverage, 2)
            }
        
        self.results["figure_alignment"] = figure_coverage
        
        sorted_figures = sorted(figure_coverage.items(),
                               key=lambda x: x[1]["total_mentions"],
                               reverse=True)
        
        print("   📊 Most mentioned figures:")
        for i, (figure, data) in enumerate(sorted_figures[:15], 1):
            print(f"      {i}. {figure}: {data['total_mentions']} mentions "
                  f"in {data['tables_with_figure']} texts")
        
        return figure_coverage
        
    def analyze_resonance(self):
        """Check for resonance patterns (repeated phrases/concepts)"""
        print("\n" + "="*70)
        print("PASS 5: RESONANCE ANALYSIS")
        print("="*70)
        
        # Key resonant phrases across traditions
        resonant_phrases = [
            "I am",
            "light",
            "way",
            "truth",
            "life",
            "kingdom",
            "father",
            "son",
            "holy",
            "spirit",
            "love",
            "peace",
            "glory",
            "name",
            "word",
            "beginning",
            "end",
            "alpha",
            "omega",
            "amen"
        ]
        
        phrase_counts = defaultdict(lambda: defaultdict(int))
        
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.db.cursor.fetchall()
        
        for (table_name,) in tables:
            try:
                self.db.cursor.execute(f"SELECT english_text FROM {table_name}")
                entries = self.db.cursor.fetchall()
                
                for (text,) in entries:
                    text_lower = (text or "").lower()
                    for phrase in resonant_phrases:
                        count = text_lower.count(phrase)
                        if count > 0:
                            phrase_counts[phrase][table_name] += count
            except:
                continue
        
        resonance_data = {}
        for phrase, tables_dict in phrase_counts.items():
            total_mentions = sum(tables_dict.values())
            resonance_data[phrase] = {
                "tables_with_phrase": len(tables_dict),
                "total_mentions": total_mentions
            }
        
        self.results["resonance"] = resonance_data
        
        sorted_resonance = sorted(resonance_data.items(),
                                 key=lambda x: x[1]["total_mentions"],
                                 reverse=True)
        
        print("   📊 Most resonant phrases:")
        for i, (phrase, data) in enumerate(sorted_resonance[:12], 1):
            print(f"      {i}. '{phrase}': {data['total_mentions']} mentions "
                  f"in {data['tables_with_phrase']} texts")
        
        return resonance_data
        
    def calculate_unification_score(self):
        """Calculate overall unification score"""
        print("\n" + "="*70)
        print("PASS 6: UNIFICATION SCORE CALCULATION")
        print("="*70)
        
        scores = []
        
        # Thematic alignment score
        if "thematic_alignment" in self.results:
            themes = self.results["thematic_alignment"]
            avg_theme = sum(t["coverage_percent"] for t in themes.values()) / len(themes)
            scores.append(("Thematic Alignment", avg_theme))
        
        # Moral alignment score
        if "moral_alignment" in self.results:
            morals = self.results["moral_alignment"]
            avg_moral = sum(m["coverage_percent"] for m in morals.values()) / len(morals)
            scores.append(("Moral/Ethical Alignment", avg_moral))
        
        # Numerological significance
        if "numerology" in self.results:
            num_data = self.results["numerology"]
            significant_found = len(num_data.get("significant_numbers_found", {}))
            num_score = min(significant_found * 5, 100)  # 5% per significant number
            scores.append(("Numerological Patterns", num_score))
        
        # Figure consistency
        if "figure_alignment" in self.results:
            figures = self.results["figure_alignment"]
            # Score based on key figures appearing in multiple texts
            consistent_figures = sum(1 for f in figures.values() if f["tables_with_figure"] > 5)
            figure_score = min(consistent_figures * 5, 100)
            scores.append(("Figure Consistency", figure_score))
        
        # Resonance
        if "resonance" in self.results:
            res = self.results["resonance"]
            widespread_phrases = sum(1 for r in res.values() if r["tables_with_phrase"] > 10)
            res_score = min(widespread_phrases * 8, 100)
            scores.append(("Linguistic Resonance", res_score))
        
        # Calculate overall
        overall = sum(s[1] for s in scores) / len(scores) if scores else 0
        
        self.results["unification_scores"] = {
            "component_scores": {name: round(score, 2) for name, score in scores},
            "overall_unification_score": round(overall, 2),
            "assessment": "EXCELLENT" if overall >= 80 else "GOOD" if overall >= 60 else "MODERATE"
        }
        
        print("\n   📊 COMPONENT SCORES:")
        for name, score in scores:
            bar = "█" * int(score / 5) + "░" * (20 - int(score / 5))
            print(f"      {name:30} [{bar}] {score:.1f}%")
        
        print(f"\n   🎯 OVERALL UNIFICATION SCORE: {overall:.1f}%")
        print(f"   🎯 ASSESSMENT: {self.results['unification_scores']['assessment']}")
        
        return overall
        
    def export_results(self):
        """Export comprehensive results"""
        print("\n" + "="*70)
        print("EXPORTING RESULTS")
        print("="*70)
        
        # Summary statistics
        summary = {
            "total_texts_analyzed": 0,
            "total_entries_analyzed": 0,
            "total_themes_identified": len(self.core_themes),
            "total_moral_principles": len(self.moral_principles),
            "total_key_figures_tracked": len(self.key_figures)
        }
        
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.db.cursor.fetchall()
        summary["total_texts_analyzed"] = len(tables)
        
        total_entries = 0
        for (table,) in tables:
            try:
                self.db.cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = self.db.cursor.fetchone()[0]
                total_entries += count
            except:
                pass
        
        summary["total_entries_analyzed"] = total_entries
        
        self.results["summary"] = summary
        
        # Save to JSON
        with open('/root/hebrew-repo/seeds_decoder_v2_analysis.json', 'w') as f:
            json.dump(self.results, f, indent=2)
        
        # Save summary to text
        with open('/root/hebrew-repo/seeds_decoder_v2_report.txt', 'w') as f:
            f.write("="*70 + "\n")
            f.write("SEEDS DECODER v2.0 - COMPREHENSIVE UNIFICATION REPORT\n")
            f.write("="*70 + "\n\n")
            f.write(f"Total Texts Analyzed: {summary['total_texts_analyzed']}\n")
            f.write(f"Total Entries Analyzed: {summary['total_entries_analyzed']}\n\n")
            
            f.write("UNIFICATION SCORES:\n")
            f.write("-" * 50 + "\n")
            for name, score in self.results.get("unification_scores", {}).get("component_scores", {}).items():
                f.write(f"  {name}: {score}%\n")
            f.write(f"\n  OVERALL: {self.results.get('unification_scores', {}).get('overall_unification_score', 0)}%\n")
            f.write(f"  ASSESSMENT: {self.results.get('unification_scores', {}).get('assessment', 'N/A')}\n")
        
        print(f"   ✅ Exported to seeds_decoder_v2_analysis.json")
        print(f"   ✅ Exported to seeds_decoder_v2_report.txt")
        
        return summary
        
    def run_all_passes(self):
        """Execute all 6 passes"""
        print("\n" + "="*70)
        print("SEEDS DECODER v2.0 - INITIATING")
        print("="*70)
        print("\nAnalyzing 1,425+ entries for unification...")
        
        self.analyze_numerology()
        self.analyze_thematic_alignment()
        self.analyze_moral_alignment()
        self.analyze_figure_alignment()
        self.analyze_resonance()
        self.calculate_unification_score()
        summary = self.export_results()
        
        print("\n" + "="*70)
        print("SEEDS DECODER v2.0 - COMPLETE")
        print("="*70)
        print(f"\n📊 Analyzed {summary['total_entries_analyzed']} entries from "
              f"{summary['total_texts_analyzed']} texts")
        print(f"📊 Overall Unification Score: "
              f"{self.results.get('unification_scores', {}).get('overall_unification_score', 0):.1f}%")
        print(f"📊 Assessment: "
              f"{self.results.get('unification_scores', {}).get('assessment', 'N/A')}")
        
        self.db.close()
        
        return self.results

def main():
    decoder = SeedsDecoderV2()
    results = decoder.run_all_passes()
    
    return results

if __name__ == "__main__":
    main()