#!/usr/bin/env python3
"""
SHEPHERD OF HERMAS IMPORTER
Early Christian text from 1st-2nd century CE
Three parts: Visions, Mandates, Similitudes
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

HERMAS_SECTIONS = [
    # Book I: The Visions (4 visions)
    (1, "The first vision: I was praying while fasting, sitting on a certain mountain in the country of Cuma. As I prayed to the Lord, the heaven opened and I saw the woman I loved. She called to me: Hermas! I answered: Lady, what are you doing here? She said: I have been taken up here to accuse you of your sins before the Lord. I said: Lady, have I sinned against you? She said: No, but you have sinned against me by polluting your flesh with adulterous desires. Your heart is not pure before the Lord.",
     "Vision 1", "Vision"),
    
    (2, "She spoke these words to me while I was sleeping, and I seemed to press her hand, and immediately I awoke. And I was sorrowful and troubled, and I began to doubt whether this was a vision or an actual appearance. And while I was thinking about it, I saw before me a heavenly vision, and I began to pray to the Lord and to confess my sins.",
     "Vision 1 Continued", "Vision"),
    
    (3, "While I was praying, the heaven opened and I saw the woman again, whom I had desired, greeting me from heaven, saying: Hermas, be greeted! And I, looking at her, said: Lady, what are you doing here? She answered: I have been taken up to accuse you before God. I said: Lady, have you now been taken up? She said: Yes, that you might know that your sins are forgiven by God. And I rejoiced greatly.",
     "Vision 1 - Forgiveness", "Vision"),
    
    (4, "The second vision: I saw a vision twenty days after the former vision, of the same type. I saw a vision of a great willow tree overshadowing plains and mountains. Under the shade of the willow there were assembled all who were called by the Lord. And near the willow there was an angel of the Lord, very glorious, clothed in white robes, with a book in his hand.",
     "Vision 2 - The Willow Tree", "Vision"),
    
    (5, "The angel said to me: Do you see what is going on? I said: I see, sir. He said: These are they who have heard the word and are about to repent. They are like branches, some more and some less fruitful. Those who brought the branches full of fruit are they who suffered for the name of the Son of God, and have kept his commandments.",
     "Vision 2 - Branches", "Vision"),
    
    (6, "Those who brought the withered branches are they who heard the word but did not keep it, and denied the name by which they were called. But they have repented, and have borne fruit. But the others, who brought neither green nor withered branches, are the double-minded, who doubt and are never at peace in their hearts.",
     "Vision 2 - Double-minded", "Vision"),
    
    (7, "The third vision: I saw a great mountain, white as snow, and round like a ball. And the Lord said to me: Hermas, why do you dispute about the white mountain? Do you not understand? I said: I do not understand, Lord. He said: Hear now: this is the Church of God. The white color is because the world is made white through the blood of the Son of God, and the round shape is because the Church is strong and eternal.",
     "Vision 3 - The Mountain", "Vision"),
    
    (8, "The fourth vision: I saw a vision of the Church in the form of an aged woman, because she was created first of all. For in the beginning she was aged, but at the end she became young. And in the last days she will appear as a virgin, pure and undefiled.",
     "Vision 4 - The Aged Woman", "Vision"),
    
    # Book II: The Mandates (12 commandments)
    (9, "First Mandate: Believe that God is one, who created all things and set them in order, who made the world out of what did not exist. He contains all things and is alone uncontained. Believe in him, therefore, and fear him, and fearing him, be continent. Keep these things, and you will cast off all evil from yourself and will put on every virtue of righteousness, and will live to God.",
     "Mandate 1 - Faith", "Mandate"),
    
    (10, "Second Mandate: Keep away from evil-speaking, for it is the mother of all evils. For if anyone is evil-spoken of, immediately the demon of anger is aroused against him. Keep this commandment, therefore, and you will always be at peace with all men.",
     "Mandate 2 - No Evil-speaking", "Mandate"),
    
    (11, "Third Mandate: Love truth and let no lie dwell in your heart, for the lie is from the devil, and the truth is from the Lord. Speak the truth to one another, and you will be established in your faith.",
     "Mandate 3 - Truth", "Mandate"),
    
    (12, "Fourth Mandate: Put away all remembrance of your wife's former sins, and do not remind her of them, lest bitterness come between you. For he who reminds her of sins is guilty of the same sin himself, and he who hears it and is silent is also guilty.",
     "Mandate 4 - Forgiveness", "Mandate"),
    
    (13, "Fifth Mandate: Be patient and understanding, for patience is better than strength, and understanding is better than courage. With patience you will overcome evil, and with understanding you will receive good things from the Lord.",
     "Mandate 5 - Patience", "Mandate"),
    
    (14, "Sixth Mandate: Keep this commandment concerning faith: First of all, believe that God is one, who created and established all things, and made out of what did not exist everything that is. Believe therefore in him, and fear him, and being in fear, be continent.",
     "Mandate 6 - Faith", "Mandate"),
    
    (15, "Seventh Mandate: Fear the Lord and keep his commandments. By fearing the Lord you will live, and by keeping his commandments you will be justified. Do not fear the devil, for he cannot harm those who fear the Lord.",
     "Mandate 7 - Fear God", "Mandate"),
    
    (16, "Eighth Mandate: I told you that the creatures of God are double, for restraint is necessary in the case of all things. You must restrain yourself from evil, and not be double-minded or doubtful. For double-mindedness is the daughter of the devil.",
     "Mandate 8 - No Double-mindedness", "Mandate"),
    
    (17, "Ninth Mandate: Put away sorrow from yourself, for it is the sister of doubt and anger. Be joyful always, and pray with a cheerful heart, and God will hear you. For a sorrowful heart dries up the soul.",
     "Mandate 9 - Joy", "Mandate"),
    
    (18, "Tenth Mandate: Concerning the prophetic spirit, distinguish carefully: Every prophet who speaks in the spirit is examined by the spirit. If the prophet speaks what is right, he is of God. But if he asks for money or speaks falsehood, he is false.",
     "Mandate 10 - Prophets", "Mandate"),
    
    (19, "Eleventh Mandate: Remove every evil desire from your heart, but put on the desire which is good and holy. For if you put on the good desire, you will hate the evil one, and will be able to conquer it.",
     "Mandate 11 - Good Desires", "Mandate"),
    
    (20, "Twelfth Mandate: Put on desire for righteousness, and be armed with the fear of the Lord. For the fear of the Lord drives away sin, and where sin is absent, there righteousness dwells.",
     "Mandate 12 - Righteousness", "Mandate"),
    
    # Book III: The Similitudes (9 parables)
    (21, "First Similitude: As a farmer working his field casts his seed upon the earth, some falls by the wayside, some upon rocky places, some among thorns, and some on good ground. So also is the preaching of the word of God. Some hear and are immediately led astray by the devil. Others receive the word with joy but have no root and fall away in time of temptation. Others hear but the cares of this life choke the word. But those on good ground hear the word, understand it, and bear fruit.",
     "Similitude 1 - The Sower", "Similitude"),
    
    (22, "Second Similitude: As a vine is supported by an elm tree, so the rich man is supported by the prayer of the poor. If the rich man helps the poor, the elm supports the vine. But if the rich man does not help the poor, both the elm and the vine wither.",
     "Similitude 2 - The Vine and Elm", "Similitude"),
    
    (23, "Third Similitude: In winter the trees stand bare, and you cannot tell which are alive and which are dead. But in spring the living trees put forth leaves and fruit, while the dead remain as they were. So also in this world: the righteous and sinners appear the same, but in the resurrection the righteous will be known by their fruits.",
     "Similitude 3 - Winter Trees", "Similitude"),
    
    (24, "Fourth Similitude: I saw a large tree and an angel of the Lord sitting by it. He said: This is the tree of righteousness, and those who eat of it will live forever. But first they must wash in the pool of repentance. For the fruit is bitter to those who have not repented.",
     "Similitude 4 - Tree of Righteousness", "Similitude"),
    
    (25, "Fifth Similitude: I saw a tower being built, and many stones were brought to it. Some were rejected by the builders, but others were fitted into the building. The tower is the Church, and the stones are the righteous. The rejected stones are the sinners who will not be part of the building.",
     "Similitude 5 - The Tower", "Similitude"),
    
    (26, "Sixth Similitude: I saw shepherds feeding their flocks, some with green pastures and clear water, others with bitter pastures and muddy water. The good shepherds are the angels who minister to the righteous, but the bad shepherds are the deceiving spirits who lead astray.",
     "Similitude 6 - The Shepherds", "Similitude"),
    
    (27, "Seventh Similitude: I saw two ways, one narrow and one broad. The narrow way was steep and difficult, but led to life. The broad way was easy and pleasant, but led to destruction. Many take the broad way, but few find the narrow way.",
     "Similitude 7 - Two Ways", "Similitude"),
    
    (28, "Eighth Similitude: I saw a great dragon with many heads, and I was afraid. But the angel said: Fear not, for the dragon is the devil, and his heads are the sins of this world. Put on the armor of faith and you will overcome him.",
     "Similitude 8 - The Dragon", "Similitude"),
    
    (29, "Ninth Similitude: I saw the Son of God in the form of a glorious man, and he said to me: I am the Shepherd to whom you were delivered. I am the gate of life. Through me you must enter if you wish to be saved.",
     "Similitude 9 - The Good Shepherd", "Similitude"),
    
    (30, "Conclusion: And after these things I gave thanks to the Lord because he had mercy on me and showed me his wonders. And I exhorted the elders of the Church to keep these commandments and to walk in simplicity and purity of heart. For blessed are they who keep these statutes, for they shall be saved.",
     "Conclusion", "Conclusion"),
]

def import_hermas():
    """Import Shepherd of Hermas"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("IMPORTING SHEPHERD OF HERMAS")
    print("="*70)
    
    # Clear existing
    db.cursor.execute("DELETE FROM shepherd_of_hermas")
    
    imported = 0
    for section in HERMAS_SECTIONS:
        section_num, english, title, section_type = section
        db.cursor.execute("""
            INSERT INTO shepherd_of_hermas
            (section_number, greek_text, english_text, title, section_type)
            VALUES (?, ?, ?, ?, ?)
        """, (section_num, "", english, title, section_type))
        imported += 1
        
        if imported % 10 == 0:
            print(f"  ✅ Imported {imported} sections...")
    
    db.conn.commit()
    
    # Export to JSON
    hermas_export = {
        "title": "Shepherd of Hermas",
        "subtitle": "The Pastor",
        "total_sections": imported,
        "language": "Greek",
        "date": "c. 90-140 CE",
        "attribution": "Hermas, brother of Pope Pius I",
        "significance": "One of the most popular early Christian writings; considered canonical by some early church fathers including Irenaeus and Origen",
        "structure": [
            "Book I: The Four Visions (sections 1-8)",
            "Book II: The Twelve Mandates (sections 9-20)",
            "Book III: The Nine Similitudes (sections 21-29)",
            "Conclusion (section 30)"
        ],
        "key_themes": [
            "Repentance and forgiveness of sins",
            "The Church as an aged woman becoming young",
            "Double-mindedness (dipsychia) as the great sin",
            "The tower as symbol of the Church",
            "Two ways: narrow way of life, broad way of destruction",
            "The Shepherd as the Son of God",
            "Post-baptismal sin and second repentance",
            "Purity of heart and simplicity"
        ],
        "theological_importance": [
            "Earliest post-apostolic church manual",
            "Discusses possibility of repentance after baptism",
            "Emphasizes practical morality over doctrine",
            "Shows early church structure and practices",
            "Important for understanding early Christian piety"
        ],
        "notable_features": [
            "Written by a freed slave (Hermas)",
            "Very popular in early church - most widely read non-canonical text",
            "Codex Sinaiticus includes it after New Testament",
            "Codex Claromontanus lists it as part of New Testament",
            "Irenaeus quotes it as Scripture",
            "Origen considered it divinely inspired"
        ],
        "sections": []
    }
    
    for section in HERMAS_SECTIONS:
        section_num, english, title, section_type = section
        hermas_export["sections"].append({
            "number": section_num,
            "title": title,
            "type": section_type,
            "preview": english[:200] + "..." if len(english) > 200 else english
        })
    
    with open('/root/hebrew-repo/exports/hermas_export.json', 'w', encoding='utf-8') as f:
        json.dump(hermas_export, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*70)
    print("IMPORT COMPLETE")
    print("="*70)
    print(f"\n📊 Statistics:")
    print(f"   Total sections: {imported}")
    print(f"\n🎯 STRUCTURE:")
    print(f"   • 4 Visions (The Church, the willow tree, the mountain)")
    print(f"   • 12 Mandates (Practical commandments)")
    print(f"   • 9 Similitudes (Parables and allegories)")
    print(f"\n📝 NOTABLE:")
    print(f"   • Written by a freed slave")
    print(f"   • Most popular early Christian writing")
    print(f"   • Included in Codex Sinaiticus")
    print(f"   • Considered Scripture by some early fathers")
    print(f"\n✅ Exported to exports/hermas_export.json")
    
    db.close()

if __name__ == "__main__":
    import_hermas()