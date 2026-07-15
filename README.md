# HEBREW BIBLE ANALYZER
## Complete Torah Analysis System

**Version:** 3.0  
**Repository:** https://github.com/kaibuzz0/HEBREW-REVIVED-

---

## 🎯 Overview

A comprehensive Hebrew Bible analysis system combining:
- **8 Seeds Pattern Recognition** (NA HA GE OR RI VO EL AM)
- **4 Gematria Methods** (Standard, Katan, Gadol, Siduri)
- **AI-Powered Theological Insights**
- **Web Dashboard** (React/Vue style HTML)
- **Mobile App** (React Native)
- **Translation Layers** (8 layers of analysis)
- **Pattern Mining** (Cross-book connections)

---

## 📊 Current Statistics

| Metric | Count |
|--------|-------|
| Torah Books | 5 |
| Key Verses | 71 |
| Words Analyzed | 428 |
| Total Gematria | 92,824 |
| Word Studies | 5 |
| Python Modules | 15+ |

---

## 🚀 Quick Start

### Requirements
- Python 3.9+
- Node.js 16+ (for mobile)
- Modern web browser

### Installation

```bash
# Clone repository
git clone https://github.com/kaibuzz0/HEBREW-REVIVED-.git
cd HEBREW-REVIVED-

# Setup Python environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run web dashboard
python3 torah_dashboard.py
# Visit http://localhost:8080

# Run gematria calculator
python3 visual_analyzer.py --menu

# Generate patterns
python3 pattern_miner_v2.py
python3 advanced_pattern_analyzer.py

# Generate AI insights
python3 theological_ai_v2.py

# Export to book
python3 torah_exporter.py
```

---

## 📁 Project Structure

```
HEBREW-REVIVED-/
├── Core Modules
│   ├── gematria_calculator.py      # 4-method calculator
│   ├── resonance_decoder.py        # 8 Seeds system
│   ├── biblical_database.py        # SQLite backend
│   └── hebrew_processor.py         # Unified interface
│
├── Import Tools
│   ├── import_genesis_full.py      # Genesis 1-12
│   ├── import_torah_complete_v2.py # All 5 books
│   └── import_genesis_chapter_1_full.py # Full chapter
│
├── Analysis Tools
│   ├── pattern_miner_v2.py         # Genesis 1 patterns
│   ├── advanced_pattern_analyzer.py # Cross-book patterns
│   └── theological_ai_v2.py        # AI insights
│
├── Web & Mobile
│   ├── simple_server.py            # Basic HTTP server
│   ├── torah_dashboard.py          # Interactive dashboard
│   ├── mobile_app/                 # React Native v1
│   └── mobile_app_v2/              # React Native v2
│
├── Export & Documentation
│   ├── torah_exporter.py           # HTML/Markdown export
│   ├── the_living_word/            # Translation layers
│   │   ├── translations/           # 8-layer system
│   │   ├── word_studies/           # Detailed studies
│   │   └── research/               # Additional research
│   └── README.md                   # This file
│
├── Generated Files
│   ├── hebrew_bible.db             # SQLite database
│   ├── genesis_1_patterns.json     # Pattern analysis
│   ├── advanced_patterns.json      # Advanced patterns
│   ├── ai_insights_v2.json         # AI analysis
│   ├── torah_book.html             # HTML export
│   └── torah_summary.md            # Markdown summary
│
└── Legacy (The-Living-word merged)
    └── (integrated into the_living_word/)
```

---

## 🔧 Core Tools

### Gematria Calculator
```python
from gematria_calculator import GematriaCalculator

gem = GematriaCalculator()
value = gem.calculate("בראשית")  # Standard: 913
katan = gem.calculate("בראשית", "katan")  # Reduced: 13
```

### 8 Seeds Decoder
```python
from resonance_decoder import ResonanceEngine

res = ResonanceEngine()
decoded = res.decode_word("בראשית")
print(decoded.seeds)  # ['EL', 'RI', 'HA', ...]
```

### Database Interface
```python
from biblical_database import BiblicalDatabase

db = BiblicalDatabase()
results = db.search_by_gematria(913)
```

---

## 🌐 Web Dashboard

```bash
python3 torah_dashboard.py
```

**Features:**
- Torah books overview
- Real-time statistics
- Hebrew text display
- API endpoints for mobile

**URL:** http://localhost:8080

---

## 📱 Mobile App

### Setup
```bash
cd mobile_app_v2
npm install
npm start
```

**Screens:**
- Dashboard (statistics)
- Torah (book browser)
- Gematria (calculator)

---

## 📖 Translation System

### 8 Layers
1. **Diplomatic** - Original Hebrew
2. **Transliteration** - SBL standard
3. **Morphological** - Word parsing
4. **Word Gloss** - Semantic range
5. **Structure** - Hebrew syntax
6. **Literal** - Readable English
7. **Expanded** - Interpretive options
8. **Commentary** - Full analysis

### Available Passages
- Genesis 1:1 (all 8 layers)
- Various key verses across Torah

---

## 📚 Word Studies

| Word | Hebrew | Theme |
|------|--------|-------|
| bereshit | בְּרֵאשִׁית | In the beginning |
| elohim | אֱלֹהִים | Divine powers |
| bara | בָּרָא | Created (divine only) |
| tselem | צֶלֶם | Image of God |
| or | אוֹר | Light |

---

## 🤖 AI Analysis

### Automated Insights
- Numerical significance detection
- 8 Seeds pattern analysis
- Cross-reference generation
- Theological theme identification

### Running AI Analysis
```bash
python3 theological_ai_v2.py
```

Output: `ai_insights_v2.json`

---

## 🎨 Pattern Analysis

### Genesis 1 Patterns
```bash
python3 pattern_miner_v2.py
```

Discovers:
- RI seed: 15/16 verses
- Creation formula: 8 occurrences
- Multiples of 26 (YHWH): 6 verses

### Cross-Book Patterns
```bash
python3 advanced_pattern_analyzer.py
```

Discovers:
- Divine speech patterns
- Thematic bridges
- Numerical connections

---

## 📤 Export Options

### HTML Book
```bash
python3 torah_exporter.py
# Generates: torah_book.html
```

### Markdown Summary
```bash
# Also generated by torah_exporter.py
# Output: torah_summary.md
```

---

## 🔬 Research Notes

### The 8 Seeds
| Seed | Value | Meaning |
|------|-------|---------|
| NA | 50 | Creation |
| HA | 6 | Breath |
| GE | 7 | Touch |
| OR | 200 | Light |
| RI | 210 | Alignment |
| VO | 12 | Voice |
| EL | 41 | Power |
| AM | 91 | Faithful |

### Key Gematria
- בראשית = 913
- אלהים = 86
- יהוה = 26

---

## 🚧 Next Steps

### Immediate
- [ ] Expand Genesis 1 to all 31 verses
- [ ] Add remaining Genesis chapters
- [ ] Complete Exodus analysis

### Future
- [ ] Nevi'im (Prophets)
- [ ] Ketuvim (Writings)
- [ ] Full Tanakh
- [ ] Greek Septuagint comparison
- [ ] Targum analysis

---

## 📜 License

MIT License - See LICENSE file

---

## 🙏 Acknowledgments

- Westminster Leningrad Codex (WLC)
- SBL Hebrew Font
- Open source Hebrew text projects

---

**Last Updated:** 2026-07-15  
**Status:** Steps 1-8 Complete ✅

**For support:** Open an issue on GitHub

---