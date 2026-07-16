#!/usr/bin/env python3
"""
COMPLETE BIBLE ARCHIVE SEARCH SYSTEM v1.0
Search across all 2,046 entries from 317 texts
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')
from complete_bible_database import CompleteBibleDatabase
import json
from collections import defaultdict
import re

class BibleArchiveSearch:
    def __init__(self):
        self.db = CompleteBibleDatabase()
        self.index = defaultdict(list)
        self.entries = []
        self.build_index()
        
    def build_index(self):
        """Build searchable index of all entries"""
        print("Building search index...")
        
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.db.cursor.fetchall()
        
        entry_id = 0
        for (table_name,) in tables:
            try:
                self.db.cursor.execute(f"SELECT chapter, english_text, theme FROM {table_name}")
                rows = self.db.cursor.fetchall()
                
                for chapter, text, theme in rows:
                    entry = {
                        'id': entry_id,
                        'table': table_name,
                        'chapter': chapter,
                        'text': text or "",
                        'theme': theme or "",
                        'phase': self.get_phase(table_name)
                    }
                    self.entries.append(entry)
                    
                    # Index words
                    words = re.findall(r'\b\w+\b', (text or "").lower())
                    for word in words:
                        if len(word) > 2:  # Skip short words
                            self.index[word].append(entry_id)
                    
                    # Index theme
                    if theme:
                        theme_words = theme.lower().split()
                        for word in theme_words:
                            if len(word) > 2:
                                self.index[word].append(entry_id)
                    
                    entry_id += 1
                    
            except Exception as e:
                continue
        
        print(f"Index built: {len(self.entries)} entries indexed")
        print(f"Unique terms: {len(self.index)}")
        
    def get_phase(self, table_name):
        """Determine phase based on table name patterns"""
        phase_patterns = {
            'genesis|exodus|leviticus|numbers|deuteronomy|joshua|judges|ruth|samuel|kings|chronicles': 'Canonical (Torah/Historical)',
            'psalms|proverbs|job|ecclesiastes|song_of_solomon': 'Canonical (Wisdom)',
            'isaiah|jeremiah|lamentations|ezekiel|daniel|hosea|joel|amos|obadiah|jonah|micah|nahum|habakkuk|zephaniah|haggai|zechariah|malachi': 'Canonical (Prophets)',
            'matthew|mark|luke|john|acts': 'Canonical (Gospels/Acts)',
            'romans|corinthians|galatians|ephesians|philippians|colossians|thessalonians|timothy|titus|philemon|hebrews|james|peter|john_epistles|jude|revelation': 'Canonical (Epistles/Apocalyptic)',
            'tobit|judith|wisdom|sirach|baruch|maccabees|esther_additions|daniel_additions|manasseh': 'Deuterocanonical',
            'jubilees|enoch|watchers|adam|abraham|isaiah_ascension|ezra|sibylline|baruch_2|baruch_3|martyrs|azmon|eldad|noah|shem|moses_death|rolls|jasher|nathan|gad': 'Pseudepigrapha',
            'community_rule|war_scroll|thanksgiving|commentary|hodayot|pesharim|milhamah|serekh|damascus|wicked_woman|sabbath_sacrifice|calendar|tohorot': 'Dead Sea Scrolls',
            'thomas|philip|mary|truth|resurrection|egyptians|romans|egyptian_gospel|thomas_infancy|mysteries|james|judas|odes|hermas|jesus_years|witnesses': 'Nag Hammadi',
            'didache|barnabas|clement|ignatius|polycarp|diognetus|papias|hegesippus|quadratus|aristides': 'Church Fathers',
            'baptism|eucharist|apostles|constitutions|canons|barnabas|peter_philip': 'Apostolic Tradition',
            'targum|peshitta|syriac|menander': 'Syriac',
            'hebrews|nazarenes|ebionites': 'Jewish-Christian',
            'zohar|yetzirah|bahir|raziel|hekhalot|zutarti|merkavah|tikkunei': 'Jewish Mystical',
            'nicodemus|pilate|descent|lentulus|vindicta': 'Medieval',
            'andrew|matthew|matthias|barnabas|paul_thecla|scillitan|carpus|clement_martyrdom|polycarp_martyrdom': 'Acts & Martyrs',
            'phocylides|sextus|silvanus|phocylides': 'Wisdom',
            'arabic|armenian|ethiopian|georgian|coptic': 'Other Traditions'
        }
        
        table_lower = table_name.lower()
        for pattern, phase in phase_patterns.items():
            if re.search(pattern, table_lower):
                return phase
        
        return 'Other'
        
    def search(self, query, limit=20):
        """Search for entries matching query"""
        query_lower = query.lower()
        words = re.findall(r'\b\w+\b', query_lower)
        
        # Find matching entry IDs
        matching_ids = set()
        for word in words:
            if len(word) > 2:
                for entry_id in self.index.get(word, []):
                    matching_ids.add(entry_id)
        
        # Get full entries
        results = []
        for entry_id in list(matching_ids)[:limit]:
            if entry_id < len(self.entries):
                results.append(self.entries[entry_id])
        
        return results
        
    def search_by_theme(self, theme):
        """Search by theme"""
        results = []
        for entry in self.entries:
            if theme.lower() in (entry['theme'] or "").lower():
                results.append(entry)
        return results[:20]
        
    def search_by_phase(self, phase_keyword):
        """Search by phase/category"""
        results = []
        for entry in self.entries:
            if phase_keyword.lower() in entry['phase'].lower():
                results.append(entry)
        return results[:20]
        
    def get_statistics(self):
        """Get archive statistics"""
        stats = {
            'total_entries': len(self.entries),
            'phases': defaultdict(int),
            'themes': defaultdict(int),
            'tables': defaultdict(int)
        }
        
        for entry in self.entries:
            stats['phases'][entry['phase']] += 1
            stats['themes'][entry['theme']] += 1
            stats['tables'][entry['table']] += 1
        
        return stats
        
    def interactive_search(self):
        """Interactive search interface"""
        print("\n" + "="*70)
        print("COMPLETE BIBLE ARCHIVE SEARCH SYSTEM v1.0")
        print("="*70)
        print(f"\n📊 {len(self.entries)} entries indexed and ready for search")
        print("\nCommands:")
        print("  \u003cquery\u003e     - Search for text")
        print("  theme:\u003cname\u003e - Search by theme")
        print("  phase:\u003cname\u003e - Search by phase/category")
        print("  stats       - Show archive statistics")
        print("  quit        - Exit search")
        print("="*70)
        
        while True:
            print()
            query = input("Search: ").strip()
            
            if query.lower() == 'quit':
                break
            elif query.lower() == 'stats':
                self.show_stats()
            elif query.startswith('theme:'):
                theme = query[6:].strip()
                results = self.search_by_theme(theme)
                self.display_results(results, f"Theme: {theme}")
            elif query.startswith('phase:'):
                phase = query[6:].strip()
                results = self.search_by_phase(phase)
                self.display_results(results, f"Phase: {phase}")
            elif query:
                results = self.search(query)
                self.display_results(results, f"Search: {query}")
            else:
                print("Please enter a search query")
                
    def display_results(self, results, title):
        """Display search results"""
        print(f"\n{'='*70}")
        print(f"RESULTS: {title}")
        print(f"{'='*70}")
        
        if not results:
            print("No results found.")
            return
            
        print(f"Found {len(results)} entries:\n")
        
        for i, entry in enumerate(results, 1):
            print(f"{i}. [{entry['phase']}] {entry['table']}")
            print(f"   Chapter {entry['chapter']} | Theme: {entry['theme']}")
            text_preview = entry['text'][:150] + "..." if len(entry['text']) > 150 else entry['text']
            print(f"   \"{text_preview}\"")
            print()
            
    def show_stats(self):
        """Display archive statistics"""
        stats = self.get_statistics()
        
        print(f"\n{'='*70}")
        print("ARCHIVE STATISTICS")
        print(f"{'='*70}")
        print(f"\nTotal Entries: {stats['total_entries']}")
        
        print(f"\nBy Phase/Category:")
        for phase, count in sorted(stats['phases'].items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {phase}: {count} entries")
        
        print(f"\nTop Tables:")
        for table, count in sorted(stats['tables'].items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {table}: {count} entries")
            
    def export_index(self):
        """Export search index to JSON"""
        index_data = {
            'total_entries': len(self.entries),
            'unique_terms': len(self.index),
            'entries_sample': self.entries[:100],  # Sample for verification
            'top_terms': dict(sorted(self.index.items(), key=lambda x: len(x[1]), reverse=True)[:50])
        }
        
        with open('/root/hebrew-repo/search_index.json', 'w') as f:
            json.dump(index_data, f, indent=2)
            
        print(f"\nSearch index exported to search_index.json")
        print(f"Total entries: {len(self.entries)}")
        print(f"Unique terms: {len(self.index)}")

def main():
    search = BibleArchiveSearch()
    search.interactive_search()
    search.export_index()
    
if __name__ == "__main__":
    main()