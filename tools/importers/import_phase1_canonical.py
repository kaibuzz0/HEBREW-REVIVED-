#!/usr/bin/env python3
"""
IMPORTER FOR MAJOR CANONICAL BOOKS
Phase 1: Psalms, Isaiah, Major NT Books

This creates the foundation of the Complete Bible
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

# PSALMS - Selected key psalms
PSALMS = [
    # Book I (Psalms 1-41)
    (1, "Blessed is the man who walks not in the counsel of the wicked, nor stands in the way of sinners, nor sits in the seat of scoffers; but his delight is in the law of the LORD, and on his law he meditates day and night. He is like a tree planted by streams of water that yields its fruit in its season, and its leaf does not wither. In all that he does, he prospers.", "Book I", "Two Ways"),
    (2, "Why do the nations rage and the peoples plot in vain? The kings of the earth set themselves, and the rulers take counsel together, against the LORD and against his Anointed... He who sits in the heavens laughs; the Lord holds them in derision. Then he will speak to them in his wrath, and terrify them in his fury.", "Book I", "Messianic"),
    (8, "O LORD, our Lord, how majestic is your name in all the earth! You have set your glory above the heavens. Out of the mouth of babies and infants, you have established strength because of your foes, to still the enemy and the avenger.", "Book I", "Praise"),
    (19, "The heavens declare the glory of God, and the sky above proclaims his handiwork. Day to day pours out speech, and night to night reveals knowledge. There is no speech, nor are there words, whose voice is not heard.", "Book I", "Creation"),
    (22, "My God, my God, why have you forsaken me? Why are you so far from saving me, from the words of my groaning? O my God, I cry by day, but you do not answer, and by night, but I find no rest.", "Book I", "Messianic, Lament"),
    (23, "The LORD is my shepherd; I shall not want. He makes me lie down in green pastures. He leads me beside still waters. He restores my soul. He leads me in paths of righteousness for his name's sake. Even though I walk through the valley of the shadow of death, I will fear no evil, for you are with me; your rod and your staff, they comfort me.", "Book I", "Trust, Shepherd"),
    (24, "The earth is the LORD's and the fullness thereof, the world and those who dwell therein, for he has founded it upon the seas and established it upon the rivers. Who shall ascend the hill of the LORD? And who shall stand in his holy place?", "Book I", "Kingship"),
    (27, "The LORD is my light and my salvation; whom shall I fear? The LORD is the stronghold of my life; of whom shall I be afraid?", "Book I", "Trust"),
    (32, "Blessed is the one whose transgression is forgiven, whose sin is covered. Blessed is the man against whom the LORD counts no iniquity, and in whose spirit there is no deceit.", "Book I", "Forgiveness"),
    (37, "Fret not yourself because of evildoers; be not envious of wrongdoers! For they will soon fade like the grass and wither like the green herb. Trust in the LORD, and do good; dwell in the land and befriend faithfulness.", "Book I", "Wisdom"),
    
    # Book II (Psalms 42-72)
    (42, "As a deer pants for flowing streams, so my soul pants for you, O God. My soul thirsts for God, for the living God. When shall I come and appear before God?", "Book II", "Longing"),
    (46, "God is our refuge and strength, a very present help in trouble. Therefore we will not fear though the earth gives way, though the mountains be moved into the heart of the sea.", "Book II", "Trust"),
    (51, "Have mercy on me, O God, according to your steadfast love; according to your abundant mercy blot out my transgressions. Wash me thoroughly from my iniquity, and cleanse me from my sin!", "Book II", "Repentance"),
    (63, "O God, you are my God; earnestly I seek you; my soul thirsts for you; my flesh faints for you, as in a dry and weary land where there is no water.", "Book II", "Longing"),
    
    # Book III (Psalms 73-89)
    (73, "Truly God is good to Israel, to those who are pure in heart. But as for me, my feet had almost stumbled, my steps had nearly slipped. For I was envious of the arrogant when I saw the prosperity of the wicked.", "Book III", "Wisdom"),
    (84, "How lovely is your dwelling place, O LORD of hosts! My soul longs, yes, faints for the courts of the LORD; my heart and flesh sing for joy to the living God.", "Book III", "Worship"),
    
    # Book IV (Psalms 90-106)
    (90, "Lord, you have been our dwelling place in all generations. Before the mountains were brought forth, or ever you had formed the earth and the world, from everlasting to everlasting you are God.", "Book IV", "Eternity"),
    (91, "He who dwells in the shelter of the Most High will abide in the shadow of the Almighty. I will say to the LORD, 'My refuge and my fortress, my God, in whom I trust.'", "Book IV", "Protection"),
    (100, "Make a joyful noise to the LORD, all the earth! Serve the LORD with gladness! Come into his presence with singing! Know that the LORD, he is God! It is he who made us, and we are his; we are his people, and the sheep of his pasture.", "Book IV", "Thanksgiving"),
    (103, "Bless the LORD, O my soul, and all that is within me, bless his holy name! Bless the LORD, O my soul, and forget not all his benefits, who forgives all your iniquity, who heals all your diseases.", "Book IV", "Praise"),
    (104, "Bless the LORD, O my soul! O LORD my God, you are very great! You are clothed with splendor and majesty, covering yourself with light as with a garment, stretching out the heavens like a tent.", "Book IV", "Creation"),
    
    # Book V (Psalms 107-150)
    (110, "The LORD says to my Lord: 'Sit at my right hand, until I make your enemies your footstool.' The LORD sends forth from Zion your mighty scepter. Rule in the midst of your enemies!", "Book V", "Messianic"),
    (116, "I love the LORD, because he has heard my voice and my pleas for mercy. Because he inclined his ear to me, therefore I will call on him as long as I live.", "Book V", "Thanksgiving"),
    (118, "Oh give thanks to the LORD, for he is good; for his steadfast love endures forever! Let Israel say, 'His steadfast love endures forever.'", "Book V", "Thanksgiving"),
    (119, "Blessed are those whose way is blameless, who walk in the law of the LORD! Blessed are those who keep his testimonies, who seek him with their whole heart.", "Book V", "Torah"),
    (121, "I lift up my eyes to the hills. From where does my help come? My help comes from the LORD, who made heaven and earth.", "Book V", "Trust"),
    (127, "Unless the LORD builds the house, those who build it labor in vain. Unless the LORD watches over the city, the watchman stays awake in vain.", "Book V", "Wisdom"),
    (130, "Out of the depths I cry to you, O LORD! O Lord, hear my voice! Let your ears be attentive to the voice of my pleas for mercy!", "Book V", "Lament"),
    (139, "O LORD, you have searched me and known me! You know when I sit down and when I rise up; you discern my thoughts from afar.", "Book V", "Omniscience"),
    (145, "I will extol you, my God and King, and bless your name forever and ever. Every day I will bless you and praise your name forever and ever.", "Book V", "Praise"),
    (150, "Praise the LORD! Praise God in his sanctuary; praise him in his mighty heavens! Praise him for his mighty deeds; praise him according to his excellent greatness! Let everything that has breath praise the LORD! Praise the LORD!", "Book V", "Doxology"),
]

# ISAIAH - Selected chapters (the whole book is 66 chapters)
ISAIAH = [
    (1, "The vision of Isaiah the son of Amoz, which he saw concerning Judah and Jerusalem in the days of Uzziah, Jotham, Ahaz, and Hezekiah, kings of Judah. Hear, O heavens, and give ear, O earth; for the LORD has spoken: 'Children have I reared and brought up, but they have rebelled against me.'", "Introduction, Rebellion"),
    (2, "It shall come to pass in the latter days that the mountain of the house of the LORD shall be established as the highest of the mountains, and shall be lifted up above the hills; and all the nations shall flow to it.", "Mountain of the Lord"),
    (6, "In the year that King Uzziah died I saw the Lord sitting upon a throne, high and lifted up; and the train of his robe filled the temple. Above him stood the seraphim. Each had six wings: with two he covered his face, and with two he covered his feet, and with two he flew.", "Vision, Call"),
    (7, "Therefore the Lord himself will give you a sign. Behold, the virgin shall conceive and bear a son, and shall call his name Immanuel.", "Immanuel Prophecy"),
    (9, "For to us a child is born, to us a son is given; and the government shall be upon his shoulder, and his name shall be called Wonderful Counselor, Mighty God, Everlasting Father, Prince of Peace.", "Messianic"),
    (11, "There shall come forth a shoot from the stump of Jesse, and a branch from his roots shall bear fruit. And the Spirit of the LORD shall rest upon him, the Spirit of wisdom and understanding, the Spirit of counsel and might, the Spirit of knowledge and the fear of the LORD.", "Messianic"),
    (25, "O LORD, you are my God; I will exalt you; I will praise your name, for you have done wonderful things, plans formed of old, faithful and sure.", "Praise"),
    (26, "In that day this song will be sung in the land of Judah: 'We have a strong city; salvation God sets up walls and bulwarks for safety.'", "Salvation"),
    (40, "Comfort, comfort my people, says your God. Speak tenderly to Jerusalem, and cry to her that her warfare is ended, that her iniquity is pardoned, that she has received from the LORD's hand double for all her sins. A voice cries: 'In the wilderness prepare the way of the LORD; make straight in the desert a highway for our God.'", "Comfort"),
    (42, "Behold my servant, whom I uphold, my chosen, in whom my soul delights; I have put my Spirit upon him; he will bring forth justice to the nations.", "Servant Song"),
    (43, "But now thus says the LORD, he who created you, O Jacob, he who formed you, O Israel: 'Fear not, for I have redeemed you; I have called you by name, you are mine.'", "Redemption"),
    (52, "How beautiful upon the mountains are the feet of him who brings good news, who publishes peace, who brings good news of happiness, who publishes salvation, who says to Zion, 'Your God reigns.'", "Gospel"),
    (53, "Who has believed what he has heard from us? And to whom has the arm of the LORD been revealed? For he grew up before him like a young plant, and like a root out of dry ground... He was despised and rejected by men, a man of sorrows and acquainted with grief... Surely he has borne our griefs and carried our sorrows... He was pierced for our transgressions; he was crushed for our iniquities; upon him was the chastisement that brought us peace, and with his wounds we are healed.", "Suffering Servant"),
    (55, "Come, everyone who thirsts, come to the waters; and he who has no money, come, buy and eat! Come, buy wine and milk without money and without price.", "Invitation"),
    (61, "The Spirit of the Lord GOD is upon me, because the LORD has anointed me to bring good news to the poor; he has sent me to bind up the brokenhearted, to proclaim liberty to the captives, and the opening of the prison to those who are bound.", "Messianic"),
    (66, "Thus says the LORD: 'Heaven is my throne, and the earth is my footstool; what is the house that you would build for me, and what is the place of my rest? All these things my hand has made, and so all these things came to be, declares the LORD. But this is the one to whom I will look: he who is humble and contrite in spirit and trembles at my word.'", "New Heavens, New Earth"),
]

# JOHN - Selected chapters (whole gospel)
GOSPEL_OF_JOHN = [
    (1, "In the beginning was the Word, and the Word was with God, and the Word was God. He was in the beginning with God. All things were made through him, and without him was not any thing made that was made. In him was life, and the life was the light of men. The light shines in the darkness, and the darkness has not overcome it... And the Word became flesh and dwelt among us, and we have seen his glory, glory as of the only Son from the Father, full of grace and truth.", "Prologue, Incarnation"),
    (3, "Now there was a man of the Pharisees named Nicodemus, a ruler of the Jews. This man came to Jesus by night and said to him, 'Rabbi, we know that you are a teacher come from God, for no one can do these signs that you do unless God is with him.' Jesus answered him, 'Truly, truly, I say to you, unless one is born again he cannot see the kingdom of God.'... 'For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.'", "Born Again, John 3:16"),
    (4, "Jesus answered her, If you knew the gift of God, and who it is that is saying to you, Give me a drink, you would have asked him, and he would have given you living water. Jesus said to her, Everyone who drinks of this water will be thirsty again, but whoever drinks of the water that I will give him will never be thirsty again. The water that I will give him will become in him a spring of water welling up to eternal life.", "Living Water"),
    (6, "Jesus said to them, 'I am the bread of life; whoever comes to me shall not hunger, and whoever believes in me shall never thirst.'... 'Truly, truly, I say to you, unless you eat the flesh of the Son of Man and drink his blood, you have no life in you. Whoever feeds on my flesh and drinks my blood has eternal life, and I will raise him up on the last day.'", "Bread of Life"),
    (8, "So Jesus said to the Jews who had believed him, 'If you abide in my word, you are truly my disciples, and you will know the truth, and the truth will set you free.'... Jesus said to them, 'Truly, truly, I say to you, before Abraham was, I am.'", "Truth, I AM"),
    (10, "I am the good shepherd. I know my own and my own know me, just as the Father knows me and I know the Father; and I lay down my life for the sheep.", "Good Shepherd"),
    (11, "Jesus said to her, 'I am the resurrection and the life. Whoever believes in me, though he die, yet shall he live, and everyone who lives and believes in me shall never die. Do you believe this?'", "Resurrection"),
    (14, "'Let not your hearts be troubled. Believe in God; believe also in me. In my Father's house are many rooms. If it were not so, would I have told you that I go to prepare a place for you? And if I go and prepare a place for you, I will come again and will take you to myself, that where I am you may be also.'... Jesus said to him, 'I am the way, and the truth, and the life. No one comes to the Father except through me.'", "Way, Truth, Life"),
    (15, "I am the vine; you are the branches. Whoever abides in me and I in him, he it is that bears much fruit, for apart from me you can do nothing.", "Vine and Branches"),
    (20, "Now on the first day of the week Mary Magdalene came to the tomb early, while it was still dark, and saw that the stone had been taken away from the tomb... But Mary stood weeping outside the tomb, and as she wept she stooped to look into the tomb... Jesus said to her, 'Mary.' She turned and said to him in Aramaic, 'Rabboni!' (which means Teacher).", "Resurrection"),
]

# REVELATION - Selected chapters (whole book)
REVELATION = [
    (1, "The revelation of Jesus Christ, which God gave him to show to his servants the things that must soon take place. He made it known by sending his angel to his servant John, who bore witness to the word of God and to the testimony of Jesus Christ... 'I am the Alpha and the Omega,' says the Lord God, 'who is and who was and who is to come, the Almighty.'... When I saw him, I fell at his feet as though dead. But he laid his right hand on me, saying, 'Fear not, I am the first and the last, and the living one. I died, and behold I am alive forevermore, and I have the keys of Death and Hades.'", "Introduction, Vision"),
    (4, "At once I was in the Spirit, and behold, a throne stood in heaven, with one seated on the throne. And he who sat there had the appearance of jasper and carnelian, and around the throne was a rainbow that had the appearance of an emerald.", "Heavenly Throne"),
    (5, "And between the throne and the four living creatures and among the elders I saw a Lamb standing, as though it had been slain... And they sang a new song, saying, 'Worthy are you to take the scroll and to open its seals, for you were slain, and by your blood you ransomed people for God from every tribe and language and people and nation.'", "Lamb Worthy"),
    (7, "After this I looked, and behold, a great multitude that no one could number, from every nation, from all tribes and peoples and languages, standing before the throne and before the Lamb, clothed in white robes, with palm branches in their hands, and crying out with a loud voice, 'Salvation belongs to our God who sits on the throne, and to the Lamb!'", "Great Multitude"),
    (12, "And a great sign appeared in heaven: a woman clothed with the sun, with the moon under her feet, and on her head a crown of twelve stars... And the dragon stood before the woman who was about to give birth, so that when she bore her child he might devour it. She gave birth to a male child, one who is to rule all the nations with a rod of iron.", "Woman and Dragon"),
    (21, "Then I saw a new heaven and a new earth, for the first heaven and the first earth had passed away, and the sea was no more. And I saw the holy city, new Jerusalem, coming down out of heaven from God, prepared as a bride adorned for her husband. And I heard a loud voice from the throne saying, 'Behold, the dwelling place of God is with man. He will dwell with them, and they will be his people, and God himself will be with them as their God. He will wipe away every tear from their eyes, and death shall be no more, neither shall there be mourning, nor crying, nor pain anymore, for the former things have passed away.'", "New Heaven, New Earth"),
    (22, "Then the angel showed me the river of the water of life, bright as crystal, flowing from the throne of God and of the Lamb through the middle of the street of the city; also, on either side of the river, the tree of life with its twelve kinds of fruit, yielding its fruit each month... And there will be no night there. They will need no light of lamp or sun, for the Lord God will be their light, and they will reign forever and ever... Behold, I am coming soon, bringing my recompense with me, to repay each one for what he has done. I am the Alpha and the Omega, the first and the last, the beginning and the end.", "Tree of Life, Alpha and Omega"),
]

def import_canonical():
    """Import major canonical books"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("IMPORTING MAJOR CANONICAL BOOKS - PHASE 1")
    print("="*70)
    
    # Create tables for canonical books
    db.cursor.execute("""
        CREATE TABLE IF NOT EXISTS book_of_psalms (
            id INTEGER PRIMARY KEY,
            psalm_number INTEGER,
            book TEXT,
            english_text TEXT,
            theme TEXT
        )
    """)
    
    db.cursor.execute("""
        CREATE TABLE IF NOT EXISTS book_of_isaiah (
            id INTEGER PRIMARY KEY,
            chapter INTEGER,
            english_text TEXT,
            theme TEXT
        )
    """)
    
    db.cursor.execute("""
        CREATE TABLE IF NOT EXISTS gospel_of_john (
            id INTEGER PRIMARY KEY,
            chapter INTEGER,
            english_text TEXT,
            theme TEXT
        )
    """)
    
    db.cursor.execute("""
        CREATE TABLE IF NOT EXISTS book_of_revelation (
            id INTEGER PRIMARY KEY,
            chapter INTEGER,
            english_text TEXT,
            theme TEXT
        )
    """)
    
    # Clear existing
    for table in ['book_of_psalms', 'book_of_isaiah', 'gospel_of_john', 'book_of_revelation']:
        db.cursor.execute(f"DELETE FROM {table}")
    
    # Import Psalms
    print("\n📖 Importing Psalms...")
    for psalm in PSALMS:
        num, text, book, theme = psalm
        db.cursor.execute("""
            INSERT INTO book_of_psalms (psalm_number, book, english_text, theme)
            VALUES (?, ?, ?, ?)
        """, (num, book, text, theme))
    print(f"   ✅ Imported {len(PSALMS)} psalms")
    
    # Import Isaiah
    print("\n📖 Importing Isaiah...")
    for chapter in ISAIAH:
        num, text, theme = chapter
        db.cursor.execute("""
            INSERT INTO book_of_isaiah (chapter, english_text, theme)
            VALUES (?, ?, ?)
        """, (num, text, theme))
    print(f"   ✅ Imported {len(ISAIAH)} chapters")
    
    # Import John
    print("\n📖 Importing Gospel of John...")
    for chapter in GOSPEL_OF_JOHN:
        num, text, theme = chapter
        db.cursor.execute("""
            INSERT INTO gospel_of_john (chapter, english_text, theme)
            VALUES (?, ?, ?)
        """, (num, text, theme))
    print(f"   ✅ Imported {len(GOSPEL_OF_JOHN)} chapters")
    
    # Import Revelation
    print("\n📖 Importing Revelation...")
    for chapter in REVELATION:
        num, text, theme = chapter
        db.cursor.execute("""
            INSERT INTO book_of_revelation (chapter, english_text, theme)
            VALUES (?, ?, ?)
        """, (num, text, theme))
    print(f"   ✅ Imported {len(REVELATION)} chapters")
    
    db.conn.commit()
    
    # Export to JSON
    export = {
        "title": "Major Canonical Books - Phase 1",
        "books_imported": [
            {"book": "Psalms", "count": len(PSALMS), "total": 150},
            {"book": "Isaiah", "count": len(ISAIAH), "total": 66},
            {"book": "Gospel of John", "count": len(GOSPEL_OF_JOHN), "total": 21},
            {"book": "Revelation", "count": len(REVELATION), "total": 22}
        ],
        "psalms": [{"number": p[0], "theme": p[3], "book": p[2]} for p in PSALMS],
        "isaiah": [{"chapter": c[0], "theme": c[2]} for c in ISAIAH],
        "john": [{"chapter": c[0], "theme": c[2]} for c in GOSPEL_OF_JOHN],
        "revelation": [{"chapter": c[0], "theme": c[2]} for c in REVELATION]
    }
    
    with open('/root/hebrew-repo/exports/phase1_canonical_export.json', 'w', encoding='utf-8') as f:
        json.dump(export, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*70)
    print("PHASE 1 COMPLETE")
    print("="*70)
    print(f"\n📊 IMPORTED:")
    print(f"   • {len(PSALMS)} Psalms")
    print(f"   • {len(ISAIAH)} Isaiah chapters")
    print(f"   • {len(GOSPEL_OF_JOHN)} John chapters")
    print(f"   • {len(REVELATION)} Revelation chapters")
    print(f"\n✅ Total: {len(PSALMS) + len(ISAIAH) + len(GOSPEL_OF_JOHN) + len(REVELATION)} entries")
    print(f"\n📁 Exported to exports/phase1_canonical_export.json")
    print(f"\n🎯 PHASE 1 FOUNDATION COMPLETE!")
    print(f"   Core canonical books now in database")
    
    db.close()

if __name__ == "__main__":
    import_canonical()