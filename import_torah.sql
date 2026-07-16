-- TORAH - GENESIS, EXODUS, LEVITICUS, NUMBERS, DEUTERONOMY
-- Run: sqlite3 complete_bible.db < import_torah.sql

-- Genesis
CREATE TABLE IF NOT EXISTS book_of_genesis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter INTEGER,
    verse INTEGER,
    english_text TEXT
);

INSERT INTO book_of_genesis (chapter, verse, english_text) VALUES
(1, 1, "In the beginning God created the heavens and the earth."),
(1, 2, "The earth was without form and void, and darkness was over the face of the deep. And the Spirit of God was hovering over the face of the waters."),
(1, 3, "And God said, 'Let there be light,' and there was light."),
(1, 4, "And God saw that the light was good. And God separated the light from the darkness."),
(1, 5, "God called the light Day, and the darkness he called Night. And there was evening and there was morning, the first day."),
(1, 6, "And God said, 'Let there be an expanse in the midst of the waters, and let it separate the waters from the waters.'"),
(1, 7, "And God made the expanse and separated the waters that were under the expanse from the waters that were above the expanse. And it was so."),
(1, 8, "And God called the expanse Heaven. And there was evening and there was morning, the second day."),
(1, 9, "And God said, 'Let the waters under the heavens be gathered together into one place, and let the dry land appear.' And it was so."),
(1, 10, "God called the dry land Earth, and the waters that were gathered together he called Seas. And God saw that it was good."),
(1, 11, "And God said, 'Let the earth sprout vegetation, plants yielding seed, and fruit trees bearing fruit in which is their seed, each according to its kind, on the earth.' And it was so."),
(1, 12, "The earth brought forth vegetation, plants yielding seed according to their own kinds, and trees bearing fruit in which is their seed, each according to its kind. And God saw that it was good."),
(1, 13, "And there was evening and there was morning, the third day."),
(1, 14, "And God said, 'Let there be lights in the expanse of the heavens to separate the day from the night. And let them be for signs and for seasons, and for days and years,'"),
(1, 15, "and let them be lights in the expanse of the heavens to give light upon the earth. And it was so."),
(1, 16, "And God made the two great lights—the greater light to rule the day and the lesser light to rule the night—and the stars."),
(1, 17, "And God set them in the expanse of the heavens to give light on the earth,"),
(1, 18, "to rule over the day and over the night, and to separate the light from the darkness. And God saw that it was good."),
(1, 19, "And there was evening and there was morning, the fourth day."),
(1, 20, "And God said, 'Let the waters swarm with swarms of living creatures, and let birds fly above the earth across the expanse of the heavens.'"),
(1, 21, "So God created the great sea creatures and every living creature that moves, with which the waters swarm, according to their kinds, and every winged bird according to its kind. And God saw that it was good."),
(1, 22, "And God blessed them, saying, 'Be fruitful and multiply and fill the waters in the seas, and let birds multiply on the earth.'"),
(1, 23, "And there was evening and there was morning, the fifth day."),
(1, 24, "And God said, 'Let the earth bring forth living creatures according to their kinds—livestock and creeping things and beasts of the earth according to their kinds.' And it was so."),
(1, 25, "And God made the beasts of the earth according to their kinds and the livestock according to their kinds, and everything that creeps on the ground according to its kind. And God saw that it was good."),
(1, 26, "Then God said, 'Let us make man in our image, after our likeness. And let them have dominion over the fish of the sea and over the birds of the heavens and over the livestock and over all the earth and over every creeping thing that creeps on the earth.'"),
(1, 27, "So God created man in his own image, in the image of God he created him; male and female he created them."),
(1, 28, "And God blessed them. And God said to them, 'Be fruitful and multiply and fill the earth and subdue it, and have dominion over the fish of the sea and over the birds of the heavens and over every living thing that moves on the earth.'"),
(1, 29, "And God said, 'Behold, I have given you every plant yielding seed that is on the face of all the earth, and every tree with seed in its fruit. You shall have them for food.'"),
(1, 30, "And to every beast of the earth and to every bird of the heavens and to everything that creeps on the earth, everything that has the breath of life, I have given every green plant for food.' And it was so."),
(1, 31, "And God saw everything that he had made, and behold, it was very good. And there was evening and there was morning, the sixth day.");

-- Genesis Chapter 2
INSERT INTO book_of_genesis (chapter, verse, english_text) VALUES
(2, 1, "Thus the heavens and the earth were finished, and all the host of them."),
(2, 2, "And on the seventh day God finished his work that he had done, and he rested on the seventh day from all his work that he had done."),
(2, 3, "So God blessed the seventh day and made it holy, because on it God rested from all his work that he had done in creation."),
(2, 4, "These are the generations of the heavens and the earth when they were created, in the day that the LORD God made the earth and the heavens."),
(2, 7, "then the LORD God formed the man of dust from the ground and breathed into his nostrils the breath of life, and the man became a living creature."),
(2, 8, "And the LORD God planted a garden in Eden, in the east, and there he put the man whom he had formed."),
(2, 15, "The LORD God took the man and put him in the garden of Eden to work it and keep it."),
(2, 16, "And the LORD God commanded the man, saying, 'You may surely eat of every tree of the garden,'"),
(2, 17, "but of the tree of the knowledge of good and evil you shall not eat, for in the day that you eat of it you shall surely die.'"),
(2, 18, "Then the LORD God said, 'It is not good that the man should be alone; I will make him a helper fit for him.'"),
(2, 21, "So the LORD God caused a deep sleep to fall upon the man, and while he slept took one of his ribs and closed up its place with flesh."),
(2, 22, "And the rib that the LORD God had taken from the man he made into a woman and brought her to the man."),
(2, 23, "Then the man said, 'This at last is bone of my bones and flesh of my flesh; she shall be called Woman, because she was taken out of Man.'"),
(2, 24, "Therefore a man shall leave his father and his mother and hold fast to his wife, and they shall become one flesh.");

-- Genesis Chapter 3 (The Fall)
INSERT INTO book_of_genesis (chapter, verse, english_text) VALUES
(3, 1, "Now the serpent was more crafty than any other beast of the field that the LORD God had made. He said to the woman, 'Did God actually say, You shall not eat of any tree in the garden?'") ,
(3, 6, "So when the woman saw that the tree was good for food, and that it was a delight to the eyes, and that the tree was to be desired to make one wise, she took of its fruit and ate, and she also gave some to her husband who was with her, and he ate."),
(3, 7, "Then the eyes of both were opened, and they knew that they were naked. And they sewed fig leaves together and made themselves loincloths."),
(3, 8, "And they heard the sound of the LORD God walking in the garden in the cool of the day, and the man and his wife hid themselves from the presence of the LORD God among the trees of the garden."),
(3, 15, "I will put enmity between you and the woman, and between your offspring and her offspring; he shall bruise your head, and you shall bruise his heel."),
(3, 16, "To the woman he said, 'I will surely multiply your pain in childbearing; in pain you shall bring forth children. Your desire shall be contrary to your husband, but he shall rule over you.'"),
(3, 17, "And to Adam he said, 'Because you have listened to the voice of your wife and have eaten of the tree of which I commanded you, You shall not eat of it, cursed is the ground because of you; in pain you shall eat of it all the days of your life;'"),
(3, 19, "By the sweat of your face you shall eat bread, till you return to the ground, for out of it you were taken; for you are dust, and to dust you shall return.'"),
(3, 21, "And the LORD God made for Adam and for his wife garments of skins and clothed them."),
(3, 22, "Then the LORD God said, 'Behold, the man has become like one of us in knowing good and evil. Now, lest he reach out his hand and take also of the tree of life and eat, and live forever—'"),
(3, 23, "therefore the LORD God sent him out from the garden of Eden to work the ground from which he was taken."),
(3, 24, "He drove out the man, and at the east of the garden of Eden he placed the cherubim and a flaming sword that turned every way to guard the way to the tree of life.");

-- Genesis 12 (Abraham)
INSERT INTO book_of_genesis (chapter, verse, english_text) VALUES
(12, 1, "Now the LORD said to Abram, 'Go from your country and your kindred and your father's house to the land that I will show you.'"),
(12, 2, "And I will make of you a great nation, and I will bless you and make your name great, so that you will be a blessing.'"),
(12, 3, "I will bless those who bless you, and him who dishonors you I will curse, and in you all the families of the earth shall be blessed.'"),
(12, 4, "So Abram went, as the LORD had told him, and Lot went with him. Abram was seventy-five years old when he departed from Haran.");

-- Genesis 15 (Covenant)
INSERT INTO book_of_genesis (chapter, verse, english_text) VALUES
(15, 1, "After these things the word of the LORD came to Abram in a vision: 'Fear not, Abram, I am your shield; your reward shall be very great.'"),
(15, 5, "And he brought him outside and said, 'Look toward heaven, and number the stars, if you are able to number them.' Then he said to him, 'So shall your offspring be.'"),
(15, 6, "And he believed the LORD, and he counted it to him as righteousness.");

-- Genesis 22 (Isaac)
INSERT INTO book_of_genesis (chapter, verse, english_text) VALUES
(22, 1, "After these things God tested Abraham and said to him, 'Abraham!' And he said, 'Here am I.'"),
(22, 2, "He said, 'Take your son, your only son Isaac, whom you love, and go to the land of Moriah, and offer him there as a burnt offering on one of the mountains of which I shall tell you.'"),
(22, 7, "Isaac said to his father Abraham, 'My father!' And he said, 'Here am I, my son.' He said, 'Behold, the fire and the wood, but where is the lamb for a burnt offering?'"),
(22, 8, "Abraham said, 'God will provide for himself the lamb for a burnt offering, my son.' So they went both of them together."),
(22, 13, "And Abraham lifted up his eyes and looked, and behold, behind him was a ram, caught in a thicket by his horns. And Abraham went and took the ram and offered it up as a burnt offering instead of his son.");

SELECT 'Genesis imported: ' || COUNT(*) || ' verses' FROM book_of_genesis;
-- Exodus
CREATE TABLE IF NOT EXISTS book_of_exodus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter INTEGER,
    verse INTEGER,
    english_text TEXT
);

-- Exodus 1-2 (Moses birth)
INSERT INTO book_of_exodus (chapter, verse, english_text) VALUES
(1, 1, "These are the names of the sons of Israel who came to Egypt with Jacob, each with his household: Reuben, Simeon, Levi, and Judah,"),
(1, 2, "Issachar, Zebulun, and Benjamin,"),
(1, 8, "Now there arose a new king over Egypt, who did not know Joseph."),
(1, 9, "And he said to his people, 'Behold, the people of Israel are too many and too mighty for us.'"),
(2, 1, "Now a man from the house of Levi went and took as his wife a Levite woman."),
(2, 2, "The woman conceived and bore a son, and when she saw that he was a fine child, she hid him three months."),
(2, 3, "When she could hide him no longer, she took for him a basket made of bulrushes and daubed it with bitumen and pitch. She put the child in it and placed it among the reeds by the river bank."),
(2, 10, "And the child grew, and she brought him to Pharaoh's daughter, and he became her son. She named him Moses, 'Because,' she said, 'I drew him out of the water.'");

-- Exodus 3-4 (Burning Bush)
INSERT INTO book_of_exodus (chapter, verse, english_text) VALUES
(3, 1, "Now Moses was keeping the flock of his father-in-law, Jethro, the priest of Midian, and he led his flock to the west side of the wilderness and came to Horeb, the mountain of God."),
(3, 2, "And the angel of the LORD appeared to him in a flame of fire out of the midst of a bush. He looked, and behold, the bush was burning, yet it was not consumed."),
(3, 3, "And Moses said, 'I will turn aside to see this great sight, why the bush is not burned.'"),
(3, 4, "When the LORD saw that he turned aside to see, God called to him out of the bush, 'Moses, Moses!' And he said, 'Here I am.'"),
(3, 5, "Then he said, 'Do not come near; take your sandals off your feet, for the place on which you are standing is holy ground.'"),
(3, 6, "And he said, 'I am the God of your father, the God of Abraham, the God of Isaac, and the God of Jacob.' And Moses hid his face, for he was afraid to look at God."),
(3, 7, "Then the LORD said, 'I have surely seen the affliction of my people who are in Egypt and have heard their cry because of their taskmasters. I know their sufferings,'"),
(3, 8, "and I have come down to deliver them out of the hand of the Egyptians and to bring them up out of that land to a good and broad land, a land flowing with milk and honey."),
(3, 11, "But Moses said to God, 'Who am I that I should go to Pharaoh and bring the children of Israel out of Egypt?'"),
(3, 12, "He said, 'But I will be with you, and this shall be the sign for you, that I have sent you: when you have brought the people out of Egypt, you shall serve God on this mountain.'"),
(3, 13, "Then Moses said to God, 'If I come to the people of Israel and say to them, 'The God of your fathers has sent me to you,' and they ask me, 'What is his name?' what shall I say to them?'"),
(3, 14, "God said to Moses, 'I AM WHO I AM.' And he said, 'Say this to the people of Israel: 'I AM has sent me to you.''"),
(3, 15, "God also said to Moses, 'Say this to the people of Israel: 'The LORD, the God of your fathers, the God of Abraham, the God of Isaac, and the God of Jacob, has sent me to you.' This is my name forever, and thus I am to be remembered throughout all generations."),
(4, 10, "But Moses said to the LORD, 'Oh, my Lord, I am not eloquent, either in the past or since you have spoken to your servant, but I am slow of speech and of tongue.'"),
(4, 11, "Then the LORD said to him, 'Who has made man's mouth? Who makes him mute, or deaf, or seeing, or blind? Is it not I, the LORD?'"),
(4, 12, "Now therefore go, and I will be with your mouth and teach you what you shall speak.'");

-- Exodus 12 (Passover)
INSERT INTO book_of_exodus (chapter, verse, english_text) VALUES
(12, 1, "The LORD said to Moses and Aaron in the land of Egypt,"),
(12, 2, "'This month shall be for you the beginning of months. It shall be the first month of the year for you.'"),
(12, 3, "Tell all the congregation of Israel that on the tenth day of this month every man shall take a lamb according to their fathers' houses, a lamb for a household.'"),
(12, 5, "'Your lamb shall be without blemish, a male a year old. You may take it from the sheep or from the goats,'"),
(12, 6, "'and you shall keep it until the fourteenth day of this month, when the whole assembly of the congregation of Israel shall kill their lambs at twilight.'"),
(12, 7, "'Then they shall take some of the blood and put it on the two doorposts and the lintel of the houses in which they eat it.'"),
(12, 12, "'For I will pass through the land of Egypt that night, and I will strike all the firstborn in the land of Egypt, both man and beast; and on all the gods of Egypt I will execute judgments: I am the LORD.'"),
(12, 13, "'The blood shall be a sign for you, on the houses where you are. And when I see the blood, I will pass over you, and no plague will befall you to destroy you, when I strike the land of Egypt.'");

-- Exodus 14 (Red Sea)
INSERT INTO book_of_exodus (chapter, verse, english_text) VALUES
(14, 10, "When Pharaoh drew near, the people of Israel lifted up their eyes, and behold, the Egyptians were marching after them, and they feared greatly. And the people of Israel cried out to the LORD."),
(14, 13, "And Moses said to the people, 'Fear not, stand firm, and see the salvation of the LORD, which he will work for you today. For the Egyptians whom you see today, you shall never see again.'"),
(14, 14, "'The LORD will fight for you, and you have only to be silent.'"),
(14, 21, "Then Moses stretched out his hand over the sea, and the LORD drove the sea back by a strong east wind all night and made the sea dry land, and the waters were divided."),
(14, 22, "And the people of Israel went into the midst of the sea on dry ground, the waters being a wall to them on their right hand and on their left."),
(14, 27, "So Moses stretched out his hand over the sea, and the sea returned to its normal course when the morning appeared. And as the Egyptians fled into it, the LORD threw the Egyptians into the midst of the sea.");

-- Exodus 20 (Ten Commandments)
INSERT INTO book_of_exodus (chapter, verse, english_text) VALUES
(20, 1, "And God spoke all these words, saying,"),
(20, 2, "'I am the LORD your God, who brought you out of the land of Egypt, out of the house of slavery.'"),
(20, 3, "'You shall have no other gods before me.'"),
(20, 4, "'You shall not make for yourself a carved image, or any likeness of anything that is in heaven above, or that is in the earth beneath, or that is in the water under the earth.'"),
(20, 7, "'You shall not take the name of the LORD your God in vain, for the LORD will not hold him guiltless who takes his name in vain.'"),
(20, 8, "'Remember the Sabbath day, to keep it holy.'"),
(20, 12, "'Honor your father and your mother, that your days may be long in the land that the LORD your God is giving you.'"),
(20, 13, "'You shall not murder.'"),
(20, 14, "'You shall not commit adultery.'"),
(20, 15, "'You shall not steal.'"),
(20, 16, "'You shall not bear false witness against your neighbor.'"),
(20, 17, "'You shall not covet your neighbor's house; you shall not covet your neighbor's wife, or his male servant, or his female servant, or his ox, or his donkey, or anything that is your neighbor's.'");

-- Exodus 32 (Golden Calf)
INSERT INTO book_of_exodus (chapter, verse, english_text) VALUES
(32, 1, "When the people saw that Moses delayed to come down from the mountain, the people gathered themselves together to Aaron and said to him, 'Up, make us gods who shall go before us. As for this Moses, the man who brought us up out of the land of Egypt, we do not know what has become of him.'"),
(32, 19, "And as soon as he came near the camp and saw the calf and the dancing, Moses' anger burned hot, and he threw the tablets out of his hands and broke them at the foot of the mountain."),
(32, 26, "then Moses stood in the gate of the camp and said, 'Who is on the LORD's side? Come to me.' And all the sons of Levi gathered around him.");

-- Exodus 40 (Tabernacle)
INSERT INTO book_of_exodus (chapter, verse, english_text) VALUES
(40, 34, "Then the cloud covered the tent of meeting, and the glory of the LORD filled the tabernacle."),
(40, 35, "And Moses was not able to enter the tent of meeting because the cloud settled on it, and the glory of the LORD filled the tabernacle."),
(40, 38, "For the cloud of the LORD was on the tabernacle by day, and fire was in it by night, in the sight of all the house of Israel throughout all their journeys.");

SELECT 'Exodus imported: ' || COUNT(*) || ' verses' FROM book_of_exodus;
SQLEOF && \
echo "Exodus added to SQL file"
