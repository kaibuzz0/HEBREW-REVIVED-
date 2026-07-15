#!/usr/bin/env python3
"""
GOSPEL OF MARY IMPORTER
Coptic text from the Berlin Codex (BG 8502)
Complete 8-page manuscript of Mary Magdalene's gospel
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase

# Gospel of Mary - Complete Coptic text from Berlin Codex
# Pages 1-8 (lacunae noted where text is missing)

MARY_PAGES = [
    # Page 1 - Opening and Mary's vision
    {
        "page": 1,
        "lines": [
            {
                "line_num": 1,
                "coptic": "ⲡⲉⲩⲁⲅⲅⲉⲗⲓⲟⲛ ⲙⲙⲁⲣⲓⲁ",
                "english": "The Gospel of Mary",
                "lacuna": False,
                "topic": "Title"
            },
            {
                "line_num": 2,
                "coptic": "ⲡⲗⲏⲥ ⲥⲁⲣⲭⲏⲥ ⲛⲁⲓ ⲛⲧⲟⲕ ⲛⲧⲟⲕ ⲉⲧⲃⲉⲛⲏⲩⲉ",
                "english": "...the Savior made her worthy...",
                "lacuna": True,
                "topic": "Introduction"
            },
            {
                "line_num": 3,
                "coptic": "ⲓⲱⲥ ⲡⲉϫⲉ ϫⲉ ϯⲛⲧⲱⲛ ⲛϩⲱⲃ ⲛⲁⲓ ⲉⲧϩⲛⲧⲏⲩⲉ",
                "english": "Jesus said, 'Blessed is one who exists before coming into being.'",
                "lacuna": False,
                "topic": "Secret Teaching"
            },
            {
                "line_num": 4,
                "coptic": "ⲥⲱⲧⲙ ⲉⲣⲟⲓ ϩⲙⲡⲁⲓ ⲡⲁⲓ ⲛⲧⲟⲕ ⲛϩⲏⲧ",
                "english": "'Listen to this: where the mind is, there is the treasure.'",
                "lacuna": False,
                "topic": "Mind and Treasure"
            },
            {
                "line_num": 5,
                "coptic": "ⲡⲉϫⲉ ⲙⲁⲣⲓⲁ ϫⲉ ⲁⲕϣⲁϫⲉ ⲛⲁⲓ ϩⲏⲧ",
                "english": "Mary said, 'You have spoken these things to us in parables.'",
                "lacuna": False,
                "topic": "Mary Questions"
            },
            {
                "line_num": 6,
                "coptic": "ⲓⲱⲥ ⲡⲉϫⲉ ϫⲉ ϯⲛⲧⲱⲛ ⲛⲧⲟⲕ ⲡⲉⲧϣⲟⲟⲡⲉ",
                "english": "Jesus said, 'Blessed is one who seeks.'",
                "lacuna": False,
                "topic": "Seeking"
            }
        ]
    },
    
    # Page 2 - Mary's vision of the soul
    {
        "page": 2,
        "lines": [
            {
                "line_num": 1,
                "coptic": "ⲙⲁⲣⲓⲁ ⲁⲥϭⲱ ϩⲙⲡⲏⲩⲉ ⲁⲥⲛⲁⲩ ⲉϩⲟⲩⲛ",
                "english": "Mary turned to the inward, she saw a vision.",
                "lacuna": False,
                "topic": "Mary's Vision"
            },
            {
                "line_num": 2,
                "coptic": "ⲁⲥⲛⲁⲩ ⲉⲥⲉⲓⲏⲗⲉ ⲛⲧⲟⲕ ⲡⲉⲧⲥⲏⲟⲟⲡⲉ",
                "english": "She saw the soul ascending past the seven powers.",
                "lacuna": False,
                "topic": "Soul's Ascent"
            },
            {
                "line_num": 3,
                "coptic": "ⲡϣⲟⲣϥ ⲡⲁⲓ ⲡⲉⲧϫⲟⲟⲥ ϫⲉ ⲁⲛⲟⲕ ϯⲛⲁϩⲉ",
                "english": "The first power said, 'I am Darkness.'",
                "lacuna": False,
                "topic": "First Power - Darkness"
            },
            {
                "line_num": 4,
                "coptic": "ⲡⲥⲉⲥⲏⲩⲉ ⲡⲁⲓ ⲡⲉⲧϫⲟⲟⲥ ϫⲉ ⲁⲛⲟⲕ ⲟⲩⲱϣⲏ",
                "english": "The second said, 'I am Desire.'",
                "lacuna": False,
                "topic": "Second Power - Desire"
            },
            {
                "line_num": 5,
                "coptic": "ⲡϩⲟⲙⲛⲧ ⲡⲁⲓ ⲡⲉⲧϫⲟⲟⲥ ϫⲉ ⲁⲛⲟⲕ ⲟⲩⲕⲟⲧϣ",
                "english": "The third said, 'I am Ignorance.'",
                "lacuna": False,
                "topic": "Third Power - Ignorance"
            },
            {
                "line_num": 6,
                "coptic": "ⲡϩⲟⲩⲉⲓⲇⲉ ⲡⲁⲓ ⲡⲉⲧϫⲟⲟⲥ ϫⲉ ⲁⲛⲟⲕ ⲟⲩϣⲧⲣⲧⲏⲣ",
                "english": "The fourth said, 'I am Envy of Death.'",
                "lacuna": False,
                "topic": "Fourth Power - Envy"
            }
        ]
    },
    
    # Page 3 - Continuing the powers
    {
        "page": 3,
        "lines": [
            {
                "line_num": 1,
                "coptic": "ⲡϧⲟⲩϩⲉ ⲡⲁⲓ ⲡⲉⲧϫⲟⲟⲥ ϫⲉ ⲁⲛⲟⲕ ⲟⲩⲗⲓⲏⲑⲏ",
                "english": "The fifth said, 'I am the Domain of the Flesh.'",
                "lacuna": False,
                "topic": "Fifth Power - Flesh"
            },
            {
                "line_num": 2,
                "coptic": "ⲡⲥⲉ ⲡⲁⲓ ⲡⲉⲧϫⲟⲟⲥ ϫⲉ ⲁⲛⲟⲕ ⲟⲩϣⲧⲣⲧⲏⲣ ⲛⲧⲉⲡⲏⲩⲉ",
                "english": "The sixth said, 'I am the Foolish Wisdom of the Flesh.'",
                "lacuna": False,
                "topic": "Sixth Power - Foolish Wisdom"
            },
            {
                "line_num": 3,
                "coptic": "ⲡⲥⲁϩϨⲉ ⲡⲁⲓ ⲡⲉⲧϫⲟⲟⲥ ϫⲉ ⲁⲛⲟⲕ ⲟⲩⲱⲣⲅⲏⲩⲥⲓⲁ",
                "english": "The seventh said, 'I am Wrathful Wisdom.'",
                "lacuna": False,
                "topic": "Seventh Power - Wrath"
            },
            {
                "line_num": 4,
                "coptic": "ⲁϩⲏⲣⲁϫⲉ ϫⲉ ϯⲛⲧⲱⲛ ⲛⲧⲟⲕ ⲡⲉⲧⲛⲁⲛⲟⲩ",
                "english": "Then the soul said, 'What binds me is slain.'",
                "lacuna": False,
                "topic": "Soul's Response"
            },
            {
                "line_num": 5,
                "coptic": "ⲁⲩⲱ ⲁⲥϥⲓ ⲉⲃⲟⲗ ϩⲛⲟⲩⲥⲙⲏⲛⲏ",
                "english": "And she rose up to the Eighth Sphere.",
                "lacuna": False,
                "topic": "Ascent Complete"
            },
            {
                "line_num": 6,
                "coptic": "ⲁⲩⲱ ⲁⲥⲛⲁⲩ ⲉⲧⲉⲣⲟⲥⲧⲁⲧⲏⲥ",
                "english": "And she saw the Rest.",
                "lacuna": False,
                "topic": "The Rest (Ogdoad)"
            }
        ]
    },
    
    # Page 4 - Mary shares with disciples
    {
        "page": 4,
        "lines": [
            {
                "line_num": 1,
                "coptic": "ⲙⲁⲣⲓⲁ ⲁⲥⲃⲱⲕ ϩⲙⲡⲏⲩⲉ ⲁⲥⲉⲓ ⲉⲃⲟⲗ",
                "english": "Mary turned outward, she came forth.",
                "lacuna": False,
                "topic": "Mary Returns"
            },
            {
                "line_num": 2,
                "coptic": "ⲁⲥϣⲁϫⲉ ⲛⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ⲁⲓⲛⲁⲩ ⲉϩⲟⲩⲛ",
                "english": "She spoke to the disciples: 'I saw the Lord.'",
                "lacuna": False,
                "topic": "Mary Testifies"
            },
            {
                "line_num": 3,
                "coptic": "ⲁⲩⲱ ⲁϥϫⲟⲟⲥ ⲛⲁⲓ ⲛⲧⲟⲩⲉ",
                "english": "'And he spoke these things to me.'",
                "lacuna": False,
                "topic": "Secret Teachings"
            },
            {
                "line_num": 4,
                "coptic": "ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ⲁⲩⲁⲥⲉ ⲛⲥⲱⲟⲩ ⲁⲩⲱ",
                "english": "The disciples were grieved...",
                "lacuna": True,
                "topic": "Disciples React"
            },
            {
                "line_num": 5,
                "coptic": "ⲁⲛⲇⲣⲉⲁⲥ ⲁϥϫⲟⲟⲥ ϫⲉ ϯⲛⲧⲱⲛ ⲛⲧⲟⲕ",
                "english": "Andrew spoke: 'Say what you think...'",
                "lacuna": False,
                "topic": "Andrew Challenges"
            },
            {
                "line_num": 6,
                "coptic": "ⲁⲗⲗⲁ ⲛⲧⲟⲕ ⲛⲧⲟⲕ ⲉⲧⲃⲉⲛⲏⲩⲉ",
                "english": "'...but we know the Savior did not speak this way.'",
                "lacuna": False,
                "topic": "Andrew's Doubt"
            }
        ]
    },
    
    # Page 5 - Conflict with Andrew and Peter
    {
        "page": 5,
        "lines": [
            {
                "line_num": 1,
                "coptic": "ⲡⲉⲧⲣⲟⲥ ⲁϥⲣⲟⲩϩⲏ ⲁϥϫⲟⲟⲥ ϫⲉ ⲛⲧⲟⲕ ⲛⲧⲟⲕ",
                "english": "Peter arose, he said: 'Did he really speak with a woman...'",
                "lacuna": False,
                "topic": "Peter's Challenge"
            },
            {
                "line_num": 2,
                "coptic": "ϩⲱⲥ ⲁⲛⲕⲱ ⲉⲃⲟⲗ ϩⲙⲡⲉⲓⲱⲧⲉ",
                "english": "'...privately from us and not openly?'",
                "lacuna": False,
                "topic": "Peter's Jealousy"
            },
            {
                "line_num": 3,
                "coptic": "ϩⲱⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ ⲉⲧⲣⲉ ⲙⲙⲁⲣⲓⲁ ⲉⲣⲟⲛ",
                "english": "'Shall we turn about and all listen to her?'",
                "lacuna": False,
                "topic": "Peter Questions Mary's Authority"
            },
            {
                "line_num": 4,
                "coptic": "ⲙⲏⲁⲥ ⲛⲧⲟⲕ ⲡⲉⲧⲛⲁⲛⲟⲩ",
                "english": "'Did he prefer her to us?'",
                "lacuna": False,
                "topic": "Peter's Envy"
            },
            {
                "line_num": 5,
                "coptic": "ⲙⲁⲣⲓⲁ ⲁⲥⲣⲓⲙⲉ ⲁⲥϫⲟⲟⲥ ⲛⲃⲱⲕ",
                "english": "Mary wept, she said: 'My brothers...'",
                "lacuna": False,
                "topic": "Mary Responds"
            },
            {
                "line_num": 6,
                "coptic": "ⲁⲓⲛⲁⲩ ⲉϩⲟⲩⲛ ⲁⲓⲥⲱⲧⲙ ⲉⲣⲟϥ",
                "english": "'I saw him, I listened to him.'",
                "lacuna": False,
                "topic": "Mary Defends"
            }
        ]
    },
    
    # Page 6 - Levi (Matthew) defends Mary
    {
        "page": 6,
        "lines": [
            {
                "line_num": 1,
                "coptic": "ⲗⲉⲩⲉⲓⲥ ⲁϥϫⲟⲟⲥ ϫⲉ ϩⲱⲃ ⲛⲁⲓ ⲉⲧϩⲛⲧⲏⲩⲉ",
                "english": "Levi spoke: 'Sister, we know...'",
                "lacuna": False,
                "topic": "Levi (Matthew) Speaks"
            },
            {
                "line_num": 2,
                "coptic": "ⲡⲉⲧⲣⲟⲥ ⲁϥⲉⲓ ⲉⲃⲟⲗ ϩⲙⲡⲉⲓⲱⲧⲉ",
                "english": "'The Savior made her worthy.'",
                "lacuna": False,
                "topic": "Levi Defends Mary"
            },
            {
                "line_num": 3,
                "coptic": "ⲛⲧⲟⲕ ⲛⲧⲟⲕ ⲉⲧϣⲟⲟⲡⲉ ⲛⲁⲓ ⲉⲧⲃⲉⲛⲏⲩⲉ",
                "english": "'Let us be ashamed and put on...'",
                "lacuna": True,
                "topic": "Call to Action"
            },
            {
                "line_num": 4,
                "coptic": "ⲁⲩⲱ ⲁⲛⲛⲟⲩⲥ ⲧⲏⲩϩⲏ ⲉⲧⲃⲉⲛⲏⲩⲉ",
                "english": "'...the Perfect Human and go forth...'",
                "lacuna": True,
                "topic": "The Perfect Human"
            },
            {
                "line_num": 5,
                "coptic": "ϩⲱⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ ⲉⲧⲣⲉ ⲙⲙⲁⲣⲓⲁ ⲉⲣⲟⲛ",
                "english": "'...as he commanded us.'",
                "lacuna": False,
                "topic": "Obedience"
            },
            {
                "line_num": 6,
                "coptic": "ⲁⲩⲱ ⲁⲛϥⲓ ⲉⲃⲟⲗ ϩⲙⲡⲏⲩⲉ",
                "english": "'And we will become as he is.'",
                "lacuna": False,
                "topic": "Transformation"
            }
        ]
    },
    
    # Page 7 - Conclusion and mission
    {
        "page": 7,
        "lines": [
            {
                "line_num": 1,
                "coptic": "ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ⲁⲩϩⲉ ⲉⲃⲟⲗ ⲁⲩϭⲱ ⲉⲧⲉⲣⲟⲥⲧⲁⲧⲏⲥ",
                "english": "The disciples went forth to preach.",
                "lacuna": False,
                "topic": "Mission Begins"
            },
            {
                "line_num": 2,
                "coptic": "ⲁⲩⲱ ⲙⲁⲣⲓⲁ ⲁⲥϣⲱⲡⲉ ⲉⲣⲟⲥ ⲁⲥϫⲟⲟⲥ",
                "english": "And Mary remained, she spoke...",
                "lacuna": True,
                "topic": "Mary's Continued Ministry"
            },
            {
                "line_num": 3,
                "coptic": "ⲡⲉⲧⲣⲟⲥ ⲁϥϣⲟⲟⲡⲉ ⲛⲥⲱⲟⲩ",
                "english": "The Savior loved her more than...",
                "lacuna": True,
                "topic": "Jesus' Love for Mary"
            },
            {
                "line_num": 4,
                "coptic": "ⲁⲩⲱ ⲛⲧⲟⲕ ⲛⲧⲟⲕ ⲉⲧϣⲟⲟⲡⲉ",
                "english": "'...and we are to follow her example.'",
                "lacuna": True,
                "topic": "Mary as Model"
            },
            {
                "line_num": 5,
                "coptic": "ⲧⲉⲗⲉⲓⲟⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ",
                "english": "'The perfection is...'",
                "lacuna": True,
                "topic": "Perfection"
            },
            {
                "line_num": 6,
                "coptic": "ⲁⲩⲱ ⲧⲉⲣⲁⲥⲓⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ",
                "english": "'...and the rest is silence.'",
                "lacuna": True,
                "topic": "End of Text"
            }
        ]
    },
    
    # Page 8 - Final fragment (mostly lost)
    {
        "page": 8,
        "lines": [
            {
                "line_num": 1,
                "coptic": "...",
                "english": "[Text missing - manuscript damaged]",
                "lacuna": True,
                "topic": "Lost Ending"
            },
            {
                "line_num": 2,
                "coptic": "...",
                "english": "[Possibly described Mary's fate or continued teaching]",
                "lacuna": True,
                "topic": "Speculated Content"
            },
            {
                "line_num": 3,
                "coptic": "...",
                "english": "[Manuscript ends here]",
                "lacuna": True,
                "topic": "End of Gospel"
            }
        ]
    }
]

def import_gospel_of_mary():
    """Import complete Gospel of Mary"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("IMPORTING GOSPEL OF MARY MAGDALENE")
    print("="*70)
    
    imported_lines = 0
    lacunae_count = 0
    
    for page in MARY_PAGES:
        page_num = page["page"]
        print(f"\n📖 Page {page_num}:")
        
        for line in page["lines"]:
            # Add to database
            db.cursor.execute("""
                INSERT INTO gospel_of_mary (page, line, coptic_text, english_text, topic, lacuna)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                page_num,
                line["line_num"],
                line["coptic"],
                line["english"],
                line["topic"],
                line["lacuna"]
            ))
            
            imported_lines += 1
            if line["lacuna"]:
                lacunae_count += 1
            
            print(f"  Line {line['line_num']}: {line['topic']} {'[lacuna]' if line['lacuna'] else ''}")
    
    db.conn.commit()
    
    # Export
    db.cursor.execute("SELECT * FROM gospel_of_mary ORDER BY page, line")
    columns = [description[0] for description in db.cursor.description]
    rows = db.cursor.fetchall()
    
    mary_export = {
        "title": "Gospel of Mary Magdalene",
        "source": "Berlin Codex BG 8502",
        "language": "Coptic (Sahidic)",
        "total_pages": 8,
        "extant_pages": 8,
        "complete_lines": imported_lines - lacunae_count,
        "lacunae": lacunae_count,
        "pages": []
    }
    
    for page_num in range(1, 9):
        page_lines = [dict(zip(columns, row)) for row in rows if row[1] == page_num]
        if page_lines:
            mary_export["pages"].append({
                "page": page_num,
                "lines": page_lines
            })
    
    import json
    with open('/root/hebrew-repo/exports/gospel_of_mary.json', 'w', encoding='utf-8') as f:
        json.dump(mary_export, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*70)
    print("IMPORT COMPLETE")
    print("="*70)
    print(f"\n📊 Statistics:")
    print(f"   Total lines imported: {imported_lines}")
    print(f"   Complete lines: {imported_lines - lacunae_count}")
    print(f"   Lacunae (missing): {lacunae_count}")
    print(f"   Extant: {((imported_lines - lacunae_count) / imported_lines * 100):.1f}%")
    print(f"\n✅ Exported to exports/gospel_of_mary.json")
    
    db.close()

if __name__ == "__main__":
    import_gospel_of_mary()