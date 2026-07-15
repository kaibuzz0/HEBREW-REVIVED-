#!/usr/bin/env python3
"""
PATTERN MINING ENGINE
Finds gematria patterns, seed clusters, and numerical connections
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from biblical_database import BiblicalDatabase
from gematria_calculator import GematriaCalculator

class PatternMiner:
    """Mines the Hebrew text for numerical patterns"""
    
    def __init__(self, db_path="hebrew_bible.db"):
        self.db = BiblicalDatabase(db_path)
        self.gem = GematriaCalculator()
    
    def find_gematria_matches(self, target_value, tolerance=0):
        """Find all verses with specific gematria"""
        results = self.db.search_by_gematria(target_value)
        return results
    
    def find_gematria_clusters(self, min_count=2):
        """Find gematria values that appear multiple times"""
        conn = self.db.conn
        cursor = conn.cursor()
        cursor.execute("""
            SELECT gematria_standard, COUNT(*)
            FROM verses
            GROUP BY gematria_standard
            HAVING COUNT(*) >= ?
            ORDER BY COUNT(*) DESC
        """, (min_count,))
        return cursor.fetchall()
    
    def find_divisible_by(self, divisor):
        """Find verses where gematria is divisible by number"""
        conn = self.db.conn
        cursor = conn.cursor()
        cursor.execute("""
            SELECT v.hebrew_text, v.chapter, v.verse, b.name, v.gematria_standard
            FROM verses v
            JOIN books b ON v.book_id = b.id
            WHERE v.gematria_standard % ? = 0
            ORDER BY v.gematria_standard
        """, (divisor,))
        return cursor.fetchall()
    
    def find_prime_gematria(self):
        """Find verses with prime number gematria"""
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        conn = self.db.conn
        cursor = conn.cursor()
        cursor.execute("SELECT gematria_standard FROM verses")
        primes = []
        for row in cursor.fetchall():
            if is_prime(row[0]):
                primes.append(row[0])
        return primes
    
    def find_sevens(self):
        """Find patterns of 7 (significant in Hebrew)"""
        # Verses divisible by 7
        return self.find_divisible_by(7)
    
    def find_thirteens(self):
        """Find gematria reducing to 13 (Echad/One = 13)"""
        conn = self.db.conn
        cursor = conn.cursor()
        cursor.execute("""
            SELECT v.hebrew_text, v.gematria_katan
            FROM verses v
            WHERE v.gematria_katan = 13
        """)
        return cursor.fetchall()
    
    def cross_reference(self, word1, word2):
        """Compare gematria of two words"""
        val1 = self.gem.calculate(word1)
        val2 = self.gem.calculate(word2)
        
        return {
            "word1": word1,
            "word2": word2,
            "value1": val1,
            "value2": val2,
            "sum": val1 + val2,
            "difference": abs(val1 - val2),
            "product": val1 * val2,
            "equal": val1 == val2,
            "ratio": val1 / val2 if val2 != 0 else 0
        }
    
    def generate_pattern_report(self):
        """Generate comprehensive pattern report"""
        print("="*60)
        print("HEBREW BIBLE PATTERN MINING REPORT")
        print("="*60)
        
        # Total statistics
        stats = self.db.get_verse_stats()
        print(f"\n📊 Database Statistics:")
        print(f"   Total verses: {stats[0]}")
        print(f"   Average gematria: {stats[1]:.1f}")
        print(f"   Max gematria: {stats[2]}")
        
        # Find clusters
        print(f"\n🔍 Gematria Clusters (appearing 2+ times):")
        clusters = self.find_gematria_clusters(2)
        for val, count in clusters[:10]:
            print(f"   {val}: appears {count} times")
        
        # Sevens pattern
        print(f"\n7️⃣  Verses with gematria divisible by 7:")
        sevens = self.find_sevens()
        for row in sevens[:5]:
            print(f"   {row[3]} {row[1]}:{row[2]} = {row[4]}")
        
        # 13s (Echad = 13)
        print(f"\n🔯 Verses with katan gematria = 13 (Echad/One):")
        thirteens = self.find_thirteens()
        for row in thirteens[:5]:
            print(f"   {row[0][:40]}... (katan: {row[1]})")
        
        # Prime gematria
        primes = self.find_prime_gematria()
        print(f"\n🌟 Verses with prime gematria: {len(primes)}")
        
        # Cross references
        print(f"\n⚖️  Notable Cross-References:")
        
        # Elohim vs YHVH
        ref1 = self.cross_reference("אלהים", "יהוה")
        print(f"   Elohim ({ref1['value1']}) vs YHVH ({ref1['value2']})")
        print(f"     Sum: {ref1['sum']}, Difference: {ref1['difference']}")
        
        # Bereshit vs Torah
        ref2 = self.cross_reference("בראשית", "תורה")
        print(f"   Bereshit ({ref2['value1']}) vs Torah ({ref2['value2']})")
        print(f"     Ratio: {ref2['ratio']:.3f}")
        
        print("\n" + "="*60)
        print("Pattern mining complete")
        print("="*60)

if __name__ == "__main__":
    miner = PatternMiner()
    miner.generate_pattern_report()