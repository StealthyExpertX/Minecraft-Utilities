from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2
from copy import deepcopy
import numpy
from numpy import zeros
import random
from pymclevel import TAG_List, TAG_Byte, TAG_Int, TAG_Compound, TAG_Short, TAG_Float, TAG_Double, TAG_String, TAG_Long

#MCEdit Filter Created By StealthyExpertX

#AB @abrightmoore thanks barrowed some source from your chester filter for your block utilities

#Filter crates a chest that has each slot populated with a minecraft:chest 
#item with the blockentitydata tag that has randomized loot_table ids and seed value of 0 
#which equals a randomized seed every time the chest item is placed

Effects = {
"Facing East": 5,
"Facing West": 4,
"Facing South": 3,
"Facing North": 2,
}

EffectKeys = ()
for key in Effects.keys():
    EffectKeys = EffectKeys + (key,)

Smokeboxs = {
	"(abandoned_mineshaft)": "abandoned_mineshaft",
	"(desert_pyramid)": "desert_pyramid",
	"(end_city_treasure)": "end_city_treasure",
	"(igloo_chest)": "igloo_chest",
	"(jungle_temple)": "jungle_temple",
	"(simple_dungeon)": "simple_dungeon",
	"(spawn_bonus_chest)": "spawn_bonus_chest",
	"(stronghold_corridor)": "stronghold_corridor",
	"(stronghold_crossing)": "stronghold_crossing",
	"(stronghold_library)": "stronghold_library",
	"(village_blacksmith)": "village_blacksmith",
	"(nether_bridge)": "nether_bridge",
	}

inputs = (
	("(Lucky Crates Filter Creates Chest With Loot Tables)", "label"),
	("(Loot ID)", tuple(Smokeboxs.keys())),
	("(Loot Seed)", 0),
	("(Chest Block)", EffectKeys),
	("(Random Loot ID)", False), 
	("(Placeable Chest)", True),
	("(1.11+)", False),
	)

def setBlockIfEmpty(level, (block, data), x, y, z):
	tempBlock = level.blockAt(x,y,z)
	if tempBlock == 0:
		setBlock(level, (block, data), x, y, z)

def setBlock(level, (block, data), x, y, z):
	level.setBlockAt(x, y, z, block)
	level.setBlockDataAt(x, y, z, data)


def setBlockToGround(level, (block, data), x, y, z, ymin):
	for iterY in xrange(ymin, y):
		setBlockIfEmpty(level, (block, data), x, iterY, z)

def getBoxSize(box):
	return box.size

	
def createChestBlockData2(x, y, z, options, seedtag, ItemsSmokeBox):
	e = TAG_Compound()
	e["x"] = TAG_Int(x)
	e["y"] = TAG_Int(y)
	e["z"] = TAG_Int(z)
	if options["(1.11+)"]:
		e["id"] = TAG_String("chest")
	else:
		e["id"] = TAG_String("Chest")
	e["Items"] = TAG_List()
	e["LootTableSeed"] = TAG_Long(int(seedtag))
	e["CustomName"] = TAG_String("Lucky Crate")
	if options["(Random Loot ID)"]:
		foo = ['nether_bridge', 'village_blacksmith', 'stronghold_crossing', 'spawn_bonus_chest', 'jungle_temple', 'simple_dungeon', 'igloo_chest', 'end_city_treasure' , 'desert_pyramid', 'abandoned_mineshaft']
		e["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		e["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	return e

def createChestBlockData(x, y, z, options, seedtag, ItemsSmokeBox):
	foo = ['nether_bridge', 'village_blacksmith', 'stronghold_crossing', 'spawn_bonus_chest', 'jungle_temple', 'simple_dungeon', 'igloo_chest','end_city_treasure' , 'desert_pyramid', 'abandoned_mineshaft']
	chest = TAG_Compound()
	chest["y"] = TAG_Int(y)
	if options["(1.11+)"]:
		chest["id"] = TAG_String("chest")
	else:
		chest["id"] = TAG_String("Chest")
	chest["x"] = TAG_Int(x)
	chest["z"] = TAG_Int(z)
	items = TAG_List()
	minecraftchest = TAG_Compound()
	minecraftchest["id"] = TAG_String(u'minecraft:chest')
	minecraftchest["Damage"] = TAG_Short(0)
	minecraftchest["Count"] = TAG_Byte(64)
	tag = TAG_Compound()
	blockEntityTag = TAG_Compound()
	blockEntityTag["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag["LootTableSeed"] = TAG_Long(int(seedtag))
	tag["BlockEntityTag"] = blockEntityTag
	display = TAG_Compound()
	display["Name"] = TAG_String(u'Lucky Crate')
	tag["display"] = display
	minecraftchest["tag"] = tag
	minecraftchest["Slot"] = TAG_Byte(0)
	items.append(minecraftchest)
	minecraftchest2 = TAG_Compound()
	minecraftchest2["id"] = TAG_String(u'minecraft:chest')
	minecraftchest2["Damage"] = TAG_Short(0)
	minecraftchest2["Count"] = TAG_Byte(64)
	tag2 = TAG_Compound()
	blockEntityTag2 = TAG_Compound()
	blockEntityTag2["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag2["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag2["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag2["LootTableSeed"] = TAG_Long(int(seedtag))
	tag2["BlockEntityTag"] = blockEntityTag2
	display2 = TAG_Compound()
	display2["Name"] = TAG_String(u'Lucky Crate')
	tag2["display"] = display2
	minecraftchest2["tag"] = tag2
	minecraftchest2["Slot"] = TAG_Byte(1)
	items.append(minecraftchest2)
	minecraftchest3 = TAG_Compound()
	minecraftchest3["id"] = TAG_String(u'minecraft:chest')
	minecraftchest3["Damage"] = TAG_Short(0)
	minecraftchest3["Count"] = TAG_Byte(64)
	tag3 = TAG_Compound()
	blockEntityTag3 = TAG_Compound()
	blockEntityTag3["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag3["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag3["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag3["LootTableSeed"] = TAG_Long(int(seedtag))
	tag3["BlockEntityTag"] = blockEntityTag3
	display3 = TAG_Compound()
	display3["Name"] = TAG_String(u'Lucky Crate')
	tag3["display"] = display3
	minecraftchest3["tag"] = tag3
	minecraftchest3["Slot"] = TAG_Byte(2)
	items.append(minecraftchest3)
	minecraftchest4 = TAG_Compound()
	minecraftchest4["id"] = TAG_String(u'minecraft:chest')
	minecraftchest4["Damage"] = TAG_Short(0)
	minecraftchest4["Count"] = TAG_Byte(64)
	tag4 = TAG_Compound()
	blockEntityTag4 = TAG_Compound()
	blockEntityTag4["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag4["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag4["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag4["LootTableSeed"] = TAG_Long(int(seedtag))
	tag4["BlockEntityTag"] = blockEntityTag4
	display4 = TAG_Compound()
	display4["Name"] = TAG_String(u'Lucky Crate')
	tag4["display"] = display4
	minecraftchest4["tag"] = tag4
	minecraftchest4["Slot"] = TAG_Byte(3)
	items.append(minecraftchest4)
	minecraftchest5 = TAG_Compound()
	minecraftchest5["id"] = TAG_String(u'minecraft:chest')
	minecraftchest5["Damage"] = TAG_Short(0)
	minecraftchest5["Count"] = TAG_Byte(64)
	tag5 = TAG_Compound()
	blockEntityTag5 = TAG_Compound()
	blockEntityTag5["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag5["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag5["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag5["LootTableSeed"] = TAG_Long(int(seedtag))
	tag5["BlockEntityTag"] = blockEntityTag5
	display5 = TAG_Compound()
	display5["Name"] = TAG_String(u'Lucky Crate')
	tag5["display"] = display5
	minecraftchest5["tag"] = tag5
	minecraftchest5["Slot"] = TAG_Byte(4)
	items.append(minecraftchest5)
	minecraftchest6 = TAG_Compound()
	minecraftchest6["id"] = TAG_String(u'minecraft:chest')
	minecraftchest6["Damage"] = TAG_Short(0)
	minecraftchest6["Count"] = TAG_Byte(64)
	tag6 = TAG_Compound()
	blockEntityTag6 = TAG_Compound()
	blockEntityTag6["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag6["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag6["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag6["LootTableSeed"] = TAG_Long(int(seedtag))
	tag6["BlockEntityTag"] = blockEntityTag6
	display6 = TAG_Compound()
	display6["Name"] = TAG_String(u'Lucky Crate')
	tag6["display"] = display6
	minecraftchest6["tag"] = tag6
	minecraftchest6["Slot"] = TAG_Byte(5)
	items.append(minecraftchest6)
	minecraftchest7 = TAG_Compound()
	minecraftchest7["id"] = TAG_String(u'minecraft:chest')
	minecraftchest7["Damage"] = TAG_Short(0)
	minecraftchest7["Count"] = TAG_Byte(64)
	tag7 = TAG_Compound()
	blockEntityTag7 = TAG_Compound()
	blockEntityTag7["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag7["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag7["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag7["LootTableSeed"] = TAG_Long(int(seedtag))
	tag7["BlockEntityTag"] = blockEntityTag7
	display7 = TAG_Compound()
	display7["Name"] = TAG_String(u'Lucky Crate')
	tag7["display"] = display7
	minecraftchest7["tag"] = tag7
	minecraftchest7["Slot"] = TAG_Byte(6)
	items.append(minecraftchest7)
	minecraftchest8 = TAG_Compound()
	minecraftchest8["id"] = TAG_String(u'minecraft:chest')
	minecraftchest8["Damage"] = TAG_Short(0)
	minecraftchest8["Count"] = TAG_Byte(64)
	tag8 = TAG_Compound()
	blockEntityTag8 = TAG_Compound()
	blockEntityTag8["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag8["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag8["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag8["LootTableSeed"] = TAG_Long(int(seedtag))
	tag8["BlockEntityTag"] = blockEntityTag8
	display8 = TAG_Compound()
	display8["Name"] = TAG_String(u'Lucky Crate')
	tag8["display"] = display8
	minecraftchest8["tag"] = tag8
	minecraftchest8["Slot"] = TAG_Byte(7)
	items.append(minecraftchest8)
	minecraftchest9 = TAG_Compound()
	minecraftchest9["id"] = TAG_String(u'minecraft:chest')
	minecraftchest9["Damage"] = TAG_Short(0)
	minecraftchest9["Count"] = TAG_Byte(64)
	tag9 = TAG_Compound()
	blockEntityTag9 = TAG_Compound()
	blockEntityTag9["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag9["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag9["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag9["LootTableSeed"] = TAG_Long(int(seedtag))
	tag9["BlockEntityTag"] = blockEntityTag9
	display9 = TAG_Compound()
	display9["Name"] = TAG_String(u'Lucky Crate')
	tag9["display"] = display9
	minecraftchest9["tag"] = tag9
	minecraftchest9["Slot"] = TAG_Byte(8)
	items.append(minecraftchest9)
	minecraftchest10 = TAG_Compound()
	minecraftchest10["id"] = TAG_String(u'minecraft:chest')
	minecraftchest10["Damage"] = TAG_Short(0)
	minecraftchest10["Count"] = TAG_Byte(64)
	tag10 = TAG_Compound()
	blockEntityTag10 = TAG_Compound()
	blockEntityTag10["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag10["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag10["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag10["LootTableSeed"] = TAG_Long(int(seedtag))
	tag10["BlockEntityTag"] = blockEntityTag10
	display10 = TAG_Compound()
	display10["Name"] = TAG_String(u'Lucky Crate')
	tag10["display"] = display10
	minecraftchest10["tag"] = tag10
	minecraftchest10["Slot"] = TAG_Byte(9)
	items.append(minecraftchest10)
	minecraftchest11 = TAG_Compound()
	minecraftchest11["id"] = TAG_String(u'minecraft:chest')
	minecraftchest11["Damage"] = TAG_Short(0)
	minecraftchest11["Count"] = TAG_Byte(64)
	tag11 = TAG_Compound()
	blockEntityTag11 = TAG_Compound()
	blockEntityTag11["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag11["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag11["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag11["LootTableSeed"] = TAG_Long(int(seedtag))
	tag11["BlockEntityTag"] = blockEntityTag11
	display11 = TAG_Compound()
	display11["Name"] = TAG_String(u'Lucky Crate')
	tag11["display"] = display11
	minecraftchest11["tag"] = tag11
	minecraftchest11["Slot"] = TAG_Byte(10)
	items.append(minecraftchest11)
	minecraftchest12 = TAG_Compound()
	minecraftchest12["id"] = TAG_String(u'minecraft:chest')
	minecraftchest12["Damage"] = TAG_Short(0)
	minecraftchest12["Count"] = TAG_Byte(64)
	tag12 = TAG_Compound()
	blockEntityTag12 = TAG_Compound()
	blockEntityTag12["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag12["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag12["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag12["LootTableSeed"] = TAG_Long(int(seedtag))
	tag12["BlockEntityTag"] = blockEntityTag12
	display12 = TAG_Compound()
	display12["Name"] = TAG_String(u'Lucky Crate')
	tag12["display"] = display12
	minecraftchest12["tag"] = tag12
	minecraftchest12["Slot"] = TAG_Byte(10)
	items.append(minecraftchest12)
	minecraftchest13 = TAG_Compound()
	minecraftchest13["id"] = TAG_String(u'minecraft:chest')
	minecraftchest13["Damage"] = TAG_Short(0)
	minecraftchest13["Count"] = TAG_Byte(64)
	tag13 = TAG_Compound()
	blockEntityTag13 = TAG_Compound()
	blockEntityTag13["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag13["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag13["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag13["LootTableSeed"] = TAG_Long(int(seedtag))
	tag13["BlockEntityTag"] = blockEntityTag13
	display13 = TAG_Compound()
	display13["Name"] = TAG_String(u'Lucky Crate')
	tag13["display"] = display13
	minecraftchest13["tag"] = tag13
	minecraftchest13["Slot"] = TAG_Byte(11)
	items.append(minecraftchest13)
	minecraftchest14 = TAG_Compound()
	minecraftchest14["id"] = TAG_String(u'minecraft:chest')
	minecraftchest14["Damage"] = TAG_Short(0)
	minecraftchest14["Count"] = TAG_Byte(64)
	tag14 = TAG_Compound()
	blockEntityTag14 = TAG_Compound()
	blockEntityTag14["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag14["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag14["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag14["LootTableSeed"] = TAG_Long(int(seedtag))
	tag14["BlockEntityTag"] = blockEntityTag14
	display14 = TAG_Compound()
	display14["Name"] = TAG_String(u'Lucky Crate')
	tag14["display"] = display14
	minecraftchest14["tag"] = tag14
	minecraftchest14["Slot"] = TAG_Byte(12)
	items.append(minecraftchest14)
	minecraftchest15 = TAG_Compound()
	minecraftchest15["id"] = TAG_String(u'minecraft:chest')
	minecraftchest15["Damage"] = TAG_Short(0)
	minecraftchest15["Count"] = TAG_Byte(64)
	tag15 = TAG_Compound()
	blockEntityTag15 = TAG_Compound()
	blockEntityTag15["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag15["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag15["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag15["LootTableSeed"] = TAG_Long(int(seedtag))
	tag15["BlockEntityTag"] = blockEntityTag15
	display15 = TAG_Compound()
	display15["Name"] = TAG_String(u'Lucky Crate')
	tag15["display"] = display15
	minecraftchest15["tag"] = tag15
	minecraftchest15["Slot"] = TAG_Byte(13)
	items.append(minecraftchest15)
	minecraftchest16 = TAG_Compound()
	minecraftchest16["id"] = TAG_String(u'minecraft:chest')
	minecraftchest16["Damage"] = TAG_Short(0)
	minecraftchest16["Count"] = TAG_Byte(64)
	tag16 = TAG_Compound()
	blockEntityTag16 = TAG_Compound()
	blockEntityTag16["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag16["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag16["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag16["LootTableSeed"] = TAG_Long(int(seedtag))
	tag16["BlockEntityTag"] = blockEntityTag16
	display16 = TAG_Compound()
	display16["Name"] = TAG_String(u'Lucky Crate')
	tag16["display"] = display16
	minecraftchest16["tag"] = tag16
	minecraftchest16["Slot"] = TAG_Byte(14)
	items.append(minecraftchest16)
	minecraftchest17 = TAG_Compound()
	minecraftchest17["id"] = TAG_String(u'minecraft:chest')
	minecraftchest17["Damage"] = TAG_Short(0)
	minecraftchest17["Count"] = TAG_Byte(64)
	tag17 = TAG_Compound()
	blockEntityTag17 = TAG_Compound()
	blockEntityTag17["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag17["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag17["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag17["LootTableSeed"] = TAG_Long(int(seedtag))
	tag17["BlockEntityTag"] = blockEntityTag17
	display17 = TAG_Compound()
	display17["Name"] = TAG_String(u'Lucky Crate')
	tag17["display"] = display17
	minecraftchest17["tag"] = tag17
	minecraftchest17["Slot"] = TAG_Byte(15)
	items.append(minecraftchest17)
	minecraftchest18 = TAG_Compound()
	minecraftchest18["id"] = TAG_String(u'minecraft:chest')
	minecraftchest18["Damage"] = TAG_Short(0)
	minecraftchest18["Count"] = TAG_Byte(64)
	tag18 = TAG_Compound()
	blockEntityTag18 = TAG_Compound()
	blockEntityTag18["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag18["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag18["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag18["LootTableSeed"] = TAG_Long(int(seedtag))
	tag18["BlockEntityTag"] = blockEntityTag18
	display18 = TAG_Compound()
	display18["Name"] = TAG_String(u'Lucky Crate')
	tag18["display"] = display18
	minecraftchest18["tag"] = tag18
	minecraftchest18["Slot"] = TAG_Byte(16)
	items.append(minecraftchest18)
	minecraftchest19 = TAG_Compound()
	minecraftchest19["id"] = TAG_String(u'minecraft:chest')
	minecraftchest19["Damage"] = TAG_Short(0)
	minecraftchest19["Count"] = TAG_Byte(64)
	tag19 = TAG_Compound()
	blockEntityTag19 = TAG_Compound()
	blockEntityTag19["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag19["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag19["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag19["LootTableSeed"] = TAG_Long(int(seedtag))
	tag19["BlockEntityTag"] = blockEntityTag19
	display19 = TAG_Compound()
	display19["Name"] = TAG_String(u'Lucky Crate')
	tag19["display"] = display19
	minecraftchest19["tag"] = tag19
	minecraftchest19["Slot"] = TAG_Byte(17)
	items.append(minecraftchest19)
	minecraftchest20 = TAG_Compound()
	minecraftchest20["id"] = TAG_String(u'minecraft:chest')
	minecraftchest20["Damage"] = TAG_Short(0)
	minecraftchest20["Count"] = TAG_Byte(64)
	tag20 = TAG_Compound()
	blockEntityTag20 = TAG_Compound()
	blockEntityTag20["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag20["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag20["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag20["LootTableSeed"] = TAG_Long(int(seedtag))
	tag20["BlockEntityTag"] = blockEntityTag20
	display20 = TAG_Compound()
	display20["Name"] = TAG_String(u'Lucky Crate')
	tag20["display"] = display20
	minecraftchest20["tag"] = tag20
	minecraftchest20["Slot"] = TAG_Byte(18)
	items.append(minecraftchest20)
	minecraftchest21 = TAG_Compound()
	minecraftchest21["id"] = TAG_String(u'minecraft:chest')
	minecraftchest21["Damage"] = TAG_Short(0)
	minecraftchest21["Count"] = TAG_Byte(64)
	tag21 = TAG_Compound()
	blockEntityTag21 = TAG_Compound()
	blockEntityTag21["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag21["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag21["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag21["LootTableSeed"] = TAG_Long(int(seedtag))
	tag21["BlockEntityTag"] = blockEntityTag21
	display21 = TAG_Compound()
	display21["Name"] = TAG_String(u'Lucky Crate')
	tag21["display"] = display21
	minecraftchest21["tag"] = tag21
	minecraftchest21["Slot"] = TAG_Byte(19)
	items.append(minecraftchest21)
	minecraftchest22 = TAG_Compound()
	minecraftchest22["id"] = TAG_String(u'minecraft:chest')
	minecraftchest22["Damage"] = TAG_Short(0)
	minecraftchest22["Count"] = TAG_Byte(64)
	tag22 = TAG_Compound()
	blockEntityTag22 = TAG_Compound()
	blockEntityTag22["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag22["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag22["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag22["LootTableSeed"] = TAG_Long(int(seedtag))
	tag22["BlockEntityTag"] = blockEntityTag22
	display22 = TAG_Compound()
	display22["Name"] = TAG_String(u'Lucky Crate')
	tag22["display"] = display22
	minecraftchest22["tag"] = tag22
	minecraftchest22["Slot"] = TAG_Byte(20)
	items.append(minecraftchest22)
	minecraftchest23 = TAG_Compound()
	minecraftchest23["id"] = TAG_String(u'minecraft:chest')
	minecraftchest23["Damage"] = TAG_Short(0)
	minecraftchest23["Count"] = TAG_Byte(64)
	tag23 = TAG_Compound()
	blockEntityTag23 = TAG_Compound()
	blockEntityTag23["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag23["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag23["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag23["LootTableSeed"] = TAG_Long(int(seedtag))
	tag23["BlockEntityTag"] = blockEntityTag23
	display23 = TAG_Compound()
	display23["Name"] = TAG_String(u'Lucky Crate')
	tag23["display"] = display23
	minecraftchest23["tag"] = tag23
	minecraftchest23["Slot"] = TAG_Byte(21)
	items.append(minecraftchest23)
	minecraftchest24 = TAG_Compound()
	minecraftchest24["id"] = TAG_String(u'minecraft:chest')
	minecraftchest24["Damage"] = TAG_Short(0)
	minecraftchest24["Count"] = TAG_Byte(64)
	tag24 = TAG_Compound()
	blockEntityTag24 = TAG_Compound()
	blockEntityTag24["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag24["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag24["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag24["LootTableSeed"] = TAG_Long(int(seedtag))
	tag24["BlockEntityTag"] = blockEntityTag24
	display24 = TAG_Compound()
	display24["Name"] = TAG_String(u'Lucky Crate')
	tag24["display"] = display24
	minecraftchest24["tag"] = tag24
	minecraftchest24["Slot"] = TAG_Byte(22)
	items.append(minecraftchest24)
	minecraftchest25 = TAG_Compound()
	minecraftchest25["id"] = TAG_String(u'minecraft:chest')
	minecraftchest25["Damage"] = TAG_Short(0)
	minecraftchest25["Count"] = TAG_Byte(64)
	tag25 = TAG_Compound()
	blockEntityTag25 = TAG_Compound()
	blockEntityTag25["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag25["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag25["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag25["LootTableSeed"] = TAG_Long(int(seedtag))
	tag25["BlockEntityTag"] = blockEntityTag25
	display25 = TAG_Compound()
	display25["Name"] = TAG_String(u'Lucky Crate')
	tag25["display"] = display25
	minecraftchest25["tag"] = tag25
	minecraftchest25["Slot"] = TAG_Byte(23)
	items.append(minecraftchest25)
	minecraftchest26 = TAG_Compound()
	minecraftchest26["id"] = TAG_String(u'minecraft:chest')
	minecraftchest26["Damage"] = TAG_Short(0)
	minecraftchest26["Count"] = TAG_Byte(64)
	tag26 = TAG_Compound()
	blockEntityTag26 = TAG_Compound()
	blockEntityTag26["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag26["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag26["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag26["LootTableSeed"] = TAG_Long(int(seedtag))
	tag26["BlockEntityTag"] = blockEntityTag26
	display26 = TAG_Compound()
	display26["Name"] = TAG_String(u'Lucky Crate')
	tag26["display"] = display26
	minecraftchest26["tag"] = tag26
	minecraftchest26["Slot"] = TAG_Byte(25)
	items.append(minecraftchest26)
	minecraftchest27 = TAG_Compound()
	minecraftchest27["id"] = TAG_String(u'minecraft:chest')
	minecraftchest27["Damage"] = TAG_Short(0)
	minecraftchest27["Count"] = TAG_Byte(64)
	tag27 = TAG_Compound()
	blockEntityTag27 = TAG_Compound()
	blockEntityTag27["CustomName"] = TAG_String(u'Lucky Crate')
	if options["(Random Loot ID)"]:
		blockEntityTag27["LootTable"] = TAG_String("minecraft:chests/"+ random.choice(foo))
	else:
		blockEntityTag27["LootTable"] = TAG_String("minecraft:chests/"+ str(ItemsSmokeBox))
	blockEntityTag27["LootTableSeed"] = TAG_Long(int(seedtag))
	tag27["BlockEntityTag"] = blockEntityTag27
	display27 = TAG_Compound()
	display27["Name"] = TAG_String(u'Lucky Crate')
	tag27["display"] = display27
	minecraftchest27["tag"] = tag27
	minecraftchest27["Slot"] = TAG_Byte(27)
	items.append(minecraftchest27)
	chest["Items"] = items
	return chest

def perform(level, box, options):
	Chester(level, box, options)
	level.markDirtyBox(box)

def Chester(level, box, options):
	(width, height, depth) = getBoxSize(box)
	centreWidth = width / 2
	centreHeight = height / 2
	centreDepth = depth / 2
	AIRBLOCK = 0
	AIR = (AIRBLOCK,0)
	CHUNKSIZE = 16
	iterX = box.minx
	iterZ = box.minz
	iterY = box.miny
	ItemsSmokeBox = Smokeboxs[options["(Loot ID)"]]
	seedtag = options["(Loot Seed)"]
	datavalue = dict([(trn._(a), b) for a, b in Effects.items()])[options["(Chest Block)"]]
	chunk = level.getChunk(iterX/CHUNKSIZE, iterZ/CHUNKSIZE)
	setBlock(level, (54,datavalue), iterX, iterY, iterZ)
	if (options["(Placeable Chest)"] == False):
		chunk.TileEntities.append( createChestBlockData2(iterX, iterY, iterZ, options, seedtag, ItemsSmokeBox))
	else:
		chunk.TileEntities.append( createChestBlockData(iterX, iterY, iterZ, options, seedtag, ItemsSmokeBox))
	print "MCEdit Filter By StealthyExpert"
	print "Follow Me On Twitter: @RedstonerLabs"