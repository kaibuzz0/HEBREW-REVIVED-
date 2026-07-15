#!/usr/bin/env python3
"""
COMPLETE TORAH IMPORTER
Genesis 1-50, Exodus, Leviticus, Numbers, Deuteronomy
Full 5 books of Torah with comprehensive analysis
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from biblical_database import BiblicalDatabase
from gematria_calculator import GematriaCalculator
from resonance_decoder import ResonanceEngine

TORAH_COMPLETE = {
    # GENESIS 1 (already have full analysis)
    "Genesis": {
        "hebrew_name": "בראשית",
        "chapters": 50,
        "sections": {
            "1-11": "Primeval History",
            "12-36": "Patriarchal History", 
            "37-50": "Joseph Narrative"
        },
        "key_verses": {
            # Chapter 1 - Creation (already have)
            (1, 1): "בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ",
            (1, 27): "וַיִּבְרָא אֱלֹהִים אֶת הָאָדָם בְּצַלְמוֹ בְּצֶלֶם אֱלֹהִים בָּרָא אֹתוֹ",
            
            # Chapter 2 - Eden
            (2, 7): "וַיִּיצֶר יְהוָה אֱלֹהִים אֶת הָאָדָם עָפָר מִן הָאֲדָמָה וַיִּפַּח בְּאַפָּיו נִשְׁמַת חַיִּים",
            (2, 24): "עַל כֵּן יַעֲזָב אִישׁ אֶת אָבִיו וְאֶת אִמּוֹ וְדָבַק בְּאִשְׁתּוֹ",
            
            # Chapter 3 - The Fall
            (3, 15): "וְאֵיבָה אָשִׁית בֵּינְךָ וּבֵין הָאִשָּׁה",
            (3, 22): "וַיֹּאמֶר יְהוָה אֱלֹהִים הֵן הָאָדָם הָיָה כְּאַחַד מִמֶּנּוּ",
            
            # Chapter 4 - Cain and Abel
            (4, 10): "קוֹל דְּמֵי אָחִיךָ צֹעֲקִים אֵלַי מִן הָאֲדָמָה",
            
            # Chapter 5 - Genealogy
            (5, 24): "וַיִּתְהַלֵּךְ חֲנוֹךְ אֶת הָאֱלֹהִים וְאֵינֶנּוּ כִּי לָקַח אֹתוֹ אֱלֹהִים",
            
            # Chapter 6 - Noah
            (6, 8): "וְנֹחַ מָצָא חֵן בְּעֵינֵי יְהוָה",
            
            # Chapter 9 - Covenant
            (9, 13): "אֶת קַשְׁתִּי נָתַתִּי בֶּעָנָן",
            
            # Chapter 11 - Babel
            (11, 1): "וַיְהִי כָל הָאָרֶץ שָׂפָה אֶחָת",
            (11, 7): "נֵרְדָה וְנָבְלָה שָׁם שְׂפָתָם",
            
            # Chapter 12 - Abraham's Call
            (12, 1): "לֶךְ לְךָ מֵאַרְצְךָ וּמִמּוֹלַדְתְּךָ וּמִבֵּית אָבִיךָ",
            (12, 2): "וְאֶעֶשְׂךָ לְגוֹי גָּדוֹל",
            (12, 3): "וַאֲבָרְכָה מְבָרְכֶיךָ וּמְקַלֶּלְךָ אָאֹר",
            
            # Chapter 15 - Covenant with Abraham
            (15, 1): "אַל תִּירָא אַבְרָם אָנֹכִי מָגֵן לָךְ",
            (15, 6): "וְהֶאֱמִין בַּיהוָה וַיַּחְשְׁבֶהָ לּוֹ צְדָקָה",
            
            # Chapter 17 - Circumcision
            (17, 1): "אֲנִי אֵל שַׁדַּי הִתְהַלֵּךְ לְפָנַי",
            
            # Chapter 22 - Akedah
            (22, 1): "וַיְהִי אַחַר הַדְּבָרִים הָאֵלֶּה וְהָאֱלֹהִים נִסָּה אֶת אַבְרָהָם",
            (22, 8): "אֱלֹהִים יִרְאֶה לּוֹ הַשֶּׂה לְעֹלָה",
            (22, 14): "וַיִּקְרָא אַבְרָהָם שֵׁם הַמָּקוֹם הַהוּא יְהוָה יִרְאֶה",
            
            # Chapter 25 - Isaac
            (25, 23): "וַיֹּאמֶר יְהוָה לָהּ שְׁנֵי גֹיִים בְּבִטְנֵךְ",
            
            # Chapter 28 - Jacob's Ladder
            (28, 12): "וַיַּחֲלֹם וְהִנֵּה סֻלָּם מֻצָּב אַרְצָה",
            (28, 16): "וַיִּיקַץ יַעֲקֹב מִשְּׁנָתוֹ וַיֹּאמֶר אָכֵן יֵשׁ יְהוָה בַּמָּקוֹם הַזֶּה",
            
            # Chapter 32 - Wrestling
            (32, 28): "לֹא יַעֲקֹב יֵאָמֵר עוֹד שִׁמְךָ כִּי אִם יִשְׂרָאֵל",
            (32, 30): "פָּנִים אֶל פָּנִים רָאִיתִי",
            
            # Chapter 37 - Joseph
            (37, 3): "וְיִשְׂרָאֵל אָהַב אֶת יוֹסֵף מִכָּל בָּנָיו",
            
            # Chapter 45 - Reconciliation
            (45, 5): "וְעַתָּה אַל תֵּעָצְבוּ וְאַל יִחַר בְּעֵינֵיכֶם",
            (45, 8): "וְעַתָּה לֹא אַתֶּם שְׁלַחְתֶּם אֶתִי הֵנָּה כִּי הָאֱלֹהִים",
            
            # Chapter 50 - Final
            (50, 20): "וְאַתֶּם חֲשַׁבְתֶּם עָלַי רָעָה אֱלֹהִים חֲשָׁבָהּ לְטֹבָה",
        }
    },
    
    # EXODUS
    "Exodus": {
        "hebrew_name": "שמות",
        "chapters": 40,
        "sections": {
            "1-18": "Deliverance from Egypt",
            "19-40": "Covenant and Tabernacle"
        },
        "key_verses": {
            (3, 14): "אֶהְיֶה אֲשֶׁר אֶהְיֶה",
            (6, 6): "וְהוֹצֵאתִי אֶתְכֶם מִתַּחַת סִבְלֹת מִצְרָיִם",
            (12, 13): "וְהָיָה הַדָּם לָכֶם לְאֹת עַל הַבָּתִּים",
            (13, 21): "וַיהוָה הֹלֵךְ לִפְנֵיהֶם יוֹמָם בְּעַמּוּד עָנָן",
            (14, 14): "יְהוָה יִלָּחֵם לָכֶם וְאַתֶּם תַּחֲרִישֽׁוּן",
            (15, 2): "עָזִּי וְזִמְרָת יָהּ וַיְהִי לִי לִישׁוּעָה",
            (19, 5): "וְעַתָּה אִם שָׁמוֹעַ תִּשְׁמְעוּ בְּקֹלִי",
            (20, 1): "וַיְדַבֵּר אֱלֹהִים אֵת כָּל הַדְּבָרִים הָאֵלֶּה לֵאמֹר",
            (20, 2): "אָנֹכִי יְהוָה אֱלֹהֶיךָ אֲשֶׁר הוֹצֵאתִיךָ מֵאֶרֶץ מִצְרָיִם",
            (24, 12): "וַיֹּאמֶר יְהוָה אֶל מֹשֶׁה עֲלֵה אֵלַי הָהָרָה",
            (25, 8): "וְעָשׂוּ לִי מִקְדָּשׁ וְשָׁכַנְתִּי בְּתוֹכָם",
            (33, 11): "וְדִבֶּר יְהוָה אֶל מֹשֶׁה פָּנִים אֶל פָּנִים",
            (34, 6): "יְהוָה יְהוָה אֵל רַחוּם וְחַנּוּן",
        }
    },
    
    # LEVITICUS
    "Leviticus": {
        "hebrew_name": "ויקרא",
        "chapters": 27,
        "sections": {
            "1-16": "Sacrifice and Purity",
            "17-27": "Holiness Code"
        },
        "key_verses": {
            (1, 1): "וַיִּקְרָא אֶל מֹשֶׁה וַיְדַבֵּר יְהוָה אֵלָיו",
            (11, 44): "וְהִתְקַדִּשְׁתֶּם וִהְיִיתֶם קְדֹשִׁים כִּי קָדוֹשׁ אֲנִי",
            (16, 2): "וַיֹּאמֶר יְהוָה אֶל מֹשֶׁה דַּבֵּר אֶל אַהֲרֹן",
            (19, 2): "קְדֹשִׁים תִּהְיוּ כִּי קָדוֹשׁ אֲנִי יְהוָה אֱלֹהֵיכֶם",
            (19, 18): "וְאָהַבְתָּ לְרֵעֲךָ כָּמוֹךָ אֲנִי יְהוָה",
            (23, 1): "וַיְדַבֵּר יְהוָה אֶל מֹשֶׁה לֵּאמֹר",
            (26, 12): "וְהִתְהַלַּכְתִּי בְּתוֹכְכֶם וְהָיִיתִי לָכֶם לֵאלֹהִים",
        }
    },
    
    # NUMBERS
    "Numbers": {
        "hebrew_name": "במדבר",
        "chapters": 36,
        "sections": {
            "1-10": "Preparation at Sinai",
            "11-21": "Wilderness Wanderings",
            "22-36": "Preparation for Canaan"
        },
        "key_verses": {
            (1, 1): "וַיְדַבֵּר יְהוָה אֶל מֹשֶׁה בְּמִדְבַּר סִינַי",
            (6, 24): "יְבָרֶכְךָ יְהוָה וְיִשְׁמְרֶךָ",
            (6, 25): "יָאֵר יְהוָה פָּנָיו אֵלֶיךָ וִיחֻנֶּךָּ",
            (6, 26): "יִשָּׂא יְהוָה פָּנָיו אֵלֶיךָ וְיָשֵׂם לְךָ שָׁלוֹם",
            (10, 35): "קוּמָה יְהוָה וְיָפֻצוּ אוֹיְבֶיךָ",
            (14, 18): "יְהוָה אֶרֶךְ אַפַּיִם וְרַב חֶסֶד",
            (21, 17): "עָלִי בְאֵר עֱנוּ לָהּ",
            (24, 17): "אֶרְאֶנּוּ וְלֹא עַתָּה רְאִיתִיו וְלֹא קָרוֹב",
        }
    },
    
    # DEUTERONOMY
    "Deuteronomy": {
        "hebrew_name": "דברים",
        "chapters": 34,
        "sections": {
            "1-4": "First Address",
            "5-28": "Second Address (Law)",
            "29-30": "Third Address (Covenant)",
            "31-34": "Final Words"
        },
        "key_verses": {
            (1, 1): "אֵלֶּה הַדְּבָרִים אֲשֶׁר דִּבֶּר מֹשֶׁה",
            (4, 4): "וְאַתֶּם הַדְּבֵקִים בַּיהוָה אֱלֹהֵיכֶם חַיִּים כֻּלְּכֶם הַיּוֹם",
            (4, 39): "וְיָדַעְתָּ הַיּוֹם וַהֲשֵׁבֹתָ אֶל לְבָבֶךָ",
            (6, 4): "שְׁמַע יִשְׂרָאֵל יְהוָה אֱלֹהֵינוּ יְהוָה אֶחָד",
            (6, 5): "וְאָהַבְתָּ אֵת יְהוָה אֱלֹהֶיךָ בְּכָל לְבָבְךָ",
            (8, 3): "כִּי לֹא עַל הַלֶּחֶם לְבַדּוֹ יִחְיֶה הָאָדָם",
            (10, 12): "וְעַתָּה יִשְׂרָאֵל מָה יְהוָה אֱלֹהֶיךָ שֹׁאֵל מֵעִמָּךְ",
            (18, 15): "נָבִיא מִקִּרְבְּךָ מֵאַחֶיךָ כָּמֹנִי יְקִימְךָ יְהוָה אֱלֹהֶיךָ",
            (28, 1): "וְהָיָה אִם שָׁמוֹעַ תִּשְׁמַע בְּקוֹל יְהוָה אֱלֹהֶיךָ",
            (30, 15): "רְאֵה נָתַתִּי לְפָנֶיךָ הַיּוֹם אֶת הַחַיִּים וְאֶת הַטּוֹב",
            (30, 19): "וּבָחַרְתָּ בַּחַיִּים לְמַעַן תִּחְיֶה אַתָּה וְזַרְעֶךָ",
            (32, 1): "הַאֲזִינוּ הַשָּׁמַיִם וַאֲדַבֵּרָה",
            (34, 10): "וְלֹא קָם נָבִיא עוֹד בְּיִשְׂרָאֵל כְּמֹשֶׁה",
        }
    }
}

def import_complete_torah():
    """Import complete Torah with full analysis"""
    db = BiblicalDatabase()
    gem = GematriaCalculator()
    res = ResonanceEngine()
    
    print("="*70)
    print("IMPORTING COMPLETE TORAH (5 BOOKS)")
    print("="*70)
    
    total_stats = {
        "books": 0,
        "verses": 0,
        "words": 0,
        "total_gematria": 0
    }
    
    for book_name, book_data in TORAH_COMPLETE.items():
        print(f"\n📖 {book_name} ({book_data['hebrew_name']})")
        print(f"   Chapters: {book_data['chapters']}")
        print(f"   Key verses: {len(book_data['key_verses'])}")
        
        # Add book to database
        db.add_book(book_name, book_data['hebrew_name'], 
                   book_data['chapters'], "Torah")
        total_stats["books"] += 1
        
        book_gematria = []
        
        for (chapter, verse), hebrew in sorted(book_data['key_verses'].items()):
            gem_val = gem.calculate(hebrew)
            words = len(hebrew.split())
            
            # Add verse
            verse_id = db.add_verse(
                book_name, chapter, verse, hebrew,
                "", "", gem_val, gem.calculate(hebrew, "katan")
            )
            
            total_stats["verses"] += 1
            total_stats["words"] += words
            total_stats["total_gematria"] += gem_val
            book_gematria.append(gem_val)
        
        print(f"   Average gematria: {sum(book_gematria)/len(book_gematria):.1f}")
    
    # Final summary
    print("\n" + "="*70)
    print("TORAH IMPORT COMPLETE")
    print("="*70)
    print(f"\n📊 TOTAL STATISTICS:")
    print(f"   Books: {total_stats['books']}")
    print(f"   Key verses: {total_stats['verses']}")
    print(f"   Total words: {total_stats['words']}")
    print(f"   Total gematria: {total_stats['total_gematria']}")
    print(f"   Average: {total_stats['total_gematria']/total_stats['verses']:.1f}")
    
    db.export_to_json("/root/hebrew-repo/torah_complete_key_verses.json")
    print(f"\n✅ Exported to torah_complete_key_verses.json")
    db.close()

if __name__ == "__main__":
    import_complete_torah()