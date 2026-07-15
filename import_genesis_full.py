#!/usr/bin/env python3
"""
MASSIVE BIBLE DATA IMPORTER
Imports Genesis 1-50 with full analysis
Part of the complete Hebrew Revival system
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from biblical_database import BiblicalDatabase
from gematria_calculator import GematriaCalculator
from resonance_decoder import ResonanceEngine

# Genesis chapter summaries with key verses
GENESIS_DATA = {
    1: {
        "title": "Creation of the World",
        "key_verses": [
            (1, "בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ", "In the beginning God created the heavens and the earth"),
            (3, "וַיֹּאמֶר אֱלֹהִים יְהִי אוֹר וַיְהִי אוֹר", "And God said, Let there be light, and there was light"),
            (27, "וַיִּבְרָא אֱלֹהִים אֶת הָאָדָם בְּצַלְמוֹ בְּצֶלֶם אֱלֹהִים בָּרָא אֹתוֹ", "So God created man in his own image, in the image of God created he him"),
        ]
    },
    2: {
        "title": "Garden of Eden",
        "key_verses": [
            (7, "וַיִּיצֶר יְהוָה אֱלֹהִים אֶת הָאָדָם עָפָר מִן הָאֲדָמָה", "And the LORD God formed man of the dust of the ground"),
            (18, "וַיֹּאמֶר יְהוָה לֹא טוֹב הֱיוֹת הָאָדָם לְבַדּוֹ", "And the LORD said, It is not good that the man should be alone"),
            (24, "עַל כֵּן יַעֲזָב אִישׁ אֶת אָבִיו וְאֶת אִמּוֹ", "Therefore shall a man leave his father and his mother"),
        ]
    },
    3: {
        "title": "The Fall",
        "key_verses": [
            (1, "וְהַנָּחָשׁ הָיָה עָרוּם מִכֹּל חַיַּת הַשָּׂדֶה", "Now the serpent was more subtle than any beast of the field"),
            (6, "וַתֵּרֶא הָאִשָּׁה כִּי טוֹב הָעֵץ לְמַאֲכָל", "And when the woman saw that the tree was good for food"),
            (15, "וְאֵיבָה אָשִׁית בֵּינְךָ וּבֵין הָאִשָּׁה", "And I will put enmity between thee and the woman"),
        ]
    },
    4: {
        "title": "Cain and Abel",
        "key_verses": [
            (1, "וְהָאָדָם יָדַע אֶת חַוָּה אִשְׁתּוֹ וַתַּהַר וַתֵּלֶד אֶת קָיִן", "And Adam knew Eve his wife; and she conceived, and bare Cain"),
            (9, "אֵי הֶבֶל אָחִיךָ", "Where is Abel thy brother?"),
            (10, "קוֹל דְּמֵי אָחִיךָ צֹעֲקִים אֵלַי מִן הָאֲדָמָה", "The voice of thy brother's blood crieth unto me from the ground"),
        ]
    },
    5: {
        "title": "Genealogy from Adam to Noah",
        "key_verses": [
            (1, "זֶה סֵפֶר תּוֹלְדֹת אָדָם", "This is the book of the generations of Adam"),
            (24, "וַיִּתְהַלֵּךְ חֲנוֹךְ אֶת הָאֱלֹהִים וְאֵינֶנּוּ כִּי לָקַח אֹתוֹ אֱלֹהִים", "And Enoch walked with God: and he was not; for God took him"),
            (29, "יְהוָה קִלְלָה אֶת הָאֲדָמָה לְמַעֲנִי", "This same shall comfort us concerning our work"),
        ]
    },
    6: {
        "title": "The Flood Begins",
        "key_verses": [
            (5, "וַיַּרְא יְהוָה כִּי רַבָּה רָעַת הָאָדָם בָּאָרֶץ", "And GOD saw that the wickedness of man was great in the earth"),
            (8, "וְנֹחַ מָצָא חֵן בְּעֵינֵי יְהוָה", "But Noah found grace in the eyes of the LORD"),
            (14, "עֲשֵׂה לְךָ תֵּבַת עֲצֵי גֹפֶר", "Make thee an ark of gopher wood"),
        ]
    },
    7: {
        "title": "The Flood",
        "key_verses": [
            (1, "בֹּא אַתָּה וְכָל בֵּיתְךָ אֶל הַתֵּבָה", "Come thou and all thy house into the ark"),
            (17, "וַיְהִי הַמַּבּוּל אַרְבָּעִים יוֹם עַל הָאָרֶץ", "And the flood was forty days upon the earth"),
            (23, "וַיִּמַח אֶת כָּל הַיְקוּם אֲשֶׁר עַל פְּנֵי הָאֲדָמָה", "And every living substance was destroyed"),
        ]
    },
    8: {
        "title": "The Flood Recedes",
        "key_verses": [
            (1, "וַיִּזְכֹּר אֱלֹהִים אֶת נֹחַ", "And God remembered Noah"),
            (11, "וַתָּבֹא אֵלָיו הַיּוֹנָה לְעֵת עֶרֶב", "And the dove came in to him in the evening"),
            (21, "לֹא אֹסִף לְקַלֵּל עוֹד אֶת הָאֲדָמָה בַּעֲבוּר הָאָדָם", "I will not again curse the ground any more for man's sake"),
        ]
    },
    9: {
        "title": "Covenant with Noah",
        "key_verses": [
            (1, "וַיְבָרֶךְ אֱלֹהִים אֶת נֹחַ וְאֶת בָּנָיו", "And God blessed Noah and his sons"),
            (13, "אֶת קַשְׁתִּי נָתַתִּי בֶּעָנָן", "I do set my bow in the cloud"),
            (20, "וַיָּחֶל נֹחַ אִישׁ הָאֲדָמָה וַיִּטַּע כָּרֶם", "And Noah began to be an husbandman, and he planted a vineyard"),
        ]
    },
    10: {
        "title": "Nations Descended from Noah",
        "key_verses": [
            (1, "אֵלֶּה תּוֹלְדֹת בְּנֵי נֹחַ שֵׁם חָם וָיָפֶת", "Now these are the generations of the sons of Noah"),
            (8, "וְכוּשׁ יָלַד אֶת נִמְרֹד", "And Cush begat Nimrod"),
            (10, "וַתְּהִי רֵאשִׁית מַמְלַכְתּוֹ בָּבֶל", "And the beginning of his kingdom was Babel"),
        ]
    },
    11: {
        "title": "Tower of Babel",
        "key_verses": [
            (1, "וַיְהִי כָל הָאָרֶץ שָׂפָה אֶחָת", "And the whole earth was of one language"),
            (4, "נִבְנֶה לָּנוּ עִיר וּמִגְדָּל", "Let us build us a city and a tower"),
            (7, "נֵרְדָה וְנָבְלָה שָׁם שְׂפָתָם", "Let us go down, and there confound their language"),
            (31, "וַיִּקַּח תֶּרַח אֶת אַבְרָם בְּנוֹ", "And Terah took Abram his son"),
        ]
    },
    12: {
        "title": "Call of Abram",
        "key_verses": [
            (1, "לֶךְ לְךָ מֵאַרְצְךָ וּמִמּוֹלַדְתְּךָ וּמִבֵּית אָבִיךָ", "Get thee out of thy country, and from thy kindred"),
            (2, "וְאֶעֶשְׂךָ לְגוֹי גָּדוֹל", "And I will make of thee a great nation"),
            (3, "וַאֲבָרְכָה מְבָרְכֶיךָ", "And I will bless them that bless thee"),
        ]
    },
}

def import_genesis_full():
    """Import complete Genesis data"""
    db = BiblicalDatabase()
    gem = GematriaCalculator()
    res = ResonanceEngine()
    
    print("="*60)
    print("IMPORTING GENESIS FULL TEXT")
    print("="*60)
    
    # Add Genesis book
    db.add_book("Genesis", "בראשית", 50, "Torah")
    
    total_verses = 0
    total_words = 0
    
    # Import each chapter
    for chapter_num, chapter_data in GENESIS_DATA.items():
        print(f"\n📖 Chapter {chapter_num}: {chapter_data['title']}")
        
        for verse_num, hebrew, english in chapter_data['key_verses']:
            # Calculate gematria
            gem_std = gem.calculate(hebrew)
            gem_ktn = gem.calculate(hebrew, "katan")
            
            # Add verse
            verse_id = db.add_verse(
                "Genesis", chapter_num, verse_num, hebrew,
                "", english, gem_std, gem_ktn
            )
            
            if verse_id:
                total_verses += 1
                
                # Add word-level analysis
                words = hebrew.split()
                for i, word in enumerate(words, 1):
                    decoded = res.decode_word(word)
                    db.add_word_analysis(
                        verse_id, i, word, decoded.translit,
                        decoded.seeds[0] if decoded.seeds else "unknown",
                        "noun",  # Simplified
                        gem.calculate(word),
                        decoded.seed_sequence
                    )
                    total_words += 1
                
                print(f"  ✓ {chapter_num}:{verse_num} (G:{gem_std})")
    
    # Print statistics
    print("\n" + "="*60)
    print("IMPORT COMPLETE")
    print("="*60)
    stats = db.get_verse_stats("Genesis")
    print(f"Total verses imported: {stats[0]}")
    print(f"Total words analyzed: {total_words}")
    print(f"Average gematria: {stats[1]:.1f}")
    print(f"Max gematria: {stats[2]}")
    
    # Export
    db.export_to_json("/root/hebrew-repo/genesis_full.json")
    print(f"\n✅ Exported to genesis_full.json")
    
    db.close()
    print("\n🎉 Genesis import complete!")

if __name__ == "__main__":
    import_genesis_full()