#!/usr/bin/env python3
"""
WITNESSES OF JESUS - Complete Database
Everyone who knew Jesus personally
Family, disciples, opponents, crowds
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

WITNESSES = [
    # FAMILY - Immediate
    {
        "name": "Mary",
        "name_hebrew": "מִרְיָם",
        "name_greek": "Μαριάμ",
        "relationship": "mother",
        "is_jesus_contemporary": True,
        "birth_year": -20,
        "death_year": 45,
        "description": "Mother of Jesus, virgin birth, present at cross",
        "feast_day": "August 15 (Dormition)",
        "canonization": "saint",
        "references": ["Luke 1-2", "John 19:26-27", "Acts 1:14"],
        "category": "Family"
    },
    {
        "name": "Joseph",
        "name_hebrew": "יוֹסֵף",
        "name_greek": "Ἰωσήφ",
        "relationship": "earthly father",
        "is_jesus_contemporary": True,
        "birth_year": -40,
        "death_year": 10,
        "description": "Carpenter, righteous man, foster father of Jesus",
        "feast_day": "March 19",
        "canonization": "saint",
        "references": ["Matthew 1-2", "Luke 2"],
        "category": "Family"
    },
    {
        "name": "James (the Just)",
        "name_hebrew": "יַעֲקֹב",
        "name_greek": "Ἰάκωβος",
        "relationship": "brother",
        "is_jesus_contemporary": True,
        "birth_year": 5,
        "death_year": 62,
        "description": "Leader of Jerusalem church, wrote Epistle, martyred",
        "feast_day": "October 23",
        "canonization": "saint",
        "references": ["Mark 6:3", "Acts 15", "James 1:1", "Galatians 1:19"],
        "category": "Family"
    },
    {
        "name": "Joses",
        "name_hebrew": "יוֹסֵף",
        "name_greek": "Ἰωσῆς",
        "relationship": "brother",
        "is_jesus_contemporary": True,
        "birth_year": 7,
        "death_year": None,
        "description": "Brother of Jesus, mentioned in Mark 6:3",
        "feast_day": None,
        "canonization": "unknown",
        "references": ["Mark 6:3", "Matthew 13:55"],
        "category": "Family"
    },
    {
        "name": "Simon",
        "name_hebrew": "שִׁמְעוֹן",
        "name_greek": "Σίμων",
        "relationship": "brother",
        "is_jesus_contemporary": True,
        "birth_year": 9,
        "death_year": None,
        "description": "Brother of Jesus, mentioned as believer in Acts",
        "feast_day": None,
        "canonization": "unknown",
        "references": ["Mark 6:3", "Matthew 13:55", "Acts 1:14"],
        "category": "Family"
    },
    {
        "name": "Jude (Judas)",
        "name_hebrew": "יְהוּדָה",
        "name_greek": "Ἰούδας",
        "relationship": "brother",
        "is_jesus_contemporary": True,
        "birth_year": 10,
        "death_year": 80,
        "description": "Author of Epistle of Jude, brother of James and Jesus",
        "feast_day": "October 28",
        "canonization": "saint",
        "references": ["Mark 6:3", "Matthew 13:55", "Jude 1:1"],
        "category": "Family"
    },
    {
        "name": "Salome (Mary's sister?)",
        "name_hebrew": "שְׁלוֹמִית",
        "name_greek": "Σαλώμη",
        "relationship": "relative (possibly aunt)",
        "is_jesus_contemporary": True,
        "birth_year": -10,
        "death_year": 45,
        "description": "At cross, asked for sons' positions",
        "feast_day": None,
        "canonization": "saint",
        "references": ["Mark 15:40", "Matthew 27:56"],
        "category": "Family"
    },
    
    # TWELVE DISCIPLES
    {
        "name": "Peter (Simon Peter)",
        "name_hebrew": "שִׁמְעוֹן",
        "name_greek": "Πέτρος",
        "relationship": "disciple",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 64,
        "description": "Rock, first to confess Christ, denied 3 times, martyred in Rome",
        "feast_day": "June 29",
        "canonization": "saint",
        "references": ["All Gospels", "Acts", "1-2 Peter"],
        "category": "Twelve"
    },
    {
        "name": "Andrew",
        "name_hebrew": "אַנְדְּרֵי",
        "name_greek": "Ἀνδρέας",
        "relationship": "disciple",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 60,
        "description": "First called, brother of Peter, missionary to Scythia",
        "feast_day": "November 30",
        "canonization": "saint",
        "references": ["Matthew 4:18-22", "Mark 1:16-20", "John 1:35-42"],
        "category": "Twelve"
    },
    {
        "name": "James (son of Zebedee)",
        "name_hebrew": "יַעֲקֹב",
        "name_greek": "Ἰάκωβος",
        "relationship": "disciple",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 44,
        "description": "Son of Thunder, martyred by Herod Agrippa",
        "feast_day": "July 25",
        "canonization": "saint",
        "references": ["Matthew 4:21-22", "Mark 1:19-20", "Acts 12:2"],
        "category": "Twelve"
    },
    {
        "name": "John",
        "name_hebrew": "יוֹחָנָן",
        "name_greek": "Ἰωάννης",
        "relationship": "disciple",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 100,
        "description": "Beloved disciple, at cross, author of Gospel, Revelation, Epistles",
        "feast_day": "December 27",
        "canonization": "saint",
        "references": ["All Gospels", "Acts", "John's writings"],
        "category": "Twelve"
    },
    {
        "name": "Philip",
        "name_hebrew": "פִּילִפּוֹס",
        "name_greek": "Φίλιππος",
        "relationship": "disciple",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 80,
        "description": "From Bethsaida, brought Nathanael, martyred in Hierapolis",
        "feast_day": "May 3",
        "canonization": "saint",
        "references": ["Matthew 10:3", "Mark 3:18", "John 1:43-48", "John 6:5-7", "John 12:20-22", "John 14:8-9"],
        "category": "Twelve"
    },
    {
        "name": "Bartholomew (Nathanael)",
        "name_hebrew": "נַתַּנְאֵל",
        "name_greek": "Βαρθολομαῖος",
        "relationship": "disciple",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 70,
        "description": "Israelite in whom is no deceit, martyred in Armenia",
        "feast_day": "August 24",
        "canonization": "saint",
        "references": ["Matthew 10:3", "Mark 3:18", "Luke 6:14", "John 1:45-51"],
        "category": "Twelve"
    },
    {
        "name": "Matthew (Levi)",
        "name_hebrew": "מַתִּתְיָהוּ",
        "name_greek": "Μαθθαῖος",
        "relationship": "disciple",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 74,
        "description": "Tax collector, author of Gospel, martyred in Ethiopia",
        "feast_day": "September 21",
        "canonization": "saint",
        "references": ["Matthew 9:9-13", "Mark 2:14-17", "Luke 5:27-32", "Matthew's Gospel"],
        "category": "Twelve"
    },
    {
        "name": "Thomas (Didymus)",
        "name_hebrew": "תּוֹמָא",
        "name_greek": "Θωμᾶς",
        "relationship": "disciple",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 72,
        "description": "Doubting Thomas, missionary to India, martyred in Mylapore",
        "feast_day": "July 3",
        "canonization": "saint",
        "references": ["Matthew 10:3", "Mark 3:18", "Luke 6:15", "John 11:16", "John 14:5", "John 20:24-29", "John 21:2"],
        "category": "Twelve"
    },
    {
        "name": "James (son of Alphaeus)",
        "name_hebrew": "יַעֲקֹב",
        "name_greek": "Ἰάκωβος",
        "relationship": "disciple",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 62,
        "description": "Called the Less, stoned in Jerusalem",
        "feast_day": "May 3",
        "canonization": "saint",
        "references": ["Matthew 10:3", "Mark 3:18", "Luke 6:15", "Acts 1:13"],
        "category": "Twelve"
    },
    {
        "name": "Thaddaeus (Jude of James)",
        "name_hebrew": "תַּדַּי",
        "name_greek": "Θαδδαῖος",
        "relationship": "disciple",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 65,
        "description": "Question about manifestation, martyred in Persia",
        "feast_day": "October 28",
        "canonization": "saint",
        "references": ["Matthew 10:3", "Mark 3:18", "Luke 6:16", "John 14:22"],
        "category": "Twelve"
    },
    {
        "name": "Simon the Zealot",
        "name_hebrew": "שִׁמְעוֹן",
        "name_greek": "Σίμων",
        "relationship": "disciple",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 65,
        "description": "Former Zealot, martyred in Britain (legend) or Persia",
        "feast_day": "October 28",
        "canonization": "saint",
        "references": ["Matthew 10:4", "Mark 3:18", "Luke 6:15", "Acts 1:13"],
        "category": "Twelve"
    },
    {
        "name": "Judas Iscariot",
        "name_hebrew": "יְהוּדָה אִישׁ קְרִיּוֹת",
        "name_greek": "Ἰούδας Ἰσκαριώτης",
        "relationship": "disciple",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 30,
        "description": "Betrayer, treasurer, hanged himself or died by field accident",
        "feast_day": None,
        "canonization": "none",
        "references": ["All Gospels", "Acts 1:18-19"],
        "category": "Twelve"
    },
    {
        "name": "Matthias",
        "name_hebrew": "מַתִּתְיָה",
        "name_greek": "Μαθθίας",
        "relationship": "disciple (replacement)",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 80,
        "description": "Chosen to replace Judas, martyred in Ethiopia",
        "feast_day": "May 14",
        "canonization": "saint",
        "references": ["Acts 1:23-26"],
        "category": "Twelve"
    },
    
    # WOMEN DISCIPLES
    {
        "name": "Mary Magdalene",
        "name_hebrew": "מִרְיָם מִגְדָּל",
        "name_greek": "Μαρία ἡ Μαγδαληνή",
        "relationship": "disciple/follower",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 63,
        "description": "Apostle to apostles, first witness to resurrection, traveled to France",
        "feast_day": "July 22",
        "canonization": "saint",
        "references": ["Luke 8:2", "All Gospels at cross/resurrection", "Gospel of Mary"],
        "category": "Women"
    },
    {
        "name": "Mary of Bethany",
        "name_hebrew": "מִרְיָם",
        "name_greek": "Μαρία",
        "relationship": "disciple/follower",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": None,
        "description": "Sister of Martha and Lazarus, anointed Jesus' feet",
        "feast_day": "June 4",
        "canonization": "saint",
        "references": ["Luke 10:38-42", "John 12:1-8", "Matthew 26:6-13", "Mark 14:3-9"],
        "category": "Women"
    },
    {
        "name": "Martha",
        "name_hebrew": "מַרְתָּא",
        "name_greek": "Μάρθα",
        "relationship": "disciple/follower",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": None,
        "description": "Sister of Mary and Lazarus, served Jesus",
        "feast_day": "July 29",
        "canonization": "saint",
        "references": ["Luke 10:38-42", "John 11:1-45", "John 12:1-2"],
        "category": "Women"
    },
    {
        "name": "Joanna",
        "name_hebrew": "יוֹחָנָה",
        "name_greek": "Ἰωάννα",
        "relationship": "disciple/follower",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": None,
        "description": "Wife of Chuza, supported Jesus' ministry financially",
        "feast_day": None,
        "canonization": "saint",
        "references": ["Luke 8:1-3", "Luke 24:10"],
        "category": "Women"
    },
    {
        "name": "Susanna",
        "name_hebrew": "שׁוֹשַׁנָּה",
        "name_greek": "Σουσάνα",
        "relationship": "disciple/follower",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": None,
        "description": "Supported Jesus' ministry",
        "feast_day": None,
        "canonization": "unknown",
        "references": ["Luke 8:3"],
        "category": "Women"
    },
    {
        "name": "Mary (wife of Clopas)",
        "name_hebrew": "מִרְיָם",
        "name_greek": "Μαρία",
        "relationship": "disciple/follower",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": None,
        "description": "At cross with Virgin Mary, mother of James the Less",
        "feast_day": None,
        "canonization": "saint",
        "references": ["Matthew 27:56", "Mark 15:40", "John 19:25"],
        "category": "Women"
    },
    
    # OPPONENTS
    {
        "name": "Caiaphas",
        "name_hebrew": "קַיָּפָא",
        "name_greek": "Καϊάφας",
        "relationship": "opponent",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 36,
        "description": "High priest, plotted Jesus' death",
        "feast_day": None,
        "canonization": "none",
        "references": ["Matthew 26:3-5", "Matthew 26:57-68", "John 11:49-53", "John 18:14-28"],
        "category": "Opponents"
    },
    {
        "name": "Pontius Pilate",
        "name_hebrew": "פּוֹנְטִיּוֹס פִּילָטוֹס",
        "name_greek": "Πόντιος Πιλᾶτος",
        "relationship": "opponent (judge)",
        "is_jesus_contemporary": True,
        "birth_year": None,
        "death_year": 39,
        "description": "Roman prefect, sentenced Jesus to death",
        "feast_day": None,
        "canonization": "none",
        "references": ["Matthew 27:11-26", "Mark 15", "Luke 23", "John 18:28-19:22", "Acts 3:13", "1 Timothy 6:13"],
        "category": "Opponents"
    },
    {
        "name": "Herod Antipas",
        "name_hebrew": "הוֹרְדוֹס",
        "name_greek": "Ἡρῴδης",
        "relationship": "opponent",
        "is_jesus_contemporary": True,
        "birth_year": -20,
        "death_year": 39,
        "description": "Tetrarch of Galilee, beheaded John the Baptist",
        "feast_day": None,
        "canonization": "none",
        "references": ["Matthew 14:1-12", "Mark 6:14-29", "Luke 3:1", "Luke 9:7-9", "Luke 13:31-33", "Luke 23:6-12", "Acts 13:1"],
        "category": "Opponents"
    },
]

def import_witnesses():
    """Import all witnesses of Jesus"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("WITNESSES OF JESUS - Complete Database")
    print("="*70)
    
    # Clear existing
    db.cursor.execute("DELETE FROM persons")
    
    imported = 0
    categories = {}
    
    for witness in WITNESSES:
        db.cursor.execute("""
            INSERT INTO persons (name, name_hebrew, name_greek, description, 
                is_jesus_contemporary, relationship_to_jesus, birth_year, death_year,
                feast_day, canonization_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            witness["name"],
            witness.get("name_hebrew"),
            witness.get("name_greek"),
            witness["description"],
            witness["is_jesus_contemporary"],
            witness["relationship"],
            witness.get("birth_year"),
            witness.get("death_year"),
            witness.get("feast_day"),
            witness.get("canonization")
        ))
        imported += 1
        
        cat = witness["category"]
        categories[cat] = categories.get(cat, 0) + 1
        
        if imported <= 10:
            print(f"  {imported:2d}. {witness['name']} ({witness['relationship']})")
    
    print(f"\n  ... and {imported - 10} more witnesses")
    
    db.conn.commit()
    
    # Export
    export = {
        "title": "Witnesses of Jesus Christ",
        "total_witnesses": imported,
        "by_category": categories,
        "saints": len([w for w in WITNESSES if w.get("canonization") == "saint"]),
        "family": len([w for w in WITNESSES if w["relationship"] in ["mother", "brother", "earthly father"]]),
        "twelve": len([w for w in WITNESSES if w["category"] == "Twelve"]),
        "women": len([w for w in WITNESSES if w["category"] == "Women"]),
        "witnesses": WITNESSES
    }
    
    with open('/root/hebrew-repo/exports/witnesses_of_jesus.json', 'w', encoding='utf-8') as f:
        json.dump(export, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*70)
    print("IMPORT COMPLETE")
    print("="*70)
    print(f"\n📊 Statistics:")
    print(f"   Total witnesses: {imported}")
    for cat, count in categories.items():
        print(f"   - {cat}: {count}")
    print(f"\n✅ Exported to exports/witnesses_of_jesus.json")
    
    print("\n🎯 KEY FINDINGS:")
    print(f"   - Family: {export['family']} immediate members")
    print(f"   - Twelve: {export['twelve']} disciples (including Matthias)")
    print(f"   - Women: {export['women']} female disciples")
    print(f"   - Saints: {export['saints']} canonized")
    
    db.close()

if __name__ == "__main__":
    import_witnesses()