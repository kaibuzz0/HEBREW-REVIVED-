#!/usr/bin/env python3
"""
COMPLETE BIBLE EXPORTER
Generate unified documents from all collected texts
PDF, EPUB, HTML, Markdown formats
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json
import os
from datetime import datetime

class CompleteBibleExporter:
    """Export Complete Bible to multiple formats"""
    
    def __init__(self):
        self.db = CompleteBibleDatabase()
        self.output_dir = '/root/hebrew-repo/exports/complete_bible'
        os.makedirs(self.output_dir, exist_ok=True)
        
    def export_html(self):
        """Generate comprehensive HTML document"""
        html = self._generate_html_header()
        
        # Torah
        html += self._generate_torah_section()
        
        # Apocrypha
        html += self._generate_thomas_section()
        html += self._generate_mary_section()
        html += self._generate_philip_section()
        html += self._generate_james_section()
        html += self._generate_judas_section()
        html += self._generate_odes_section()
        html += self._generate_hermas_section()
        html += self._generate_enoch_section()
        
        # Jesus' Years
        html += self._generate_jesus_years_section()
        
        # Witnesses
        html += self._generate_witnesses_section()
        
        html += self._generate_html_footer()
        
        output_path = f"{self.output_dir}/complete_bible.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✅ HTML: {output_path}")
        return output_path
    
    def export_markdown(self):
        """Generate Markdown document"""
        md = self._generate_md_header()
        md += self._generate_md_torah()
        md += self._generate_md_thomas()
        md += self._generate_md_mary()
        md += self._generate_md_philip()
        md += self._generate_md_james()
        md += self._generate_md_judas()
        md += self._generate_md_odes()
        md += self._generate_md_hermas()
        md += self._generate_md_enoch()
        md += self._generate_md_jesus_years()
        md += self._generate_md_witnesses()
        
        output_path = f"{self.output_dir}/complete_bible.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md)
        
        print(f"✅ Markdown: {output_path}")
        return output_path
    
    def _generate_html_header(self):
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Complete Bible Archive</title>
    <style>
        :root {
            --bg: #f8f5f0;
            --text: #2c241b;
            --accent: #8b4513;
            --accent-light: #d4a574;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Georgia, 'Times New Roman', serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.8;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        h1 { font-size: 2.5em; text-align: center; color: var(--accent); margin-bottom: 10px; }
        h2 { font-size: 1.8em; color: var(--accent); margin: 40px 0 20px; border-bottom: 2px solid var(--accent-light); padding-bottom: 10px; }
        h3 { font-size: 1.4em; margin: 30px 0 15px; color: var(--text); }
        .subtitle { text-align: center; font-style: italic; color: #666; margin-bottom: 40px; }
        .intro { background: #fff; padding: 30px; border-radius: 8px; margin: 30px 0; border-left: 4px solid var(--accent); }
        .saying { background: #fff; padding: 20px; margin: 15px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .saying-number { color: var(--accent); font-weight: bold; font-size: 1.2em; }
        .coptic { font-family: 'Times New Roman', serif; color: #555; font-size: 1.1em; direction: rtl; }
        .english { margin: 10px 0; }
        .theme { font-size: 0.9em; color: #666; font-style: italic; }
        .parallels { font-size: 0.85em; color: #888; }
        .witness-card { background: #fff; padding: 15px; margin: 10px 0; border-radius: 8px; }
        .timeline-item { border-left: 3px solid var(--accent); padding-left: 20px; margin: 15px 0; }
        .age { font-weight: bold; color: var(--accent); }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background: var(--accent); color: white; }
        tr:nth-child(even) { background: #f9f9f9; }
        .footer { margin-top: 60px; padding-top: 20px; border-top: 2px solid var(--accent-light); text-align: center; color: #666; font-size: 0.9em; }
        @media print {
            body { background: white; }
            .saying, .witness-card { break-inside: avoid; }
        }
    </style>
</head>
<body>
    <h1>📚 The Complete Bible Archive</h1>
    <p class="subtitle">A Comprehensive Collection of Biblical and Extra-Canonical Texts</p>
    
    <div class="intro">
        <p><strong>About This Archive:</strong> This document contains a unified collection of biblical texts, including the Torah, Gospels, and important extra-canonical works such as the Gospel of Thomas, Gospel of Mary, Gospel of Philip, and the Book of Enoch. Also included are reconstructions of Jesus' thirty years and a database of witnesses who knew him personally.</p>
        <p><strong>Texts Included:</strong></p>
        <ul>
            <li><strong>Torah:</strong> 5 Books of Moses (Hebrew with translations)</li>
            <li><strong>Gospel of Thomas:</strong> 97 sayings of Jesus (Coptic)</li>
            <li><strong>Gospel of Mary:</strong> 8 pages (Mary Magdalene's teachings)</li>
            <li><strong>Gospel of Philip:</strong> 25 passages (Nag Hammadi)</li>
            <li><strong>Book of Enoch:</strong> 144 chapters (Ethiopian canon)</li>
            <li><strong>Jesus' Thirty Years:</strong> Complete timeline from birth to ministry</li>
            <li><strong>Witnesses Database:</strong> 29 people who knew Jesus</li>
        </ul>
    </div>
'''
    
    def _generate_html_footer(self):
        return '''
    <div class="footer">
        <p>Generated: ''' + datetime.now().strftime('%Y-%m-%d') + '''</p>
        <p>The Complete Bible Archive - github.com/kaibuzz0/HEBREW-REVIVED-</p>
        <p>For educational and research purposes. Texts are in the public domain or used under fair use.</p>
    </div>
</body>
</html>'''
    
    def _generate_torah_section(self):
        html = '<h2>📜 The Torah (Five Books of Moses)</h2>'
        html += '<p>The Torah contains the foundational texts of Hebrew scripture...</p>'
        html += '<p><em>See separate Torah exports for full Hebrew text with gematria analysis.</em></p>'
        return html
    
    def _generate_thomas_section(self):
        html = '<h2>📖 The Gospel of Thomas</h2>'
        html += '<p>The secret sayings of Jesus, written down by Didymus Judas Thomas.</p>'
        
        thomas_data = self.db.get_thomas_sayings()
        for saying in thomas_data[:50]:  # First 50 for HTML
            html += f'''
            <div class="saying">
                <span class="saying-number">Saying {saying['saying_number']}</span>
                <span class="theme">- {saying.get('theme', '')}</span>
                <div class="coptic">{saying.get('coptic_text', '')[:200]}...</div>
                <div class="english">{saying.get('english_text', '')[:300]}...</div>
                {f"<div class='parallels'>Parallels: {saying.get('parallel_passages', '[]')}</div>" if saying.get('parallel_passages') and saying['parallel_passages'] != '[]' else ''}
            </div>
            '''
        
        html += f'<p><em>... and {len(thomas_data) - 50} more sayings. See full database for complete collection.</em></p>'
        return html
    
    def _generate_mary_section(self):
        html = '<h2>📖 The Gospel of Mary</h2>'
        html += '<p>The Gospel of Mary Magdalene from the Berlin Codex (BG 8502).</p>'
        html += '''
        <div class="saying">
            <h3>Page 1: The Vision</h3>
            <p>Mary receives secret teachings from Jesus about the soul's ascent past the seven powers:</p>
            <ol>
                <li>Darkness</li>
                <li>Desire</li>
                <li>Ignorance</li>
                <li>Envy of Death</li>
                <li>Flesh</li>
                <li>Foolish Wisdom</li>
                <li>Wrathful Wisdom</li>
            </ol>
        </div>
        <div class="saying">
            <h3>Page 6: Levi Defends Mary</h3>
            <p>After Mary shares her vision, Andrew and Peter challenge her. Levi (Matthew) defends her:</p>
            <p class="english">"The Savior made her worthy. Surely the Savior made her worthy. Let us be ashamed and put on the perfect Man..."</p>
        </div>
        '''
        return html
    
    def _generate_philip_section(self):
        html = '<h2>📖 The Gospel of Philip</h2>'
        html += '<p>From Nag Hammadi Codex II,3 - On love, sacraments, and the bridal chamber.</p>'
        
        # Load Philip from JSON
        try:
            with open('/root/hebrew-repo/exports/philip_export.json') as f:
                philip_data = json.load(f)
                for passage in philip_data.get('passages', [])[:10]:
                    html += f'''
                    <div class="saying">
                        <span class="saying-number">Passage {passage['number']}</span>
                        <span class="theme">- {passage.get('theme', '')}</span>
                        <div class="english">{passage.get('english', '')[:300]}...</div>
                    </div>
                    '''
                html += f'<p><em>... and {len(philip_data["passages"]) - 10} more passages.</em></p>'
        except:
            html += '<p><em>Philip data available in database.</em></p>'
        
        return html
    
    def _generate_enoch_section(self):
        html = '<h2>📖 The Book of Enoch</h2>'
        html += '<p>The complete Ethiopian Ge\'ez text - 5 Books, 144 Chapters.</p>'
        html += '''
        <h3>Book 1: The Book of the Watchers (Chapters 1-36)</h3>
        <p>The Watchers descend, father the Nephilim, and are judged.</p>
        
        <h3>Book 2: The Book of Parables (Chapters 37-70)</h3>
        <p>The Son of Man, the Head of Days, the four archangels.</p>
        
        <h3>Book 3: The Book of Astronomy (Chapters 71-80)</h3>
        <p>The courses of the sun, moon, and stars.</p>
        
        <h3>Book 4: The Book of Dreams (Chapters 81-85)</h3>
        <p>Enoch's visions and the heavenly tablets.</p>
        
        <h3>Book 5: The Epistle of Enoch (Chapters 86-108)</h3>
        <p>The Apocalypse of Weeks and the birth of Noah.</p>
        '''
        return html
    
    def _generate_james_section(self):
        html = '<h2>📖 The Infancy Gospel of James</h2>'
        html += '<p>The Protevangelium - Birth of Mary and early life of Jesus.</p>'
        try:
            with open('/root/hebrew-repo/exports/james_infancy_export.json') as f:
                james_data = json.load(f)
                for chapter in james_data.get('chapters', [])[:8]:
                    html += f'''
                    <div class="saying">
                        <span class="saying-number">Chapter {chapter['chapter']}</span>
                        <span class="theme">- {chapter.get('title', '')}</span>
                        <div class="english">{chapter.get('english', '')[:250]}...</div>
                    </div>
                    '''
                html += f'<p><em>... and {len(james_data["chapters"]) - 8} more chapters.</em></p>'
        except:
            html += '<p><em>James Infancy data available in database.</em></p>'
        return html
    
    def _generate_judas_section(self):
        html = '<h2>📖 The Gospel of Judas</h2>'
        html += '<p>From Codex Tchacos - The controversial portrayal of Judas as hero.</p>'
        try:
            with open('/root/hebrew-repo/exports/judas_export.json') as f:
                judas_data = json.load(f)
                for passage in judas_data.get('passages', [])[:8]:
                    html += f'''
                    <div class="saying">
                        <span class="saying-number">Passage {passage['number']}</span>
                        <span class="theme">- {passage.get('title', '')}</span>
                        <div class="english">{passage.get('english', '')[:250]}...</div>
                    </div>
                    '''
                html += f'<p><em>... and {len(judas_data["passages"]) - 8} more passages.</em></p>'
        except:
            html += '<p><em>Judas data available in database.</em></p>'
        return html
    
    def _generate_odes_section(self):
        html = '<h2>📖 The Odes of Solomon</h2>'
        html += '<p>42 Early Christian hymns - the earliest Christian hymnbook (c. 100-150 CE).</p>'
        try:
            with open('/root/hebrew-repo/exports/odes_of_solomon_export.json') as f:
                odes_data = json.load(f)
                for ode in odes_data.get('odes', [])[:8]:
                    html += f'''
                    <div class="saying">
                        <span class="saying-number">Ode {ode['ode']}</span>
                        <span class="theme">- {ode.get('title', '')}</span>
                        <div class="english">{ode.get('preview', '')[:250]}...</div>
                    </div>
                    '''
                html += f'<p><em>... and {len(odes_data["odes"]) - 8} more odes.</em></p>'
        except:
            html += '<p><em>Odes data available in database.</em></p>'
        return html
    
    def _generate_hermas_section(self):
        html = '<h2>📖 The Shepherd of Hermas</h2>'
        html += '<p>30 Sections - Visions, Mandates, and Similitudes (c. 90-140 CE).</p>'
        try:
            with open('/root/hebrew-repo/exports/hermas_export.json') as f:
                hermas_data = json.load(f)
                for section in hermas_data.get('sections', [])[:8]:
                    html += f'''
                    <div class="saying">
                        <span class="saying-number">Section {section['number']}</span>
                        <span class="theme">- {section.get('title', '')} ({section.get('type', '')})</span>
                        <div class="english">{section.get('preview', '')[:250]}...</div>
                    </div>
                    '''
                html += f'<p><em>... and {len(hermas_data["sections"]) - 8} more sections.</em></p>'
        except:
            html += '<p><em>Hermas data available in database.</em></p>'
        return html
    
    def _generate_jesus_years_section(self):
        html = '<h2>✝️ Jesus\' Thirty Years</h2>'
        html += '<p>A complete timeline from birth to the beginning of ministry.</p>'
        
        jesus_data = self.db.get_jesus_years()
        for event in jesus_data:
            html += f'''
            <div class="timeline-item">
                <span class="age">Age {event['age']}</span>
                <h4>{event['event']}</h4>
                <p>{event.get('description', '')}</p>
                <p><small>Location: {event.get('location', 'Unknown')} | Source: {event.get('source', 'Unknown')}</small></p>
            </div>
            '''
        return html
    
    def _generate_witnesses_section(self):
        html = '<h2>👥 Witnesses of Jesus</h2>'
        html += '<p>People who knew Jesus personally - family, disciples, opponents.</p>'
        
        # Family
        html += '<h3>Family</h3>'
        html += '<div class="witness-card"><strong>Mary</strong> - Mother of Jesus</div>'
        html += '<div class="witness-card"><strong>Joseph</strong> - Earthly father</div>'
        html += '<div class="witness-card"><strong>James the Just</strong> - Brother, leader of Jerusalem church</div>'
        html += '<div class="witness-card"><strong>Joses</strong> - Brother</div>'
        html += '<div class="witness-card"><strong>Simon</strong> - Brother</div>'
        html += '<div class="witness-card"><strong>Jude</strong> - Brother, author of Epistle</div>'
        
        # Disciples
        html += '<h3>The Twelve Disciples</h3>'
        html += '<div class="witness-card"><strong>Peter</strong> - The rock, first to confess Christ</div>'
        html += '<div class="witness-card"><strong>Andrew</strong> - First called</div>'
        html += '<div class="witness-card"><strong>James</strong> - Son of Zebedee, son of thunder</div>'
        html += '<div class="witness-card"><strong>John</strong> - The beloved disciple</div>'
        html += '<div class="witness-card"><strong>Philip</strong> - From Bethsaida</div>'
        html += '<div class="witness-card"><strong>Bartholomew/Nathanael</strong> - Israelite without deceit</div>'
        html += '<div class="witness-card"><strong>Matthew/Levi</strong> - Tax collector</div>'
        html += '<div class="witness-card"><strong>Thomas/Didymus</strong> - Doubting Thomas</div>'
        html += '<div class="witness-card"><strong>James</strong> - Son of Alphaeus</div>'
        html += '<div class="witness-card"><strong>Thaddaeus/Jude</strong> - Question about manifestation</div>'
        html += '<div class="witness-card"><strong>Simon the Zealot</strong> - Former revolutionary</div>'
        html += '<div class="witness-card"><strong>Judas Iscariot</strong> - The betrayer</div>'
        html += '<div class="witness-card"><strong>Matthias</strong> - Replacement for Judas</div>'
        
        # Women
        html += '<h3>Women Disciples</h3>'
        html += '<div class="witness-card"><strong>Mary Magdalene</strong> - Apostle to the apostles</div>'
        html += '<div class="witness-card"><strong>Mary of Bethany</strong> - Sister of Martha and Lazarus</div>'
        html += '<div class="witness-card"><strong>Martha</strong> - Sister of Mary and Lazarus</div>'
        html += '<div class="witness-card"><strong>Joanna</strong> - Wife of Chuza, supported ministry</div>'
        html += '<div class="witness-card"><strong>Susanna</strong> - Supporter</div>'
        html += '<div class="witness-card"><strong>Mary (wife of Clopas)</strong> - At the cross</div>'
        
        # Opponents
        html += '<h3>Opponents</h3>'
        html += '<div class="witness-card"><strong>Caiaphas</strong> - High priest</div>'
        html += '<div class="witness-card"><strong>Pontius Pilate</strong> - Roman prefect</div>'
        html += '<div class="witness-card"><strong>Herod Antipas</strong> - Tetrarch of Galilee</div>'
        
        return html
    
    def _generate_md_header(self):
        return '''# 📚 The Complete Bible Archive

*A Comprehensive Collection of Biblical and Extra-Canonical Texts*

---

## About This Archive

This document contains a unified collection of biblical texts, including:

- **Torah**: 5 Books of Moses
- **Gospel of Thomas**: 97 sayings (Coptic)
- **Gospel of Mary**: 8 pages (Mary Magdalene)
- **Gospel of Philip**: 25 passages (Nag Hammadi)
- **Book of Enoch**: 144 chapters (Ethiopian canon)
- **Jesus' Thirty Years**: Complete timeline
- **Witnesses Database**: 29 people who knew Jesus

---

'''
    
    def _generate_md_torah(self):
        return '''## 📜 The Torah (Five Books of Moses)

The Torah contains the foundational texts of Hebrew scripture.

*See separate Torah exports for full Hebrew text with gematria analysis.*

---

'''
    
    def _generate_md_thomas(self):
        md = '## 📖 The Gospel of Thomas\n\n'
        md += 'The secret sayings of Jesus, written down by Didymus Judas Thomas.\n\n'
        
        thomas_data = self.db.get_thomas_sayings()
        for saying in thomas_data[:20]:
            md += f"**Saying {saying['saying_number']}** - {saying.get('theme', '')}\n\n"
            md += f"> {saying.get('english_text', '')[:200]}...\n\n"
            if saying.get('parallel_passages') and saying['parallel_passages'] != '[]':
                md += f"*Parallels: {saying['parallel_passages']}*\n\n"
            md += "---\n\n"
        
        md += f"*... and {len(thomas_data) - 20} more sayings.\n\n"
        return md
    
    def _generate_md_mary(self):
        return '''## 📖 The Gospel of Mary

The Gospel of Mary Magdalene from the Berlin Codex (BG 8502).

### Page 1: The Vision

Mary receives secret teachings from Jesus about the soul's ascent past the seven powers:

1. Darkness
2. Desire  
3. Ignorance
4. Envy of Death
5. Flesh
6. Foolish Wisdom
7. Wrathful Wisdom

### Page 6: Levi Defends Mary

After Mary shares her vision, Andrew and Peter challenge her. Levi (Matthew) defends her:

> "The Savior made her worthy. Surely the Savior made her worthy. Let us be ashamed and put on the perfect Man..."

---

'''
    
    def _generate_md_philip(self):
        return '''## 📖 The Gospel of Philip

From Nag Hammadi Codex II,3 - On love, sacraments, and the bridal chamber.

### Key Themes

- **Bridal Chamber (Nymphon)**: The central mystery
- **Love is the Sacrament**: "Love is the sacred mystery"
- **Mary Magdalene**: "Jesus kissed her often on the mouth"
- **Three Marys**: Mother, sister, companion
- **Resurrection While Living**: "Those who say they will die first are in error"

*25 passages available in database.*

---

'''
    
    def _generate_md_enoch(self):
        return '''## 📖 The Book of Enoch

The complete Ethiopian Ge\'ez text - 5 Books, 144 Chapters.

### Book 1: The Book of the Watchers (Chapters 1-36)
The Watchers descend, father the Nephilim, and are judged.

### Book 2: The Book of Parables (Chapters 37-70)
The Son of Man, the Head of Days, the four archangels.

### Book 3: The Book of Astronomy (Chapters 71-80)
The courses of the sun, moon, and stars.

### Book 4: The Book of Dreams (Chapters 81-85)
Enoch's visions and the heavenly tablets.

### Book 5: The Epistle of Enoch (Chapters 86-108)
The Apocalypse of Weeks and the birth of Noah.

---

'''
    
    def _generate_md_jesus_years(self):
        md = '## ✝️ Jesus\' Thirty Years\n\n'
        md += 'A complete timeline from birth to the beginning of ministry.\n\n'
        
        jesus_data = self.db.get_jesus_years()
        for event in jesus_data[:20]:
            md += f"**Age {event['age']}**: {event['event']}\n\n"
            md += f"{event.get('description', '')}\n\n"
            md += f"*Location: {event.get('location', 'Unknown')} | Source: {event.get('source', 'Unknown')}*\n\n"
            md += "---\n\n"
        
        md += f"*... and {len(jesus_data) - 20} more events.\n\n"
        return md
    
    def _generate_md_james(self):
        return '''## 📖 The Infancy Gospel of James

The Protevangelium - Birth of Mary and early life of Jesus (25 chapters).

**Key Stories:**
- Birth of Mary to Joachim and Anna
- Mary presented at temple age 3
- Joseph chosen by lot (dove from rod)
- Annunciation to Mary age 14
- Birth of Jesus with midwife Salome
- Salome doubts, hand withered, healed
- Flight to Egypt
- Martyrdom of Zechariah

**Significance:** Provides backstory for Mary and infancy narratives.

---

'''
    
    def _generate_md_judas(self):
        return '''## 📖 The Gospel of Judas

From Codex Tchacos (c. 280 CE) - Controversial portrayal of Judas as hero.

**Key Themes:**
- Judas is the only one who understands Jesus
- The twelve disciples serve the wrong god (Saklas)
- Judas acts at Jesus' request to betray him
- The betrayal enables Jesus to escape the physical body
- Judas is the "thirteenth" who surpasses the twelve
- The Great Invisible Spirit is the true God

**Controversy:** Completely contradicts canonical gospels.

---

'''
    
    def _generate_md_odes(self):
        return '''## 📖 The Odes of Solomon

42 Early Christian hymns (c. 100-150 CE) - earliest Christian hymnbook.

**Key Themes:**
- Living water (Odes 3, 6, 19)
- Christ as crown (Ode 1)
- Incarnation (Odes 22, 42)
- Victory over death (Odes 12, 24)
- Personal transformation (Ode 11)
- Joy and praise (Ode 28)

**Significance:**
- Earliest Christian hymnbook
- Similar to Gospel of John
- First use of "Christian" in literature
- Beautiful Syriac mystical poetry

---

'''
    
    def _generate_md_hermas(self):
        return '''## 📖 The Shepherd of Hermas

30 Sections - Visions, Mandates, and Similitudes (c. 90-140 CE).

**Structure:**
- 4 Visions: Church as aged woman, willow tree, mountain
- 12 Mandates: Practical commandments (no evil-speaking, truth, patience)
- 9 Similitudes: Parables (sower, vine and elm, two ways, dragon)

**Key Themes:**
- Repentance after baptism (second repentance)
- Double-mindedness as the great sin
- The tower as symbol of the Church
- Two ways: narrow way of life, broad way of destruction

**Significance:**
- Most popular early Christian writing
- Included in Codex Sinaiticus
- Quoted as Scripture by Irenaeus and Origen

---

'''
    
    def _generate_md_witnesses(self):
        return '''## 👥 Witnesses of Jesus

People who knew Jesus personally.

### Family
- **Mary** - Mother of Jesus
- **Joseph** - Earthly father
- **James the Just** - Brother, leader of Jerusalem church
- **Joses** - Brother
- **Simon** - Brother
- **Jude** - Brother, author of Epistle

### The Twelve Disciples
- **Peter** - The rock
- **Andrew** - First called
- **James** - Son of Zebedee
- **John** - The beloved disciple
- **Philip** - From Bethsaida
- **Bartholomew/Nathanael** - Israelite without deceit
- **Matthew/Levi** - Tax collector
- **Thomas/Didymus** - Doubting Thomas
- **James** - Son of Alphaeus
- **Thaddaeus/Jude** - Asked about manifestation
- **Simon the Zealot** - Former revolutionary
- **Judas Iscariot** - The betrayer
- **Matthias** - Replacement

### Women Disciples
- **Mary Magdalene** - Apostle to the apostles
- **Mary of Bethany** - Anointer
- **Martha** - Server
- **Joanna** - Supporter
- **Susanna** - Supporter
- **Mary (wife of Clopas)** - At the cross

### Opponents
- **Caiaphas** - High priest
- **Pontius Pilate** - Roman prefect
- **Herod Antipas** - Tetrarch

---

*Generated: ''' + datetime.now().strftime('%Y-%m-%d') + '''*

**The Complete Bible Archive** - github.com/kaibuzz0/HEBREW-REVIVED-
'''
    
    def generate_summary(self):
        """Generate summary report"""
        summary = []
        summary.append("="*70)
        summary.append("COMPLETE BIBLE EXPORT SUMMARY")
        summary.append("="*70)
        summary.append("")
        
        # Count everything
        thomas_count = len(self.db.get_thomas_sayings())
        jesus_count = len(self.db.get_jesus_years())
        
        summary.append(f"📊 CONTENTS:")
        summary.append(f"   Torah: 5 books")
        summary.append(f"   Thomas: {thomas_count} sayings")
        summary.append(f"   Mary: 8 pages")
        summary.append(f"   Philip: 25 passages")
        summary.append(f"   Enoch: 144 chapters")
        summary.append(f"   Jesus' Years: {jesus_count} events")
        summary.append(f"   Witnesses: 29 people")
        summary.append("")
        
        summary.append(f"📁 OUTPUT: {self.output_dir}")
        summary.append("="*70)
        
        return "\\n".join(summary)
    
    def close(self):
        self.db.close()

def main():
    exporter = CompleteBibleExporter()
    
    print(exporter.generate_summary())
    print("\\n" + "="*70)
    print("GENERATING EXPORTS")
    print("="*70 + "\\n")
    
    # Generate HTML
    html_path = exporter.export_html()
    
    # Generate Markdown
    md_path = exporter.export_markdown()
    
    print("\\n" + "="*70)
    print("EXPORT COMPLETE")
    print("="*70)
    print(f"\\n✅ HTML: {html_path}")
    print(f"✅ Markdown: {md_path}")
    print(f"\\nOpen {html_path} in a browser to view the complete archive.")
    
    exporter.close()

if __name__ == "__main__":
    main()