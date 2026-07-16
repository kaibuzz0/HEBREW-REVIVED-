# Gematria Calculator - Extended
"""
Gematria calculations for Hebrew words
Includes: standard, mispar gadol, mispar katan, mispar siduri
"""

class GematriaCalculator:
    # Standard values
    STANDARD = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
        'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90,
        'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400,
        'ך': 20, 'ם': 40, 'ן': 50, 'ף': 80, 'ץ': 90  # Final forms
    }
    
    # Mispar Gadol (final letters worth hundreds)
    GADOL = {
        **STANDARD,
        'ך': 500, 'ם': 600, 'ן': 700, 'ף': 800, 'ץ': 900
    }
    
    # Mispar Katan (single digits only)
    KATAN = {k: (v % 9 or 9) for k, v in STANDARD.items()}
    
    # Mispar Siduri (ordinal position)
    SIDURI = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
        'י': 10, 'כ': 11, 'ל': 12, 'מ': 13, 'נ': 14, 'ס': 15, 'ע': 16, 'פ': 17, 'צ': 18,
        'ק': 19, 'ר': 20, 'ש': 21, 'ת': 22,
        'ך': 11, 'ם': 13, 'ן': 14, 'ף': 17, 'ץ': 18
    }
    
    def calculate(self, word: str, method: str = 'standard') -> int:
        """Calculate gematria value"""
        mapping = {
            'standard': self.STANDARD,
            'gadol': self.GADOL,
            'katan': self.KATAN,
            'siduri': self.SIDURI
        }.get(method, self.STANDARD)
        
        return sum(mapping.get(c, 0) for c in word)
    
    def all_methods(self, word: str) -> dict:
        """Calculate all gematria methods"""
        return {
            'standard': self.calculate(word, 'standard'),
            'gadol': self.calculate(word, 'gadol'),
            'katan': self.calculate(word, 'katan'),
            'siduri': self.calculate(word, 'siduri')
        }
    
    def compare_words(self, word1: str, word2: str) -> bool:
        """Check if two words have same gematria value"""
        return self.calculate(word1) == self.calculate(word2)
    
    def find_matches(self, target_word: str, word_list: list) -> list:
        """Find words with matching gematria"""
        target = self.calculate(target_word)
        return [w for w in word_list if self.calculate(w) == target]

# Example: Genesis 1:1
if __name__ == "__main__":
    calc = GematriaCalculator()
    
    # Bereshit (In beginning)
    bereshit = "בראשית"
    print(f"{bereshit} (Bereshit):")
    for method, value in calc.all_methods(bereshit).items():
        print(f"  {method}: {value}")
    
    # Elohim
    elohim = "אלהים"
    print(f"\n{elohim} (Elohim):")
    for method, value in calc.all_methods(elohim).items():
        print(f"  {method}: {value}")
    
    # Bara (created)
    bara = "ברא"
    print(f"\n{bara} (Bara):")
    for method, value in calc.all_methods(bara).items():
        print(f"  {method}: {value}")
    
    # First verse total
    first_verse = "בראשית ברא אלהים"
    print(f"\nFirst verse total: {calc.calculate(first_verse)}")