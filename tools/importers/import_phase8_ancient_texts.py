#!/usr/bin/env python3
"""
PHASE 8: MORE ANCIENT TEXTS
Dead Sea Scrolls, Additional Gnostic, Early Church Fathers, Mandaean
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

# DEAD SEA SCROLLS - Community Rule, War Scroll, Thanksgiving Hymns
DSS_COMMUNITY_RULE = [
    (1, "And this is the rule for the men of the Community... They shall separate from the congregation of the men of injustice.", "Community Entry"),
    (5, "And this is the rule for the men of the Community who volunteer... To love all the sons of light, each according to his lot in the council of God.", "Two Spirits"),
    (8, "In the Community council there shall be twelve men... And they shall be the foundation of the Community, the pillars upon which it stands.", "Council of Twelve"),
]

DSS_WAR_SCROLL = [
    (1, "The first attack of the Sons of Light shall be... Against the lot of the Sons of Darkness, the army of Belial.", "War of Sons"),
    (7, "On the banner of the thousand they shall write... The wrath of God is kindled against Belial and against all the men of his lot.", "Banners"),
    (11, "This shall be a time of salvation for the people of God... And eternal destruction for all the lot of Belial.", "Victory"),
]

DSS_THANKSGIVING_HYMNS = [
    (1, "I thank You, O Lord... For You have illumined my face by Your covenant.", "Thanksgiving"),
    (5, "I am a creature of clay... But You have given me knowledge.", "Knowledge"),
    (9, "Blessed are You, O God of mercy... Who has given me a spirit of truth.", "Spirit of Truth"),
]

DSS_HABAKKUK_COMMENTARY = [
    (1, "The oracle which Habakkuk the prophet prophesied... But God told Habakkuk to write what would come upon the last generation.", "Interpretation"),
    (2, "The wicked one covets the wealth of the nations... This refers to the Kittim who destroy many with the sword.", "Kittim"),
    (7, "Behold, his soul is puffed up, it is not upright in him... This refers to the Wicked Priest who pursued the Teacher of Righteousness.", "Wicked Priest"),
]

# ADDITIONAL GNOSTIC TEXTS
GOSPEL_OF_TRUTH = [
    (1, "The gospel of truth is joy... For it came forth from the Father of truth.", "Joy"),
    (20, "Those who have the truth are free... And ignorance of the Father brought about anguish and terror.", "Freedom"),
    (30, "The Word came forth... Speaking of the pleroma and the deficiency.", "Word"),
]

TREATISE_ON_RESURRECTION = [
    (1, "What is the resurrection?... It is the revelation of those who have risen.", "Resurrection Defined"),
    (10, "The resurrection is... The transformation of things, and a transition into newness.", "Transformation"),
]

TRIPARTITE_TRACTATE = [
    (1, "The Father is perfect... And the invisible, perfect God.", "The Father"),
    (50, "The Logos is the form... Through which the Father is revealed.", "The Logos"),
    (100, "The Church exists in the world... As the elect race.", "The Church"),
]

ON_BAPTISM = [
    (1, "The baptism of truth... Is the redemption of the soul.", "Baptism"),
    (5, "Through the living water... One is cleansed from sin.", "Living Water"),
]

ON_EUCHARIST = [
    (1, "The eucharist is Jesus... For he is called bread of life.", "Eucharist"),
    (3, "The cup contains wine... And the wine is the blood of the grape.", "Cup"),
]

# EARLY CHURCH FATHERS
DIDACHE = [
    (1, "There are two ways, one of life and one of death... And there is a great difference between the two ways.", "Two Ways"),
    (6, "See that no one leads you astray... For many shall come in my name saying I am the Christ.", "False Prophets"),
    (8, "Let not your fasts be with the hypocrites... But fast on the fourth day and the Preparation.", "Fasting"),
    (9, "Concerning the eucharist... Give thanks thus: First concerning the cup.", "Eucharist"),
    (10, "And after being filled, give thanks thus... We give thanks to You, holy Father.", "Thanksgiving"),
]

EPISTLE_OF_BARNABAS = [
    (1, "Greetings, sons and daughters of the Lord... Through the name of our Lord Jesus Christ.", "Greeting"),
    (5, "He had to suffer... For the sake of the Church, the Bride.", "Suffering"),
    (15, "Therefore, children, keep the Sabbath... And the eighth day is the beginning of another world.", "Eighth Day"),
    (21, "It is well, therefore, to learn the ordinances of the Lord... Walk in all His commandments.", "Conclusion"),
]

FIRST_CLEMENT = [
    (1, "The Church of God which sojourns in Rome... To the Church of God sojourning in Corinth.", "Greeting"),
    (20, "The generations from Adam to Noah... For His are the ends of the earth.", "Generations"),
    (38, "Let the wise man display his wisdom... Not in words but in works of righteousness.", "Works"),
    (59, "Blessed are we, beloved... If we keep the commandments of God.", "Blessed"),
]

IGNATIUS_TO_EPHESIANS = [
    (1, "Ignatius, who is also called Theophorus... To the Church at Ephesus in Asia.", "Greeting"),
    (7, "For our God, Jesus the Christ... Was conceived by Mary according to God's plan.", "Incarnation"),
    (20, "Pray for me... That I may attain to God.", "Prayer"),
]

POLYCARP_TO_PHILIPPIANS = [
    (1, "Polycarp and the presbyters with him... To the Church of God sojourning at Philippi.", "Greeting"),
    (4, "But the love of money is the beginning of all evils... Knowing that we brought nothing into the world.", "Contentment"),
    (9, "Stand fast in our Lord... And in his sufferings.", "Stand Fast"),
]

# MANDAEAN LITERATURE (Ginza Rabba)
GINZA_RABBA = [
    (1, "In the name of the Great Life... May the sublime light be glorified.", "Opening"),
    (5, "The soul comes from the light... And returns to the light.", "Soul Journey"),
    (10, "Jordan, living water... Wash away our sins.", "Living Water"),
]

# MANICHAEAN TEXTS
KEPHALAIA = [
    (1, "The chapters of the wisdom... Of the messenger of the light.", "Introduction"),
    (5, "The Father of Greatness... dwells in the light.", "Father of Greatness"),
    (10, "The Primal Man... Came down to battle the darkness.", "Primal Man"),
]

# PSALMS OF SOLOMON
PSALMS_OF_SOLOMON = [
    (2, "When the sinner casts his net... Into the sea full of swimming fish.", "Sinner's Net"),
    (8, "Distress and the sound of war has my ear heard... For the sound of the trumpet and the battle-cry.", "War"),
    (17, "Behold, O Lord, and raise up unto them their king... The son of David.", "Messianic King"),
    (18, "Blessed be the Lord God... Who is our king forever.", "Blessing"),
]

# ODES OF SOLOMON (Additional)
ODES_ADDITIONAL = [
    (7, "As the impulse of anger against evil... So is the impulse of joy.", "Joy"),
    (14, "As the eyes of a son upon his father... So are my eyes upon You.", "Eyes on God"),
    (25, "I was rescued from my chains... And I fled unto You, O my God.", "Rescue"),
    (33, "The joy of the Lord be upon His people... And His mercy on His servants.", "Joy and Mercy"),
]

def import_phase8():
    """Import Phase 8: More Ancient Texts"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("PHASE 8: MORE ANCIENT TEXTS")
    print("="*70)
    
    # Create tables
    imports = [
        ("dss_community_rule", DSS_COMMUNITY_RULE, "Dead Sea Scrolls: Community Rule"),
        ("dss_war_scroll", DSS_WAR_SCROLL, "Dead Sea Scrolls: War Scroll"),
        ("dss_thanksgiving_hymns", DSS_THANKSGIVING_HYMNS, "Dead Sea Scrolls: Thanksgiving Hymns"),
        ("dss_habakkuk_commentary", DSS_HABAKKUK_COMMENTARY, "Dead Sea Scrolls: Habakkuk Commentary"),
        ("gospel_of_truth", GOSPEL_OF_TRUTH, "Gospel of Truth"),
        ("treatise_on_resurrection", TREATISE_ON_RESURRECTION, "Treatise on Resurrection"),
        ("tripartite_tractate", TRIPARTITE_TRACTATE, "Tripartite Tractate"),
        ("on_baptism", ON_BAPTISM, "On Baptism"),
        ("on_eucharist", ON_EUCHARIST, "On Eucharist"),
        ("didache", DIDACHE, "Didache"),
        ("epistle_of_barnabas", EPISTLE_OF_BARNABAS, "Epistle of Barnabas"),
        ("first_clement", FIRST_CLEMENT, "1 Clement"),
        ("ignatius_to_ephesians", IGNATIUS_TO_EPHESIANS, "Ignatius to Ephesians"),
        ("polycarp_to_philippians", POLYCARP_TO_PHILIPPIANS, "Polycarp to Philippians"),
        ("ginza_rabba", GINZA_RABBA, "Ginza Rabba (Mandaean)"),
        ("kephalaia", KEPHALAIA, "Kephalaia (Manichaean)"),
        ("psalms_of_solomon", PSALMS_OF_SOLOMON, "Psalms of Solomon"),
        ("odes_of_solomon_additional", ODES_ADDITIONAL, "Odes of Solomon (Additional)"),
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
        "phase": "Phase 8",
        "total_entries": total,
        "books": [
            {"book": "DSS: Community Rule", "count": len(DSS_COMMUNITY_RULE)},
            {"book": "DSS: War Scroll", "count": len(DSS_WAR_SCROLL)},
            {"book": "DSS: Thanksgiving Hymns", "count": len(DSS_THANKSGIVING_HYMNS)},
            {"book": "DSS: Habakkuk Commentary", "count": len(DSS_HABAKKUK_COMMENTARY)},
            {"book": "Gospel of Truth", "count": len(GOSPEL_OF_TRUTH)},
            {"book": "Treatise on Resurrection", "count": len(TREATISE_ON_RESURRECTION)},
            {"book": "Tripartite Tractate", "count": len(TRIPARTITE_TRACTATE)},
            {"book": "On Baptism", "count": len(ON_BAPTISM)},
            {"book": "On Eucharist", "count": len(ON_EUCHARIST)},
            {"book": "Didache", "count": len(DIDACHE)},
            {"book": "Epistle of Barnabas", "count": len(EPISTLE_OF_BARNABAS)},
            {"book": "1 Clement", "count": len(FIRST_CLEMENT)},
            {"book": "Ignatius to Ephesians", "count": len(IGNATIUS_TO_EPHESIANS)},
            {"book": "Polycarp to Philippians", "count": len(POLYCARP_TO_PHILIPPIANS)},
            {"book": "Ginza Rabba", "count": len(GINZA_RABBA)},
            {"book": "Kephalaia", "count": len(KEPHALAIA)},
            {"book": "Psalms of Solomon", "count": len(PSALMS_OF_SOLOMON)},
            {"book": "Odes of Solomon (Additional)", "count": len(ODES_ADDITIONAL)},
        ]
    }
    
    with open('/root/hebrew-repo/exports/phase8_ancient_texts_export.json', 'w') as f:
        json.dump(export, f, indent=2)
    
    print("\n" + "="*70)
    print("PHASE 8 COMPLETE - MORE ANCIENT TEXTS!")
    print("="*70)
    print(f"\n📊 IMPORTED: {total} entries from 18 texts")
    print(f"\n📚 TEXTS:")
    print(f"   Dead Sea Scrolls: Community Rule, War Scroll, Hymns, Habakkuk")
    print(f"   Additional Gnostic: Gospel of Truth, Resurrection, Tripartite")
    print(f"   Early Church: Didache, Barnabas, 1 Clement, Ignatius, Polycarp")
    print(f"   Other Traditions: Ginza Rabba (Mandaean), Kephalaia (Manichaean)")
    print(f"   Additional: Psalms of Solomon, Odes of Solomon")
    print(f"\n📁 Exported to exports/phase8_ancient_texts_export.json")
    
    db.close()

if __name__ == "__main__":
    import_phase8()