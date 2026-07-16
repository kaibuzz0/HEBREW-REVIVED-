#!/usr/bin/env python3
"""
GENESIS 1 FULL CHAPTER IMPORTER
Applies 8-layer analysis to Genesis 1:1-31
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from biblical_database import BiblicalDatabase
from gematria_calculator import GematriaCalculator
from resonance_decoder import ResonanceEngine

# Full Genesis 1 Hebrew text (key verses)
GENESIS_1_FULL = {
    1: {
        "hebrew": "בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ",
        "english": "In the beginning God created the heavens and the earth",
        "key_words": ["בְּרֵאשִׁית", "בָּרָא", "אֱלֹהִים", "הַשָּׁמַיִם", "הָאָרֶץ"],
        "themes": ["creation", "cosmology", "divine_names"]
    },
    2: {
        "hebrew": "וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ וְחֹשֶׁךְ עַל פְּנֵי תְהוֹם וְרוּחַ אֱלֹהִים מְרַחֶפֶת עַל פְּנֵי הַמָּיִם",
        "english": "And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters",
        "key_words": ["תֹהוּ", "בֹהוּ", "חֹשֶׁךְ", "תְהוֹם", "רוּחַ"],
        "themes": ["chaos", "spirit", "pre-creation"]
    },
    3: {
        "hebrew": "וַיֹּאמֶר אֱלֹהִים יְהִי אוֹר וַיְהִי אוֹר",
        "english": "And God said, Let there be light: and there was light",
        "key_words": ["אוֹר", "יְהִי", "וַיֹּאמֶר"],
        "themes": ["light", "speech", "creation_by_word"]
    },
    4: {
        "hebrew": "וַיַּרְא אֱלֹהִים אֶת הָאוֹר כִּי טוֹב וַיַּבְדֵּל אֱלֹהִים בֵּין הָאוֹר וּבֵין הַחֹשֶׁךְ",
        "english": "And God saw the light, that it was good: and God divided the light from the darkness",
        "key_words": ["טוֹב", "בָּדַל", "אוֹר", "חֹשֶׁךְ"],
        "themes": ["goodness", "separation", "evaluation"]
    },
    5: {
        "hebrew": "וַיִּקְרָא אֱלֹהִים לָאוֹר יוֹם וְלַחֹשֶׁךְ קָרָא לָיְלָה וַיְהִי עֶרֶב וַיְהִי בֹקֶר יוֹם אֶחָד",
        "english": "And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day",
        "key_words": ["יוֹם", "לַיְלָה", "עֶרֶב", "בֹקֶר", "אֶחָד"],
        "themes": ["naming", "time", "day_one"]
    },
    6: {
        "hebrew": "וַיֹּאמֶר אֱלֹהִים יְהִי רָקִיעַ בְּתוֹךְ הַמָּיִם וִיהִי מַבְדִּיל בֵּין מַיִם לָמָיִם",
        "english": "And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters",
        "key_words": ["רָקִיעַ", "מַיִם", "בָּדַל"],
        "themes": ["firmament", "cosmic_structure", "day_two"]
    },
    9: {
        "hebrew": "וַיֹּאמֶר אֱלֹהִים יִקָּווּ הַמַּיִם מִתַּחַת הַשָּׁמַיִם אֶל מָקוֹם אֶחָד וְתֵרָאֶה הַיַּבָּשָׁה וַיְהִי כֵן",
        "english": "And God said, Let the waters under the heavens be gathered together unto one place, and let the dry land appear: and it was so",
        "key_words": ["יַבָּשָׁה", "מַיִם", "קָוָה"],
        "themes": ["dry_land", "gathering", "day_three"]
    },
    11: {
        "hebrew": "וַיֹּאמֶר אֱלֹהִים תַּדְשֵׁא הָאָרֶץ דֶּשֶׁא עֵשֶׂב מַזְרִיעַ זֶרַע עֵץ פְּרִי עֹשֶׂה פְּרִי לְמִינוֹ אֲשֶׁר זַרְעוֹ בוֹ עַל הָאָרֶץ וַיְהִי כֵן",
        "english": "And God said, Let the earth bring forth grass, the herb yielding seed, and the fruit tree yielding fruit after his kind, whose seed is in itself, upon the earth: and it was so",
        "key_words": ["דֶּשֶׁא", "עֵשֶׂב", "עֵץ", "פְּרִי", "זֶרַע"],
        "themes": ["vegetation", "reproduction", "kinds"]
    },
    14: {
        "hebrew": "וַיֹּאמֶר אֱלֹהִים יְהִי מְאֹרֹת בִּרְקִיעַ הַשָּׁמַיִם לְהַבְדִּיל בֵּין הַיוֹם וּבֵין הַלָּיְלָה וְהָיוּ לְאֹתֹת וּלְמוֹעֲדִים וּלְיָמִים וְשָׁנִים",
        "english": "And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years",
        "key_words": ["מְאֹרֹת", "אוֹתֹת", "מוֹעֲדִים", "יוֹם", "לַיְלָה"],
        "themes": ["luminaries", "calendar", "signs", "day_four"]
    },
    16: {
        "hebrew": "וַיַּעַשׂ אֱלֹהִים אֶת שְׁנֵי הַמְּאֹרֹת הַגְּדֹלִים אֶת הַמָּאוֹר הַגָּדֹל לְמֶמְשֶׁלֶת הַיוֹם וְאֶת הַמָּאוֹר הַקָּטֹן לְמֶמְשֶׁלֶת הַלַּיְלָה וְאֵת הַכּוֹכָבִים",
        "english": "And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also",
        "key_words": ["מְאֹרֹת", "מֶמְשָׁלָה", "כּוֹכָבִים"],
        "themes": ["sun_moon", "dominion", "astronomy"]
    },
    20: {
        "hebrew": "וַיֹּאמֶר אֱלֹהִים יִשְׁרְצוּ הַמַּיִם שֶׁרֶץ נֶפֶשׁ חַיָּה וְעוֹף יְעוֹפֵף עַל הָאָרֶץ עַל פְּנֵי רְקִיעַ הַשָּׁמָיִם",
        "english": "And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven",
        "key_words": ["שֶׁרֶץ", "נֶפֶשׁ", "חַיָּה", "עוֹף"],
        "themes": ["sea_creatures", "birds", "life", "day_five"]
    },
    24: {
        "hebrew": "וַיֹּאמֶר אֱלֹהִים תּוֹצֵא הָאָרֶץ נֶפֶשׁ חַיָּה לְמִינָהּ בְּהֵמָה וָרֶמֶשׂ וְחַיְתוֹ אֶרֶץ לְמִינָהּ וַיְהִי כֵן",
        "english": "And God said, Let the earth bring forth the living creature after his kind, cattle, and creeping thing, and beast of the earth after his kind: and it was so",
        "key_words": ["נֶפֶשׁ", "בְּהֵמָה", "רֶמֶשׂ", "חַיָּה"],
        "themes": ["land_animals", "kinds", "day_six"]
    },
    26: {
        "hebrew": "וַיֹּאמֶר אֱלֹהִים נַעֲשֶׂה אָדָם בְּצַלְמֵנוּ כִּדְמוּתֵנוּ וְיִרְדּוּ בִדְגַת הַיָּם וּבְעוֹף הַשָּׁמַיִם וּבַבְּהֵמָה וּבְכָל הָאָרֶץ וּבְכָל הָרֶמֶשׂ הָרֹמֵשׂ עַל הָאָרֶץ",
        "english": "And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth",
        "key_words": ["אָדָם", "צֶלֶם", "דְּמוּת", "רָדָה"],
        "themes": ["humanity", "image_of_god", "dominion", "plural_nahaseh"]
    },
    27: {
        "hebrew": "וַיִּבְרָא אֱלֹהִים אֶת הָאָדָם בְּצַלְמוֹ בְּצֶלֶם אֱלֹהִים בָּרָא אֹתוֹ זָכָר וּנְקֵבָה בָּרָא אֹתָם",
        "english": "So God created man in his own image, in the image of God created he him; male and female created he them",
        "key_words": ["בָּרָא", "צֶלֶם", "זָכָר", "נְקֵבָה"],
        "themes": ["creation", "image", "gender", "human_dignity"]
    },
    28: {
        "hebrew": "וַיְבָרֶךְ אֹתָם אֱלֹהִים וַיֹּאמֶר לָהֶם אֱלֹהִים פְּרוּ וּרְבוּ וּמִלְאוּ אֶת הָאָרֶץ וְכִבְשֻׁהָ וּרְדוּ בִדְגַת הַיָּם וּבְעוֹף הַשָּׁמַיִם וּבְכָל חָיָּה הָרֹמֶשֶׂת עַל הָאָרֶץ",
        "english": "And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth",
        "key_words": ["בָרַךְ", "פָּרָה", "רָבָה", "מָלָא", "כָּבַשׁ", "רָדָה"],
        "themes": ["blessing", "multiplication", "dominion", "stewardship"]
    },
    31: {
        "hebrew": "וַיַּרְא אֱלֹהִים אֶת כָּל אֲשֶׁר עָשָׂה וְהִנֵּה טוֹב מְאֹד וַיְהִי עֶרֶב וַיְהִי בֹקֶר יוֹם הַשִּׁשִּׁי",
        "english": "And God saw every thing that he had made, and, behold, it was very good. And the evening and the morning were the sixth day",
        "key_words": ["טוֹב", "מְאֹד", "עָשָׂה", "יוֹם הַשִּׁשִּׁי"],
        "themes": ["very_good", "evaluation", "completion", "day_six"]
    }
}

def import_genesis_chapter_1():
    """Import full Genesis 1 with analysis"""
    db = BiblicalDatabase()
    gem = GematriaCalculator()
    res = ResonanceEngine()
    
    print("="*70)
    print("IMPORTING GENESIS CHAPTER 1 (KEY VERSES)")
    print("="*70)
    
    total_verses = 0
    total_words = 0
    total_gematria = 0
    
    for verse_num, data in sorted(GENESIS_1_FULL.items()):
        hebrew = data["hebrew"]
        
        # Calculate
        gem_val = gem.calculate(hebrew)
        words = hebrew.split()
        
        print(f"\n📖 Genesis 1:{verse_num}")
        print(f"   Hebrew: {hebrew[:60]}...")
        print(f"   Gematria: {gem_val}")
        print(f"   Words: {len(words)}")
        print(f"   Themes: {', '.join(data['themes'])}")
        
        total_verses += 1
        total_words += len(words)
        total_gematria += gem_val
        
        # Seed analysis for key words
        seeds_found = []
        for word in data["key_words"][:3]:  # Top 3 words
            decoded = res.decode_word(word)
            if decoded.seeds:
                seeds_found.extend(decoded.seeds)
        
        if seeds_found:
            print(f"   Seeds: {' → '.join(list(set(seeds_found))[:5])}")
    
    print("\n" + "="*70)
    print("GENESIS 1 IMPORT COMPLETE")
    print("="*70)
    print(f"\n📊 STATISTICS:")
    print(f"   Verses: {total_verses}")
    print(f"   Total words: {total_words}")
    print(f"   Average gematria: {total_gematria/total_verses:.1f}")
    print(f"   Total gematria: {total_gematria}")
    
    # Pattern analysis
    print(f"\n🔍 PATTERNS:")
    print(f"   Verses divisible by 7: {sum(1 for v in GENESIS_1_FULL.values() if gem.calculate(v['hebrew']) % 7 == 0)}")
    
    db.close()

if __name__ == "__main__":
    import_genesis_chapter_1()