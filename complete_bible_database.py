#!/usr/bin/env python3
"""
COMPLETE BIBLE DATABASE v3.0
Extended schema for Ethiopian canon, apocrypha, and extra-canonical texts
"""

import sqlite3
import json
from datetime import datetime
from typing import Dict, List, Optional

class CompleteBibleDatabase:
    """Extended database for complete biblical archive"""
    
    def __init__(self, db_path="/root/hebrew-repo/complete_bible.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_extended_schema()
    
    def _create_extended_schema(self):
        """Create extended database schema"""
        
        # Canon categories
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS canons (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL,  -- "Hebrew", "Greek", "Ethiopian", "Syriac", etc.
                description TEXT,
                book_count INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Extended books table with canon flags
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books_extended (
                id INTEGER PRIMARY KEY,
                canonical_name TEXT NOT NULL,
                hebrew_name TEXT,
                greek_name TEXT,
                latin_name TEXT,
                gez_name TEXT,  -- Ge'ez (Ethiopic)
                coptic_name TEXT,
                syriac_name TEXT,
                chapters INTEGER,
                canon TEXT,  -- "Tanakh", "NT", "Apocrypha", "Ethiopian", "NT_Apoocryphal"
                testament TEXT,  -- "OT", "NT", "AN" (Apocrypha New), "AO" (Apocrypha Old)
                category TEXT,  -- "Torah", "Prophets", "Writings", "Gospels", "Letters", etc.
                status TEXT,  -- "canonical", "deuterocanonical", "apocryphal", "pseudepigraphal"
                estimated_date TEXT,  -- When written
                source_manuscript TEXT,  -- Oldest known source
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Manuscript sources
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS manuscripts (
                id INTEGER PRIMARY KEY,
                codex_name TEXT,  -- "Vaticanus", "Sinaiticus", "Alexandrinus", "Leningradensis", etc.
                language TEXT,
                date TEXT,
                location TEXT,
                status TEXT,  -- "extant", "fragmentary", "lost"
                digital_images_url TEXT
            )
        """)
        
        # Verses with extended metadata
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS verses_extended (
                id INTEGER PRIMARY KEY,
                book_id INTEGER,
                chapter INTEGER,
                verse INTEGER,
                hebrew_text TEXT,
                greek_text TEXT,
                latin_text TEXT,
                gez_text TEXT,  -- Ge'ez
                coptic_text TEXT,
                aramaic_text TEXT,
                english_text TEXT,
                
                -- Analysis
                gematria_standard INTEGER,
                gematria_katan INTEGER,
                isopsephy INTEGER,  -- Greek numerics
                seeds_detected TEXT,  -- JSON array
                
                -- Metadata
                manuscript_source TEXT,  -- Which manuscript this verse comes from
                confidence_score REAL,  -- 0.0 to 1.0 for reconstruction certainty
                notes TEXT,
                
                FOREIGN KEY (book_id) REFERENCES books_extended (id)
            )
        """)
        
        # Cross-references
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cross_references (
                id INTEGER PRIMARY KEY,
                source_verse_id INTEGER,
                target_verse_id INTEGER,
                reference_type TEXT,  -- "quotation", "allusion", "parallel", "theme"
                confidence REAL,
                FOREIGN KEY (source_verse_id) REFERENCES verses_extended (id),
                FOREIGN KEY (target_verse_id) REFERENCES verses_extended (id)
            )
        """)
        
        # Persons/Characters
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS persons (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                name_hebrew TEXT,
                name_greek TEXT,
                name_latin TEXT,
                description TEXT,
                is_jesus_contemporary BOOLEAN,  -- For your specific focus
                relationship_to_jesus TEXT,  -- "brother", "mother", "disciple", "witness", "opponent", etc.
                birth_year INTEGER,
                death_year INTEGER,
                feast_day TEXT,
                canonization_status TEXT  -- "saint", "blessed", "venerable", "unknown"
            )
        """)
        
        # Person-verse connections
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS person_verses (
                id INTEGER PRIMARY KEY,
                person_id INTEGER,
                verse_id INTEGER,
                role_in_verse TEXT,  -- "speaker", "subject", "mentioned", etc.
                FOREIGN KEY (person_id) REFERENCES persons (id),
                FOREIGN KEY (verse_id) REFERENCES verses_extended (id)
            )
        """)
        
        # Books of Enoch (special table because it's so important)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS enoch_books (
                id INTEGER PRIMARY KEY,
                book_number INTEGER,  -- 1-5 (Parables, Similitudes, etc.)
                chapter INTEGER,
                verse INTEGER,
                gez_text TEXT,
                english_text TEXT,
                topic TEXT,  -- "Fallen Angels", "Astronomy", "Prophecies", etc.
                apocryphal BOOLEAN  -- Some sections are in some canons
            )
        """)
        
        # Mary's Gospel (special attention)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS gospel_of_mary (
                id INTEGER PRIMARY KEY,
                page INTEGER,  -- Coptic manuscript pages
                line INTEGER,
                coptic_text TEXT,
                english_text TEXT,
                topic TEXT,  -- "The Soul", "Powers", "Ascending", etc.
                lacuna BOOLEAN  -- True if text is missing/fragmentary
            )
        """)
        
        # Thomas sayings
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS gospel_of_thomas (
                id INTEGER PRIMARY KEY,
                saying_number INTEGER UNIQUE,
                coptic_text TEXT,
                greek_fragments TEXT,
                english_text TEXT,
                parallel_passages TEXT,
                theme TEXT
            )
        """)
        
        # Gospel of Philip passages
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS gospel_of_philip (
                id INTEGER PRIMARY KEY,
                passage_number INTEGER,
                coptic_text TEXT,
                greek_fragments TEXT,
                english_text TEXT,
                parallel_passages TEXT,
                theme TEXT
            )
        """)
        
        # Infancy Gospel of James (Protevangelium)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS infancy_james (
                id INTEGER PRIMARY KEY,
                chapter_number INTEGER,
                greek_text TEXT,
                syriac_text TEXT,
                english_text TEXT,
                parallel_passages TEXT,
                title TEXT
            )
        """)
        
        # Gospel of Judas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS gospel_of_judas (
                id INTEGER PRIMARY KEY,
                passage_number INTEGER,
                coptic_text TEXT,
                greek_fragments TEXT,
                english_text TEXT,
                parallel_passages TEXT,
                theme TEXT
            )
        """)
        
        # Odes of Solomon
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS odes_of_solomon (
                id INTEGER PRIMARY KEY,
                ode_number INTEGER,
                syriac_text TEXT,
                english_text TEXT,
                title TEXT,
                themes TEXT
            )
        """)
        
        # Jesus' 30 years reconstruction
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS jesus_years (
                id INTEGER PRIMARY KEY,
                age INTEGER,  -- 0-30
                event TEXT,
                source TEXT,  -- "Infancy Gospel", "Tradition", "Historical", "Speculative"
                canonical BOOLEAN,  -- Is this in official gospels?
                apocryphal_source TEXT,  -- Which text has this story
                location TEXT,
                description TEXT,
                theological_significance TEXT,
                historical_confidence REAL  -- 0.0 to 1.0
            )
        """)
        
        self.conn.commit()
        print("✅ Extended database schema created")
    
    def add_canon(self, name: str, description: str, book_count: int):
        """Add a canon tradition"""
        self.cursor.execute("""
            INSERT OR IGNORE INTO canons (name, description, book_count)
            VALUES (?, ?, ?)
        """, (name, description, book_count))
        self.conn.commit()
    
    def add_book_extended(self, book_data: Dict) -> int:
        """Add a book with extended metadata"""
        self.cursor.execute("""
            INSERT INTO books_extended 
            (canonical_name, hebrew_name, greek_name, latin_name, gez_name, coptic_name, syriac_name,
             chapters, canon, testament, category, status, estimated_date, source_manuscript)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            book_data.get("canonical_name"),
            book_data.get("hebrew_name"),
            book_data.get("greek_name"),
            book_data.get("latin_name"),
            book_data.get("gez_name"),
            book_data.get("coptic_name"),
            book_data.get("syriac_name"),
            book_data.get("chapters"),
            book_data.get("canon"),
            book_data.get("testament"),
            book_data.get("category"),
            book_data.get("status"),
            book_data.get("estimated_date"),
            book_data.get("source_manuscript")
        ))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def add_thomas_saying(self, saying_num: int, coptic: str, greek: str, english: str, 
                          parallels: List[str], theme: str):
        """Add a saying from Gospel of Thomas"""
        self.cursor.execute("""
            INSERT INTO gospel_of_thomas 
            (saying_number, coptic_text, greek_fragments, english_text, parallel_passages, theme)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (saying_num, coptic, greek, english, json.dumps(parallels), theme))
        self.conn.commit()
    
    def add_philip_passage(self, passage_num: int, coptic: str, greek: str, english: str,
                           parallels: List[str], theme: str):
        """Add a passage from Gospel of Philip"""
        self.cursor.execute("""
            INSERT INTO gospel_of_philip
            (passage_number, coptic_text, greek_fragments, english_text, parallel_passages, theme)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (passage_num, coptic, greek, english, json.dumps(parallels), theme))
        self.conn.commit()
    
    def add_jesus_year(self, age: int, event: str, source: str, canonical: bool,
                       location: str, description: str, confidence: float):
        """Add an event from Jesus' 30 years"""
        self.cursor.execute("""
            INSERT INTO jesus_years 
            (age, event, source, canonical, location, description, historical_confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (age, event, source, canonical, location, description, confidence))
        self.conn.commit()
    
    def get_thomas_sayings(self) -> List[Dict]:
        """Get all Thomas sayings"""
        self.cursor.execute("SELECT * FROM gospel_of_thomas ORDER BY saying_number")
        columns = [description[0] for description in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def get_jesus_years(self) -> List[Dict]:
        """Get Jesus' life chronology"""
        self.cursor.execute("SELECT * FROM jesus_years ORDER BY age")
        columns = [description[0] for description in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def export_complete(self, output_file: str):
        """Export complete database to JSON"""
        export = {
            "canons": [],
            "books": [],
            "thomas_sayings": self.get_thomas_sayings(),
            "jesus_years": self.get_jesus_years()
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Exported to {output_file}")
    
    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("COMPLETE BIBLE DATABASE v3.0")
    print("Extended Schema for Ethiopian Canon + Apocrypha")
    print("="*70)
    
    # Add canon traditions
    canons = [
        ("Hebrew", "Jewish canon (24 books)", 24),
        ("Protestant", "66 books OT+NT", 66),
        ("Catholic", "73 books with deuterocanon", 73),
        ("Orthodox", "G Orthodox canon (variable)", 76),
        ("Ethiopian", "Complete Ethiopian canon", 81),
        ("Syriac", "Peshitta tradition", 51),
        ("Nag Hammadi", "Gnostic library", 52),
        ("Oxyrhynchus", "Papyrus fragments", 0)
    ]
    
    for canon in canons:
        db.add_canon(*canon)
    
    print(f"\n✅ Added {len(canons)} canon traditions")
    
    # Add some extended books
    books = [
        {
            "canonical_name": "Book of Enoch",
            "gez_name": "መጽሐፈ ሄኖክ",
            "chapters": 108,
            "canon": "Ethiopian",
            "testament": "AN",
            "category": "Apocalyptic",
            "status": "canonical",
            "estimated_date": "300-200 BCE"
        },
        {
            "canonical_name": "Gospel of Thomas",
            "coptic_name": "ⲡⲉⲩⲁⲅⲅⲉⲗⲓⲟⲛ ⲕⲁⲧⲁ ⲑⲱⲙⲁⲥ",
            "chapters": 114,  # 114 sayings
            "canon": "Nag Hammadi",
            "testament": "AN",
            "category": "Gospel",
            "status": "apocryphal",
            "estimated_date": "50-140 CE"
        },
        {
            "canonical_name": "Gospel of Mary",
            "coptic_name": "ⲡⲉⲩⲁⲅⲅⲉⲗⲓⲟⲛ ⲛⲙⲁⲣⲓⲁ",
            "chapters": 8,  # pages in extant manuscript
            "canon": "Nag Hammadi",
            "testament": "AN",
            "category": "Gospel",
            "status": "apocryphal",
            "estimated_date": "120-180 CE"
        }
    ]
    
    for book in books:
        book_id = db.add_book_extended(book)
        print(f"✅ Added: {book['canonical_name']}")
    
    print("\n" + "="*70)
    print("DATABASE INITIALIZED")
    print("="*70)
    print("\nReady to import:")
    print("  - Gospel of Thomas (114 sayings)")
    print("  - Gospel of Mary (8 pages)")
    print("  - Book of Enoch (108 chapters)")
    print("  - Jesus' 30 years chronology")
    print("  - Ethiopian canon complete")
    
    db.close()