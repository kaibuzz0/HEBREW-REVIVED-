#!/usr/bin/env python3
"""
PHASE 3: MAJOR PROPHETS & HISTORICAL BOOKS
Jeremiah, Ezekiel, Joshua, Judges, Samuel, Kings
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

# JEREMIAH - Selected chapters
JEREMIAH = [
    (1, "The words of Jeremiah, the son of Hilkiah, one of the priests who were in Anathoth in the land of Benjamin... Now the word of the LORD came to me, saying, Before I formed you in the womb I knew you, and before you were born I consecrated you; I appointed you a prophet to the nations.", "Call of Jeremiah"),
    (7, "The word that came to Jeremiah from the LORD: Stand in the gate of the LORD's house, and proclaim there this word... Thus says the LORD of hosts, the God of Israel: Amend your ways and your deeds, and I will let you dwell in this place.", "Temple Sermon"),
    (17, "Thus says the LORD: Cursed is the man who trusts in man and makes flesh his strength, whose heart turns away from the LORD... The heart is deceitful above all things, and desperately sick; who can understand it? I the LORD search the heart and test the mind, to give every man according to his ways, according to the fruit of his deeds.", "Heart Deceitful"),
    (23, "Woe to the shepherds who destroy and scatter the sheep of my pasture! declares the LORD. Therefore thus says the LORD, the God of Israel, concerning the shepherds who care for my people: You have scattered my flock and have driven them away, and you have not attended to them. Behold, I will attend to you for your evil deeds, declares the LORD.", "Righteous Branch"),
    (29, "These are the words of the letter that Jeremiah the prophet sent from Jerusalem to the surviving elders of the exiles... For thus says the LORD: When seventy years are completed for Babylon, I will visit you, and I will fulfill to you my promise and bring you back to this place. For I know the plans I have for you, declares the LORD, plans for welfare and not for evil, to give you a future and a hope.", "Letter to Exiles"),
    (31, "Behold, the days are coming, declares the LORD, when I will make a new covenant with the house of Israel and the house of Judah... For this is the covenant that I will make with the house of Israel after those days, declares the LORD: I will put my law within them, and I will write it on their hearts. And I will be their God, and they shall be my people.", "New Covenant"),
    (33, "Behold, the days are coming, declares the LORD, when I will fulfill the promise I made to the house of Israel and the house of Judah. In those days and at that time I will cause a righteous Branch to spring up for David, and he shall execute justice and righteousness in the land.", "Righteous Branch"),
]

# EZEKIEL - Selected chapters
EZEKIEL = [
    (1, "In the thirtieth year, in the fourth month, on the fifth day of the month, as I was among the exiles by the Chebar canal, the heavens were opened, and I saw visions of God... As for the likeness of the living creatures, their appearance was like burning coals of fire, like the appearance of torches moving to and fro among the living creatures.", "Vision of Glory"),
    (2, "And he said to me, Son of man, stand on your feet, and I will speak with you. And as he spoke to me, the Spirit entered into me and set me on my feet... And he said to me, Son of man, I send you to the people of Israel, to nations of rebels, who have rebelled against me.", "Call of Ezekiel"),
    (3, "And he said to me, Son of man, eat whatever you find here. Eat this scroll, and go, speak to the house of Israel. So I opened my mouth, and he gave me this scroll to eat. And he said to me, Son of man, feed your belly with this scroll that I give you and fill your stomach with it. Then I ate it, and it was in my mouth as sweet as honey.", "Eat the Scroll"),
    (36, "Therefore say to the house of Israel, Thus says the Lord GOD: It is not for your sake, O house of Israel, that I am about to act, but for the sake of my holy name... And I will give you a new heart, and a new spirit I will put within you. And I will remove the heart of stone from your flesh and give you a heart of flesh.", "New Heart"),
    (37, "The hand of the LORD was upon me, and he brought me out in the Spirit of the LORD and set me down in the middle of the valley; it was full of bones... Then he said to me, Son of man, these bones are the whole house of Israel. Behold, they say, Our bones are dried up, and our hope is lost; we are indeed cut off. Therefore prophesy, and say to them, Thus says the Lord GOD: Behold, I will open your graves and raise you from your graves, O my people.", "Valley of Dry Bones"),
]

# JOSHUA - Selected chapters
JOSHUA = [
    (1, "After the death of Moses the servant of the LORD, the LORD said to Joshua the son of Nun, Moses' assistant, Moses my servant is dead. Now therefore arise, go over this Jordan, you and all this people, into the land that I am giving to them, to the people of Israel... Have I not commanded you? Be strong and courageous. Do not be frightened, and do not be dismayed, for the LORD your God is with you wherever you go.", "Be Strong and Courageous"),
    (3, "Then Joshua rose early in the morning and they set out from Shittim. And they came to the Jordan, he and all the people of Israel, and lodged there before they passed over... And when the soles of the feet of the priests bearing the ark of the LORD, the Lord of all the earth, shall rest in the waters of the Jordan, the waters of the Jordan shall be cut off from flowing, and the waters coming down from above shall stand in one heap.", "Crossing Jordan"),
    (6, "Now Jericho was shut up inside and outside because of the people of Israel. None went out, and none came in. And the LORD said to Joshua, See, I have given Jericho into your hand, with its king and mighty men of valor... So the people shouted, and the trumpets were blown. As soon as the people heard the sound of the trumpet, the people shouted a great shout, and the wall fell down flat.", "Fall of Jericho"),
    (24, "Joshua gathered all the tribes of Israel to Shechem and summoned the elders, the heads, the judges, and the officers of Israel... And if it is evil in your eyes to serve the LORD, choose this day whom you will serve, whether the gods your fathers served in the region beyond the River, or the gods of the Amorites in whose land you dwell. But as for me and my house, we will serve the LORD.", "Choose This Day"),
]

# JUDGES - Selected chapters
JUDGES = [
    (2, "And the people of Israel did what was evil in the sight of the LORD and served the Baals. And they abandoned the LORD, the God of their fathers... Whenever the LORD raised up judges for them, the LORD was with the judge, and he saved them from the hand of their enemies all the days of the judge.", "Cycle of Sin"),
    (4, "And the people of Israel again did what was evil in the sight of the LORD... And Deborah said to Barak, Up! For this is the day in which the LORD has given Sisera into your hand. Does not the LORD go out before you?", "Deborah and Barak"),
    (6, "And the angel of the LORD appeared to him and said to him, The LORD is with you, O mighty man of valor. And Gideon said to him, Please, my lord, if the LORD is with us, why then has all this happened to us?", "Gideon's Call"),
    (7, "Then Jerubbaal (that is, Gideon) and all the people who were with him rose early and encamped beside the spring of Harod... And the LORD said to Gideon, The people with you are too many for me to give the Midianites into their hand, lest Israel boast over me saying, My own hand has saved me.", "Gideon's 300"),
    (13, "And the woman bore a son and called his name Samson. And the young man grew, and the LORD blessed him. And the Spirit of the LORD began to stir him in Mahaneh-dan, between Zorah and Eshtaol.", "Samson's Birth"),
    (16, "And Samson called to the LORD and said, O Lord GOD, please remember me and please strengthen me only this once, O God, that I may be avenged on the Philistines for my two eyes. And Samson grasped the two middle pillars on which the house rested, and he leaned his weight against them, his right hand on the one and his left hand on the other.", "Samson's Death"),
]

# 1 SAMUEL - Selected chapters
SAMUEL_1 = [
    (1, "There was a certain man of Ramathaim-zophim of the hill country of Ephraim whose name was Elkanah... She was deeply distressed and prayed to the LORD and wept bitterly. And she vowed a vow and said, O LORD of hosts, if you will indeed look on the affliction of your servant and remember me and not forget your servant, but will give to your servant a son, then I will give him to the LORD all the days of his life.", "Hannah's Prayer"),
    (3, "And the boy Samuel was ministering to the LORD in the presence of Eli... And the LORD came and stood, calling as at other times, Samuel! Samuel! And Samuel said, Speak, for your servant hears. Then the LORD said to Samuel, Behold, I am about to do a thing in Israel at which the two ears of everyone who hears it will tingle.", "Call of Samuel"),
    (8, "So all the elders of Israel gathered together and came to Samuel at Ramah and said to him, Behold, you are old and your sons do not walk in your ways. Now appoint for us a king to judge us like all the nations... But the people refused to obey the voice of Samuel. And they said, No! But there shall be a king over us.", "Israel Demands a King"),
    (13, "Samuel said to Saul, You have done foolishly. You have not kept the command of the LORD your God, with which he commanded you. For then the LORD would have established your kingdom over Israel forever. But now your kingdom shall not continue. The LORD has sought out a man after his own heart, and the LORD has commanded him to be prince over his people.", "Saul Rejected"),
    (16, "And the LORD said to Samuel, How long will you grieve over Saul, since I have rejected him from being king over Israel? Fill your horn with oil, and go. I will send you to Jesse the Bethlehemite, for I have provided for myself a king among his sons... Then Samuel took the horn of oil and anointed him in the midst of his brothers. And the Spirit of the LORD rushed upon David from that day forward.", "David Anointed"),
    (17, "Then David said to the Philistine, You come to me with a sword and with a spear and with a javelin, but I come to you in the name of the LORD of hosts, the God of the armies of Israel, whom you have defied... So David prevailed over the Philistine with a sling and with a stone, and struck the Philistine and killed him.", "David and Goliath"),
]

# 2 SAMUEL - Selected chapters
SAMUEL_2 = [
    (5, "Then all the tribes of Israel came to David at Hebron and said, Behold, we are your bone and flesh... And the LORD said to you, You shall be shepherd of my people Israel, and you shall be prince over Israel. So all the elders of Israel came to the king at Hebron, and King David made a covenant with them at Hebron before the LORD. And they anointed David king over Israel.", "David Becomes King"),
    (7, "Now when the king lived in his house and the LORD had given him rest from all his surrounding enemies, the king said to Nathan the prophet, See now, I dwell in a house of cedar, but the ark of God dwells in a tent... When your days are fulfilled and you lie down with your fathers, I will raise up your offspring after you, who shall come from your body, and I will establish his kingdom. He shall build a house for my name, and I will establish the throne of his kingdom forever.", "Davidic Covenant"),
    (11, "In the spring of the year, the time when kings go out to battle, David sent Joab, and his servants with him, and all Israel... One evening David arose from his couch and was walking on the roof of the king's house, and he saw from the roof a woman bathing; and the woman was very beautiful.", "David and Bathsheba"),
    (12, "And the LORD sent Nathan to David. He came to him and said to him, There were two men in a certain city, the one rich and the other poor... Nathan said to David, You are the man! Thus says the LORD, the God of Israel, I anointed you king over Israel, and I delivered you out of the hand of Saul.", "Nathan Confronts David"),
]

# 1 KINGS - Selected chapters
KINGS_1 = [
    (1, "Now King David was old and advanced in years. And although they covered him with clothes, he could not get warm... So Bathsheba went to King Solomon to speak to him on behalf of Adonijah. And the king rose to meet her and bowed down to her. Then he sat on his throne and had a seat brought for the king's mother. And she sat on his right.", "Solomon Becomes King"),
    (3, "And Solomon loved the LORD, walking in the statutes of David his father, only he sacrificed and made offerings at the high places... At Gibeon the LORD appeared to Solomon in a dream by night, and God said, Ask what I shall give you. And Solomon said, You have shown great and steadfast love to your servant David my father... Give your servant therefore an understanding mind to govern your people, that I may discern between good and evil.", "Solomon's Wisdom"),
    (8, "Then Solomon assembled the elders of Israel and all the heads of the tribes, the leaders of the fathers' houses of the people of Israel, before King Solomon in Jerusalem, to bring up the ark of the covenant of the LORD out of the city of David, which is Zion... But will God indeed dwell on the earth? Behold, heaven and the highest heaven cannot contain you; how much less this house that I have built!", "Temple Dedication"),
    (17, "Now Elijah the Tishbite, of Tishbe in Gilead, said to Ahab, As the LORD, the God of Israel, lives, before whom I stand, there shall be neither dew nor rain these years, except by my word... And the word of the LORD came to him: Depart from here and turn eastward and hide yourself by the brook Cherith, which is east of the Jordan.", "Elijah and the Drought"),
    (18, "And at the time of the offering of the oblation, Elijah the prophet came near and said, O LORD, God of Abraham, Isaac, and Israel, let it be known this day that you are God in Israel, and that I am your servant, and that I have done all these things at your word. Answer me, O LORD, answer me, that this people may know that you, O LORD, are God, and that you have turned their hearts back.", "Mt Carmel"),
    (19, "And he lay down and slept under a broom tree. And behold, an angel touched him and said to him, Arise and eat... And behold, the LORD passed by, and a great and strong wind tore the mountains and broke in pieces the rocks before the LORD, but the LORD was not in the wind. And after the wind an earthquake, but the LORD was not in the earthquake.", "Still Small Voice"),
]

# 2 KINGS - Selected chapters
KINGS_2 = [
    (2, "Now when the LORD was about to take Elijah up to heaven by a whirlwind, Elijah and Elisha were on their way from Gilgal... And as they still went on and talked, behold, a chariot of fire and horses of fire separated the two of them. And Elijah went up by a whirlwind into heaven.", "Elijah Taken Up"),
    (4, "One day Elisha went on to Shunem, where a wealthy woman lived, who urged him to eat some food... When Elisha came into the house, he saw the child lying dead on his bed. So he went in and shut the door behind the two of them and prayed to the LORD.", "Elisha's Miracles"),
    (17, "Therefore the LORD was very angry with Israel and removed them out of his sight. None was left but the tribe of Judah only... And the LORD rejected all the descendants of Israel and afflicted them and gave them into the hand of plunderers, until he had cast them out of his sight.", "Fall of Israel"),
    (25, "And in the ninth year of his reign, in the tenth month, on the tenth day of the month, Nebuchadnezzar king of Babylon came with all his army against Jerusalem and laid siege to it... And Jehoiachin king of Judah came out to the king of Babylon, with his mother and his servants and his officials and his palace officials. The king of Babylon took him prisoner in the eighth year of his reign.", "Fall of Jerusalem"),
]

def import_phase3():
    """Import Phase 3: Major Prophets and Historical Books"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("IMPORTING PHASE 3: MAJOR PROPHETS & HISTORICAL BOOKS")
    print("="*70)
    
    # Create tables
    tables = [
        ("book_of_jeremiah", "Jeremiah"),
        ("book_of_ezekiel", "Ezekiel"),
        ("book_of_joshua", "Joshua"),
        ("book_of_judges", "Judges"),
        ("book_of_first_samuel", "1 Samuel"),
        ("book_of_second_samuel", "2 Samuel"),
        ("book_of_first_kings", "1 Kings"),
        ("book_of_second_kings", "2 Kings"),
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
    
    # Import all data
    imports = [
        ("book_of_jeremiah", JEREMIAH),
        ("book_of_ezekiel", EZEKIEL),
        ("book_of_joshua", JOSHUA),
        ("book_of_judges", JUDGES),
        ("book_of_first_samuel", SAMUEL_1),
        ("book_of_second_samuel", SAMUEL_2),
        ("book_of_first_kings", KINGS_1),
        ("book_of_second_kings", KINGS_2),
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
        "phase": "Phase 3",
        "total_entries": total,
        "books": [
            {"book": "Jeremiah", "count": len(JEREMIAH)},
            {"book": "Ezekiel", "count": len(EZEKIEL)},
            {"book": "Joshua", "count": len(JOSHUA)},
            {"book": "Judges", "count": len(JUDGES)},
            {"book": "1 Samuel", "count": len(SAMUEL_1)},
            {"book": "2 Samuel", "count": len(SAMUEL_2)},
            {"book": "1 Kings", "count": len(KINGS_1)},
            {"book": "2 Kings", "count": len(KINGS_2)},
        ]
    }
    
    with open('/root/hebrew-repo/exports/phase3_canonical_export.json', 'w') as f:
        json.dump(export, f, indent=2)
    
    print("\n" + "="*70)
    print("PHASE 3 COMPLETE")
    print("="*70)
    print(f"\n📊 IMPORTED: {total} chapters")
    print(f"\n📚 BOOKS:")
    print(f"   Prophets: Jeremiah ({len(JEREMIAH)}), Ezekiel ({len(EZEKIEL)})")
    print(f"   Historical: Joshua ({len(JOSHUA)}), Judges ({len(JUDGES)})")
    print(f"   Kingdom: 1 Samuel ({len(SAMUEL_1)}), 2 Samuel ({len(SAMUEL_2)})")
    print(f"             1 Kings ({len(KINGS_1)}), 2 Kings ({len(KINGS_2)})")
    print(f"\n📁 Exported to exports/phase3_canonical_export.json")
    
    db.close()

if __name__ == "__main__":
    import_phase3()