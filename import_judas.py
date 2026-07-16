#!/usr/bin/env python3
"""
GOSPEL OF JUDAS IMPORTER
Codex Tchacos, ca. 280 CE (copy)
Discovered 1970s, published 2006

Presents Judas Iscariot as Jesus' most trusted disciple
who acts at Jesus' request to betray him, enabling the 
Savior's escape from the physical body

Sources: Codex Tchacos Coptic text
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

# Gospel of Judas - 4 main sections/pages
JUDAS_PASSAGES = [
    # Scene 1: Jesus with disciples
    (1, "ⲡⲉⲩⲁⲅⲅⲉⲗⲓⲟⲛ ⲛⲓⲟⲩⲇⲁⲥ", "",
     "The secret account of the revelation that Jesus spoke in conversation with Judas Iscariot during a week, three days before he celebrated Passover.",
     [], "Introduction"),
    
    (2, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ", "",
     "When Jesus appeared on earth, he performed miracles and great wonders for the salvation of humanity. And since some walked in the way of righteousness while others walked in their transgressions, the twelve disciples were called.",
     [], "Jesus Appears"),
    
    (3, "ⲁⲩⲱ ⲛⲧⲉⲣⲟⲩ ⲛϩⲟⲩⲟ", "",
     "He began to speak with them about the mysteries beyond the world and what would take place at the end. Often he did not appear to his disciples as himself, but he was found among them as a child.",
     [], "Jesus Speaks of Mysteries"),
    
    (4, "ⲁⲩⲱ ⲛⲧⲉⲣⲟⲩ ⲛϩⲟⲩⲟ", "",
     "One day he happened to be in the village with his disciples. Judas said to him, 'I know who you are and where you have come from. You are from the immortal realm of Barbelo. And I am not worthy to utter the name of the one who has sent you.'",
     [], "Judas Recognizes Jesus"),
    
    (5, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ", "",
     "Jesus said to him, 'Step away from the others and I shall tell you the mysteries of the kingdom. It is possible for you to reach it, but you will grieve a great deal. For someone else will replace you, in order that the twelve may again come to completion with their God.'",
     [], "Jesus Speaks to Judas Privately"),
    
    (6, "ⲁⲩⲱ ⲛⲧⲉⲣⲟⲩ ⲛϩⲟⲩⲟ", "",
     "Jesus said, 'The rulers above have a likeness to the stars that bring the seasons and the months to completion. Their names, when listed, are a mystery. For the stars complete their circuits and bring forth everything upon earth, but they do not know that these things are established by Saklas.",
     [], "Rulers Above and Stars"),
    
    (7, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ", "",
     "The twelve disciples said to Jesus, 'Teach us about the error of the rulers of the world, for we have already served them.' Jesus said, 'The rulers have a likeness to the great generation with no king over it. They have a great angel as their ruler, but he is foolish. And he said to them, Let twelve angels come into being to rule over chaos and the underworld.' And behold, from the cloud there appeared an angel whose face flashed with fire and whose appearance was defiled with blood. His name was Nebro, which means 'rebel.'",
     [], "Origin of the Rulers"),
    
    (8, "ⲁⲩⲱ ⲛⲧⲉⲣⲟⲩ ⲛϩⲟⲩⲟ", "",
     "Nebro created six angels—as well as Saklas—to be assistants, and these produced twelve angels in the heavens, with each one receiving a portion in the heavens. The twelve rulers spoke with the twelve angels: Let each of you take a portion of the angels under your authority, and let them minister to the great generation.' And the twelve rulers each took a portion.",
     [], "Creation of Angels"),
    
    (9, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ", "",
     "Then Saklas said to his angels, 'Let us create a human being after the likeness and after the image.' And they fashioned Adam and his wife Eve, who is called, in the cloud, Zoe. For by this name all the generations seek the man, and each of them calls the woman by these names. And Saklas said to Adam, 'You shall live long, with your children.'",
     [], "Creation of Adam"),
    
    (10, "ⲁⲩⲱ ⲛⲧⲉⲣⲟⲩ ⲛϩⲟⲩⲟ", "",
     "Judas said to Jesus, 'What is the long duration of time that the human being will live?' Jesus said, 'Why are you wondering about this, that Adam, with his generation, has lived his span of time in the place where he has received his kingdom, with longevity with his ruler?' Judas said, 'Does the human spirit die?' Jesus said, 'This is why God ordered the angels to provide assistance to Adam's generation, so that the human spirit might remain alive. But the spirit is not left to live alone. It is left with its counterpart, the soul, within the holy generation.'",
     [], "Conversation on Life and Death"),
    
    # Scene 2: Vision of the temple
    (11, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ϩⲱⲥ", "",
     "The disciples said to Jesus, 'Master, you are the Son of our God!' Jesus said to them, 'How do you know me? Truly I say to you, no generation of the people that are among you will know me.' When his disciples heard this, they started getting angry and furious and began blaspheming against him in their hearts.",
     [], "Disciples Do Not Understand"),
    
    (12, "ⲁⲩⲱ ⲛⲧⲉⲣⲟⲩ ⲛϩⲟⲩⲟ", "",
     "But when Jesus observed their lack of understanding, he said to them, 'Why has this agitation produced your anger? Your god who is within you and the stars have become wrathful with the generation. And when Judas observed this, he said to Jesus, 'What advantage have I received, for you have set me apart from that generation?' Jesus answered and said, 'You will become the thirteenth, and you will be cursed by the other generations, and you will come to rule over them. In the last days they will curse your ascent to the holy generation.'",
     [], "Judas Set Apart"),
    
    # Scene 3: Cosmology - The Great Invisible Spirit
    (13, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ", "",
     "Jesus said, 'Come, that I may teach you about the secrets that no one has seen. For there is a great and boundless realm, whose extent no generation of angels has seen, in which there is a great invisible Spirit, which no eye of an angel has ever seen, no thought of the heart has ever comprehended, and it was never called by any name.'",
     [], "The Great Invisible Spirit"),
    
    (14, "ⲁⲩⲱ ⲛⲧⲉⲣⲟⲩ ⲛϩⲟⲩⲟ", "",
     "And a luminous cloud appeared there. He said, 'Let an angel come into being as my attendant.' And a great angel, the Self-Generated, the God of the Light, came from the cloud. And because of him, four other angels came into being from another cloud, and they became attendants for the angelic Self-Generated. And the Self-Generated said, Let Adamas come into being, and the face of the angelic Self-Generated appeared. And its consort, the Great Sophia, was with it, and she produced the god of the aconic realms, and angels, a people numbering seventy-two. And the twelve rulers were established with their seven angels and five finisherers.'",
     [], "Cosmology - Emergence of Realms"),
    
    (15, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ", "",
     "Jesus said, 'Adamas was in the first luminous cloud that no angel has ever seen among all those called God. And he called the self-generated and the twelve aeons into being. He placed twelve aeons into the aeon of the eighth, and into each of the heavens he placed 360 firmaments, with all their divisions according to the aeon of the stars, and with all their divisions that are numbered according to the course of the stars. And the first is Athoth, the second is Harmas, the third is Kalila-Oumbri, the fourth is Yabel, the fifth is Adonaios, the sixth is Cain, the seventh is Abel, the eighth is Abrisene, the ninth is Yobel, the tenth is Armoupieel, the eleventh is Melceir-Adonein, the twelfth is Belias.'",
     [], "The Twelve Rulers Named"),
    
    (16, "ⲁⲩⲱ ⲛⲧⲉⲣⲟⲩ ⲛϩⲟⲩⲟ", "",
     "Jesus said, 'These are the twelve rulers who rule over chaos and the underworld. The first is Athoth, who has the face of a sheep. The second is Eloaios, who has the face of a donkey. The third is Astaphaios, who has the face of a hyena. The fourth is Yao, who has the face of a seven-headed snake. The fifth is Sabaoth, who has the face of a dragon. The sixth is Adonin, who has the face of a monkey. The seventh is Sabbataios, who has the face of a flame of fire. The eighth is Athoth, who has the face of a cat. The ninth is Ores, who has the face of an eagle. The tenth is Nethumiathos, who has the face of a falcon. The eleventh is Akros, who has the face of a buzzard. The twelfth is Belias, who has the face of a viper. And these are the ones who have taken hold of the generations of people.'",
     [], "Rulers with Animal Faces"),
    
    (17, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ", "",
     "Jesus said, 'This is the number of the stars: 72. And each of them has five firmaments of heaven, making 360 firmaments. This is the division of them, and this is the calculation of them. And the one who is the Great King of all these is the Self-Generated. And he is the one who has been anointed by Sophia and given power over all the aeons, subduing chaos and the underworld.'",
     [], "Number of Stars and Firmaments"),
    
    (18, "ⲁⲩⲱ ⲛⲧⲉⲣⲟⲩ ⲛϩⲟⲩⲟ", "",
     "And the stars complete their circuits according to the number of the firmaments. And their courses are established according to the aeons that have been fixed for them. For the twelve, with their seven angels and five finisherers, were established in their aeons, and they complete their courses according to the calculation of the stars. And these are the ones who have been established in their aeons, with the names that were given to them by their God, Saklas, and Nebroel.'",
     [], "Courses of the Stars"),
    
    # Scene 4: Judas' betrayal foretold
    (19, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ϩⲱⲥ", "",
     "Judas said, 'Rabbi, what is the fruit of these things that you have said to me? And what will be my advantage if you have sent me?' Jesus said, 'The fruit is that you will become the thirteenth, and you will be cursed by the other generations. And you will come to rule over them. In the last days they will curse your ascent to the holy generation. And you will not ascend on the days when the generation of the stars is completed, because your star has passed by. It is the thirteenth aeon. The twelve aeons are completed with their god. And you will grieve greatly when you see the kingdom with its generation. And you will not be there.'",
     [], "Judas' Role Foretold"),
    
    (20, "ⲁⲩⲱ ⲛⲧⲉⲣⲟⲩ ⲛϩⲟⲩⲟ", "",
     "Judas said, 'What good is it that I have received it? For you have set me apart for that generation.' Jesus answered and said, 'You will become the thirteenth, and the rest of the generations of the stars will complete their course with their god Saklas. And with your hand you will lift me up, and you will sacrifice the man who clothes me.'",
     [], "The Betrayal Foretold"),
    
    (21, "ⲁⲩⲱ ⲛⲧⲉⲣⲟⲩ ⲛϩⲟⲩⲟ", "",
     "Jesus said to him, 'Lift up your hands, and let the holy Spirit come upon you. And the stars that bring the seasons and the months will complete their course. And after this, Judas lifted up his hands, and a luminous cloud came, and he entered it. And he was no longer visible to those who were standing there. And when Judas had done these things, the great generation of the other generation looked down, but it found no form there.'",
     [], "Judas Lifted Up"),
    
    (22, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ϩⲱⲥ", "",
     "The high priests approached and said to Judas, 'What are you doing here? You are Jesus' disciple.' And he answered them according to what he wanted. And the high priests paid Judas some money. And he handed Jesus over to them.'",
     [], "The Betrayal"),
    
    (23, "ⲥϩⲁⲓⲙ", "",
     "The Gospel of Judas.",
     [], "End"),
]

def import_judas():
    """Import Gospel of Judas"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("IMPORTING GOSPEL OF JUDAS (CODEX TCHACOS)")
    print("="*70)
    
    # Clear existing
    db.cursor.execute("DELETE FROM gospel_of_judas")
    
    imported = 0
    for passage in JUDAS_PASSAGES:
        passage_num, coptic, greek, english, parallels, title = passage
        db.cursor.execute("""
            INSERT INTO gospel_of_judas
            (passage_number, coptic_text, greek_fragments, english_text, parallel_passages, theme)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (passage_num, coptic, greek, english, json.dumps(parallels), title))
        imported += 1
        
        if imported % 5 == 0:
            print(f"  ✅ Imported {imported} passages...")
    
    db.conn.commit()
    
    # Export to JSON
    judas_export = {
        "title": "Gospel of Judas",
        "subtitle": "From Codex Tchacos",
        "total_passages": imported,
        "language": "Coptic (Sahidic)",
        "date": "c. 280 CE (copy), original c. 150 CE",
        "discovery": "1970s near Beni Masah, Egypt",
        "publication": "2006 (National Geographic)",
        "significance": "Presents Judas as Jesus' most trusted disciple who acts at Jesus' request",
        "key_concepts": [
            "Judas as the 'thirteenth' who surpasses the twelve",
            "The physical body as a prison to escape",
            "The twelve disciples serve the wrong god",
            "The Great Invisible Spirit beyond all aeons",
            "Saklas (Satan) as the foolish creator god",
            "The stars and their angelic rulers",
            "Judas' betrayal enables Jesus' escape from flesh"
        ],
        "cast_of_characters": [
            "Jesus - The Savior who teaches the mysteries",
            "Judas Iscariot - The only one who understands",
            "The Twelve - Deceived by the lesser god",
            "Saklas - The foolish creator of the material world",
            "The Great Invisible Spirit - The true God",
            "Barbelo - The divine realm",
            "The Self-Generated - The angelic Christ",
            "Nebro - The rebel who creates Adam"
        ],
        "structure": [
            "Introduction - Jesus appears on earth",
            "Scene 1 - Jesus teaches the twelve (who misunderstand)",
            "Scene 2 - Judas recognized and set apart",
            "Scene 3 - Cosmology of the upper realms",
            "Scene 4 - Judas' betrayal foretold and executed"
        ],
        "controversy": "Contradicts canonical gospels by presenting Judas as the hero rather than villain",
        "passages": []
    }
    
    for passage in JUDAS_PASSAGES:
        passage_num, coptic, greek, english, parallels, title = passage
        judas_export["passages"].append({
            "number": passage_num,
            "title": title,
            "english": english[:200] + "..." if len(english) > 200 else english
        })
    
    with open('/root/hebrew-repo/exports/judas_export.json', 'w', encoding='utf-8') as f:
        json.dump(judas_export, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*70)
    print("IMPORT COMPLETE")
    print("="*70)
    print(f"\n📊 Statistics:")
    print(f"   Total passages: {imported}")
    print(f"\n🎯 KEY THEMES:")
    for concept in judas_export['key_concepts'][:5]:
        print(f"   • {concept}")
    print(f"\n✅ Exported to exports/judas_export.json")
    
    db.close()

if __name__ == "__main__":
    import_judas()