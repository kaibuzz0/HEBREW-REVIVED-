#!/usr/bin/env python3
"""
CREATE COMPLETE GROUPED BIBLE
Extracts all scriptures organized by category
"""

import sqlite3
import os

base = '/root/hebrew-repo'
conn = sqlite3.connect(f'{base}/data/complete_bible.db')
cursor = conn.cursor()

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
all_tables = [t[0] for t in cursor.fetchall()]

print(f"Total tables: {len(all_tables)}")
print("\nCreating COMPLETE BIBLE with full scriptures...\n")

# Category mapping with search patterns
categories = {
    '01_Torah': {
        'patterns': ['genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy'],
        'books': []
    },
    '02_Historical': {
        'patterns': ['joshua', 'judges', 'ruth', 'samuel', 'kings', 'chronicles', 'ezra', 'nehemiah', 'esther'],
        'books': []
    },
    '03_Wisdom': {
        'patterns': ['job', 'psalms', 'proverbs', 'ecclesiastes', 'song'],
        'books': []
    },
    '04_Major_Prophets': {
        'patterns': ['isaiah', 'jeremiah', 'lamentations', 'ezekiel', 'daniel'],
        'books': []
    },
    '05_Minor_Prophets': {
        'patterns': ['hosea', 'joel', 'amos', 'obadiah', 'jonah', 'micah', 'nahum', 'habakkuk', 'zephaniah', 'haggai', 'zechariah', 'malachi'],
        'books': []
    },
    '06_Gospels': {
        'patterns': ['matthew', 'mark', 'luke', 'john'],
        'books': []
    },
    '07_Epistles': {
        'patterns': ['acts', 'romans', 'corinthians', 'galatians', 'ephesians', 'philippians', 'colossians', 'thessalonians', 'timothy', 'titus', 'philemon', 'hebrews', 'james', 'peter', 'jude'],
        'books': []
    },
    '08_Revelation': {
        'patterns': ['revelation'],
        'books': []
    },
    '09_Deuterocanonical': {
        'patterns': ['tobit', 'judith', 'wisdom', 'sirach', 'baruch', 'maccabees'],
        'books': []
    },
    '10_Nag_Hammadi': {
        'patterns': ['gospel_of_thomas', 'gospel_of_philip', 'gospel_of_mary', 'gospel_of_truth', 'gospel_of_judas', 'apocryphon'],
        'books': []
    },
    '11_Dead_Sea_Scrolls': {
        'patterns': ['community_rule', 'war_scroll', 'thanksgiving', 'temple_scroll', 'copper_scroll', 'serekh', 'pesher'],
        'books': []
    },
    '12_Church_Fathers': {
        'patterns': ['didache', 'barnabas', 'clement', 'ignatius', 'polycarp', 'diognetus'],
        'books': []
    },
    '13_Other': {
        'patterns': [],
        'books': []
    }
}

# Categorize tables
for table in all_tables:
    table_lower = table.lower()
    found = False
    
    for category, info in categories.items():
        for pattern in info['patterns']:
            if pattern in table_lower:
                info['books'].append(table)
                found = True
                break
        if found:
            break
    
    if not found and 'english_text' in [c[1] for c in cursor.execute(f"PRAGMA table_info({table})").fetchall()]:
        categories['13_Other']['books'].append(table)

# Create book files
total_books = 0
total_verses = 0

for category, info in categories.items():
    if info['books']:
        print(f"\n{'='*80}")
        print(f"CATEGORY: {category}")
        print(f"{'='*80}")
        
        category_path = f'{base}/COMPLETE_BIBLE/{category}'
        os.makedirs(category_path, exist_ok=True)
        
        for table in sorted(info['books']):
            try:
                # Get table structure
                cursor.execute(f"PRAGMA table_info({table})")
                columns = cursor.fetchall()
                col_names = [c[1] for c in columns]
                
                if 'english_text' not in col_names:
                    continue
                
                # Build query based on available columns
                select_cols = []
                if 'chapter' in col_names:
                    select_cols.append('chapter')
                if 'verse' in col_names:
                    select_cols.append('verse')
                if 'passage_number' in col_names:
                    select_cols.append('passage_number')
                if 'saying_number' in col_names:
                    select_cols.append('saying_number')
                if 'psalm_number' in col_names:
                    select_cols.append('psalm_number')
                    
                select_cols.append('english_text')
                
                query = f"SELECT {', '.join(select_cols)} FROM {table}"
                cursor.execute(query)
                entries = cursor.fetchall()
                
                if entries:
                    # Create book file
                    book_file = f'{category_path}/{table}.txt'
                    with open(book_file, 'w', encoding='utf-8') as f:
                        f.write('='*80 + '\n')
                        f.write(f'{table.upper().replace("_", " ")}\n')
                        f.write(f'Category: {category.replace("_", " ")}\n')
                        f.write('='*80 + '\n\n')
                        
                        for entry in entries:
                            # Format based on available columns
                            if len(entry) == 2:
                                # Just chapter/text or verse/text
                                ref = str(entry[0]) if entry[0] else ""
                                text = entry[1]
                            elif len(entry) == 3:
                                # chapter, verse, text
                                ref = f"{entry[0]}:{entry[1]}"
                                text = entry[2]
                            else:
                                ref = ""
                                text = entry[-1] if entry else ""
                            
                            if text:
                                if ref:
                                    f.write(f'{ref} {text}\n\n')
                                else:
                                    f.write(f'{text}\n\n')
                        
                        f.write(f'\n[End of {table}]\n')
                    
                    total_books += 1
                    total_verses += len(entries)
                    print(f'  ✅ {table}: {len(entries)} verses')
                    
            except Exception as e:
                print(f'  ⚠️  {table}: {str(e)[:50]}')

# Create master index
print(f"\n{'='*80}")
print("CREATING MASTER INDEX")
print(f"{'='*80}")

with open(f'{base}/COMPLETE_BIBLE/_MASTER_INDEX.txt', 'w') as f:
    f.write('='*80 + '\n')
    f.write('COMPLETE BIBLE ARCHIVE\n')
    f.write('All Scriptures Organized by Category\n')
    f.write('='*80 + '\n\n')
    f.write(f'Total Books: {total_books}\n')
    f.write(f'Total Verses/Passages: {total_verses}\n')
    f.write(f'Categories: {len([c for c in categories.values() if c["books"]])}\n\n')
    f.write('DIRECTORY STRUCTURE:\n')
    f.write('-'*80 + '\n\n')
    
    for category in sorted(os.listdir(f'{base}/COMPLETE_BIBLE')):
        if category.startswith('_'):
            continue
        cat_path = f'{base}/COMPLETE_BIBLE/{category}'
        if os.path.isdir(cat_path):
            books = [b for b in os.listdir(cat_path) if b.endswith('.txt')]
            f.write(f'{category}/\n')
            for book in sorted(books):
                f.write(f'  {book}\n')
            f.write('\n')

conn.close()

print(f"\n{'='*80}")
print("COMPLETE BIBLE CREATION FINISHED")
print(f"{'='*80}")
print(f'\nTotal Books Created: {total_books}')
print(f'Total Verses: {total_verses}')
print(f'Location: {base}/COMPLETE_BIBLE/')
print(f'Master Index: _MASTER_INDEX.txt')