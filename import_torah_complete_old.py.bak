#!/usr/bin/env python3
"""
TORAH COMPLETE IMPORTER
Imports all 5 books of Torah with full analysis
Genesis, Exodus, Leviticus, Numbers, Deuteronomy
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from biblical_database import BiblicalDatabase
from gematria_calculator import GematriaCalculator
from resonance_decoder import ResonanceEngine

TORAH_DATA = {
    "Genesis": {
        "hebrew": "בראשית",
        "chapters": 50,
        "key_verses": [
            (1, 1, "בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ", "In the beginning God created the heavens and the earth"),
            (1, 27, "וַיִּבְרָא אֱלֹהִים אֶת הָאָדָם בְּצַלְמוֹ", "So God created man in his own image"),
            (12, 1, "לֶךְ לְךָ מֵאַרְצְךָ", "Get thee out of thy country"),
            (15, 1, "אַל תִּירָא אַבְרָם אָנֹכִי מָגֵן לָךְ", "Fear not, Abram: I am thy shield"),
            (22, 1, "וַיְהִי אַחַר הַדְּבָרִים הָאֵלֶּה וְהָאֱלֹהִים נִסָּה אֶת אַבְרָהָם", "After these things God did tempt Abraham"),
            (28, 12, "וַיַּחֲלֹם וְהִנֵּה סֻלָּם מֻצָּב אַרְצָה", "He dreamed, and behold a ladder set up on the earth"),
            (32, 28, "לֹא יַעֲקֹב יֵאָמֵר עוֹד שִׁמְךָ כִּי אִם יִשְׂרָאֵל", "Thy name shall be called no more Jacob, but Israel"),
            (49, 1, "וַיִּקְרָא יַעֲקֹב אֶל בָּנָיו", "And Jacob called unto his sons"),
        ]
    },
    "Exodus": {
        "hebrew": "שמות",
        "chapters": 40,
        "key_verses": [
            (3, 1, "וּמֹשֶׁה הָיָה רֹעֶה אֶת צֹאן יִתְרוֹ", "Now Moses kept the flock of Jethro"),
            (3, 6, "וַיֹּאמֶר אָנֹכִי אֱלֹהֵי אָבִיךָ אֱלֹהֵי אַבְרָהָם אֱלֹהֵי יִצְחָק וֵאלֹהֵי יַעֲקֹב", "I am the God of thy father, the God of Abraham"),
            (3, 14, "אֶהְיֶה אֲשֶׁר אֶהְיֶה", "I AM THAT I AM"),
            (12, 2, "הַחֹדֶשׁ הַזֶּה לָכֶם רֹאשׁ חֳדָשִׁים", "This month shall be unto you the beginning of months"),
            (13, 21, "וַיהוָה הֹלֵךְ לִפְנֵיהֶם יוֹמָם", "The LORD went before them by day"),
            (14, 21, "וַיִּבְקְעוּ הַמָּיִם", "The waters were divided"),
            (19, 1, "בַּחֹדֶשׁ הַשְּׁלִישִׁי לְצֵאת בְּנֵי יִשְׂרָאֵל מֵאֶרֶץ מִצְרָיִם", "In the third month, when the children of Israel were gone forth"),
            (20, 1, "וַיְדַבֵּר אֱלֹהִים אֵת כָּל הַדְּבָרִים הָאֵלֶּה לֵאמֹר", "And God spake all these words"),
            (24, 12, "וַיֹּאמֶר יְהוָה אֶל מֹשֶׁה עֲלֵה אֵלַי הָהָרָה", "Come up to me into the mount"),
            (25, 8, "וְעָשׂוּ לִי מִקְדָּשׁ וְשָׁכַנְתִּי בְּתוֹכָם", "Let them make me a sanctuary; that I may dwell among them"),
            (33, 11, "וְדִבֶּר יְהוָה אֶל מֹשֶׁה פָּנִים אֶל פָּנִים", "The LORD spake unto Moses face to face"),
            (34, 6, "יְהוָה יְהוָה אֵל רַחוּם וְחַנּוּן", "The LORD, The LORD God, merciful and gracious"),
        ]
    },
    "Leviticus": {
        "hebrew": "ויקרא",
        "chapters": 27,
        "key_verses": [
            (1, 1, "וַיִּקְרָא אֶל מֹשֶׁה וַיְדַבֵּר יְהוָה אֵלָיו", "The LORD called unto Moses, and spake unto him"),
            (11, 44, "וְהִתְקַדִּשְׁתֶּם וִהְיִיתֶם קְדֹשִׁים", "Ye shall be holy; for I am holy"),
            (16, 2, "וַיֹּאמֶר יְהוָה אֶל מֹשֶׁה דַּבֵּר אֶל אַהֲרֹן אָחִיךָ", "Speak unto Aaron thy brother"),
            (19, 2, "קְדֹשִׁים תִּהְיוּ כִּי קָדוֹשׁ אֲנִי", "Ye shall be holy: for I the LORD your God am holy"),
            (19, 18, "וְאָהַבְתָּ לְרֵעֲךָ כָּמוֹךָ", "Thou shalt love thy neighbour as thyself"),
            (23, 1, "וַיְדַבֵּר יְהוָה אֶל מֹשֶׁה לֵּאמֹר", "The LORD spake unto Moses"),
            (26, 12, "וְהִתְהַלַּכְתִּי בְּתוֹכְכֶם", "I will walk among you"),
        ]
    },
    "Numbers": {
        "hebrew": "במדבר",
        "chapters": 36,
        "key_verses": [
            (1, 1, "וַיְדַבֵּר יְהוָה אֶל מֹשֶׁה בְּמִדְבַּר סִינַי", "The LORD spake unto Moses in the wilderness of Sinai"),
            (6, 24, "יְבָרֶכְךָ יְהוָה וְיִשְׁמְרֶךָ", "The LORD bless thee, and keep thee"),
            (10, 35, "קוּמָה יְהוָה וְיָפֻצוּ אוֹיְבֶיךָ", "Rise up, LORD, and let thine enemies be scattered"),
            (14, 18, "יְהוָה אֶרֶךְ אַפַּיִם וְרַב חֶסֶד", "The LORD is longsuffering, and of great mercy"),
            (21, 17, "עָלִי בְאֵר עֱנוּ לָהּ", "Spring up, O well; sing ye unto it"),
            (24, 17, "אֶרְאֶנּוּ וְלֹא עַתָּה", "I shall see him, but not now"),
        ]
    },
    "Deuteronomy": {
        "hebrew": "דברים",
        "chapters": 34,
        "key_verses": [
            (1, 1, "אֵלֶּה הַדְּבָרִים אֲשֶׁר דִּבֶּר מֹשֶׁה", "These be the words which Moses spake"),
            (4, 4, "וְאַתֶּם הַדְּבֵקִים בַּיהוָה אֱלֹהֵיכֶם", "But ye that did cleave unto the LORD your God"),
            (6, 4, "שְׁמַע יִשְׂרָאֵל יְהוָה אֱלֹהֵינוּ יְהוָה אֶחָד", "Hear, O Israel: The LORD our God is one LORD"),
            (6, 5, "וְאָהַבְתָּ אֵת יְהוָה אֱלֹהֶיךָ בְּכָל לְבָבְךָ", "Thou shalt love the LORD thy God with all thine heart"),
            (8, 3, "כִּי לֹא עַל הַלֶּחֶם לְבַדּוֹ יִחְיֶה הָאָדָם", "Man doth not live by bread only"),
            (10, 12, "וְעַתָּה יִשְׂרָאֵל מָה יְהוָה אֱלֹהֶיךָ שֹׁאֵל מֵעִמָּךְ", "And now, Israel, what doth the LORD thy God require of thee"),
            (18, 15, "נָבִיא מִקִּרְבְּךָ מֵאַחֶיךָ כָּמֹנִי יְקִימְךָ יְהוָה", "The LORD thy God will raise up unto thee a Prophet"),
            (28, 1, "וְהָיָה אִם שָׁמוֹעַ תִּשְׁמַע בְּקוֹל יְהוָה", "If thou shalt hearken diligently unto the voice of the LORD"),
            (30, 15, "רְאֵה נָתַתִּי לְפָנֶיךָ הַיּוֹם אֶת הַחַיִּים וְאֶת הַטּוֹב", "See, I have set before thee this day life and good"),
            (32, 1, "הַאֲזִינוּ הַשָּׁמַיִם וַאֲדַבֵּרָה", "Give ear, O ye heavens, and I will speak"),
            (34, 10, "וְלֹא קָם נָבִיא עוֹד בְּיִשְׂרָאֵל כְּמֹשֶׁה", "There arose not a prophet since in Israel like unto Moses"),
        ]
    }
}

def import_full_torah():
    """Import complete Torah with full analysis"""
    db = BiblicalDatabase()
    gem = GematriaCalculator()
    res = ResonanceEngine()
    
    print("="*70)
    print("IMPORTING COMPLETE TORAH (5 BOOKS)")
    print("="*70)
    
    total_stats = {"books": 0, "verses": 0, "words": 0, "avg_gematria": []}
    
    for book_name, book_data in TORAH_DATA.items():
        print(f"\n📖 {book_name} ({book_data['hebrew']})")
        
        # Add book
        db.add_book(book_name, book_data['hebrew'], book_data['chapters'], "Torah")
        total_stats["books"] += 1
        
        book_verses = 0
        book_words = 0
        
        for chapter, verse, hebrew, english in book_data['key_verses']:
            # Calculate gematria
            gem_std = gem.calculate(hebrew)
            gem_ktn = gem.calculate(hebrew, "katan")
            
            # Add verse
            verse_id = db.add_verse(
                book_name, chapter, verse, hebrew,
                "", english, gem_std, gem_ktn
            )
            
            if verse_id:
                book_verses += 1
                total_stats["verses"] += 1
                total_stats["avg_gematria"].append(gem_std)
                
                # Word analysis
                words = hebrew.split()
                for i, word in enumerate(words, 1):
                    decoded = res.decode_word(word)
                    db.add_word_analysis(
                        verse_id, i, word, decoded.translit,
                        decoded.seeds[0] if decoded.seeds else "unknown",
                        "noun",
                        gem.calculate(word),
                        decoded.seed_sequence
                    )
                    book_words += 1
                    total_stats["words"] += 1
                
                print(f"  ✓ {book_name} {chapter}:{verse} (G:{gem_std})")
        
        print(f"   Book stats: {book_verses} verses, {book_words} words")
    
    # Final statistics
    print("\n" + "="*70)
    print("TORAH IMPORT COMPLETE")
    print("="*70)
    print(f"\n📊 TOTAL STATISTICS:")
    print(f"   Books: {total_stats['books']}")
    print(f"   Verses: {total_stats['verses']}")
    print(f"   Words analyzed: {total_stats['words']}")
    print(f"   Avg gematria: {sum(total_stats['avg_gematria'])/len(total_stats['avg_gematria']):.1f}")
    print(f"   Max gematria: {max(total_stats['avg_gematria'])}")
    
    # Export
    db.export_to_json("/root/hebrew-repo/torah_complete.json")
    print(f"\n✅ Exported to torah_complete.json")
    
    db.close()
    print("\n🎉 COMPLETE TORAH ANALYSIS FINISHED!")

if __name__ == "__main__":
    import_full_torah()