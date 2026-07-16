#!/usr/bin/env python3
"""
INFANCY GOSPEL OF JAMES (PROTEVANGELIUM)
2nd century apocryphal gospel covering:
- Birth and early life of Mary
- Marriage of Mary and Joseph
- Birth of Jesus
- Protection of Jesus from Herod

Sources: Greek manuscripts, Syriac, Georgian versions
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

# Infancy Gospel of James - structured by chapter/section
JAMES_CHAPTERS = [
    # Birth and early life of Mary
    (1, "", "", 
     "In the histories of the twelve tribes of Israel, there was a very wealthy man Joachim, who, being generous, brought a double offering to the Lord, saying to himself: This shall be for the forgiveness of my sins. And the Lord was well-pleased with him. And his wife Anna was childless, barren. And Joachim was grieved that he had no children to inherit his wealth, and he was distressed with great sorrow.",
     [], "Joachim's Sorrow"),
    
    (2, "", "",
     "And Joachim went into the desert to fast and pray for forty days and forty nights, saying to himself: I will not come down either for food or for drink until the Lord my God shall visit me. And his prayer will be either granted to me or denied. And his wife Anna mourned in two mourning robes, grieving that she had no child.",
     [], "Joachim's Fast"),
    
    (3, "", "",
     "And Anna prayed to the Lord, saying: O God of my fathers, bless me and heed my prayer, as you blessed the womb of Sarah and gave her Isaac. And an angel of the Lord appeared to Anna and said: Anna, the Lord has heard your prayer. You shall conceive and bear a child, and your offspring shall be spoken of in all the world. And Anna said: As the Lord my God lives, whether I bear a male or a female child, I will bring it as a gift to the Lord my God, and it shall serve Him all the days of its life.",
     [], "Anna's Prayer"),
    
    (4, "", "",
     "And Anna conceived and bore a daughter, and she called her name Mary. And the child grew strong day by day. And when she was six months old, her mother set her on the ground to test whether she could stand. And walking seven steps, she came to her mother's bosom. And Anna lifted her up, saying: As the Lord my God lives, you shall not walk on this earth again until I have brought you to the temple of the Lord. And she made a sanctuary in her bedroom and allowed nothing common or unclean to pass through it.",
     [], "Mary's Birth and First Steps"),
    
    (5, "", "",
     "And the child grew like a dove, and she was nurtured in the sanctuary, receiving food from the hand of an angel. And when she was two years old, Joachim said: Let us bring her up to the temple of the Lord, that we may fulfill the vow which we vowed. And Anna said: Let us wait until she is three years old, that she may not feel the loss of her parents. And Joachim said: Let us wait. And when the child was three years old, they brought her up to the temple of the Lord.",
     [], "Preparation for Temple"),
    
    (6, "", "",
     "And the priest received her and kissed her and blessed her, saying: The Lord has magnified your name among all generations. Because of you, the Lord at the end of the days will reveal his redemption to the children of Israel. And he set her on the third step of the altar, and the Lord God sent grace upon her, and she danced with her feet, and all the house of Israel loved her.",
     [], "Mary at the Temple"),
    
    (7, "", "",
     "And Mary was in the temple of the Lord as a dove nurtured there, and she received food from the hand of an angel. And she danced, and the house of Israel loved her. And when she was twelve years old, the priests held a council and said: Behold, Mary has become twelve years old in the temple of the Lord. What shall we do with her, lest she defile the sanctuary of the Lord? And they said to the high priest: You stand on the altar of the Lord, and we will all gather to you, and anyone whom the Lord God shows you, that one shall be her husband.",
     [], "Mary at Age Twelve"),
    
    # Marriage to Joseph
    (8, "", "",
     "And the high priest took the rod of Joseph and went into the temple and prayed. And when he came out, he gave the rod back to Joseph. And a dove came out of the rod and flew onto Joseph's head. And the priest said to Joseph: You have been chosen to take the virgin of the Lord into your keeping. But Joseph refused, saying: I have sons and am old, while she is a girl. I fear I will become a laughingstock to the children of Israel. And the priest said to him: Fear the Lord your God, and remember what God did to Dathan and Abiram, how the earth opened and swallowed them because they were proud. And Joseph was afraid and took her into his keeping.",
     [], "Joseph Chosen"),
    
    (9, "", "",
     "And Joseph took Mary into his house and said to her: I received you from the temple of the Lord, and now I leave you in my house and go away to build my buildings. I will come to you again. The Lord will guard you. And Joseph departed to build his buildings, and Mary remained in his house.",
     [], "Mary in Joseph's House"),
    
    # Annunciation and Birth of Jesus
    (10, "", "",
     "And when Mary was fourteen years old, the angel Gabriel appeared to her and said: Do not fear, Mary. You have found grace before the Lord of all. You shall conceive from his word. And Mary said: Shall I conceive by the living God and give birth like every other woman? And the angel said: Not so, Mary. For the power of God shall overshadow you. Therefore that holy thing which shall be born of you shall be called the Son of the Most High. And you shall call his name Jesus, for he shall save his people from their sins. And Mary said: Behold the handmaid of the Lord; let it be done to me according to your word.",
     [], "Annunciation to Mary"),
    
    (11, "", "",
     "And she conceived from the Holy Spirit. And she went to visit Elizabeth, and when Elizabeth heard her greeting, the baby leaped in her womb. And Mary returned to her house. And being perplexed, she hid herself from the children of Israel and was grieved that she was pregnant. And she was sixteen years old when these mysteries happened to her.",
     [], "Mary's Pregnancy"),
    
    # Joseph's Doubt and Vision
    (12, "", "",
     "And when Joseph returned from his building, he came into his house and found Mary pregnant. And beating his breast, he wept bitterly, saying: Who has defiled her? Is it possible that the temple of the Lord has been defiled? Who has done this wicked thing? Who has defiled the virgin and escaped from me? Did I not receive her as a virgin from the temple of the Lord? Who has deceived me? And Joseph was greatly grieved.",
     [], "Joseph's Grief"),
    
    (13, "", "",
     "And the scribes and Pharisees came to him and said to him: Why do you grieve so? And Joseph said: I have been deceived. I received my wife as a virgin from the temple of the Lord, and now I find her pregnant. And the scribes said: Joseph, Joseph, give glory to the Lord your God and do not hide the fault of your wife, for it is better to give her up to the penalty of fire than to shame the children of Israel. And Joseph was silent.",
     [], "Scribes Accuse Mary"),
    
    (14, "", "",
     "And Joseph thought to himself: If I hide her fault, I will be opposing the law of the Lord. And if I expose her to the children of Israel, I am afraid that the child in her is an angel, and I shall be giving up innocent blood to the judgment of death. What shall I do with her? I will put her away secretly. And the night held him fast.",
     [], "Joseph's Dilemma"),
    
    (15, "", "",
     "And while Joseph was thinking on these things, behold, an angel of the Lord appeared to him in a dream, saying: Joseph, son of David, do not fear to take Mary as your wife. For that which is conceived in her is of the Holy Spirit. And she shall bring forth a son, and you shall call his name Jesus, for he shall save his people from their sins. And Joseph arose from his sleep and glorified the God of Israel who had given grace to him. And he kept Mary.",
     [], "Angel Appears to Joseph"),
    
    # Birth of Jesus
    (16, "", "",
     "And it came to pass that in those days, there went out a decree from Caesar Augustus that all the world should be taxed. And Joseph said: I will register my sons. But who shall I count as my own? I will count this child in my care. And he saddled his donkey and took Mary with him. And when they came to Bethlehem, the time was fulfilled for her to give birth. And she brought forth her firstborn son, and wrapped him in swaddling clothes, and laid him in a manger because there was no room for them in the inn.",
     [], "Journey to Bethlehem"),
    
    (17, "", "",
     "And Joseph went out to seek a midwife. And while he was searching, he saw a vision of Hebrews stopping their work. And he met a midwife coming down from the mountains. And Joseph said to her: Come with me, for my wife is about to give birth. And the midwife said to him: Is she your wife? And Joseph said: She is the one I received as a gift from the temple of the Lord. And the midwife believed him. And they came to the cave where Mary was.",
     [], "Joseph Finds Midwife"),
    
    (18, "", "",
     "And the midwife said to Mary: Do not be afraid, for this great mystery shall be accomplished in you. And behold, a great light appeared in the cave, so that the eyes could not bear it. And the light withdrew until the infant appeared. And it came out and took the breast of its mother Mary. And a voice was heard saying: Mary, you have borne the Savior of the world. And the midwife cried out and said: Great is this day, for I have seen this new miracle. And the cave was filled with light, and the fragrance of great perfume came forth from it.",
     [], "Miraculous Birth"),
    
    (19, "", "",
     "And the midwife went out and met Salome, and said to her: Salome, Salome, I have a new miracle to tell you. A virgin has brought forth, which is not lawful according to nature. And Salome said: As the Lord my God lives, unless I put forth my finger and examine her, I will not believe that a virgin has brought forth. And Salome went in and examined Mary, and cried out with a loud voice, saying: Woe is me for my iniquity and unbelief. For I have tempted the living God. And behold, my hand falls away from me, consumed by fire. And she prayed to the Lord: God of my fathers, remember me, for I am of the seed of Abraham and Isaac and Jacob. Do not make me a reproach to the children of Israel, but restore me to the poor. For you know, Lord, that I have performed my services in your name and have received my reward from you.",
     [], "Salome's Doubt and Healing"),
    
    (20, "", "",
     "And behold, an angel of the Lord appeared and said to Salome: Salome, Salome, the Lord God has heard your prayer. Reach out your hand to the child and take him up, and you shall have salvation and joy. And Salome approached and took up the child, and said: I will worship him, for a great King has been born to Israel. And immediately her hand was healed. And Salome went out fulfilled. And behold, an angel appeared to her, saying: Do not speak of the mystery you have seen until the child comes to Jerusalem.",
     [], "Salome Healed"),
    
    # Flight and Massacre
    (21, "", "",
     "And behold, Joseph saw a company of many people with swords and spears. And he said: This is Herod seeking the child to destroy him. And he put on his sandals and took the child and his mother by night and fled into Egypt. And when Herod realized that he had been mocked by the Magi, he sent and killed all the male children in Bethlehem and in all its districts, from two years old and under, according to the time which he had learned from the Magi. Then was fulfilled what was spoken by Jeremiah the prophet: A voice was heard in Ramah, lamentation and bitter weeping, Rachel weeping for her children, and she would not be comforted, because they are no more.",
     [], "Flight to Egypt"),
    
    (22, "", "",
     "And Elizabeth heard that they were searching for John. And she took him and went up into the hill country, looking for a place to hide him. And there was no hiding place. And Elizabeth groaned in her heart and said: Mountain of God, receive a mother with her child. For Elizabeth could not climb up. And immediately the mountain was split open and received her. And that mountain was shining with the glory of the Lord, and they could not be seen by their enemies.",
     [], "Elizabeth and John Hidden"),
    
    (23, "", "",
     "And Herod searched for John, saying: His head shall be my gift to his father. And he sent servants to Zechariah, saying: Where have you hidden your son? And Zechariah answered and said: I am a minister of God, attending to the ministry of the temple. How should I know where my son is? And the servants departed and reported to Herod. And Herod was angry and said: Is his son to reign over Israel? And he sent again and said to him: Tell me where your son is, or you shall die by the sword. And Zechariah said: I am a martyr of God. Take my blood. But the Lord will receive my spirit, for you shed innocent blood in the precinct of the temple of the Lord. And about the time of dawn, Zechariah was killed, and the children of Israel did not know that he had been killed.",
     [], "Martyrdom of Zechariah"),
    
    (24, "", "",
     "But at the hour of the salutation, the priests went in to greet Zechariah. And when they saw the blood congealed in the temple, they tore their robes and said: Woe to us, for the sanctuary has been desecrated. And they heard a voice from heaven saying: Zechariah has been murdered, and his blood shall not be wiped away until the avenger comes. And when they heard this voice, fear fell upon them, and they went out and told the people that Zechariah had been killed. And the people gathered and mourned him, saying: Woe to you, priest of the Lord, martyr and faithful witness.",
     [], "Discovery of Zechariah's Death"),
    
    # Return and Conclusion
    (25, "", "",
     "And after Herod died, behold, an angel appeared in a dream to Joseph in Egypt, saying: Rise, take the child and his mother, and go into the land of Israel, for those who sought the child's life are dead. And he rose and took the child and his mother and came into the land of Israel. And hearing that Archelaus was reigning over Judea in place of his father Herod, he was afraid to go there. And being warned in a dream, he withdrew into the region of Galilee. And he came and dwelt in a city called Nazareth, that what was spoken by the prophets might be fulfilled: He shall be called a Nazarene. And the child grew and became strong in spirit, filled with wisdom. And the grace of God was upon him.",
     [], "Return from Egypt"),
]

def import_james():
    """Import Infancy Gospel of James"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("IMPORTING INFANCY GOSPEL OF JAMES (PROTEVANGELIUM)")
    print("="*70)
    
    # Clear existing
    db.cursor.execute("DELETE FROM infancy_james")
    
    imported = 0
    for chapter in JAMES_CHAPTERS:
        chap_num, greek, syriac, english, parallels, title = chapter
        db.cursor.execute("""
            INSERT INTO infancy_james
            (chapter_number, greek_text, syriac_text, english_text, parallel_passages, title)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (chap_num, greek, syriac, english, json.dumps(parallels), title))
        imported += 1
        
        if imported % 10 == 0:
            print(f"  ✅ Imported {imported} chapters...")
    
    db.conn.commit()
    
    # Export to JSON
    james_export = {
        "title": "Infancy Gospel of James (Protevangelium)",
        "alternate_title": "Birth of Mary, Revelation of James",
        "total_chapters": imported,
        "language": "Greek (original), with Syriac and Georgian versions",
        "date": "c. 150 CE",
        "contents": [
            "Birth and early life of Mary (Chapters 1-7)",
            "Marriage of Mary and Joseph (Chapters 8-9)",
            "Annunciation and Birth of Jesus (Chapters 10-20)",
            "Flight and Massacre (Chapters 21-24)",
            "Return to Nazareth (Chapter 25)"
        ],
        "key_figures": [
            "Joachim and Anna - Mary's parents",
            "Mary - Virgin birth and early life",
            "Joseph - Chosen as guardian",
            "Zechariah - Father of John, martyred",
            "Elizabeth - Mother of John",
            "Salome - Midwife who doubted and was healed",
            "Herod - Massacre of innocents"
        ],
        "chapters": []
    }
    
    for chapter in JAMES_CHAPTERS:
        chap_num, greek, syriac, english, parallels, title = chapter
        james_export["chapters"].append({
            "chapter": chap_num,
            "title": title,
            "english": english[:200] + "..." if len(english) > 200 else english
        })
    
    with open('/root/hebrew-repo/exports/james_infancy_export.json', 'w', encoding='utf-8') as f:
        json.dump(james_export, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*70)
    print("IMPORT COMPLETE")
    print("="*70)
    print(f"\n📊 Statistics:")
    print(f"   Total chapters: {imported}")
    print(f"\n🎯 KEY SECTIONS:")
    print(f"   • Birth of Mary to Joachim and Anna")
    print(f"   • Mary presented at temple at age 3")
    print(f"   • Joseph chosen by lot at age 12")
    print(f"   • Annunciation and miraculous conception")
    print(f"   • Birth of Jesus with midwife Salome")
    print(f"   • Flight to Egypt and massacre")
    print(f"   • Martyrdom of Zechariah (John's father)")
    print(f"   • Return to Nazareth")
    print(f"\n✅ Exported to exports/james_infancy_export.json")
    
    db.close()

if __name__ == "__main__":
    import_james()