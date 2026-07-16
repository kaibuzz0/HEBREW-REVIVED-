#!/usr/bin/env python3
"""
PHASE 4: REMAINING NEW TESTAMENT EPISTLES
Galatians, Ephesians, Philippians, Colossians, Thessalonians, Pastoral, General
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

# GALATIANS
GALATIANS = [
    (1, "Paul, an apostle - not from men nor through man, but through Jesus Christ and God the Father, who raised him from the dead... For I would have you know, brothers, that the gospel that was preached by me is not man's gospel. For I did not receive it from any man, nor was I taught it, but I received it through a revelation of Jesus Christ.", "Introduction"),
    (2, "Yet because of false brothers secretly brought in - who slipped in to spy out our freedom that we have in Christ Jesus, so that they might bring us into slavery - to them we did not yield in submission even for a moment... We know that a person is not justified by works of the law but through faith in Jesus Christ.", "Justification by Faith"),
    (3, "O foolish Galatians! Who has bewitched you? It was before your eyes that Jesus Christ was publicly portrayed as crucified. Let me ask you only this: Did you receive the Spirit by works of the law or by hearing with faith?", "Faith vs Law"),
    (5, "For freedom Christ has set us free; stand firm therefore, and do not submit again to a yoke of slavery... But the fruit of the Spirit is love, joy, peace, patience, kindness, goodness, faithfulness, gentleness, self-control; against such things there is no law.", "Fruit of the Spirit"),
]

# EPHESIANS
EPHESIANS = [
    (1, "Blessed be the God and Father of our Lord Jesus Christ, who has blessed us in Christ with every spiritual blessing in the heavenly places... In him we have redemption through his blood, the forgiveness of our trespasses, according to the riches of his grace.", "Spiritual Blessings"),
    (2, "And you were dead in the trespasses and sins in which you once walked... But God, being rich in mercy, because of the great love with which he loved us, even when we were dead in our trespasses, made us alive together with Christ - by grace you have been saved.", "By Grace Saved"),
    (4, "There is one body and one Spirit - just as you were called to the one hope that belongs to your call - one Lord, one faith, one baptism, one God and Father of all, who is over all and through all and in all.", "Unity of the Spirit"),
    (6, "Finally, be strong in the Lord and in the strength of his might. Put on the whole armor of God, that you may be able to stand against the schemes of the devil.", "Armor of God"),
]

# PHILIPPIANS
PHILIPPIANS = [
    (1, "I thank my God in all my remembrance of you... And I am sure of this, that he who began a good work in you will bring it to completion at the day of Jesus Christ.", "Thanksgiving"),
    (2, "Do nothing from selfish ambition or conceit, but in humility count others more significant than yourselves. Let each of you look not only to his own interests, but also to the interests of others. Have this mind among yourselves, which is yours in Christ Jesus...", "Christ's Humility"),
    (3, "Indeed, I count everything as loss because of the surpassing worth of knowing Christ Jesus my Lord. For his sake I have suffered the loss of all things and count them as rubbish, in order that I may gain Christ.", "Gain Christ"),
    (4, "Rejoice in the Lord always; again I will say, rejoice. Let your reasonableness be known to everyone. The Lord is at hand; do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God.", "Rejoice, Prayer"),
]

# COLOSSIANS
COLOSSIANS = [
    (1, "He is the image of the invisible God, the firstborn of all creation. For by him all things were created, in heaven and on earth, visible and invisible, whether thrones or dominions or rulers or authorities - all things were created through him and for him.", "Christ Supreme"),
    (3, "If then you have been raised with Christ, seek the things that are above, where Christ is, seated at the right hand of God. Set your minds on things that are above, not on things that are on earth.", "Seek Above"),
]

# 1 THESSALONIANS
THESSALONIANS_1 = [
    (4, "But we do not want you to be uninformed, brothers, about those who are asleep, that you may not grieve as others do who have no hope. For since we believe that Jesus died and rose again, even so, through Jesus, God will bring with him those who have fallen asleep.", "Hope in Death"),
    (5, "Now concerning the times and the seasons, brothers, you have no need to have anything written to you. For you yourselves are fully aware that the day of the Lord will come like a thief in the night... For God has not destined us for wrath, but to obtain salvation through our Lord Jesus Christ.", "Day of the Lord"),
]

# 2 THESSALONIANS
THESSALONIANS_2 = [
    (2, "Now concerning the coming of our Lord Jesus Christ and our being gathered together to him... Let no one deceive you in any way. For that day will not come, unless the rebellion comes first, and the man of lawlessness is revealed, the son of destruction.", "Man of Lawlessness"),
    (3, "But the Lord is faithful. He will establish you and guard you against the evil one... Now may the Lord of peace himself give you peace at all times in every way. The Lord be with you all.", "Lord of Peace"),
]

# 1 TIMOTHY
TIMOTHY_1 = [
    (1, "But I received mercy because I had acted ignorantly in unbelief, and the grace of our Lord overflowed for me with the faith and love that are in Christ Jesus. The saying is trustworthy and deserving of full acceptance, that Christ Jesus came into the world to save sinners, of whom I am the foremost.", "Grace Overflowed"),
    (2, "First of all, then, I urge that supplications, prayers, intercessions, and thanksgivings be made for all people, for kings and all who are in high positions, that we may lead a peaceful and quiet life, godly and dignified in every way.", "Pray for All"),
    (6, "But godliness with contentment is great gain, for we brought nothing into the world, and we cannot take anything out of the world.", "Contentment"),
]

# 2 TIMOTHY
TIMOTHY_2 = [
    (1, "I thank God whom I serve, as did my ancestors, with a clear conscience, as I remember you constantly in my prayers night and day... For God gave us a spirit not of fear but of power and love and self-control.", "Spirit of Power"),
    (3, "All Scripture is breathed out by God and profitable for teaching, for reproof, for correction, and for training in righteousness, that the man of God may be complete, equipped for every good work.", "All Scripture"),
    (4, "I have fought the good fight, I have finished the race, I have kept the faith. Henceforth there is laid up for me the crown of righteousness, which the Lord, the righteous judge, will award to me on that day, and not only to me but also to all who have loved his appearing.", "Finished the Race"),
]

# TITUS
TITUS = [
    (1, "Paul, a servant of God and an apostle of Jesus Christ, for the sake of the faith of God's elect and their knowledge of the truth, which accords with godliness...", "Introduction"),
    (2, "For the grace of God has appeared, bringing salvation for all people, training us to renounce ungodliness and worldly passions, and to live self-controlled, upright, and godly lives in the present age.", "Grace of God"),
    (3, "But when the goodness and loving kindness of God our Savior appeared, he saved us, not because of works done by us in righteousness, but according to his own mercy, by the washing of regeneration and renewal of the Holy Spirit.", "Not by Works"),
]

# PHILEMON
PHILEMON = [
    (1, "I thank my God always when I remember you in my prayers, because I hear of your love and of the faith that you have toward the Lord Jesus and for all the saints... Perhaps this is why he was parted from you for a while, that you might have him back forever, no longer as a bondservant but more than a bondservant, as a beloved brother.", "Onesimus"),
]

# HEBREWS
HEBREWS = [
    (1, "Long ago, at many times and in many ways, God spoke to our fathers by the prophets, but in these last days he has spoken to us by his Son, whom he appointed the heir of all things, through whom also he created the world. He is the radiance of the glory of God and the exact imprint of his nature.", "Son Superior"),
    (4, "For the word of God is living and active, sharper than any two-edged sword, piercing to the division of soul and of spirit, of joints and of marrow, and discerning the thoughts and intentions of the heart.", "Living Word"),
    (11, "Now faith is the assurance of things hoped for, the conviction of things not seen. For by it the people of old received their commendation... And without faith it is impossible to please him, for whoever would draw near to God must believe that he exists and that he rewards those who seek him.", "Hall of Faith"),
    (12, "Therefore, since we are surrounded by so great a cloud of witnesses, let us also lay aside every weight, and sin which clings so closely, and let us run with endurance the race that is set before us, looking to Jesus, the founder and perfecter of our faith.", "Cloud of Witnesses"),
]

# JAMES (the epistle, different from James brother of Jesus in Infancy)
JAMES_EPISTLE = [
    (1, "Count it all joy, my brothers, when you meet trials of various kinds, for you know that the testing of your faith produces steadfastness. And let steadfastness have its full effect, that you may be perfect and complete, lacking in nothing... But be doers of the word, and not hearers only, deceiving yourselves.", "Trials, Doers"),
    (2, "What good is it, my brothers, if someone says he has faith but does not have works? Can that faith save him? So also faith by itself, if it does not have works, is dead.", "Faith and Works"),
    (3, "If any of you lacks wisdom, let him ask God, who gives generously to all without reproach, and it will be given him... And the tongue is a fire, a world of unrighteousness. The tongue is set among our members, staining the whole body.", "Wisdom, Tongue"),
    (4, "You do not have, because you do not ask. You ask and do not receive, because you ask wrongly, to spend it on your passions... Submit yourselves therefore to God. Resist the devil, and he will flee from you. Draw near to God, and he will draw near to you.", "Draw Near"),
]

# 1 PETER
PETER_1 = [
    (1, "Blessed be the God and Father of our Lord Jesus Christ! According to his great mercy, he has caused us to be born again to a living hope through the resurrection of Jesus Christ from the dead.", "Living Hope"),
    (2, "But you are a chosen race, a royal priesthood, a holy nation, a people for his own possession, that you may proclaim the excellencies of him who called you out of darkness into his marvelous light.", "Royal Priesthood"),
    (3, "Now who is there to harm you if you are zealous for what is good? But even if you should suffer for righteousness' sake, you will be blessed. Have no fear of them, nor be troubled, but in your hearts honor Christ the Lord as holy.", "Suffer for Righteousness"),
    (5, "Humble yourselves, therefore, under the mighty hand of God so that at the proper time he may exalt you, casting all your anxieties on him, because he cares for you.", "Cast Anxieties"),
]

# 2 PETER
PETER_2 = [
    (1, "His divine power has granted to us all things that pertain to life and godliness, through the knowledge of him who called us to his own glory and excellence... For this very reason, make every effort to supplement your faith with virtue, and virtue with knowledge.", "Add to Faith"),
    (3, "The Lord is not slow to fulfill his promise as some count slowness, but is patient toward you, not wishing that any should perish, but that all should reach repentance. But the day of the Lord will come like a thief.", "Patience of God"),
]

# 1 JOHN
JOHN_1 = [
    (1, "That which was from the beginning, which we have heard, which we have seen with our eyes, which we looked upon and have touched with our hands, concerning the word of life... This is the message we have heard from him and proclaim to you, that God is light, and in him is no darkness at all.", "God is Light"),
    (2, "My little children, I am writing these things to you so that you may not sin. But if anyone does sin, we have an advocate with the Father, Jesus Christ the righteous... Do not love the world or the things in the world. If anyone loves the world, the love of the Father is not in him.", "Do Not Love World"),
    (3, "See what kind of love the Father has given to us, that we should be called children of God; and so we are... No one has ever seen God; if we love one another, God abides in us and his love is perfected in us.", "Children of God"),
    (4, "Beloved, do not believe every spirit, but test the spirits to see whether they are from God, for many false prophets have gone out into the world... So we have come to know and to believe the love that God has for us. God is love, and whoever abides in love abides in God, and God abides in him.", "God is Love"),
]

# 2 JOHN
JOHN_2 = [
    (1, "The elder to the elect lady and her children, whom I love in truth... And this is love, that we walk according to his commandments... For many deceivers have gone out into the world, those who do not confess the coming of Jesus Christ in the flesh.", "Walk in Truth"),
]

# 3 JOHN
JOHN_3 = [
    (1, "Beloved, it is a faithful thing you do when you give full support to the brothers, especially when they are strangers... I have no greater joy than to hear that my children are walking in the truth.", "Walking in Truth"),
]

# JUDE
JUDE = [
    (1, "Beloved, although I was very eager to write to you about our common salvation, I found it necessary to write appealing to you to contend for the faith that was once for all delivered to the saints.", "Contend for Faith"),
    (24, "Now to him who is able to keep you from stumbling and to present you blameless before the presence of his glory with great joy, to the only God, our Savior, through Jesus Christ our Lord, be glory, majesty, dominion, and authority, before all time and now and forever. Amen.", "Doxology"),
]

def import_phase4():
    """Import Phase 4: Remaining Epistles"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("IMPORTING PHASE 4: REMAINING NEW TESTAMENT EPISTLES")
    print("="*70)
    
    # Create tables
    tables = [
        ("epistle_to_galatians", "Galatians"),
        ("epistle_to_ephesians", "Ephesians"),
        ("epistle_to_philippians", "Philippians"),
        ("epistle_to_colossians", "Colossians"),
        ("first_epistle_to_thessalonians", "1 Thessalonians"),
        ("second_epistle_to_thessalonians", "2 Thessalonians"),
        ("first_epistle_to_timothy", "1 Timothy"),
        ("second_epistle_to_timothy", "2 Timothy"),
        ("epistle_to_titus", "Titus"),
        ("epistle_to_philemon", "Philemon"),
        ("epistle_to_hebrews", "Hebrews"),
        ("epistle_of_james", "James"),
        ("first_epistle_of_peter", "1 Peter"),
        ("second_epistle_of_peter", "2 Peter"),
        ("first_epistle_of_john", "1 John"),
        ("second_epistle_of_john", "2 John"),
        ("third_epistle_of_john", "3 John"),
        ("epistle_of_jude", "Jude"),
    ]
    
    for table, name in tables:
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
    imports = [
        ("epistle_to_galatians", GALATIANS),
        ("epistle_to_ephesians", EPHESIANS),
        ("epistle_to_philippians", PHILIPPIANS),
        ("epistle_to_colossians", COLOSSIANS),
        ("first_epistle_to_thessalonians", THESSALONIANS_1),
        ("second_epistle_to_thessalonians", THESSALONIANS_2),
        ("first_epistle_to_timothy", TIMOTHY_1),
        ("second_epistle_to_timothy", TIMOTHY_2),
        ("epistle_to_titus", TITUS),
        ("epistle_to_philemon", PHILEMON),
        ("epistle_to_hebrews", HEBREWS),
        ("epistle_of_james", JAMES_EPISTLE),
        ("first_epistle_of_peter", PETER_1),
        ("second_epistle_of_peter", PETER_2),
        ("first_epistle_of_john", JOHN_1),
        ("second_epistle_of_john", JOHN_2),
        ("third_epistle_of_john", JOHN_3),
        ("epistle_of_jude", JUDE),
    ]
    
    total = 0
    for table, data in imports:
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
        print(f"   ✅ {table}: {count} chapters")
    
    db.conn.commit()
    
    # Export
    export = {
        "phase": "Phase 4",
        "total_entries": total,
        "books": [
            {"book": "Galatians", "count": len(GALATIANS)},
            {"book": "Ephesians", "count": len(EPHESIANS)},
            {"book": "Philippians", "count": len(PHILIPPIANS)},
            {"book": "Colossians", "count": len(COLOSSIANS)},
            {"book": "1 Thessalonians", "count": len(THESSALONIANS_1)},
            {"book": "2 Thessalonians", "count": len(THESSALONIANS_2)},
            {"book": "1 Timothy", "count": len(TIMOTHY_1)},
            {"book": "2 Timothy", "count": len(TIMOTHY_2)},
            {"book": "Titus", "count": len(TITUS)},
            {"book": "Philemon", "count": len(PHILEMON)},
            {"book": "Hebrews", "count": len(HEBREWS)},
            {"book": "James", "count": len(JAMES_EPISTLE)},
            {"book": "1 Peter", "count": len(PETER_1)},
            {"book": "2 Peter", "count": len(PETER_2)},
            {"book": "1 John", "count": len(JOHN_1)},
            {"book": "2 John", "count": len(JOHN_2)},
            {"book": "3 John", "count": len(JOHN_3)},
            {"book": "Jude", "count": len(JUDE)},
        ]
    }
    
    with open('/root/hebrew-repo/exports/phase4_epistles_export.json', 'w') as f:
        json.dump(export, f, indent=2)
    
    print("\n" + "="*70)
    print("PHASE 4 COMPLETE - NEW TESTAMENT EPISTLES FINISHED!")
    print("="*70)
    print(f"\n📊 IMPORTED: {total} chapters from 18 epistles")
    print(f"\n📚 PAULINE EPISTLES:")
    print(f"   Prison: Ephesians, Philippians, Colossians, Philemon")
    print(f"   Pastoral: 1-2 Timothy, Titus")
    print(f"   Others: Galatians, 1-2 Thessalonians")
    print(f"\n📚 GENERAL EPISTLES:")
    print(f"   Hebrews, James, 1-2 Peter, 1-2-3 John, Jude")
    print(f"\n📁 Exported to exports/phase4_epistles_export.json")
    
    db.close()

if __name__ == "__main__":
    import_phase4()