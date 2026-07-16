#!/usr/bin/env python3
"""
Hebrew Resonance Decoder - 8 Seeds System
Based on HEBREW-REVIVED- Genesis Chapter 1 Decoded

8 Seeds: NA, HA, GE, OR, RI, VO, EL, AM
Each represents a phonetic/resonance pattern in Hebrew
"""

from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional
import re

@dataclass
class Phoneme:
    """Represents a phonetic unit"""
    symbol: str
    name: str
    meaning: str
    quality: str  # stillness, breath, form, light, etc.
    hebrew_equiv: List[str]  # Hebrew letters/letter combinations
    examples: List[str]

@dataclass
class DecodedWord:
    """Result of decoding a Hebrew word"""
    original: str
    translit: str
    seeds: List[str]
    seed_sequence: str
    meaning: str
    resonance_pattern: str

class ResonanceEngine:
    """Core engine for Hebrew resonance decoding"""
    
    # The 8 Seeds with their properties
    SEEDS = {
        'NA': Phoneme(
            symbol='NA',
            name='Nun-Aleph',
            meaning='Sacred Stillness',
            quality='stillness',
            hebrew_equiv=['נ', 'ן', 'נא'],
            examples=['נָ', 'נֹ', 'נֻ']
        ),
        'HA': Phoneme(
            symbol='HA',
            name='He-Aleph',
            meaning='Living Breath',
            quality='breath/life',
            hebrew_equiv=['ה', 'הא'],
            examples=['הַ', 'הָ', 'הֶ']
        ),
        'GE': Phoneme(
            symbol='GE',
            name='Gimel-He',
            meaning='Sacred Form',
            quality='pattern/form',
            hebrew_equiv=['ג', 'גה'],
            examples=['גּ', 'ג', 'גְ']
        ),
        'OR': Phoneme(
            symbol='OR',
            name='Ayin-Resh',
            meaning='Unveiling Light',
            quality='light/reveal',
            hebrew_equiv=['ע', 'ר', 'אור', 'ער'],
            examples=['אוֹר', 'עֵר']
        ),
        'RI': Phoneme(
            symbol='RI',
            name='Resh-Yod',
            meaning='Turning Alignment',
            quality='turn/align',
            hebrew_equiv=['ר', 'רי', 'ריא'],
            examples=['רִי', 'רֵא']
        ),
        'VO': Phoneme(
            symbol='VO',
            name='Vav-He',
            meaning='Sounded Truth',
            quality='voice',
            hebrew_equiv=['ו', 'וה'],
            examples=['וֹ', 'וֹא', 'וּ']
        ),
        'EL': Phoneme(
            symbol='EL',
            name='Ayin-Lamed',
            meaning='Seal / Witness',
            quality='seal',
            hebrew_equiv=['אל', 'על'],
            examples=['אֵל', 'אֶל', 'עַל']
        ),
        'AM': Phoneme(
            symbol='AM',
            name='Ayin-Mem',
            meaning='Embodiment',
            quality='manifestation',
            hebrew_equiv=['עם', 'אם', 'ם'],
            examples=['עַם', 'אֵם', 'אַם']
        ),
    }
    
    # Genesis 1:1 mapping
    GENESIS_PATTERNS = {
        'בראשית': {
            'translit': 'bereshit',
            'seeds': ['BE', 'RE', 'SHI', 'YT'],
            'meaning': 'In the beginning of head/creation',
            'pattern': 'container → essence → manifestation → seal'
        },
        'ברא': {
            'translit': 'bara',
            'seeds': ['BA', 'RA'],
            'meaning': 'he created/fattened/filled',
            'pattern': 'entrance + seeing (vision → manifestation)'
        },
        'אלהים': {
            'translit': 'elohim',
            'seeds': ['EL', 'OH', 'IM'],
            'meaning': 'divine powers/council',
            'pattern': 'seal + breath + pluralization'
        },
        'את': {
            'translit': 'et',
            'seeds': ['ET'],
            'meaning': 'direct object marker (marking)',
            'pattern': 'sign/seal'
        },
        'השמים': {
            'translit': 'hashamayim',
            'seeds': ['HA', 'SHA', 'MA', 'YIM'],
            'meaning': 'the heavens (waters above)',
            'pattern': 'breath + fire/water + water + plural'
        },
        'הארץ': {
            'translit': 'haaretz',
            'seeds': ['HA', 'AR', 'ETZ'],
            'meaning': 'the earth (land)',
            'pattern': 'breath + light/source + tree/structure'
        },
    }
    
    def __init__(self):
        self.seed_map = self._build_seed_map()
    
    def _build_seed_map(self) -> Dict[str, str]:
        """Build reverse mapping from Hebrew letters to seeds"""
        mapping = {}
        for seed_name, seed in self.SEEDS.items():
            for heb in seed.hebrew_equiv:
                mapping[heb] = seed_name
        return mapping
    
    def decode_word(self, hebrew_word: str) -> DecodedWord:
        """Decode a Hebrew word into its seed components"""
        # Strip vowels (simplified)
        consonants = self._extract_consonants(hebrew_word)
        
        # Attempt seed extraction
        seeds_found = []
        i = 0
        while i < len(consonants):
            # Try 2-letter match
            if i + 1 < len(consonants):
                pair = consonants[i:i+2]
                if pair in self.seed_map:
                    seeds_found.append(self.seed_map[pair])
                    i += 2
                    continue
            # Try 1-letter match
            if consonants[i] in self.seed_map:
                seeds_found.append(self.seed_map[consonants[i]])
            i += 1
        
        # Generate transliteration (simplified)
        translit = self._transliterate(consonants)
        
        return DecodedWord(
            original=hebrew_word,
            translit=translit,
            seeds=seeds_found,
            seed_sequence=' → '.join(seeds_found) if seeds_found else 'unknown',
            meaning=self._lookup_meaning(hebrew_word),
            resonance_pattern=self._interpret_pattern(seeds_found)
        )
    
    def _extract_consonants(self, text: str) -> str:
        """Remove vowel points and extract consonantal text"""
        # Remove Hebrew vowel points (niqqud)
        # Unicode range for Hebrew vowels: \u0591-\u05C7
        import re
        consonants = re.sub(r'[\u0591-\u05C7]', '', text)
        return consonants
    
    def _transliterate(self, consonants: str) -> str:
        """Simple transliteration"""
        mapping = {
            'א': 'ʾ', 'ב': 'b', 'ג': 'g', 'ד': 'd', 'ה': 'h',
            'ו': 'w', 'ז': 'z', 'ח': 'ḥ', 'ט': 'ṭ', 'י': 'y',
            'כ': 'k', 'ל': 'l', 'מ': 'm', 'נ': 'n', 'ס': 's',
            'ע': 'ʿ', 'פ': 'p', 'צ': 'ṣ', 'ק': 'q', 'ר': 'r',
            'ש': 'š', 'ת': 't', 'ך': 'k', 'ם': 'm', 'ן': 'n',
            'ף': 'p', 'ץ': 'ṣ'
        }
        return ''.join(mapping.get(c, c) for c in consonants)
    
    def _lookup_meaning(self, word: str) -> str:
        """Look up word meaning from built-in dictionary"""
        if word in self.GENESIS_PATTERNS:
            return self.GENESIS_PATTERNS[word]['meaning']
        return "(meaning lookup requires full lexicon)"
    
    def _interpret_pattern(self, seeds: List[str]) -> str:
        """Interpret the resonance pattern from seed sequence"""
        if not seeds:
            return "unknown"
        
        qualities = []
        for seed in seeds:
            if seed in self.SEEDS:
                qualities.append(self.SEEDS[seed].quality)
        
        return ' → '.join(qualities)
    
    def decode_genesis_1_1(self) -> Dict:
        """Decode the full Genesis 1:1 verse"""
        verse = [
            "בְּרֵאשִׁית", "בָּרָא", "אֱלֹהִים", "אֵת",
            "הַשָּׁמַיִם", "וְאֵת", "הָאָרֶץ"
        ]
        
        results = []
        for word in verse:
            decoded = self.decode_word(word)
            results.append({
                'hebrew': word,
                'translit': decoded.translit,
                'seeds': decoded.seed_sequence,
                'meaning': decoded.meaning,
                'pattern': decoded.resonance_pattern
            })
        
        return {
            'verse': 'Genesis 1:1',
            'words': results,
            'full_resonance': ' '.join([r['seeds'] for r in results])
        }
    
    def visualize_word(self, word: str) -> str:
        """Create ASCII visualization of word structure"""
        decoded = self.decode_word(word)
        
        lines = [
            f"Word: {word}",
            f"Translit: {decoded.translit}",
            f"Seeds: {decoded.seed_sequence}",
            f"Pattern: {decoded.resonance_pattern}",
            "─" * 40
        ]
        
        # Show seed breakdown
        for seed in decoded.seeds:
            if seed in self.SEEDS:
                s = self.SEEDS[seed]
                lines.append(f"  {seed}: {s.name} - {s.meaning}")
        
        return '\n'.join(lines)


# Example usage
if __name__ == "__main__":
    engine = ResonanceEngine()
    
    print("=" * 60)
    print("HEBREW RESONANCE DECODER")
    print("8 Seeds: NA HA GE OR RI VO EL AM")
    print("=" * 60)
    print()
    
    # Decode Genesis 1:1
    result = engine.decode_genesis_1_1()
    print(f"{result['verse']}")
    print("=" * 40)
    
    for word_data in result['words']:
        print(f"\n{word_data['hebrew']}")
        print(f"  Transliteration: {word_data['translit']}")
        print(f"  Seeds: {word_data['seeds']}")
        print(f"  Meaning: {word_data['meaning']}")
        print(f"  Pattern: {word_data['pattern']}")
    
    print()
    print("=" * 60)
    print("Full Resonance Flow:")
    print(result['full_resonance'])
    print("=" * 60)