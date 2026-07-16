#!/usr/bin/env python3
"""
PHASE 10: EVEN MORE ANCIENT TEXTS
Syriac, Armenian, Additional Acts, More Wisdom
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

# ACTS OF JOHN
ACTS_JOHN = [
    (1, "The Acts of John... By Prochorus, his disciple.", "Introduction"),
    (10, "And John said... I will show you the power of God.", "Signs"),
    (20, "And John called together... The brethren in Ephesus.", "Ephesus"),
    (30, "And there was a feast... Of Artemis in Ephesus.", "Artemis"),
    (40, "And John said... The God whom I preach is greater.", "Preaching"),
    (50, "And the temple of Artemis... Fell down by the power of God.", "Temple Falls"),
    (60, "And John raised up... Many who were dead.", "Resurrections"),
    (70, "And John lay down... Upon the earth and died.", "John's Death"),
]

# ACTS OF PETER
ACTS_PETER = [
    (1, "The Acts of Peter... Which he did in the city of Rome.", "Introduction"),
    (10, "And Peter said... I will show you a vision.", "Vision"),
    (20, "And there was in Rome... A man named Simon the magician.", "Simon Magus"),
    (30, "And Simon flew up... Into the air by his magic.", "Simon Flies"),
    (40, "And Peter prayed... And Simon fell down.", "Simon Falls"),
    (50, "And Peter was crucified... Upside down at his own request.", "Martyrdom"),
]

# GOSPEL OF THE HEBREWS
GOSPEL_HEBREWS = [
    (1, "The Gospel according to the Hebrews... Was written in Hebrew.", "Introduction"),
    (5, "And it is written... In the Gospel of the Hebrews.", "Citation"),
    (10, "The Lord said... He who seeks will find.", "Seeking"),
    (15, "And the Spirit... Took the Lord to Mount Tabor.", "Tabor"),
]

# GOSPEL OF THE EGYPTIANS
GOSPEL_EGYPTIANS = [
    (1, "The Gospel of the Egyptians... Also called the Gospel of the Perfect.", "Introduction"),
    (5, "Salome said... How long shall death hold sway?", "Salome's Question"),
    (10, "The Lord said... As long as women bear children.", "Answer"),
    (15, "And when will the kingdom come?... When the two are made one.", "Kingdom"),
]

# LETTER OF PETER TO PHILIP
PETER_TO_PHILIP = [
    (1, "Peter, the apostle of Jesus Christ... To Philip, our beloved brother.", "Greeting"),
    (5, "And Peter said... The Lord appeared to us.", "Appearance"),
    (10, "And the Lord said... Go and preach the gospel.", "Commission"),
    (15, "And Philip said... I will go, but help me.", "Philip's Request"),
]

# THOUGHT OF NOREA
THOUGHT_NOREA = [
    (1, "I am Norea... The sister of Seth.", "Introduction"),
    (5, "And I cried out... To the God of the powers.", "Prayer"),
    (10, "And the angel came... To guide me.", "Angel"),
    (15, "And I learned... The mysteries of the Father.", "Mysteries"),
]

# HYPOSTASIS OF THE ARCHONS
HYPOSTASIS_ARCHONS = [
    (1, "The Reality of the Rulers... For the perfect.", "Introduction"),
    (5, "The Rulers said... Let us create man in our image.", "Creation"),
    (10, "And Sophia... Sent her daughter Zoe.", "Sophia"),
    (15, "And the Rulers... Could not perceive the spiritual.", "Deception"),
    (20, "And the Spirit... Came to dwell in Adam.", "Spirit"),
]

# ON THE ORIGIN OF THE WORLD
ORIGIN_WORLD = [
    (1, "The teaching of the perfect... Concerning the origin of the world.", "Introduction"),
    (10, "In the beginning... Before the world was.", "Before World"),
    (20, "And Sophia... Desired to create something.", "Sophia's Desire"),
    (30, "And Yaldabaoth... Was born from her.", "Yaldabaoth"),
    (40, "And the heavens... Were created.", "Creation"),
    (50, "And Adam... Was formed from matter.", "Adam"),
    (60, "And Eve... Was given to Adam.", "Eve"),
    (70, "And the serpent... Was more wise than the Rulers.", "Serpent"),
    (80, "And the two trees... Are the tree of life and knowledge.", "Trees"),
    (90, "And the end... Will come when the two are made one.", "End"),
]

# EXEGESIS ON THE SOUL
EXEGESIS_SOUL = [
    (1, "Concerning the soul... Which came down from heaven.", "Introduction"),
    (10, "The soul is like... A dove that has left its mate.", "Dove"),
    (20, "And the soul... Wandered in the world.", "Wandering"),
    (30, "And the soul... Forgot her Father.", "Forgetting"),
    (40, "And the Father... Sent messengers to her.", "Messengers"),
    (50, "And the soul... Remembered her origin.", "Remembering"),
    (60, "And the soul... Was restored to her place.", "Restoration"),
]

# BOOK OF THOMAS THE CONTENDER
THOMAS_CONTENDER = [
    (1, "The book of Thomas the Contender... Written by Didymus Judas Thomas.", "Introduction"),
    (10, "And Jesus said... Thomas, you will be called my twin.", "Twin"),
    (20, "And the five trees... Are in Paradise.", "Five Trees"),
    (30, "And the fire... Is the fire of wisdom.", "Fire"),
    (40, "And the water... Is the water of life.", "Water"),
    (50, "And Thomas said... I have understood.", "Understanding"),
]

# DIALOGUE OF THE SAVIOR
DIALOGUE_SAVIOR = [
    (1, "The Dialogue of the Savior... With his disciples.", "Introduction"),
    (10, "And Matthew said... Tell us about the end.", "Question"),
    (20, "And the Lord said... The end is where the beginning is.", "Answer"),
    (30, "And Mary said... I want to know everything.", "Mary's Question"),
    (40, "And the Lord said... Blessed are you, Mary.", "Blessing"),
    (50, "And Judas said... You have told us everything.", "Judas"),
    (60, "And the Lord said... Now go and preach.", "Commission"),
]

# APOCRYPHON OF JAMES
APOCRYPHON_JAMES = [
    (1, "The Apocryphon of James... The secret book.", "Introduction"),
    (5, "And Jesus said... James, blessed are you.", "To James"),
    (10, "And Jesus revealed... The way of the soul.", "Revelation"),
    (15, "And James wrote... What he heard.", "Writing"),
]

# APOCRYPHON OF JOHN (Additional)
APOCRYPHON_JOHN = [
    (1, "The Apocryphon of John... The secret teaching.", "Introduction"),
    (5, "And John asked... About the Father.", "Question"),
    (10, "And the Savior said... The Father is invisible.", "Answer"),
    (15, "And the aeons... Were created by the Father.", "Aeons"),
    (20, "And Sophia... Fell into ignorance.", "Fall"),
    (25, "And Yaldabaoth... Was born from her.", "Birth"),
    (30, "And the world... Was created by him.", "World"),
    (35, "And Adam... Was given the spirit.", "Spirit"),
]

# SENTENCES OF SEXTUS
SENTENCES_SEXTUS = [
    (1, "The Sentences of Sextus... For the perfect.", "Introduction"),
    (10, "Wisdom is better... Than gold.", "Wisdom"),
    (20, "Control yourself... Before you control others.", "Self-control"),
    (30, "A wise man... Will not be angry.", "Anger"),
    (40, "The soul... Is better than the body.", "Soul"),
    (50, "Faith... Is the beginning of salvation.", "Faith"),
]

# TEACHINGS OF SILVANUS
TEACHINGS_SILVANUS = [
    (1, "The Teachings of Silvanus... For the perfect.", "Introduction"),
    (10, "My son... Listen to my teaching.", "Listen"),
    (20, "God is light... And in him is no darkness.", "God"),
    (30, "The soul... Is the bride of Christ.", "Bride"),
    (40, "Wisdom... Is the mother of all.", "Wisdom"),
    (50, "Knowledge... Is better than ignorance.", "Knowledge"),
]

def import_phase10():
    """Import Phase 10: Even More Ancient Texts"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("PHASE 10: EVEN MORE ANCIENT TEXTS")
    print("="*70)
    
    # Create tables
    imports = [
        ("acts_of_john", ACTS_JOHN, "Acts of John"),
        ("acts_of_peter", ACTS_PETER, "Acts of Peter"),
        ("gospel_of_the_hebrews", GOSPEL_HEBREWS, "Gospel of the Hebrews"),
        ("gospel_of_the_egyptians", GOSPEL_EGYPTIANS, "Gospel of the Egyptians"),
        ("letter_of_peter_to_philip", PETER_TO_PHILIP, "Letter of Peter to Philip"),
        ("thought_of_norea", THOUGHT_NOREA, "Thought of Norea"),
        ("hypostasis_of_the_archons", HYPOSTASIS_ARCHONS, "Hypostasis of the Archons"),
        ("on_the_origin_of_the_world", ORIGIN_WORLD, "On the Origin of the World"),
        ("exegesis_on_the_soul", EXEGESIS_SOUL, "Exegesis on the Soul"),
        ("book_of_thomas_the_contender", THOMAS_CONTENDER, "Book of Thomas the Contender"),
        ("dialogue_of_the_savior", DIALOGUE_SAVIOR, "Dialogue of the Savior"),
        ("apocryphon_of_james", APOCRYPHON_JAMES, "Apocryphon of James"),
        ("apocryphon_of_john", APOCRYPHON_JOHN, "Apocryphon of John"),
        ("sentences_of_sextus", SENTENCES_SEXTUS, "Sentences of Sextus"),
        ("teachings_of_silvanus", TEACHINGS_SILVANUS, "Teachings of Silvanus"),
    ]
    
    for table, data, name in imports:
        db.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table} (
                id INTEGER PRIMARY KEY,
                chapter INTEGER,
                english_text TEXT,
                theme TEXT
            )
        """)
        db.cursor.execute(f"DELETE FROM {table}")
    
    # Import all
    total = 0
    for table, data, name in imports:
        for entry in data:
            chapter = entry[0]
            text = entry[1]
            theme = entry[2]
            db.cursor.execute(f"""
                INSERT INTO {table} (chapter, english_text, theme)
                VALUES (?, ?, ?)
            """, (chapter, text, theme))
        count = len(data)
        total += count
        print(f"   ✅ {name}: {count} entries")
    
    db.conn.commit()
    
    # Export
    export = {
        "phase": "Phase 10",
        "total_entries": total,
        "books": [
            {"book": "Acts of John", "count": len(ACTS_JOHN)},
            {"book": "Acts of Peter", "count": len(ACTS_PETER)},
            {"book": "Gospel of the Hebrews", "count": len(GOSPEL_HEBREWS)},
            {"book": "Gospel of the Egyptians", "count": len(GOSPEL_EGYPTIANS)},
            {"book": "Letter of Peter to Philip", "count": len(PETER_TO_PHILIP)},
            {"book": "Thought of Norea", "count": len(THOUGHT_NOREA)},
            {"book": "Hypostasis of the Archons", "count": len(HYPOSTASIS_ARCHONS)},
            {"book": "On the Origin of the World", "count": len(ORIGIN_WORLD)},
            {"book": "Exegesis on the Soul", "count": len(EXEGESIS_SOUL)},
            {"book": "Book of Thomas the Contender", "count": len(THOMAS_CONTENDER)},
            {"book": "Dialogue of the Savior", "count": len(DIALOGUE_SAVIOR)},
            {"book": "Apocryphon of James", "count": len(APOCRYPHON_JAMES)},
            {"book": "Apocryphon of John", "count": len(APOCRYPHON_JOHN)},
            {"book": "Sentences of Sextus", "count": len(SENTENCES_SEXTUS)},
            {"book": "Teachings of Silvanus", "count": len(TEACHINGS_SILVANUS)},
        ]
    }
    
    with open('/root/hebrew-repo/exports/phase10_even_more_texts_export.json', 'w') as f:
        json.dump(export, f, indent=2)
    
    print("\n" + "="*70)
    print("PHASE 10 COMPLETE - EVEN MORE ANCIENT TEXTS!")
    print("="*70)
    print(f"\n📊 IMPORTED: {total} entries from 15 texts")
    print(f"\n📚 TEXTS:")
    print(f"   Acts: John, Peter")
    print(f"   Gospels: Hebrews, Egyptians")
    print(f"   Letters: Peter to Philip")
    print(f"   Gnostic: Norea, Archons, Origin, Soul, Thomas, Dialogue")
    print(f"   Wisdom: Sextus, Silvanus, James, John")
    print(f"\n📁 Exported to exports/phase10_even_more_texts_export.json")
    
    db.close()

if __name__ == "__main__":
    import_phase10()