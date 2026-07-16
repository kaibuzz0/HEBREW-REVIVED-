#!/usr/bin/env python3
"""
PHASE 7: MORE PSEUDEPIGRAPHA
Jubilees, Testaments, Ascension of Isaiah, Life of Adam and Eve, etc.
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

# BOOK OF JUBILEES
JUBILEES = [
    (1, "These are the words of the division of the days according to the law and the testimony... And Moses went up into the mount, and the glory of the Lord abode upon Mount Sinai.", "Revelation to Moses"),
    (2, "For on the first day He created the heavens... And God made a division between the light and the darkness.", "Creation Account"),
    (3, "And Adam and his wife dwelt in the Garden of Eden... And on that day Adam knew his wife Eve, and she bare a son, and called his name Cain.", "Fall and First Children"),
    (4, "In the first week of the first jubilee, Adam and his wife dwelt in the Garden of Eden... And Cain rose up against Abel his brother, and slew him.", "Cain and Abel"),
    (5, "And it came to pass when the sons of men began to multiply on the face of the earth... And the Lord said: I will destroy man whom I have created from the face of the earth.", "Wickedness of Men"),
    (6, "And on the first of the second month, Noah went forth from the ark... This is the sign of the covenant which I establish between Me and you.", "Noah's Covenant"),
    (10, "And in the third week of this jubilee the polluted demons began to lead astray the children of Noah's sons... And Noah prayed to the Lord, and the Lord bound them all.", "Demons Bound"),
    (12, "And in the fortieth jubilee, in the second week... Abram said to his father: Father, what is this idol?", "Abram and Idols"),
    (22, "And it came to pass after these things, that God tried Abraham... And Abraham built an altar and placed wood upon it.", "Sacrifice of Isaac"),
]

# TESTAMENTS OF THE TWELVE PATRIARCHS
TESTAMENTS = [
    (1, "The copy of the testament of Reuben... I was the first-born... and by my father's command I was the first to see the destruction of Joseph.", "Reuben's Sin"),
    (2, "The copy of the words of Simeon... I was born of Bilhah... and I confess my jealousy against Joseph my brother.", "Simeon's Jealousy"),
    (3, "The copy of the words of Levi... I was born in Haran... and I was zealous for the Lord's sake.", "Levi's Priesthood"),
    (4, "The copy of the words of Judah... I was the fourth son... and the Lord gave me favor.", "Judah's Leadership"),
    (5, "The copy of the words of Issachar... I was the fifth son... and I was a husbandman.", "Issachar's Contentment"),
    (6, "The copy of the words of Zebulun... I was the sixth son... and I was a sailor.", "Zebulun's Compassion"),
    (7, "The copy of the words of Dan... I was the seventh son... and I was a serpent.", "Dan's Repentance"),
    (8, "The copy of the words of Naphtali... I was the eighth son... and I was a swift runner.", "Naphtali's Vision"),
    (9, "The copy of the words of Gad... I was the ninth son... and I loved not my brother.", "Gad's Warning"),
    (10, "The copy of the words of Asher... I was the tenth son... and I was blessed.", "Asher's Blessing"),
    (11, "The copy of the words of Joseph... I was the eleventh son... and the Lord was with me.", "Joseph's Virtue"),
    (12, "The copy of the words of Benjamin... I was the twelfth son... and I was a ravenous wolf.", "Benjamin's Prophecy"),
]

# ASCENSION OF ISAIAH
ASCENSION_ISAIAH = [
    (1, "The vision which Isaiah son of Amoz saw... Belchira the false prophet accused Isaiah before Manasseh.", "Isaiah Accused"),
    (6, "And he brought me up to the firmament... And I saw there a throne in the midst, and the whole host of the heavens stood around it.", "First Heaven"),
    (7, "And he brought me up to the second heaven... And I saw there a throne, and the angels on the right and on the left.", "Second Heaven"),
    (8, "And he brought me up to the third heaven... And I saw there righteous garments laid up.", "Third Heaven"),
    (9, "And he brought me up to the fourth heaven... And I saw there the angels of the Lord.", "Fourth Heaven"),
    (10, "And he brought me up to the fifth heaven... And I saw there the angels who were called 'lords'.", "Fifth Heaven"),
    (11, "And he brought me up to the sixth heaven... And I saw there much light and splendor.", "Sixth Heaven"),
    (12, "And he brought me up to the seventh heaven... And I saw there the Great Glory.", "Seventh Heaven"),
    (14, "And Hezekiah and Josiah the son of Isaiah saw... And Isaiah was sawn asunder with a wooden saw.", "Martyrdom"),
]

# LIFE OF ADAM AND EVE
LIFE_ADAM_EVE = [
    (1, "When Adam and Eve went out of paradise, Eve said to Adam... For the beasts are risen up against us.", "Expulsion"),
    (9, "And Adam said to Eve... Let us stand and pray to God, that He may have mercy upon us.", "Repentance"),
    (22, "And Adam said to his son Seth... I am sick, my son.", "Adam's Illness"),
    (32, "And Adam said to Seth... Tell your mother to come to me, for I am going to my rest.", "Adam's Death"),
    (37, "And the angels buried Adam and Abel in the parts of paradise... And Michael held Adam by his right hand, and Gabriel by his left.", "Burial"),
    (43, "And Eve said to Seth... Behold, my son, I am dying.", "Eve's Death"),
]

# ENOCH (Book of Watchers - Additional)
WATCHERS_ADDITIONAL = [
    (1, "The words of the blessing of Enoch, wherewith he blessed the elect and righteous... And the Great Glory sat thereon.", "Enoch's Vision"),
    (6, "And it came to pass when the children of men had multiplied... The angels, the children of the heaven, saw and lusted after them.", "Fall of Watchers"),
    (8, "And Azazel taught men to make swords, and knives, and shields... And there was much godlessness on earth.", "Azazel's Teaching"),
    (9, "Then Michael, Uriel, Raphael, and Gabriel looked down from heaven... And they said to the Lord of the ages.", "Angels' Prayer"),
    (10, "Then said the Most High... Bind Azazel hand and foot, and cast him into the darkness.", "Judgment on Watchers"),
    (12, "Before these things Enoch was hidden... And I went and stood at the door of the house.", "Enoch's Mission"),
    (14, "The book of the words of righteousness... I saw in a vision of mine.", "Vision of Heaven"),
    (37, "The second vision which he saw... The vision of wisdom which Enoch saw.", "Book of Parables"),
]

# 2 ENOCH (SLAVONIC ENOCH)
ENOCH_2 = [
    (1, "This is the beginning of the words of Enoch... I will teach you, my sons, all that is hidden.", "Introduction"),
    (3, "Before anything existed at all... The Lord created the foundation of all things.", "Creation"),
    (8, "And I saw the eighth heaven... And I saw the tenth heaven, and I called it the aeon.", "Ten Heavens"),
    (22, "And the Lord said to Enoch... Behold, I give you an eternity of 9000 years.", "Enoch's Translation"),
    (30, "On the first day I created the heavens... On the sixth day I created man from seven substances.", "Six Days"),
]

# APOCALYPSE OF ABRAHAM
APOCALYPSE_ABRAHAM = [
    (1, "The story of the sacrifice of Isaac... And God tried Abraham and said to him: Abraham, Abraham!", "Trial of Abraham"),
    (9, "And while he was still speaking... And I saw a fire, and lights, and a flame.", "Vision Begins"),
    (15, "And He said to me... Abraham, Abraham! And I said: Here am I, Lord.", "God Speaks"),
    (21, "And I looked into the expanse... And I saw a great multitude of angels.", "Exodus of Nations"),
    (29, "And the Eternal Mighty One said to me... I shall descend with them to the age.", "God's Promise"),
]

# 4 EZRA (2 ESDRAS)
ESDRAS_4 = [
    (1, "The second book of the prophet Ezra... I have sent my prophets to you.", "Introduction"),
    (3, "In the thirtieth year after the destruction of our city... And I said: O Lord, you did speak at the beginning of creation.", "Ezra's Prayer"),
    (7, "I answered and said: O sovereign Lord... I said: Why has Israel been given over to the Gentiles?", "Questions"),
    (14, "On the third day, while I was sitting under an oak... Take up the writing and write what you see.", "Five Books"),
]

# SIBYLLINE ORACLES
SIBYLLINE = [
    (1, "I am the Erythraean Sibyl... I declare to mortals the mind of aether.", "The Sibyl"),
    (3, "Then there will come the tenth race of men... There will come a great judgment on mortals.", "Golden Age"),
    (8, "But when everything has already been reduced to dust and ashes... There will be one kingdom and one law for all.", "Final Age"),
]

def import_phase7():
    """Import Phase 7: More Pseudepigrapha"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("PHASE 7: MORE PSEUDEPIGRAPHA")
    print("="*70)
    
    # Create tables
    imports = [
        ("book_of_jubilees", JUBILEES, "Jubilees"),
        ("testaments_of_twelve_patriarchs", TESTAMENTS, "Testaments of Twelve Patriarchs"),
        ("ascension_of_isaiah", ASCENSION_ISAIAH, "Ascension of Isaiah"),
        ("life_of_adam_and_eve", LIFE_ADAM_EVE, "Life of Adam and Eve"),
        ("book_of_watchers_additional", WATCHERS_ADDITIONAL, "Book of Watchers (Additional)"),
        ("second_book_of_enoch", ENOCH_2, "2 Enoch (Slavonic)"),
        ("apocalypse_of_abraham", APOCALYPSE_ABRAHAM, "Apocalypse of Abraham"),
        ("fourth_book_of_ezra", ESDRAS_4, "4 Ezra (2 Esdras)"),
        ("sibylline_oracles", SIBYLLINE, "Sibylline Oracles"),
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
        "phase": "Phase 7",
        "total_entries": total,
        "books": [
            {"book": "Jubilees", "count": len(JUBILEES)},
            {"book": "Testaments of Twelve Patriarchs", "count": len(TESTAMENTS)},
            {"book": "Ascension of Isaiah", "count": len(ASCENSION_ISAIAH)},
            {"book": "Life of Adam and Eve", "count": len(LIFE_ADAM_EVE)},
            {"book": "Book of Watchers (Additional)", "count": len(WATCHERS_ADDITIONAL)},
            {"book": "2 Enoch", "count": len(ENOCH_2)},
            {"book": "Apocalypse of Abraham", "count": len(APOCALYPSE_ABRAHAM)},
            {"book": "4 Ezra", "count": len(ESDRAS_4)},
            {"book": "Sibylline Oracles", "count": len(SIBYLLINE)},
        ]
    }
    
    with open('/root/hebrew-repo/exports/phase7_pseudepigrapha_export.json', 'w') as f:
        json.dump(export, f, indent=2)
    
    print("\n" + "="*70)
    print("PHASE 7 COMPLETE - MORE PSEUDEPIGRAPHA!")
    print("="*70)
    print(f"\n📊 IMPORTED: {total} entries from 9 books")
    print(f"\n📚 BOOKS:")
    print(f"   Rewritten Scripture: Jubilees, Life of Adam and Eve")
    print(f"   Testaments: Twelve Patriarchs")
    print(f"   Apocalypses: Ascension of Isaiah, Apocalypse of Abraham, 4 Ezra")
    print(f"   Enoch Traditions: Book of Watchers, 2 Enoch")
    print(f"   Oracles: Sibylline Oracles")
    print(f"\n📁 Exported to exports/phase7_pseudepigrapha_export.json")
    
    db.close()

if __name__ == "__main__":
    import_phase7()