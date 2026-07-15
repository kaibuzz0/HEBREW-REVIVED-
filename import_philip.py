#!/usr/bin/env python3
"""
GOSPEL OF PHILIP IMPORTER
Nag Hammadi Codex II,3
Coptic text on love, sacraments, and mystical theology
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

# Gospel of Philip - key sayings and passages
# Note: Philip is not organized by numbered sayings like Thomas,
# but by thematic sections. We'll organize by paragraph/section numbers.

PHILIP_PASSAGES = [
    (1, "Ⲡⲉⲩⲁⲅⲅⲉⲗⲓⲟⲛ ⲛⲫⲓⲗⲓⲡⲡⲟⲥ", "",
     "The Gospel of Philip. A Hebrew makes a Hebrew, and such a person is called a proselyte. But a Greek does not make a Greek. So it is with those who are spiritual. A spiritual person makes another spiritual, and such a person is called a proselyte of the faith.",
     [], "Prologue - Spiritual Birth"),
    
    (2, "Ⲡⲉϫⲉ ϫⲉ ⲡⲱⲛϩ ⲛⲁϩⲙⲟⲩ ⲛϩⲏⲧ", "",
     "The living do not die, and those who have died cannot live. For this reason, too, faith receives baptism first, and then it receives the resurrection.",
     [], "Life and Resurrection"),
    
    (3, "Ⲡⲉϫⲉ ϫⲉ ⲡϫⲟⲉⲓⲥ ⲉⲧⲁϩⲉ", "",
     "The one who creates something is more blessed than the thing that is created. So it is with the children of the bridal chamber (nymphon), who have received the resurrection and the light. If someone receives the light, they will not be seen, nor can they be held back.",
     [], "Bridal Chamber - Nymphon"),
    
    (4, "Ⲡⲉϫⲉ ϫⲉ ϩⲙ ⲡϩⲟⲟⲩ ⲛⲧⲁⲗⲏⲑⲓⲁ", "",
     "On the day when we were Hebrews, we were orphans, with only a mother. But when we became Christians, we had both a father and a mother.",
     [], "Orphans to Christians"),
    
    (5, "Ⲡⲉϫⲉ ϫⲉ ⲧⲁⲅⲁⲡⲏ ⲉⲧⲟⲩⲁⲁⲃ", "",
     "Love is the sacred mystery (sacrament). The perfect are conceived through love and born through love, and they are perfected through love. For the separated can be brought together only through love.",
     [], "Love is the Sacrament"),
    
    (6, "Ⲡⲉϫⲉ ϫⲉ ⲡϣⲱⲃ ϩⲓⲱⲱⲧ ⲡⲱⲧ", "",
     "The veil at first concealed how God controlled the creation, but when the veil was torn, the things inside were revealed. The veil was torn not only at that time, so that things inside might be seen, but also so that things outside might pass inside.",
     ["Mark 15:38", "Matthew 27:51"], "Tearing the Veil"),
    
    (7, "Ⲡⲉϫⲉ ϫⲉ ⲡⲉⲓⲟⲧ ⲛⲧⲟⲕ", "",
     "The one who is satisfied is never empty. The one who is empty is never satisfied. For it is good to be satisfied and to be empty at the same time. This is what is called the true fullness.",
     [], "Fullness and Emptiness"),
    
    (8, "Ⲡⲉϫⲉ ϫⲉ ⲧⲉϥⲛⲩⲙⲫⲏ", "",
     "The bridal chamber (nymphon) is not for the animals, nor is it for the slaves, nor is it for the defiled women. It is for the free men and the virgins.",
     [], "Bridal Chamber Mysteries"),
    
    (9, "Ⲡⲉϫⲉ ϫⲉ ⲡⲥⲟⲩ ⲙⲛ ⲧⲥϩⲓⲙⲉ", "",
     "The man and the woman are united in the bridal chamber. Those who are united in the bridal chamber will not be separated again. Adam came into being through two virgins, from the Spirit and from the virgin earth. Christ, therefore, was born through a virgin, so that he might rectify the fall that occurred in the beginning.",
     [], "Union in Bridal Chamber"),
    
    (10, "Ⲡⲉϫⲉ ϫⲉ ϯϩⲉⲗⲗⲏⲛⲓⲥⲧⲏⲥ", "",
      "The Greeks believe that the Egyptians speak of the gods who are not really gods. But they are very much mistaken. The Egyptians speak of the gods who are really gods, for they speak of the powers of God.",
      [], "Egyptians and Gods"),
    
    (11, "Ⲡⲉϫⲉ ϫⲉ ⲧⲙⲉⲧⲛⲟⲩⲧⲉ", "",
     "Ignorance is the mother of all evil. Those who come from ignorance cannot be saved until they receive the knowledge of the truth. Those who receive the knowledge of the truth will not perish.",
     [], "Ignorance Mother of Evil"),
    
    (12, "Ⲡⲉϫⲉ ϫⲉ ⲡⲓⲥⲧⲟⲥ ⲉⲧⲁⲗⲏⲑⲏⲥ", "",
     "The perfect faithful one is the one who has received the gnosis (knowledge). The perfect gnostic is the one who has received the revelation of the truth.",
     [], "Perfect Gnostic"),
    
    (13, "Ⲡⲉϫⲉ ϫⲉ ⲡϫⲟⲉⲓⲥ ⲉⲧⲟⲩⲁⲁⲃ", "",
     "Those who say they will die first and then rise are in error. If they do not first receive the resurrection while they live, they will not receive anything when they die.",
     [], "Resurrection While Living"),
    
    (14, "Ⲡⲉϫⲉ ϫⲉ ⲡⲱⲛϩ ⲛⲁϩⲙⲟⲩ", "",
     "God is a dyer. As the good dyes, which are called true, dissolve with the things dyed in them, so it is with those whom God has dyed. Since his dyes are imperishable, they are immortal.",
     [], "God the Dyer"),
    
    (15, "Ⲡⲉϫⲉ ϫⲉ ⲡⲉⲓⲱⲧ ⲛⲑⲉ ⲛⲉⲓⲟⲩⲇⲁⲓⲟⲥ", "",
     "It is not possible for anyone to see anything of the things that actually exist unless he becomes like them. This is not the way with man in the world: he sees the sun without being a sun, and he sees the heaven and the earth and all other things, but he is not these things. This is the way with the truth: you saw something of that place, you became those things. You saw the Spirit, you became spirit. You saw Christ, you became Christ. You saw the Father, you shall become Father.",
     [], "Becoming What You See"),
    
    (16, "Ⲡⲉϫⲉ ϫⲉ ϯϩⲉⲗⲗⲏⲛⲓⲥⲧⲏⲥ", "",
     "In this world, the slaves serve the free. In the Kingdom of Heaven, the free will serve the slaves. The children of the bridal chamber will serve the children of the marriage. But the children of the marriage have no part in the bridal chamber.",
     [], "Children of Bridal Chamber"),
    
    (17, "Ⲡⲉϫⲉ ϫⲉ ⲡⲁⲣⲑⲉⲛⲟⲥ ⲛⲁⲧⲉⲛⲟⲩⲧⲉ", "",
     "The virginal woman conceives through the Holy Spirit and gives birth. For this reason, too, she is the one who is not defiled. For the Holy Spirit is the one who makes the virgins. The power of the Spirit will make the virgins pregnant and give them birth without defilement.",
     [], "Virginal Conception"),
    
    (18, "Ⲡⲉϫⲉ ϫⲉ ⲧⲙⲉⲧⲣⲱⲙⲉ", "",
     "Some are afraid lest they rise naked. Because of this, they want to rise in the flesh, and they do not know that those who wear the flesh are naked. Those who are able to strip themselves of the flesh are the ones who are not naked.",
     [], "Rising Naked"),
    
    (19, "Ⲡⲉϫⲉ ϫⲉ ⲡϫⲱⲱⲙⲉ ⲛⲧⲁⲗⲏⲑⲏⲁ", "",
     "'Flesh and blood shall not inherit the Kingdom of God.' What is this which will not inherit? This which is on us. But what is this, too, which will inherit? It is that which belongs to Jesus and his blood. Because of this he said: 'He who shall not eat my flesh and drink my blood has no life in him.' What is it? His flesh is the word, and his blood is the Holy Spirit. Whoever has received these has food and he has drink and clothing.",
     ["1 Corinthians 15:50", "John 6:53"], "Flesh and Blood"),
    
    (20, "Ⲡⲉϫⲉ ϫⲉ ⲧⲥⲩⲛⲁⲝⲓⲥ", "",
     "There were three who always walked with the Lord: Mary, his mother, and her sister, and Magdalene, the one who was called his companion. His sister and his mother and his companion were each a Mary.",
     [], "Three Marys"),
    
    (21, "Ⲡⲉϫⲉ ϫⲉ ⲧⲁⲅⲁⲡⲏ ⲛⲧⲁⲗⲏⲑⲁ", "",
     "There were three Mariams who walked with the Lord: his mother, his sister, and Magdalene, who was his companion. For Mary is the name of his sister, his mother, and his companion.",
     [], "Three Mariams"),
    
    (22, "Ⲡⲉϫⲉ ϫⲉ ⲡⲉⲓⲱⲧ ⲛⲧⲟⲕ", "",
     "The companion of the Savior is Mary Magdalene. But Christ loved her more than all the other disciples and used to kiss her often on her mouth. The rest of the disciples were offended by it and expressed disapproval. They said to him, 'Why do you love her more than all of us?' The Savior answered and said to them, 'Why do I not love you like her? When a blind man and one who sees are both together in darkness, they are no different from one another. When the light comes, then he who sees will see the light, and he who is blind will remain in darkness.'",
     [], "Mary Magdalene Loved Most"),
    
    (23, "Ⲡⲉϫⲉ ϫⲉ ⲡⲥⲱⲧⲏⲣ ⲛⲧⲟⲕ", "",
     "The Lord said: 'Blessed is he who is before he came into being. For he who is, was and shall be.' The kingdom is within you and outside you. When you know yourselves, then you will be known, and you will know that you are the sons of the living Father. But if you do not know yourselves, then you are in poverty and you are poverty.",
     [], "Blessed Is He Who Is Before"),
    
    (24, "Ⲡⲉϫⲉ ϫⲉ ⲧⲉⲣⲛⲟⲩⲥ ⲉⲧⲟⲩⲁⲁⲃ", "",
     "The bridal chamber (nymphon) is superior to everything. For you will find rest in it and embrace the truth. The perfect are conceived in it and born in it and perfected in it.",
     [], "Bridal Chamber Superior"),
    
    (25, "Ⲡⲉϫⲉ ϫⲉ ⲡⲓⲥⲧⲓⲥ ⲛⲧⲁⲗⲏⲑⲁ", "",
     "Faith receives, love gives. No one will be able to receive without faith, and no one will be able to give without love. Therefore, we believe so that we might receive, but we love so that we might give.",
     [], "Faith Receives, Love Gives"),
]

def import_philip():
    """Import Gospel of Philip passages"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("IMPORTING GOSPEL OF PHILIP")
    print("="*70)
    
    # Clear existing
    db.cursor.execute("DELETE FROM gospel_of_philip")
    
    imported = 0
    for passage in PHILIP_PASSAGES:
        passage_num, coptic, greek, english, parallels, theme = passage
        db.add_philip_passage(passage_num, coptic, greek, english, parallels, theme)
        imported += 1
        
        if imported % 10 == 0:
            print(f"  ✅ Imported {imported} passages...")
    
    db.conn.commit()
    
    # Export
    philip_export = {
        "title": "Gospel of Philip",
        "total_passages": imported,
        "language": "Coptic",
        "source": "Nag Hammadi Codex II,3",
        "themes": list(set([p[5] for p in PHILIP_PASSAGES])),
        "key_concepts": [
            "Bridal Chamber (Nymphon)",
            "Love as sacrament",
            "Spiritual birth",
            "Mary Magdalene",
            "Faith and love",
            "Three Marys",
            "Resurrection while living"
        ],
        "passages": []
    }
    
    for passage in PHILIP_PASSAGES:
        philip_export["passages"].append({
            "number": passage[0],
            "coptic": passage[1][:100] + "..." if len(passage[1]) > 100 else passage[1],
            "english": passage[3][:200] + "..." if len(passage[3]) > 200 else passage[3],
            "theme": passage[5]
        })
    
    with open('/root/hebrew-repo/exports/philip_export.json', 'w', encoding='utf-8') as f:
        json.dump(philip_export, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*70)
    print("IMPORT COMPLETE")
    print("="*70)
    print(f"\n📊 Statistics:")
    print(f"   Total passages: {imported}")
    print(f"   Themes: {len(philip_export['themes'])}")
    print(f"\n🎯 KEY THEMES:")
    for concept in philip_export['key_concepts']:
        print(f"   • {concept}")
    print(f"\n✅ Exported to exports/philip_export.json")
    
    db.close()

if __name__ == "__main__":
    import_philip()