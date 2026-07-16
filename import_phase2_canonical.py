#!/usr/bin/env python3
"""
PHASE 2: MORE CANONICAL BOOKS
Matthew, Mark, Luke, Acts, Major Epistles, Major Prophets
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

# MATTHEW - Selected chapters
MATTHEW = [
    (1, "The book of the genealogy of Jesus Christ, the son of David, the son of Abraham. Abraham was the father of Isaac, and Isaac the father of Jacob, and Jacob the father of Judah and his brothers... So all the generations from Abraham to David were fourteen generations, and from David to the deportation to Babylon fourteen generations, and from the deportation to Babylon to the Christ fourteen generations. Now the birth of Jesus Christ took place in this way. When his mother Mary had been betrothed to Joseph, before they came together she was found to be with child from the Holy Spirit.", "Genealogy, Birth"),
    (2, "Now after Jesus was born in Bethlehem of Judea in the days of Herod the king, behold, wise men from the east came to Jerusalem, saying, Where is he who has been born king of the Jews? For we saw his star when it rose and have come to worship him.", "Wise Men"),
    (3, "In those days John the Baptist came preaching in the wilderness of Judea, Repent, for the kingdom of heaven is at hand. For this is he who was spoken of by the prophet Isaiah: The voice of one crying in the wilderness: Prepare the way of the Lord; make his paths straight.", "John the Baptist"),
    (4, "Then Jesus was led up by the Spirit into the wilderness to be tempted by the devil. And after fasting forty days and forty nights, he was hungry. And the tempter came and said to him, If you are the Son of God, command these stones to become loaves of bread.", "Temptation"),
    (5, "Seeing the crowds, he went up on the mountain, and when he sat down, his disciples came to him. And he opened his mouth and taught them, saying: Blessed are the poor in spirit, for theirs is the kingdom of heaven. Blessed are those who mourn, for they shall be comforted. Blessed are the meek, for they shall inherit the earth.", "Sermon on the Mount"),
    (6, "Beware of practicing your righteousness before other people in order to be seen by them, for then you will have no reward from your Father who is in heaven. Thus, when you give to the needy, sound no trumpet before you, as the hypocrites do in the synagogues and in the streets, that they may be praised by others.", "Lord's Prayer, Giving"),
    (7, "Judge not, that you be not judged. For with the judgment you pronounce you will be judged, and with the measure you use it will be measured to you. Why do you see the speck that is in your brother's eye, but do not notice the log that is in your own eye? Ask, and it will be given to you; seek, and you will find; knock, and it will be opened to you. So whatever you wish that others would do to you, do also to them, for this is the Law and the Prophets.", "Golden Rule"),
    (13, "That same day Jesus went out of the house and sat beside the sea. And great crowds gathered about him, so that he got into a boat and sat down. And the whole crowd stood on the beach. And he told them many things in parables, saying: A sower went out to sow. And as he sowed, some seeds fell along the path, and the birds came and devoured them. Other seeds fell on rocky ground, where they did not have much soil, and immediately they sprang up... Other seeds fell among thorns, and the thorns grew up and choked them. Other seeds fell on good soil and produced grain, some a hundredfold, some sixty, some thirty.", "Parable of Sower"),
    (16, "Now when Jesus came into the district of Caesarea Philippi, he asked his disciples, Who do people say that the Son of Man is? And they said, Some say John the Baptist, others say Elijah, and others Jeremiah or one of the prophets. He said to them, But who do you say that I am? Simon Peter replied, You are the Christ, the Son of the living God.", "Peter's Confession"),
    (22, "But when the Pharisees heard that he had silenced the Sadducees, they gathered together. And one of them, a lawyer, asked him a question to test him. Teacher, which is the great commandment in the Law? And he said to him, You shall love the Lord your God with all your heart and with all your soul and with all your mind. This is the great and first commandment. And a second is like it: You shall love your neighbor as yourself. On these two commandments depend all the Law and the Prophets.", "Great Commandment"),
    (24, "Jesus left the temple and was going away, when his disciples came to point out to him the buildings of the temple. But he answered them, You see all these, do you not? Truly, I say to you, there will not be left here one stone upon another that will not be thrown down... For many will come in my name, saying, I am the Christ, and they will lead many astray. And you will hear of wars and rumors of wars. See that you are not alarmed, for this must take place, but the end is not yet.", "Olivet Discourse"),
    (25, "Then the kingdom of heaven will be like ten virgins who took their lamps and went to meet the bridegroom. Five of them were foolish, and five were wise. For when the foolish took their lamps, they took no oil with them, but the wise took flasks of oil with their lamps... Watch therefore, for you know neither the day nor the hour.", "Parables of Watchfulness"),
    (26, "Now as they were eating, Jesus took bread, and after blessing it broke it and gave it to the disciples, and said, Take, eat; this is my body. And he took a cup, and when he had given thanks he gave it to them, saying, Drink of it, all of you, for this is my blood of the covenant, which is poured out for many for the forgiveness of sins.", "Last Supper"),
    (28, "Now after the Sabbath, toward the dawn of the first day of the week, Mary Magdalene and the other Mary went to see the tomb. And behold, there was a great earthquake, for an angel of the Lord descended from heaven and came and rolled back the stone and sat on it... And Jesus came and said to them, All authority in heaven and on earth has been given to me. Go therefore and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit, teaching them to observe all that I have commanded you. And behold, I am with you always, to the end of the age.", "Resurrection, Great Commission"),
]

# MARK - Selected chapters (shortest gospel)
MARK = [
    (1, "The beginning of the gospel of Jesus Christ, the Son of God. As it is written in Isaiah the prophet: Behold, I send my messenger before your face, who will prepare your way, the voice of one crying in the wilderness: Prepare the way of the Lord, make his paths straight... Now John was clothed with camel's hair and wore a leather belt around his waist and ate locusts and wild honey.", "Beginning, John the Baptist"),
    (4, "Again he began to teach beside the sea. And a very large crowd gathered about him, so that he got into a boat and sat in it on the sea, and the whole crowd was beside the sea on the land. And he was teaching them many things in parables, and in his teaching he said to them: Listen! A sower went out to sow.", "Parable of Sower"),
    (8, "And he asked them, But who do you say that I am? Peter answered him, You are the Christ. And he strictly charged them to tell no one about him. And he began to teach them that the Son of Man must suffer many things and be rejected by the elders and the chief priests and the scribes and be killed, and after three days rise again.", "Peter's Confession"),
    (9, "And after six days Jesus took with him Peter and James and John, and led them up a high mountain by themselves. And he was transfigured before them, and his clothes became radiant, intensely white, as no one on earth could bleach them.", "Transfiguration"),
    (10, "And as Jesus was setting out on his journey, a man ran up and knelt before him and asked him, Good Teacher, what must I do to inherit eternal life? And Jesus said to him, Why do you call me good? No one is good except God alone.", "Rich Young Ruler"),
    (12, "And one of the scribes came up and heard them disputing with one another, and seeing that he answered them well, asked him, Which commandment is the most important of all? Jesus answered, The most important is, Hear, O Israel: The Lord our God, the Lord is one. And you shall love the Lord your God with all your heart and with all your soul and with all your mind and with all your strength. The second is this: You shall love your neighbor as yourself. There is no other commandment greater than these.", "Great Commandment"),
    (13, "And as he came out of the temple, one of his disciples said to him, Look, Teacher, what wonderful stones and what wonderful buildings! And Jesus said to him, Do you see these great buildings? There will not be left here one stone upon another that will not be thrown down.", "Olivet Discourse"),
    (14, "And as they were eating, he took bread, and after blessing it broke it and gave it to them, and said, Take; this is my body. And he took a cup, and when he had given thanks he gave it to them, and they all drank of it. And he said to them, This is my blood of the covenant, which is poured out for many.", "Last Supper"),
    (15, "And they crucified him and divided his garments among them, casting lots for them, to decide what each should take. And it was the third hour when they crucified him. And the inscription of the charge against him read, The King of the Jews.", "Crucifixion"),
    (16, "When the Sabbath was past, Mary Magdalene, Mary the mother of James, and Salome bought spices, so that they might go and anoint him. And very early on the first day of the week, when the sun had risen, they went to the tomb. And they were saying to one another, Who will roll away the stone for us from the entrance of the tomb? And looking up, they saw that the stone had been rolled back - it was very large.", "Resurrection"),
]

# LUKE - Selected chapters
LUKE = [
    (1, "Inasmuch as many have undertaken to compile a narrative of the things that have been accomplished among us, just as those who from the beginning were eyewitnesses and ministers of the word have delivered them to us, it seemed good to me also, having followed all things closely for some time past, to write an orderly account for you, most excellent Theophilus... And the angel said to her, Do not be afraid, Mary, for you have found favor with God. And behold, you will conceive in your womb and bear a son, and you shall call his name Jesus.", "Introduction, Annunciation"),
    (2, "In those days a decree went out from Caesar Augustus that all the world should be registered. This was the first registration when Quirinius was governor of Syria. And all went to be registered, each to his own town. And Joseph also went up from Galilee, from the town of Nazareth, to Judea, to the city of David, which is called Bethlehem, because he was of the house and lineage of David... And the angel said to them, Fear not, for behold, I bring you good news of great joy that will be for all the people. For unto you is born this day in the city of David a Savior, who is Christ the Lord.", "Birth of Jesus"),
    (4, "And Jesus returned in the power of the Spirit to Galilee, and a report about him went out through all the surrounding country. And he taught in their synagogues, being glorified by all. And he came to Nazareth, where he had been brought up. And as was his custom, he went to the synagogue on the Sabbath day, and he stood up to read. And the scroll of the prophet Isaiah was given to him. He unrolled the scroll and found the place where it was written: The Spirit of the Lord is upon me, because he has anointed me to proclaim good news to the poor.", "Jesus in Nazareth"),
    (6, "On a Sabbath, while he was going through the grainfields, his disciples plucked and ate some heads of grain, rubbing them in their hands. But some of the Pharisees said, Why are you doing what is not lawful to do on the Sabbath?... And he lifted up his eyes on his disciples, and said: Blessed are you who are poor, for yours is the kingdom of God. Blessed are you who are hungry now, for you shall be satisfied. Blessed are you who weep now, for you shall laugh.", "Beatitudes"),
    (10, "After this the Lord appointed seventy-two others and sent them on ahead of him, two by two, into every town and place where he himself was about to go... The seventy-two returned with joy, saying, Lord, even the demons are subject to us in your name! And he said to them, I saw Satan fall like lightning from heaven. Behold, I have given you authority to tread on serpents and scorpions, and over all the power of the enemy, and nothing shall hurt you.", "Seventy-two Disciples"),
    (15, "Now the tax collectors and sinners were all drawing near to hear him. And the Pharisees and the scribes grumbled, saying, This man receives sinners and eats with them. So he told them this parable: What man of you, having a hundred sheep, if he has lost one of them, does not leave the ninety-nine in the open country, and go after the one that is lost, until he finds it? And when he has found it, he lays it on his shoulders, rejoicing.", "Lost Sheep, Prodigal Son"),
    (17, "And he said to his disciples, Temptations to sin are sure to come, but woe to the one through whom they come! It would be better for him if a millstone were hung around his neck and he were cast into the sea than that he should cause one of these little ones to sin.", "Forgiveness, Faith"),
    (19, "He entered Jericho and was passing through. And behold, there was a man named Zacchaeus. He was a chief tax collector and was rich. And he was seeking to see who Jesus was, but on account of the crowd he could not, because he was small in stature. So he ran on ahead and climbed up into a sycamore tree to see him, for he was about to pass that way.", "Zacchaeus"),
    (22, "And when the hour came, he reclined at table, and the apostles with him. And he said to them, I have earnestly desired to eat this Passover with you before I suffer. For I tell you I will not eat it until it is fulfilled in the kingdom of God. And he took a cup, and when he had given thanks he said, Take this, and divide it among yourselves. For I tell you that from now on I will not drink of the fruit of the vine until the kingdom of God comes. And he took bread, and when he had given thanks, he broke it and gave it to them, saying, This is my body, which is given for you. Do this in remembrance of me.", "Last Supper"),
    (23, "And when they came to the place that is called The Skull, there they crucified him, and the criminals, one on his right and one on his left. And Jesus said, Father, forgive them, for they know not what they do... It was now about the sixth hour, and there was darkness over the whole land until the ninth hour, while the sun's light failed. And the curtain of the temple was torn in two. Then Jesus, calling out with a loud voice, said, Father, into your hands I commit my spirit! And having said this he breathed his last.", "Crucifixion"),
    (24, "But on the first day of the week, at early dawn, they went to the tomb, taking the spices they had prepared. And they found the stone rolled away from the tomb, but when they went in they did not find the body of the Lord Jesus... And he said to them, Thus it is written, that the Christ should suffer and on the third day rise from the dead, and that repentance and forgiveness of sins should be proclaimed in his name to all nations, beginning from Jerusalem. You are witnesses of these things.", "Resurrection, Emmaus"),
]

# ACTS - Selected chapters
ACTS = [
    (1, "In the first book, O Theophilus, I have dealt with all that Jesus began to do and teach, until the day when he was taken up, after he had given commands through the Holy Spirit to the apostles whom he had chosen. He presented himself alive to them after his suffering by many proofs, appearing to them during forty days and speaking about the kingdom of God... So when they had come together, they asked him, Lord, will you at this time restore the kingdom to Israel? He said to them, It is not for you to know times or seasons that the Father has fixed by his own authority. But you will receive power when the Holy Spirit has come upon you, and you will be my witnesses in Jerusalem and in all Judea and Samaria, and to the end of the earth.", "Ascension, Promise"),
    (2, "When the day of Pentecost arrived, they were all together in one place. And suddenly there came from heaven a sound like a mighty rushing wind, and it filled the entire house where they were sitting. And divided tongues as of fire appeared to them and rested on each one of them. And they were all filled with the Holy Spirit and began to speak in other tongues as the Spirit gave them utterance... Now when they heard this they were cut to the heart, and said to Peter and the rest of the apostles, Brothers, what shall we do? And Peter said to them, Repent and be baptized every one of you in the name of Jesus Christ for the forgiveness of your sins, and you will receive the gift of the Holy Spirit.", "Pentecost"),
    (4, "And as they were speaking to the people, the priests and the captain of the temple and the Sadducees came upon them, greatly annoyed because they were teaching the people and proclaiming in Jesus the resurrection from the dead. And they arrested them and put them in custody until the next day, for it was already evening.", "Peter and John Arrested"),
    (6, "Now in these days when the disciples were increasing in number, a complaint by the Hellenists arose against the Hebrews because their widows were being neglected in the daily distribution. And the twelve summoned the full number of the disciples and said, It is not right that we should give up preaching the word of God to serve tables. Therefore, brothers, pick out from among you seven men of good repute, full of the Spirit and of wisdom, whom we will appoint to this duty.", "Seven Chosen"),
    (7, "And Stephen said: Brothers and fathers, hear me. The God of glory appeared to our father Abraham when he was in Mesopotamia, before he lived in Haran... You stiff-necked people, uncircumcised in heart and ears, you always resist the Holy Spirit. As your fathers did, so do you. Which of the prophets did your fathers not persecute? And they killed those who announced beforehand the coming of the Righteous One, whom you have now betrayed and murdered.", "Stephen's Speech"),
    (9, "But Saul, still breathing threats and murder against the disciples of the Lord, went to the high priest and asked him for letters to the synagogues at Damascus, so that if he found any belonging to the Way, men or women, he might bring them bound to Jerusalem. Now as he went on his way, he approached Damascus, and suddenly a light from heaven shone around him. And falling to the ground he heard a voice saying to him, Saul, Saul, why are you persecuting me?", "Conversion of Saul"),
    (10, "At Caesarea there was a man named Cornelius, a centurion of what was known as the Italian Cohort, a devout man who feared God with all his household... And Peter said to them, You yourselves know how unlawful it is for a Jew to associate with or to visit anyone of another nation, but God has shown me that I should not call any person common or unclean.", "Cornelius"),
    (16, "And they went through the region of Phrygia and Galatia, having been forbidden by the Holy Spirit to speak the word in Asia. And when they had come up to Mysia, they attempted to go into Bithynia, but the Spirit of Jesus did not allow them. So, passing by Mysia, they went down to Troas. And a vision appeared to Paul in the night: a man of Macedonia was standing there, urging him and saying, Come over to Macedonia and help us.", "Macedonian Call"),
    (17, "Now when they had passed through Amphipolis and Apollonia, they came to Thessalonica, where there was a synagogue of the Jews. And Paul went in, as was his custom, and on three Sabbath days he reasoned with them from the Scriptures, explaining and proving that it was necessary for the Christ to suffer and to rise from the dead, and saying, This Jesus, whom I proclaim to you, is the Christ.", "Thessalonica, Berea"),
    (28, "When they had appointed a day for him, they came to him at his lodging in greater numbers. From morning till evening he expounded to them, testifying to the kingdom of God and trying to convince them about Jesus both from the Law of Moses and from the Prophets. Some were convinced by what he said, but others disbelieved... He lived there two whole years at his own expense, and welcomed all who came to him, proclaiming the kingdom of God and teaching about the Lord Jesus Christ with all boldness and without hindrance.", "Rome"),
]

# ROMANS - Selected chapters
ROMANS = [
    (1, "Paul, a servant of Christ Jesus, called to be an apostle, set apart for the gospel of God... For I am not ashamed of the gospel, for it is the power of God for salvation to everyone who believes, to the Jew first and also to the Greek. For in it the righteousness of God is revealed from faith for faith, as it is written, The righteous shall live by faith.", "Introduction, Gospel Power"),
    (3, "Then what advantage has the Jew? Or what is the value of circumcision? Much in every way. To begin with, the Jews were entrusted with the oracles of God... For by works of the law no human being will be justified in his sight, since through the law comes knowledge of sin. But now the righteousness of God has been manifested apart from the law, although the Law and the Prophets bear witness to it - the righteousness of God through faith in Jesus Christ for all who believe.", "Justification by Faith"),
    (5, "Therefore, since we have been justified by faith, we have peace with God through our Lord Jesus Christ. Through him we have also obtained access by faith into this grace in which we stand, and we rejoice in hope of the glory of God... For while we were still weak, at the right time Christ died for the ungodly. For one will scarcely die for a righteous person - though perhaps for a good person one would dare even to die - but God shows his love for us in that while we were still sinners, Christ died for us.", "Peace with God"),
    (8, "There is therefore now no condemnation for those who are in Christ Jesus. For the law of the Spirit of life has set you free in Christ Jesus from the law of sin and death... For those whom he foreknew he also predestined to be conformed to the image of his Son, in order that he might be the firstborn among many brothers. And those whom he predestined he also called, and those whom he called he also justified, and those whom he justified he also glorified.", "Life in the Spirit"),
    (12, "I appeal to you therefore, brothers, by the mercies of God, to present your bodies as a living sacrifice, holy and acceptable to God, which is your spiritual worship. Do not be conformed to this world, but be transformed by the renewal of your mind, that by testing you may discern what is the will of God, what is good and acceptable and perfect.", "Living Sacrifice"),
]

# 1 CORINTHIANS - Selected chapters
CORINTHIANS = [
    (1, "Paul, called by the will of God to be an apostle of Christ Jesus, and our brother Sosthenes, to the church of God that is in Corinth... For the word of the cross is folly to those who are perishing, but to us who are being saved it is the power of God.", "Introduction"),
    (13, "If I speak in the tongues of men and of angels, but have not love, I am a noisy gong or a clanging cymbal. And if I have prophetic powers, and understand all mysteries and all knowledge, and if I have all faith, so as to remove mountains, but have not love, I am nothing. If I give away all I have, and if I deliver up my body to be burned, but have not love, I gain nothing. Love is patient and kind; love does not envy or boast; it is not arrogant or rude. It does not insist on its own way; it is not irritable or resentful; it does not rejoice at wrongdoing, but rejoices with the truth. Love bears all things, believes all things, hopes all things, endures all things. Love never ends.", "Love Chapter"),
    (15, "Now I would remind you, brothers, of the gospel I preached to you, which you received, in which you stand, and by which you are being saved... For I delivered to you as of first importance what I also received: that Christ died for our sins in accordance with the Scriptures, that he was buried, that he was raised on the third day in accordance with the Scriptures.", "Resurrection"),
]

def import_phase2():
    """Import Phase 2 canonical books"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("IMPORTING PHASE 2: MORE CANONICAL BOOKS")
    print("="*70)
    
    # Create tables
    tables = [
        ("gospel_of_matthew", "Matthew"),
        ("gospel_of_mark", "Mark"),
        ("gospel_of_luke", "Luke"),
        ("book_of_acts", "Acts"),
        ("epistle_to_romans", "Romans"),
        ("first_epistle_to_corinthians", "1 Corinthians"),
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
    
    # Import data
    imports = [
        ("gospel_of_matthew", MATTHEW),
        ("gospel_of_mark", MARK),
        ("gospel_of_luke", LUKE),
        ("book_of_acts", ACTS),
        ("epistle_to_romans", ROMANS),
        ("first_epistle_to_corinthians", CORINTHIANS),
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
        "phase": "Phase 2",
        "total_entries": total,
        "books": [
            {"book": "Matthew", "count": len(MATTHEW)},
            {"book": "Mark", "count": len(MARK)},
            {"book": "Luke", "count": len(LUKE)},
            {"book": "Acts", "count": len(ACTS)},
            {"book": "Romans", "count": len(ROMANS)},
            {"book": "1 Corinthians", "count": len(CORINTHIANS)},
        ]
    }
    
    with open('/root/hebrew-repo/exports/phase2_canonical_export.json', 'w') as f:
        json.dump(export, f, indent=2)
    
    print("\n" + "="*70)
    print("PHASE 2 COMPLETE")
    print("="*70)
    print(f"\n📊 IMPORTED: {total} chapters")
    print(f"\n📁 Exported to exports/phase2_canonical_export.json")
    
    db.close()

if __name__ == "__main__":
    import_phase2()