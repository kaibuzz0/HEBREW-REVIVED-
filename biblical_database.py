#!/usr/bin/env python3
"""
Biblical Text Database - SQLite storage for Hebrew analysis
Part of the massive Hebrew Revival project
"""

import sqlite3
import json
from pathlib import Path
from datetime import datetime

class BiblicalDatabase:
    """SQLite database for storing Hebrew text analysis"""
    
    def __init__(self, db_path="hebrew_bible.db"):
        self.db_path = db_path
        self.conn = None
        self.init_database()
    
    def init_database(self):
        """Create database tables"""
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()
        
        # Books table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL,
                hebrew_name TEXT,
                chapters INTEGER,
                testament TEXT
            )
        """)
        
        # Verses table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS verses (
                id INTEGER PRIMARY KEY,
                book_id INTEGER,
                chapter INTEGER,
                verse INTEGER,
                hebrew_text TEXT,
                transliteration TEXT,
                translation TEXT,
                gematria_standard INTEGER,
                gematria_katan INTEGER,
                UNIQUE(book_id, chapter, verse),
                FOREIGN KEY (book_id) REFERENCES books(id)
            )
        """)
        
        # Words table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS words (
                id INTEGER PRIMARY KEY,
                verse_id INTEGER,
                position INTEGER,
                hebrew TEXT,
                translit TEXT,
                root TEXT,
                pos TEXT,
                gematria INTEGER,
                seeds TEXT,
                FOREIGN KEY (verse_id) REFERENCES verses(id)
            )
        """)
        
        # Analysis table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analysis (
                id INTEGER PRIMARY KEY,
                verse_id INTEGER,
                analysis_type TEXT,
                result TEXT,
                confidence REAL,
                timestamp TEXT,
                FOREIGN KEY (verse_id) REFERENCES verses(id)
            )
        """)
        
        # Patterns table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS patterns (
                id INTEGER PRIMARY KEY,
                pattern_type TEXT,
                description TEXT,
                verse_ids TEXT,
                discovered_date TEXT
            )
        """)
        
        self.conn.commit()
        print(f"✅ Database initialized: {self.db_path}")
    
    def add_book(self, name, hebrew_name, chapters, testament):
        """Add a biblical book"""
        if not self.conn:
            self.init_database()
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO books (name, hebrew_name, chapters, testament)
            VALUES (?, ?, ?, ?)
        """, (name, hebrew_name, chapters, testament))
        self.conn.commit()
        return cursor.lastrowid
    
    def add_verse(self, book_name, chapter, verse, hebrew_text, 
                  transliteration="", translation="", gematria_std=0, gematria_ktn=0):
        """Add a verse with analysis"""
        if not self.conn:
            self.init_database()
        cursor = self.conn.cursor()
        
        # Get book_id
        cursor.execute("SELECT id FROM books WHERE name=?", (book_name,))
        result = cursor.fetchone()
        if not result:
            return None
        book_id = result[0]
        
        cursor.execute("""
            INSERT OR REPLACE INTO verses 
            (book_id, chapter, verse, hebrew_text, transliteration, translation,
             gematria_standard, gematria_katan)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (book_id, chapter, verse, hebrew_text, transliteration, 
              translation, gematria_std, gematria_ktn))
        self.conn.commit()
        return cursor.lastrowid
    
    def add_word_analysis(self, verse_id, position, hebrew, translit, 
                         root, pos, gematria, seeds):
        """Add word-level analysis"""
        if not self.conn:
            self.init_database()
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO words (verse_id, position, hebrew, translit, root, pos, gematria, seeds)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (verse_id, position, hebrew, translit, root, pos, gematria, seeds))
        self.conn.commit()
    
    def search_by_gematria(self, value, method="standard"):
        """Find verses with specific gematria value"""
        if not self.conn:
            self.init_database()
        cursor = self.conn.cursor()
        column = "gematria_standard" if method == "standard" else "gematria_katan"
        cursor.execute(f"""
            SELECT v.hebrew_text, v.chapter, v.verse, b.name
            FROM verses v
            JOIN books b ON v.book_id = b.id
            WHERE v.{column} = ?
        """, (value,))
        return cursor.fetchall()
    
    def search_by_seed(self, seed_pattern):
        """Find verses containing specific seed pattern"""
        if not self.conn:
            self.init_database()
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT DISTINCT v.hebrew_text, v.chapter, v.verse, b.name
            FROM verses v
            JOIN books b ON v.book_id = b.id
            JOIN words w ON w.verse_id = v.id
            WHERE w.seeds LIKE ?
        """, (f"%{seed_pattern}%",))
        return cursor.fetchall()
    
    def get_verse_stats(self, book_name=None):
        """Get statistics for verses"""
        if not self.conn:
            self.init_database()
        cursor = self.conn.cursor()
        if book_name:
            cursor.execute("""
                SELECT COUNT(*), AVG(gematria_standard), MAX(gematria_standard)
                FROM verses v
                JOIN books b ON v.book_id = b.id
                WHERE b.name = ?
            """, (book_name,))
        else:
            cursor.execute("""
                SELECT COUNT(*), AVG(gematria_standard), MAX(gematria_standard)
                FROM verses
            """)
        return cursor.fetchone()
    
    def export_to_json(self, output_file):
        """Export entire database to JSON"""
        if not self.conn:
            self.init_database()
        cursor = self.conn.cursor()
        
        data = {
            "books": [],
            "verses": [],
            "patterns": []
        }
        
        cursor.execute("SELECT * FROM books")
        for row in cursor.fetchall():
            data["books"].append({
                "id": row[0], "name": row[1], 
                "hebrew_name": row[2], "chapters": row[3]
            })
        
        cursor.execute("SELECT * FROM verses")
        for row in cursor.fetchall():
            data["verses"].append({
                "id": row[0], "book_id": row[1], "chapter": row[2],
                "verse": row[3], "hebrew": row[4], "translit": row[5],
                "gematria": row[7]
            })
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Exported to {output_file}")
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

# Import and populate with Genesis data
if __name__ == "__main__":
    import sys
    sys.path.insert(0, '/root/hebrew-repo')
    
    from gematria_calculator import GematriaCalculator
    from resonance_decoder import ResonanceEngine
    
    # Initialize
    db = BiblicalDatabase()
    gem = GematriaCalculator()
    res = ResonanceEngine()
    
    # Add Genesis
    db.add_book("Genesis", "בראשית", 50, "Torah")
    
    # Add Genesis 1:1
    verse_text = "בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ"
    words = verse_text.split()
    
    verse_id = db.add_verse(
        "Genesis", 1, 1, verse_text,
        "bereshit bara elohim et hashamayim ve'et ha'aretz",
        "In the beginning God created the heavens and the earth",
        gem.calculate(verse_text, "standard"),
        gem.calculate(verse_text, "katan")
    )
    
    # Add word-level analysis
    for i, word in enumerate(words, 1):
        decoded = res.decode_word(word)
        db.add_word_analysis(
            verse_id, i, word, decoded.translit,
            decoded.seeds[0] if decoded.seeds else "unknown",
            "unknown",  # Would need full morphology
            gem.calculate(word),
            decoded.seed_sequence
        )
    
    print(f"\n📊 Database Statistics:")
    stats = db.get_verse_stats()
    print(f"   Total verses: {stats[0]}")
    print(f"   Avg gematria: {stats[1]:.1f}")
    print(f"   Max gematria: {stats[2]}")
    
    # Search examples
    print(f"\n🔍 Search results:")
    results = db.search_by_seed("EL")
    for r in results[:5]:
        print(f"   {r[3]} {r[1]}:{r[2]} - {r[0][:30]}...")
    
    # Export
    db.export_to_json("/root/hebrew-repo/genesis_export.json")
    
    db.close()
    print("\n✅ Database operations complete!")