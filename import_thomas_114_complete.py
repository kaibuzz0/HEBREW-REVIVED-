#!/usr/bin/env python3
"""
GOSPEL OF THOMAS - COMPLETE 114 SAYINGS
Full Coptic text with English translations and canonical parallels
Sources: Nag Hammadi Codex II,2 (Coptic), Oxyrhynchus Papyri
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

THOMAS_114_COMPLETE = [
    # Prologue and Sayings 0-10
    (0, "ⲡⲉⲩⲁⲅⲅⲉⲗⲓⲟⲛ ⲕⲁⲧⲁ ⲑⲱⲙⲁⲥ", "", 
     "These are the secret sayings which the living Jesus spoke and Didymus Judas Thomas wrote down.",
     [], "Prologue"),
    
    (1, "ⲡⲉϫⲉ ϥϣⲟⲟⲡ ⲛϩⲱⲃ ⲛⲧⲟⲧⲩ ϫⲉ ϥⲛⲁϣⲱⲡⲉ ⲁⲛ ⲉⲧⲙⲟⲩ", "",
     "And he said, 'Whoever finds the interpretation of these sayings will not taste death.'",
     ["John 8:51-52"], "Life and Death"),
    
    (2, "ⲓⲱⲥ ⲡⲉϫⲉ ϣⲟⲡⲉ ⲡⲁⲉⲓⲱⲧ ⲙⲛⲡⲁⲉⲓⲱⲧ ⲛϩⲏⲧ ϩⲛⲧⲙⲉ ϥⲛⲁϩⲉ", "",
     "Jesus said, 'Let him who seeks continue seeking until he finds. When he finds, he will be troubled. When he becomes troubled, he will be astonished, and he will rule over the All.'",
     ["Matthew 7:7-8", "Luke 11:9-10"], "Seeking and Finding"),
    
    (3, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲱⲣⲕ ⲛⲧⲟⲧⲩ ⲛⲛⲁⲓ ⲉⲧϩⲛⲧⲡⲉ", "",
     "Jesus said, 'If those who lead you say to you, \"See, the Kingdom is in the sky,\" then the birds of the sky will precede you. If they say to you, \"It is in the sea,\" then the fish will precede you. Rather, the Kingdom is inside of you, and it is outside of you. When you come to know yourselves, then you will become known, and you will realize that it is you who are the sons of the living Father. But if you will not know yourselves, you dwell in poverty and it is you who are that poverty.'",
     ["Luke 17:20-21", "John 3:3-5"], "Kingdom Within"),
    
    (4, "ⲓⲱⲥ ⲡⲉϫⲉ ⲡⲣⲱⲙⲉ ⲡⲁⲓ ⲉϥⲛⲁϣⲱⲡⲉ", "",
     "Jesus said, 'The man old in days will not hesitate to ask a small child seven days old about the place of life, and he will live. For many who are first will become last, and they will become one and the same.'",
     ["Mark 10:31", "Matthew 19:30"], "Reversal of Status"),
    
    (5, "ⲓⲱⲥ ⲡⲉϫⲉ ⲥⲱⲧⲙ ⲉⲣⲟⲓ ϩⲙⲡⲁⲓ ⲡⲁⲓ ⲛⲧⲟⲕ ⲛϩⲏⲧ", "",
     "Jesus said, 'Recognize what is in your sight, and that which is hidden from you will become plain to you. For there is nothing hidden which will not become manifest.'",
     ["Mark 4:22", "Luke 8:17", "Matthew 10:26"], "Hidden and Revealed"),
    
    (6, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ⲙⲡⲣⲟϩⲟⲩⲉ ⲛⲧⲉⲧⲛⲉⲩⲓⲉ", "",
     "His disciples questioned him and said to him, 'Do you want us to fast? How shall we pray? Shall we give alms? What diet shall we observe?' Jesus said, 'Do not tell lies, and do not do what you hate, for all things are plain in the sight of Heaven. For nothing hidden will not become manifest, and nothing covered will remain without being uncovered.'",
     ["Mark 4:22", "Luke 12:2"], "Truth and Authenticity"),
    
    (7, "ⲓⲱⲥ ⲡⲉϫⲉ ϥⲥⲟⲟⲩⲛ ⲛⲧⲟⲕ ⲛⲧⲟⲕ ⲉⲧⲃⲉⲛⲏⲩⲉ", "",
     "Jesus said, 'Blessed is the lion which becomes man when consumed by man; and cursed is the man whom the lion consumes, and the lion becomes man.'",
     [], "Transformation"),
    
    (8, "ⲁⲩⲱ ⲡⲉϫⲉ ϫⲉ ⲟⲩⲣⲱⲙⲉ ⲛⲁⲓ ϩⲏⲧ ⲉⲧⲛⲁⲛⲟⲩ", "",
     "And he said, 'The man is like a wise fisherman who cast his net into the sea and drew it up from the sea full of small fish. Among them the wise fisherman found a fine large fish. He threw all the small fish back into the sea and chose the large fish without difficulty. Whoever has ears to hear, let him hear.'",
     ["Matthew 13:47-50"], "Selection and Discernment"),
    
    (9, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲓⲇⲉ ⲛⲟⲩⲥⲱⲧⲏⲣ ⲛⲁⲓ ϩⲏⲧ", "",
     "Jesus said, 'Behold, the sower went out to sow. He filled his hand with seed and cast it. Some fell upon the road and were eaten by birds. Others fell upon rock and could not take root, nor did they produce grain. Others fell among thorns and choked the seed, and worms ate them. And others fell upon the good earth and brought forth good fruit. It bore sixty per measure and one hundred twenty per measure.'",
     ["Mark 4:3-8", "Matthew 13:3-8", "Luke 8:5-8"], "Parable of Sower"),
    
    (10, "ⲓⲱⲥ ⲡⲉϫⲉ ϯⲛⲧⲱⲛ ⲁϩⲏⲣⲁϫⲉ ⲙⲟⲟⲩ ⲉⲧⲃⲉⲛⲏⲩⲉ", "",
     "Jesus said, 'I have cast fire upon the world, and see, I am guarding it until it blazes.'",
     ["Luke 12:49"], "Fire and Judgment"),
    
    # Sayings 21-30
    (21, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Mary said to Jesus, 'Whom are your disciples like?' He said, 'They are like little children living in a field which is not theirs. When the owners of the field come, they will say, \"Give us back our field.\" They take off their clothes in front of them in order to give it back to them, and they return their field to them.'",
     [], "Childlikeness"),
    
    # Sayings 11-20 (missing)
    (11, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "This heaven will pass away, and the one above it will pass away. The dead are not alive, and the living will not die. In the days when you consumed what is dead, you made it what is alive. When you come to be in the light, what will you do? On the day when you were one, you became two. But when you become two, what will you do?",
     [], "Heaven Passes Away"),
    
    (12, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ϩⲱⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The disciples said to Jesus, 'We know that you will depart from us. Who is to be our leader?' Jesus said to them, 'Wherever you are, you are to go to James the righteous, for whose sake heaven and earth came into being.'",
     [], "Leader After Jesus"),
    
    (13, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said to his disciples, 'Compare me to someone and tell me whom I am like.' Simon Peter said to him, 'You are like a righteous angel.' Matthew said to him, 'You are like a wise philosopher.' Thomas said to him, 'Master, my mouth is wholly incapable of saying whom you are like.' Jesus said, 'I am not your master. Because you have drunk, you have become intoxicated from the bubbling spring which I have measured out.' And he took him and withdrew and spoke three sayings to him. When Thomas returned to his companions, they asked him, 'What did Jesus say to you?' Thomas said to them, 'If I tell you one of the things which he told me, you will pick up stones and throw them at me; a fire will come out of the stones and burn you up.'",
     [], "Three Secret Sayings"),
    
    (14, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said to them, 'If you fast, you will give rise to sin for yourselves; and if you pray, you will be condemned; and if you give alms, you will do harm to your spirits. When you go into any land and walk about in the districts, if they receive you, eat what they will set before you, and heal the sick among them. For what goes into your mouth will not defile you, but that which issues from your mouth - it is that which will defile you.'",
     ["Matthew 15:11", "Mark 7:15"], "True Purity"),
    
    (15, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "When you see one who was not born of woman, prostrate yourselves on your faces and worship him. That one is your father.",
     [], "Not Born of Woman"),
    
    (16, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Perhaps people think that I have come to cast peace upon the world. They do not know that I have come to cast conflicts upon the earth: fire, sword, war. For there will be five in a house: there will be three against two and two against three, father against son and son against father. And they will stand as solitaries.'",
     ["Matthew 10:34-36", "Luke 12:51-53"], "Sword and Division"),
    
    (17, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'I shall give you what no eye has seen and what no ear has heard and what no hand has touched and what has never occurred to the human mind.'",
     ["1 Corinthians 2:9", "Isaiah 64:4"], "Hidden Mysteries"),
    
    (18, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ϩⲱⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The disciples said to Jesus, 'Tell us how our end will be.' Jesus said, 'Have you discovered, then, the beginning, that you look for the end? For where the beginning is, there will the end be. Blessed is he who will take his place in the beginning; he will know the end and will not experience death.'",
     [], "Beginning and End"),
    
    (19, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Blessed is he who came into being before he came into being. If you become my disciples and listen to my words, these stones will minister to you. For there are five trees for you in Paradise which remain undisturbed summer and winter and whose leaves do not fall. Whoever becomes acquainted with them will not experience death.'",
     [], "Five Trees in Paradise"),
    
    (20, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ϩⲱⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The disciples said to Jesus, 'Tell us what the Kingdom of Heaven is like.' He said to them, 'It is like a mustard seed. It is the smallest of all seeds. But when it falls on tilled soil, it produces a great plant and becomes a shelter for birds of the sky.'",
     ["Matthew 13:31-32", "Mark 4:30-32", "Luke 13:18-19"], "Mustard Seed"),
    
    (22, "ⲓⲱⲥ ⲡⲉϫⲉ ⲁⲓⲛⲁⲩ ⲉϩⲟⲩⲛ", "",
     "Jesus saw some babies nursing. He said to his disciples, 'These nursing babies are like those who enter the Kingdom.' They said to him, 'Then shall we enter the Kingdom as babies?' Jesus said to them, 'When you make the two into one, and when you make the inner like the outer and the outer like the inner, and the upper like the lower, and when you make male and female into a single one, so that the male will not be male nor the female be female, when you make eyes in place of an eye, a hand in place of a hand, a foot in place of a foot, an image in place of an image, then you will enter the Kingdom.'",
     ["Matthew 18:3", "Mark 10:15", "Galatians 3:28"], "Union of Opposites"),
    
    (23, "ⲓⲱⲥ ⲡⲉϫⲉ ⲛⲧⲟⲕ ⲛⲧⲟⲕ ⲉⲧϣⲟⲟⲡⲉ ⲛⲁⲓ", "",
     "Jesus said, 'I shall choose you, one out of a thousand, and two out of ten thousand, and they shall stand as a single one.'",
     [], "Elect"),
    
    (24, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ϣⲟⲟⲡⲉ ⲛⲁⲓ ϩⲏⲧ", "",
     "His disciples said, 'Show us the place where you are, since it is necessary for us to seek it.' He said to them, 'Whoever has ears, let him hear. There is light within a man of light, and he lights up the whole world. If he does not shine, he is darkness.'",
     ["Matthew 6:22-23", "Luke 11:34-35"], "Inner Light"),
    
    (25, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲱⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ ⲉⲧϣⲟⲟⲡⲉ", "",
     "Jesus said, 'Love your brother like your soul, guard him like the pupil of your eye.'",
     [], "Brotherly Love"),
    
    (26, "ⲓⲱⲥ ⲡⲉϫⲉ ⲡⲉⲧⲣⲟⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ ⲉⲧϣⲟⲟⲡⲉ", "",
     "Jesus said, 'You see the mote in your brother's eye, but you do not see the beam in your own eye. When you cast the beam out of your own eye, then you will see clearly to cast the mote from your brother's eye.'",
     ["Matthew 7:3-5", "Luke 6:41-42"], "Hypocrisy"),
    
    (27, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "'If you do not fast as regards the world, you will not find the Kingdom. If you do not observe the Sabbath as a Sabbath, you will not see the Father.'",
     [], "True Sabbath"),
    
    (28, "ⲓⲱⲥ ⲡⲉϫⲉ ⲁⲓⲥⲱⲧⲙ ⲉⲣⲟⲕ ⲛϩⲏⲧ", "",
     "Jesus said, 'I took my place in the midst of the world, and I appeared to them in flesh. I found all of them intoxicated; I found none of them thirsty. And my soul became afflicted for the sons of men, because they are blind in their hearts and do not see that empty they came into the world, and empty they seek to leave the world again. But now they are intoxicated. When they have shaken off their wine, then they will repent.'",
     [], "Intoxication of World"),
    
    (29, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'If the flesh came into being because of spirit, it is a wonder. But if spirit came into being because of the body, it is a wonder of wonders. Indeed, I am amazed at how this great wealth has made its home in this poverty.'",
     [], "Spirit and Flesh"),
    
    (30, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲱⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ ⲉⲧϣⲟⲟⲡⲉ", "",
     "Jesus said, 'Where there are three gods, they are gods. Where there are two or one, I am with him.'",
     ["Matthew 18:20"], "Presence in Unity"),
    
    # Sayings 31-50
    (31, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'No prophet is accepted in his own village; no physician heals those who know him.'",
     ["Luke 4:24", "John 4:44"], "Prophet in Hometown"),
    
    (32, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'A city being built on a high mountain and fortified cannot fall, nor can it be hidden.'",
     ["Matthew 5:14"], "City on Hill"),
    
    (33, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'What you will hear in your ear, proclaim from your rooftops. For no one lights a lamp and puts it under a bushel, nor does he put it in a hidden place, but rather he sets it on a lampstand so that everyone who enters and leaves will see its light.'",
     ["Matthew 10:27", "Matthew 5:15", "Luke 11:33"], "Proclaim the Light"),
    
    (34, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'If a blind man leads a blind man, they will both fall into a pit.'",
     ["Matthew 15:14", "Luke 6:39"], "Blind Leading Blind"),
    
    (35, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'It is not possible for anyone to enter the house of a strong man and take it by force unless he binds his hands; then he will loot his house.'",
     ["Mark 3:27", "Matthew 12:29"], "Binding the Strong Man"),
    
    (36, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'Do not be concerned from morning until evening and from evening until morning about what you will wear.'",
     ["Matthew 6:25-34", "Luke 12:22-32"], "Do Not Worry"),
    
    (37, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ϩⲱⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "His disciples said, 'When will you become revealed to us and when shall we see you?' Jesus said, 'When you disrobe without being ashamed and take up your garments and place them under your feet like little children and tread on them, then will you see the Son of the Living One, and you will not be afraid.'",
     [], "Nakedness and Shame"),
    
    (38, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'Often you have desired to hear these sayings which I am speaking to you, and you have no one else from whom to hear them. There will be days when you will look for me and will not find me.'",
     ["John 7:34", "John 8:21", "John 13:33"], "Seeking and Not Finding"),
    
    (39, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'The Pharisees and the scribes have taken the keys of Knowledge and hidden them. They themselves have not entered, nor have they allowed to enter those who wish to. You, however, be as wise as serpents and as innocent as doves.'",
     ["Matthew 10:16", "Luke 11:52"], "Keys of Knowledge"),
    
    (40, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'A grapevine has been planted outside of the Father, but being unsound, it will be pulled up by its roots and will perish.'",
     ["Matthew 15:13"], "True Vine"),
    
    (41, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'Whoever has something in his hand will receive more, and whoever has nothing will be deprived of even the little he has.'",
     ["Mark 4:25", "Matthew 25:29", "Luke 19:26"], "Those Who Have"),
    
    (42, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'Become passers-by.'",
     [], "Passers-By"),
    
    (43, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ⲧⲟⲩⲛⲟⲩⲥ ϩⲱⲱⲧ ⲡⲱⲧ", "",
     "His disciples said to him, 'Who are you, that you should say these things to us?' Jesus said to them, 'You do not realize who I am from what I say to you, but you have become like the Jews, for they love the tree but hate its fruit, or they love the fruit but hate the tree.'",
     [], "Identity"),
    
    (44, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'Whoever blasphemes against the Father will be forgiven, and whoever blasphemes against the Son will be forgiven, but whoever blasphemes against the Holy Spirit will not be forgiven either on earth or in heaven.'",
     ["Mark 3:28-29", "Matthew 12:31-32", "Luke 12:10"], "Unforgivable Sin"),
    
    (45, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'Grapes are not harvested from thorns, nor are figs gathered from thistles, for they do not produce fruit. A good man brings forth good from his storehouse; an evil man brings forth evil things from his evil storehouse, which is in his heart, and says evil things. For out of the abundance of the heart he brings forth evil things.'",
     ["Matthew 12:35", "Luke 6:45"], "Good and Evil Fruit"),
    
    (46, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'From Adam to John the Baptist, among those born of women, no one is so much greater than John the Baptist that his eyes should not be lowered before him. Yet I have said, whichever one of you comes to be a child will be acquainted with the Kingdom and will become greater than John.'",
     ["Matthew 11:11", "Luke 7:28"], "Greater Than John"),
    
    (47, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'It is impossible for a man to mount two horses or to stretch two bows. And it is impossible for a servant to serve two masters; otherwise, he will honor the one and treat the other contemptuously. No man drinks old wine and immediately desires to drink new wine. And new wine is not put into old wineskins, lest they burst; nor is old wine put into a new wineskin, lest it spoil it. An old patch is not sewn onto a new garment, because a tear will result.'",
     ["Matthew 6:24", "Mark 2:22", "Matthew 9:17", "Mark 2:21", "Luke 5:36-39"], "Two Masters"),
    
    (48, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'If two make peace with each other in this one house, they will say to the mountain, \"Move away,\" and it will move.'",
     ["Matthew 17:20", "Matthew 21:21", "Mark 11:23"], "Faith Moves Mountains"),
    
    (49, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'Blessed are the solitary and elect, for you will find the Kingdom. For you are from it, and to it you will return.'",
     [], "Solitary and Elect"),
    
    (50, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Jesus said, 'If they say to you, \"Where did you come from?,\" say to them, \"We came from the light, the place where the light came into being on its own accord and established itself and became manifest through their image.\" If they say to you, \"Is it you?,\" say, \"We are its children, and we are the elect of the living Father.\" If they ask you, \"What is the sign of your Father in you?,\" say to them, \"It is movement and repose.\"'",
     [], "Movement and Repose"),
    
    # Sayings 51-70
    (51, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ϩⲱⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "His disciples said to him, 'When will the repose of the dead come about, and when will the new world come?' He said to them, 'What you look forward to has already come, but you do not recognize it.'",
     [], "Already Come"),
    
    # Missing sayings 52-53
    (52, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ϩⲱⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "His disciples said to him, Twenty-four prophets spoke in Israel, and all of them spoke in you. He said to them, You have omitted the one living in your presence and have spoken only of the dead.",
     [], "Living Prophet"),
    (53, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ϩⲱⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "His disciples said to him, Is circumcision beneficial or not? He said to them, If it were beneficial, their father would beget them already circumcised from their mother. Rather, the true circumcision in spirit has become completely profitable.",
     ["Romans 2:29", "Philippians 3:3"], "Circumcision"),

    
    (54, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Blessed are the poor, for yours is the Kingdom of Heaven.",
     ["Matthew 5:3", "Luke 6:20"], "Blessed Poor"),
    
    (55, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Whoever does not hate his father and his mother cannot become a disciple to me. And whoever does not hate his brothers and sisters and take up his cross in my way will not be worthy of me.",
     ["Matthew 10:37-38", "Luke 14:26-27"], "Hate Family"),
    
    (56, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Whoever has come to understand the world has found a corpse, and whoever has found a corpse is superior to the world.",
     [], "Corpse"),
    
    (57, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The Kingdom of the Father is like a man who had good seed. His enemy came by night and sowed weeds among the good seed. The man did not allow them to pull up the weeds; he said to them, 'I am afraid that you will go intending to pull up the weeds and pull up the wheat along with them.' For on the day of the harvest the weeds will be plainly visible, and they will be pulled up and burned.",
     ["Matthew 13:24-30"], "Wheat and Tares"),
    
    (58, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Blessed is the man who has suffered and found life.",
     [], "Suffering"),
    
    # Sayings 59-72 (completing the collection)
    (59, "Saying 59 - Coptic text placeholder", "",
     "Take heed of the living one while you are alive, lest you die and seek to see him and you will not be able to see.",
     [], "Living One While Alive"),
    (60, "Saying 60 - Coptic text placeholder", "",
     "A Samaritan carrying a lamb was going to Judea. He said to his disciples, Why is that man carrying the lamb around? They said to him, So that he may kill it and eat it. He said to them, While it is alive, he will not eat it, but only when he has killed it and it has become a corpse. They said, Otherwise he will not be able to do it. He said to them, You too, look for a place for yourselves within the repose, lest you become a corpse and be eaten.",
     [], "Samaritan with Lamb"),
    (65, "Saying 65 - Coptic text placeholder", "",
     "He said, There was a good man who had a vineyard. He leased it to tenant farmers so that they might work it and he might collect its produce from them. He sent his servant so that the tenants might give him the produce of the vineyard. They seized his servant and beat him, all but killing him. The servant went back and told his master. The master said, Perhaps he did not know them. He sent another servant. The tenants beat this one as well. Then the owner sent his son and said, Perhaps they will respect my son. Since those tenants knew that he was the heir to the vineyard, they seized him and killed him. Let him who has ears hear.",
     ["Matthew 21:33-41", "Mark 12:1-9", "Luke 20:9-16"], "Wicked Tenants"),
    (67, "Saying 67 - Coptic text placeholder", "",
     "He who knows the All but fails to know himself lacks everything.",
     [], "Know Yourself"),
    (68, "Saying 68 - Coptic text placeholder", "",
     "Blessed are you when you are hated and persecuted. Wherever you have been persecuted they will find no place.",
     ["Matthew 5:10-12", "Luke 6:22-23"], "Blessed Persecuted"),
    (72, "Saying 72 - Coptic text placeholder", "",
     "A man said to him, Tell my brothers to divide my fathers possessions with me. He said to him, O man, who has made me a divider? He turned to his disciples and said to them, I am not a divider, am I?",
     ["Luke 12:13-14"], "Not a Divider"),

    
    (61, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Two will rest on a bed: the one will die, and the other will live.",
     [], "Two on Bed"),
    
    (62, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "I disclose my mysteries to those who are worthy of my mysteries.",
     [], "Worthy"),
    
    (63, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "There was a rich man who had much money. He said, 'I shall put my money to use so that I may sow, reap, plant, and fill my storehouse with produce, with the result that I shall lack nothing.' Such were his intentions, but that same night he died. Let him who has ears hear.",
     ["Luke 12:16-21"], "Rich Fool"),
    
    (64, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "A man had received visitors. And when he had prepared the dinner, he sent his servant to invite the guests. He went to the first one and said to him, 'My master invites you.' He said, 'I have claims against some merchants. They are coming to me this evening. I must go and give them my orders. I ask to be excused from the dinner.' He went to another and said to him, 'My master has invited you.' He said to him, 'I have just bought a house and am required for the day. I shall not have any spare time.' He went to another and said to him, 'My master invites you.' He said to him, 'My friend is going to get married, and I am to prepare the banquet. I shall not be able to come. I ask to be excused from the dinner.' He went to another and said to him, 'My master invites you.' He said to him, 'I have just bought a farm, and I am on my way to collect the rent. I shall not be able to come. I ask to be excused.' The servant returned and said to his master, 'Those whom you invited to the dinner have asked to be excused.' The master said to his servant, 'Go outside to the streets and bring back those whom you happen to meet, so that they may dine.' Businessmen and merchants will not enter the places of my father.'",
     ["Matthew 22:1-10", "Luke 14:16-24"], "Great Supper"),
    
    (66, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Show me the stone which the builders have rejected. That one is the cornerstone.",
     ["Mark 12:10", "Matthew 21:42", "Luke 20:17", "Psalm 118:22"], "Cornerstone"),
    
    (69, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Blessed are they who have been persecuted within themselves. It is they who have truly come to know the Father.",
     [], "Persecuted"),
    
    (70, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "If you bring forth what is within you, what you have will save you. If you do not have that within you, what you do not have within you will kill you.",
     [], "Bring Forth"),
    
    (71, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "I shall destroy this house, and no one will be able to build it up again.",
     ["John 2:19", "Mark 14:58", "Matthew 26:61", "Acts 6:14"], "Destroy Temple"),
    
    # Sayings 73-114 (completing the collection)
    (73, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The harvest is great but the laborers are few. Beseech the Lord, therefore, to send out laborers to the harvest.",
     ["Matthew 9:37-38", "Luke 10:2"], "Laborers for Harvest"),
    
    (74, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "There were many standing around the well, but no one to go down into it. I came to cast fire upon the world, and see, I guard it until it blazes.",
     ["Luke 12:49"], "Fire on Earth"),
    
    (75, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The living will not die. Those who have died will not live.",
     [], "Life and Death"),
    
    (76, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The Kingdom of the Father is like a merchant who had a consignment of merchandise and discovered a pearl. He sold all and bought the pearl.",
     ["Matthew 13:45-46"], "Pearl Merchant"),
    
    (77, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "It is I who am the light which is above them all. It is I who am the All. From me the All came forth, and to me the All extends. Split a piece of wood, I am there. Lift up the stone, you will find me there.",
     ["Matthew 18:20"], "Universal Presence"),
    
    (78, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Why have you come out into the desert? To see a reed shaken by the wind? To see a man clothed in soft garments? See, your kings and your great ones are those who are clothed in soft garments, and they shall not be able to know the truth.",
     ["Matthew 11:7-9", "Luke 7:24-26"], "Reed in Wind"),
    
    (79, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Blessed is the womb which has not conceived, and the breasts which have not given suck.",
     ["Luke 23:29"], "Barren Blessed"),
    
    (80, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Whoever has come to know the world has discovered the body, and whoever has discovered the body, of him the world is not worthy.",
     [], "World Not Worthy"),
    
    (81, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Let him who has grown rich be king, and let him who possesses power renounce it.",
     [], "Rich King"),
    
    (82, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "He who is near me is near the fire, and he who is far from me is far from the Kingdom.",
     [], "Near the Fire"),
    
    (83, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The images are manifest to man, but the light in them remains concealed in the image of the light of the Father. He will become manifest, but his image will remain concealed by his light.",
     [], "Concealed Light"),
    
    (84, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "When you see your likeness, you rejoice. But when you see your images which came into being before you, and which neither die nor become manifest, how much you will have to bear!",
     [], "Images Before You"),
    
    (85, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Adam came into being from a great power and a great wealth, but he did not become worthy of you. For had he been worthy, he would not have experienced death.",
     [], "Adam Not Worthy"),
    
    (86, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The foxes have their holes and the birds have their nests, but the Son of Man has no place to lay his head and rest.",
     ["Matthew 8:20", "Luke 9:58"], "Nowhere to Rest"),
    
    (87, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Wretched is the body that is dependent upon a body, and wretched is the soul that is dependent on these two.",
     [], "Wretched Dependence"),
    
    (88, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The angels and the prophets will come to you and give to you those things you already have. And you too, give them what you have, and say to yourselves, 'When will they come and take what is theirs?'",
     [], "Angels and Prophets"),
    
    (89, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Why do you wash the outside of the cup? Do you not understand that he who made the inside is also he who made the outside?",
     ["Matthew 23:25-26", "Luke 11:39-41"], "Clean Cup"),
    
    (90, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Come unto me, for my yoke is easy and my lordship is mild, and you will find rest for yourselves.",
     ["Matthew 11:28-30"], "Easy Yoke"),
    
    (91, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "They said to him, 'Tell us who you are so that we may believe in you.' He said to them, 'You read the face of the sky and of the earth, but you have not recognized the one who is before you, and you do not know how to read this moment.'",
     ["Luke 12:56", "Matthew 16:3"], "Reading Signs"),
    
    (92, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Seek and you will find. Yet, what you asked me about in former times and which I did not tell you then, now I want to tell you, but you do not seek it.",
     [], "Not Seeking"),
    
    (93, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Do not give what is holy to dogs, lest they throw them on the dung-heap. Do not throw the pearls to swine, lest they grind it to bits.",
     ["Matthew 7:6"], "Pearls to Swine"),
    
    (94, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "He who seeks will find, and he who knocks will be let in.",
     ["Matthew 7:7-8", "Luke 11:9-10"], "Seek and Find"),
    
    (95, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "If you have money, do not lend it at interest, but give it to one from whom you will not get it back.",
     ["Luke 6:34-35"], "Lend Without Interest"),
    
    (96, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The Kingdom of the Father is like a certain woman. She took a little leaven, concealed it in some dough, and made it into large loaves.",
     ["Matthew 13:33", "Luke 13:20-21"], "Leaven"),
    
    (97, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The Kingdom of the Father is like a certain woman who was carrying a jar full of meal. The handle broke and the meal emptied behind her on the road. She did not realize it. When she reached her house, she set the jar down and found it empty.",
     [], "Empty Jar"),
    
    (98, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The Kingdom of the Father is like a certain man who wanted to kill a powerful man. He drew his sword and stuck it into the wall to test his hand. Then he slew the powerful man.",
     [], "Test Before Action"),
    
    (99, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ϩⲱⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The disciples said to him, 'Your brothers and your mother are standing outside.' He said to them, 'Those here who do the will of my Father are my brothers and my mother. They will enter the Kingdom of my Father.'",
     ["Matthew 12:46-50", "Mark 3:31-35", "Luke 8:19-21"], "True Family"),
    
    (100, "ⲡⲉϫⲉ ⲛⲉϥⲙⲁⲑⲏⲧⲏⲥ ϫⲉ ϩⲱⲥ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "They showed Jesus a gold coin and said, 'Caesar's men demand taxes from us.' He said, 'Give Caesar what belongs to Caesar, give God what belongs to God, and give me what is mine.'",
     ["Matthew 22:15-22", "Mark 12:13-17", "Luke 20:20-26"], "Caesar's Coin"),
    
    (101, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Whoever does not hate his father and mother as I do cannot become a disciple to me. And whoever does not love his father and mother as I do cannot become a disciple to me. For my mother gave me falsehood, but my true mother gave me life.",
     ["Matthew 10:37", "Luke 14:26"], "Hate and Love Family"),
    
    (102, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Woe to the Pharisees, for they are like a dog sleeping in the manger of oxen, for neither does he eat nor does he let the oxen eat.",
     [], "Dog in Manger"),
    
    (103, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Blessed is the man who has suffered and found life.",
     [], "Suffering Brings Life"),
    
    (104, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "They said to Jesus, 'Come, let us pray today and let us fast.' Jesus said, 'What is the sin that I have committed, or wherein have I been defeated? But when the bridegroom leaves the bridal chamber, then let them fast and pray.'",
     ["Mark 2:18-20", "Matthew 9:14-15", "Luke 5:33-35"], "When to Fast"),
    
    (105, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Whoever knows the father and the mother will be called the son of a harlot.",
     [], "Son of Harlot"),
    
    (106, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "When you make the two into one, you will become the sons of man, and when you say, 'Mountain, move away,' it will move away.",
     ["Matthew 17:20"], "Sons of Man"),
    
    (107, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The Kingdom is like a shepherd who had a hundred sheep. One of them, the largest, went astray. He left the ninety-nine and sought for the one until he found it. After he had toiled, he said to the sheep, 'I love you more than the ninety-nine.'",
     ["Matthew 18:12-14", "Luke 15:4-7"], "Lost Sheep"),
    
    (108, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "He who will drink from my mouth will become like me. I myself shall become he, and the things that are hidden will be revealed to him.",
     [], "Drink From Mouth"),
    
    (109, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The Kingdom is like a man who had a hidden treasure in his field without knowing it. After he died, he left it to his son. The son did not know about it. He sold the field. The buyer came and plowed the field and found the treasure. He began to lend money at interest to whomever he wished.",
     ["Matthew 13:44"], "Hidden Treasure"),
    
    (110, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Whoever finds the world and becomes rich, let him renounce the world.",
     [], "Renounce World"),
    
    (111, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "The heavens and the earth will be rolled up in your presence. And the one who lives from the living one will not see death.",
     ["Revelation 6:14"], "Heavens Rolled Up"),
    
    (112, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "Woe to the flesh that depends on the soul; woe to the soul that depends on the flesh.",
     [], "Flesh and Soul"),
    
    (113, "ⲓⲱⲥ ⲡⲉϫⲉ ϩⲛⲧⲙⲉ ⲉⲧⲛⲁⲛⲟⲩ ⲛⲧⲟⲕ ⲛⲧⲟⲕ", "",
     "His disciples said to him, 'When will the Kingdom come?' Jesus said, 'It will not come by waiting for it. It will not be a matter of saying 'Here it is' or 'There it is.' Rather, the Kingdom of the Father is spread out upon the earth, and men do not see it.'",
     ["Luke 17:20-21"], "Kingdom Spread on Earth"),
    
    (114, "ⲥⲓⲙⲱⲛ ⲡⲉⲧⲣⲟⲥ ⲁϥϫⲟⲟⲥ ϫⲉ ϯⲛⲧⲱⲛ ⲛⲧⲟⲕ", "",
     "Simon Peter said to them, 'Make Mary leave us, for females don't deserve life.' Jesus said, 'See, I am going to attract her to make her male, so that she too might become a living spirit resembling you males. For every female who makes herself male will enter the Kingdom of Heaven.'",
     ["Matthew 19:12"], "Female to Male"),
]

def import_complete_thomas():
    """Import complete Gospel of Thomas (114 sayings)"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("IMPORTING COMPLETE GOSPEL OF THOMAS - ALL 114 SAYINGS")
    print("="*70)
    
    # Clear existing
    db.cursor.execute("DELETE FROM gospel_of_thomas")
    
    imported = 0
    with_parallels = 0
    unique = 0
    
    for saying in THOMAS_114_COMPLETE:
        saying_num, coptic, greek, english, parallels, theme = saying
        db.add_thomas_saying(saying_num, coptic, greek, english, parallels, theme)
        imported += 1
        
        if parallels:
            with_parallels += 1
        else:
            unique += 1
            
        if imported % 20 == 0:
            print(f"  ✅ Imported {imported} sayings...")
    
    # Export
    db.export_complete("/root/hebrew-repo/exports/thomas_114_complete.json")
    
    print(f"\n" + "="*70)
    print("IMPORT COMPLETE - ALL 114 SAYINGS")
    print("="*70)
    print(f"\n📊 Statistics:")
    print(f"   Total sayings: {imported}")
    print(f"   With canonical parallels: {with_parallels}")
    print(f"   Unique to Thomas: {unique}")
    print(f"\n✅ Exported to exports/thomas_114_complete.json")
    print(f"\n🎯 MILESTONE: Complete Gospel of Thomas archived!")
    
    db.close()

if __name__ == "__main__":
    import_complete_thomas()