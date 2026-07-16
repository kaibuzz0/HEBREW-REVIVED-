#!/usr/bin/env python3
"""
CREATE GROUPED BIBLE - Complete Scriptures
Organizes all 1,974 entries into complete books with full text
"""

import sqlite3
import os
import re
from datetime import datetime

class GroupedBibleCreator:
    def __init__(self):
        self.base = '/root/hebrew-repo'
        self.db_path = f'{self.base}/data/complete_bible.db'
        self.output_base = f'{self.base}/grouped_bible'
        self.stats = {
            'total_entries': 0,
            'books_created': 0,
            'categories': 0
        }
        
        # Define categories with their tables
        self.categories = {
            '01_Torah': {
                'name': 'Torah - The Law of Moses',
                'books': ['genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy']
            },
            '02_Historical': {
                'name': 'Historical Books',
                'books': ['joshua', 'judges', 'ruth', 'samuel', 'kings', 'chronicles', 
                         'ezra', 'nehemiah', 'esther']
            },
            '03_Wisdom': {
                'name': 'Wisdom and Poetry',
                'books': ['job', 'psalms', 'proverbs', 'ecclesiastes', 'song_of_solomon']
            },
            '04_Major_Prophets': {
                'name': 'Major Prophets',
                'books': ['isaiah', 'jeremiah', 'lamentations', 'ezekiel', 'daniel']
            },
            '05_Minor_Prophets': {
                'name': 'Minor Prophets',
                'books': ['hosea', 'joel', 'amos', 'obadiah', 'jonah', 'micah',
                         'nahum', 'habakkuk', 'zephaniah', 'haggai', 'zechariah', 'malachi']
            },
            '06_Gospels_and_Acts': {
                'name': 'Gospels and Acts',
                'books': ['matthew', 'mark', 'luke', 'john', 'acts']
            },
            '07_Epistles': {
                'name': 'Epistles',
                'books': ['romans', 'corinthians', 'galatians', 'ephesians', 'philippians',
                         'colossians', 'thessalonians', 'timothy', 'titus', 'philemon',
                         'hebrews', 'james', 'peter', 'john_epistles', 'jude']
            },
            '08_Apocalyptic': {
                'name': 'Apocalyptic Literature',
                'books': ['revelation']
            },
            '09_Deuterocanonical': {
                'name': 'Deuterocanonical Books',
                'books': ['tobit', 'judith', 'wisdom', 'sirach', 'baruch', 'maccabees']
            },
            '10_Pseudepigrapha': {
                'name': 'Pseudepigrapha',
                'books': ['enoch', 'jubilees', 'testaments', 'apocalypse']
            },
            '11_Nag_Hammadi': {
                'name': 'Nag Hammadi Library',
                'books': ['gospel_of_thomas', 'gospel_of_philip', 'gospel_of_mary',
                         'gospel_of_truth', 'gospel_of_judas']
            },
            '12_Dead_Sea_Scrolls': {
                'name': 'Dead Sea Scrolls',
                'books': ['community_rule', 'war_scroll', 'thanksgiving', 'temple_scroll']
            },
            '13_Church_Fathers': {
                'name': 'Early Church Fathers',
                'books': ['didache', 'barnabas', 'clement', 'ignatius']
            },
            '14_Jewish_Mystical': {
                'name': 'Jewish Mystical Texts',
                'books': ['zohar', 'sefer_yetzirah', 'bahir']
            },
            '15_Additional_Traditions': {
                'name': 'Additional Traditions',
                'books': []
            }
        }
        
    def get_all_tables(self):
        """Get all tables from database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [t[0] for t in cursor.fetchall()]
        conn.close()
        return tables
        
    def get_book_content(self, table_name):
        """Get all content from a book table"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            column_names = [c[1] for c in columns]
            
            if 'english_text' in column_names:
                cursor.execute(f"SELECT chapter, verse, english_text FROM {table_name} ORDER BY chapter, verse")
                entries = cursor.fetchall()
                return entries
        except Exception as e:
            print(f"   Error reading {table_name}: {e}")
        finally:
            conn.close()
        
        return []
        
    def create_book_file(self, category, book_name, content):
        """Create a complete book file with all scripture"""
        if not content:
            return False
            
        category_path = f'{self.output_base}/{category}'
        os.makedirs(category_path, exist_ok=True)
        
        book_file = f'{category_path}/{book_name}.txt'
        
        with open(book_file, 'w', encoding='utf-8') as f:
            f.write('='*80 + '\n')
            f.write(f'{book_name.upper().replace("_", " ")}\n')
            f.write(f'Category: {self.categories[category]["name"]}\n')
            f.write('='*80 + '\n\n')
            
            for chapter, verse, text in content:
                if text:
                    f.write(f'{chapter}:{verse} {text}\n\n')
                    
            f.write(f'\nEnd of {book_name}\n')
            
        self.stats['total_entries'] += len(content)
        self.stats['books_created'] += 1
        return True
        
    def create_category_master(self, category, books_info):
        """Create master file for each category"""
        category_path = f'{self.output_base}/{category}'
        master_file = f'{category_path}/_COMPLETE_{category}.txt'
        
        with open(master_file, 'w', encoding='utf-8') as f:
            f.write('='*80 + '\n')
            f.write(f'{self.categories[category]["name"].upper()}\n')
            f.write(f'Complete Collection\n')
            f.write('='*80 + '\n\n')
            
            for book_name, entry_count in books_info:
                f.write(f'{book_name}: {entry_count} verses\n')
                
        print(f"   Created master file for {category}")
        
    def run(self):
        """Execute all passes"""
        print('='*80)
        print('CREATING GROUPED BIBLE - COMPLETE SCRIPTURES')
        print('='*80)
        
        all_tables = self.get_all_tables()
        print(f'\nFound {len(all_tables)} tables in database')
        
        # Process each category
        pass_num = 0
        for category, info in self.categories.items():
            pass_num += 1
            print(f'\n[PASS {pass_num}] Creating {info["name"]}...')
            
            books_in_category = []
            
            # Find matching tables
            for table in all_tables:
                table_lower = table.lower()
                
                # Check if table matches any book in this category
                for book_pattern in info['books']:
                    if book_pattern in table_lower:
                        content = self.get_book_content(table)
                        if content:
                            success = self.create_book_file(category, table, content)
                            if success:
                                books_in_category.append((table, len(content)))
                                print(f'   ✅ {table}: {len(content)} verses')
                                
            # Create category master file
            if books_in_category:
                self.create_category_master(category, books_in_category)
                self.stats['categories'] += 1
                
        # Summary
        print('\n' + '='*80)
        print('GROUPED BIBLE CREATION COMPLETE')
        print('='*80)
        print(f'\nTotal Passes: {pass_num}')
        print(f'Books Created: {self.stats["books_created"]}')
        print(f'Total Verses: {self.stats["total_entries"]}')
        print(f'Categories: {self.stats["categories"]}')
        print(f'\nOutput: {self.output_base}/')
        
        # Create index
        self.create_master_index()
        
    def create_master_index(self):
        """Create master index file"""
        index_file = f'{self.output_base}/_MASTER_INDEX.txt'
        
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write('='*80 + '\n')
            f.write('COMPLETE BIBLE ARCHIVE - GROUPED EDITION\n')
            f.write('All Scriptures Organized by Category\n')
            f.write('='*80 + '\n\n')
            f.write(f'Total Books: {self.stats["books_created"]}\n')
            f.write(f'Total Verses: {self.stats["total_entries"]}\n')
            f.write(f'Categories: {self.stats["categories"]}\n\n')
            f.write('DIRECTORY STRUCTURE:\n')
            f.write('-'*80 + '\n\n')
            
            for category in sorted(os.listdir(self.output_base)):
                cat_path = f'{self.output_base}/{category}'
                if os.path.isdir(cat_path):
                    books = [b for b in os.listdir(cat_path) if b.endswith('.txt')]
                    f.write(f'{category}/\n')
                    for book in sorted(books):
                        f.write(f'  - {book}\n')
                    f.write('\n')
                    
        print(f'\n✅ Master index created: {index_file}')

def main():
    creator = GroupedBibleCreator()
    creator.run()
    
if __name__ == "__main__":
    main()