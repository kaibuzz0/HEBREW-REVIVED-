#!/usr/bin/env python3
"""
PHASE 6: DEUTEROCANONICAL BOOKS
Tobit, Judith, Wisdom, Sirach, Baruch, 1-2 Maccabees
Plus: Additions to Esther/Daniel, Prayer of Manasseh
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

# TOBIT
TOBIT = [
    (1, "This book tells the story of Tobit, son of Tobiel... I Tobit have walked all the days of my life in the ways of truth and righteousness.", "Tobit's Righteousness"),
    (2, "Now when I was come home again... I said to my son, Go and bring whatsoever poor man you find.", "Almsgiving"),
    (3, "Then I being grieved did weep, and in my sorrow prayed... And Tobias took his journey, and the dog went with him.", "Tobias' Journey"),
    (5, "So they went forth both, and the young man's dog with them.", "The Journey Begins"),
    (6, "And as they went on their journey, they came in the evening to the river Tigris... And the angel said to him, Take the fish, and the heart and liver and gall.", "The Fish"),
    (7, "Raguel's daughter Sara... And Raguel gave him his daughter Sara.", "Marriage"),
    (8, "And he took the heart and liver of the fish, and put them upon the coals... And the angel said, Take hold of her, and fear not.", "The Demon Defeated"),
    (11, "And Tobias went in, and his eyes were opened... And he saw his son Tobias.", "Healing"),
    (12, "And Raguel and Edna his wife came forth and blessed Tobias... I am Raphael, one of the seven holy angels.", "Raphael Revealed"),
    (14, "And Tobit wrote a prayer of rejoicing... Wherefore I say unto you, keep the ways of the Lord.", "Conclusion"),
]

# JUDITH
JUDITH = [
    (1, "In the twelfth year of the reign of Nebuchadnezzar, who reigned in Nineveh... Arphaxad fortified Ecbatana.", "Setting"),
    (4, "Now the children of Israel that dwelt in Judea heard... And they cried unto the Lord with all their might.", "Israel's Fear"),
    (8, "Now at that time Judith heard thereof... She was of a goodly countenance, and very beautiful to behold.", "Judith Introduced"),
    (9, "And Judith fell upon her face, and put ashes upon her head... O Lord God of my father Simeon.", "Judith's Prayer"),
    (10, "And when she had done this, she went out... And they brought her to the tent of Holofernes.", "To the Camp"),
    (13, "Now when they were gone out, and all were asleep... Then she took his head out of the bag.", "The Deed"),
    (14, "Then Judith said to them... Take this head and hang it upon the highest place.", "Victory"),
    (16, "Then Judith began to sing this thanksgiving... Begin to my God with timbrels.", "Song of Victory"),
]

# WISDOM OF SOLOMON
WISDOM = [
    (1, "Love righteousness, you that be judges of the earth... For the Spirit of the Lord fills the world.", "Exhortation"),
    (2, "For the ungodly said... Let us lie in wait for the righteous; because he is not for our turn.", "Ungodly Counsel"),
    (3, "But the souls of the righteous are in the hand of God... In the sight of the unwise they seemed to die.", "Hope of the Righteous"),
    (4, "Better is it to have no children, and to have virtue... He being made perfect in a short time, fulfilled a long time.", "Virtue"),
    (6, "Hear therefore, O you kings... Wisdom is glorious, and never fades away.", "Call to Kings"),
    (7, "I myself also am a mortal man... And I preferred her before kingdoms and thrones.", "Solomon's Wisdom"),
    (9, "O God of my fathers... Give me wisdom, that sits by your throne.", "Prayer for Wisdom"),
    (11, "She made all things... By what things a man sins, by the same also he is punished.", "Wisdom's Works"),
]

# SIRACH (ECCLESIASTICUS)
SIRACH = [
    (1, "All wisdom comes from the Lord... To whom has the root of wisdom been revealed?", "Praise of Wisdom"),
    (2, "My son, if you come to serve the Lord... Wait on him with patience.", "Serving God"),
    (3, "Honor your father and mother... For the blessing of the father establishes the houses of children.", "Honor Parents"),
    (6, "Become not an enemy instead of a friend... A faithful friend is a strong defense.", "Friendship"),
    (24, "Wisdom shall praise herself... I came out of the mouth of the most High.", "Wisdom's Praise"),
    (38, "Honor a physician with the honor due unto him... For the Lord has created him.", "Physicians"),
    (51, "I will thank you, O Lord and King... I sought wisdom openly in my prayer.", "Thanksgiving"),
]

# BARUCH
BARUCH = [
    (1, "These are the words of the book, which Baruch the son of Neriah... wrote in Babylon.", "Introduction"),
    (3, "O Lord Almighty, God of Israel... Hear, O Israel, the commandments of life.", "Prayer"),
    (4, "This is the book of the commandments of God... She has received of the Lord double for all her sins.", "Jerusalem's Comfort"),
    (5, "Put off, O Jerusalem, the garment of mourning... For God will show your brightness to every nation.", "Joy"),
    (6, "A copy of the letter that Jeremiah sent... Now you shall see in Babylon gods of silver, gold, wood.", "Letter of Jeremiah"),
]

# 1 MACCABEES
MACCABEES_1 = [
    (1, "Now it came to pass, after Alexander the Macedonian had smitten Darius... And he was lifted up in pride.", "Alexander"),
    (2, "In those days arose Mattathias... Whoever is zealous of the law, and maintains the covenant, let him follow me.", "Mattathias"),
    (3, "Then his son Judas, called Maccabeus... He fought the battles of the Lord with the men that were joyful.", "Judas Maccabeus"),
    (4, "Then took Gorgias five thousand footmen... They rent the stones, and cast them away.", "The Battle"),
    (6, "Now when Judas and his brethren saw that evils were multiplied... They said, Behold, our enemies are discomfited.", "Victory"),
    (7, "When Demetrius heard that Nicanor and his host were slain... They cried unto heaven, saying, What shall we do with these?", "Demetrius"),
]

# 2 MACCABEES
MACCABEES_2 = [
    (1, "The brethren the Jews that are in Egypt... For he has made us glad this day.", "Letter to Egypt"),
    (3, "Now when Onias the high priest was dead... Heliodorus came to execute the king's purpose.", "Heliodorus"),
    (7, "It came to pass also, that seven brethren... We are ready to die rather than transgress the laws.", "Seven Brothers"),
    (10, "Now Maccabeus and his company... They ordained to keep this day holy.", "Purification"),
    (15, "But when Judas and his company had prayed... They fought with their hands, but prayed unto God in their hearts.", "Courage"),
]

# ADDITIONS TO ESTHER
ADDITIONS_ESTHER = [
    (10, "And Mordecai prayed unto the Lord... O Lord, Lord, King Almighty.", "Mordecai's Prayer"),
    (13, "Queen Esther also, being in fear of death... O my Lord, you only are our King.", "Esther's Prayer"),
    (16, "The great King Artaxerxes... I determined to do this for the safety of our kingdom.", "King's Letter"),
]

# ADDITIONS TO DANIEL (Susanna, Bel and Dragon)
ADDITIONS_DANIEL = [
    (13, "There dwelt a man in Babylon, called Joacim... Now Susanna was exceeding delicate.", "Susanna"),
    (13, "And the two elders saw her... She said, I am straitened on every side.", "False Accusation"),
    (13, "Then Daniel cried with a loud voice... I am clear from the blood of this woman.", "Daniel's Justice"),
    (14, "And Daniel made a trial of the priests of Bel... You are great, O Bel.", "Bel and the Dragon"),
    (14, "Then said Daniel unto the king... I will show you the deceit.", "The Dragon"),
    (14, "Then said the king to Daniel... Throw him into the den of lions.", "Daniel in Den"),
]

# PRAYER OF MANASSEH
PRAYER_MANASSEH = [
    (1, "O Lord, Almighty God of our fathers... I have sinned above the number of the sands of the sea.", "Confession"),
    (1, "For I have set up abominations... And now I bend the knee of my heart, beseeching you.", "Repentance"),
    (1, "O Lord, according to your great goodness... Now therefore I bow the knee.", "Petition"),
]

def import_phase6():
    """Import Phase 6: Deuterocanonical Books"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("PHASE 6: DEUTEROCANONICAL BOOKS (APOCRYPHA)")
    print("="*70)
    
    # Create tables
    imports = [
        ("book_of_tobit", TOBIT, "Tobit"),
        ("book_of_judith", JUDITH, "Judith"),
        ("book_of_wisdom", WISDOM, "Wisdom of Solomon"),
        ("book_of_sirach", SIRACH, "Sirach"),
        ("book_of_baruch", BARUCH, "Baruch"),
        ("book_of_first_maccabees", MACCABEES_1, "1 Maccabees"),
        ("book_of_second_maccabees", MACCABEES_2, "2 Maccabees"),
        ("additions_to_esther", ADDITIONS_ESTHER, "Additions to Esther"),
        ("additions_to_daniel", ADDITIONS_DANIEL, "Additions to Daniel"),
        ("prayer_of_manasseh", PRAYER_MANASSEH, "Prayer of Manasseh"),
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
        "phase": "Phase 6",
        "total_entries": total,
        "books": [
            {"book": "Tobit", "count": len(TOBIT)},
            {"book": "Judith", "count": len(JUDITH)},
            {"book": "Wisdom of Solomon", "count": len(WISDOM)},
            {"book": "Sirach", "count": len(SIRACH)},
            {"book": "Baruch", "count": len(BARUCH)},
            {"book": "1 Maccabees", "count": len(MACCABEES_1)},
            {"book": "2 Maccabees", "count": len(MACCABEES_2)},
            {"book": "Additions to Esther", "count": len(ADDITIONS_ESTHER)},
            {"book": "Additions to Daniel", "count": len(ADDITIONS_DANIEL)},
            {"book": "Prayer of Manasseh", "count": len(PRAYER_MANASSEH)},
        ]
    }
    
    with open('/root/hebrew-repo/exports/phase6_deuterocanonical_export.json', 'w') as f:
        json.dump(export, f, indent=2)
    
    print("\n" + "="*70)
    print("PHASE 6 COMPLETE - DEUTEROCANONICAL BOOKS!")
    print("="*70)
    print(f"\n📊 IMPORTED: {total} entries from 10 books")
    print(f"\n📚 BOOKS:")
    print(f"   Histories: Tobit, Judith, 1-2 Maccabees")
    print(f"   Wisdom: Wisdom of Solomon, Sirach, Baruch")
    print(f"   Additions: Esther, Daniel (Susanna, Bel)")
    print(f"   Prayers: Prayer of Manasseh")
    print(f"\n📁 Exported to exports/phase6_deuterocanonical_export.json")
    
    db.close()

if __name__ == "__main__":
    import_phase6()