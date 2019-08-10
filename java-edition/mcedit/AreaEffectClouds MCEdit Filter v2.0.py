#**************************************************************#
#Created By StealthyExpert and also known as AKA @RedstonerLabs#
#**************************************************************#

#*********************************************************************#
#AreaEffectCloud Filter V2.0 Creates Custom Particles & Potion Effects#
#*********************************************************************#

#********************#
#Imports For NBT TAGS#
#********************#
from pymclevel import TAG_Byte, TAG_Int, TAG_Compound, TAG_String, TileEntity, TAG_Long, TAG_List, TAG_Short, TAG_Double, TAG_Float

#***************************************************#
#Console & Java Particles Ids List By StealthyExpert#
#***************************************************#
# 48 = fallingdust
# 46 = damageIndicator
# 45 = endRod
# 44 = dragonbreath
# 43 = Invisible Particle Effect Causes Extreme lag when looking at it. :Console Exclusive
# 40 = blockcrack ParticleParam1 = Block ID example 22 = lapiz block
# 39 = iconcrack
# 38 = barrier
# 37 = cloud
# 35 = magicCrit
# 34 = splash
# 33 = fireworksSpark
# 32 = happyVillager
# 31 = angryVillager
# 29 = enchantmenttable
# 28 = fallingdust
# 27 = suspended
# 25 = mobSpellAmbient
# 24 = mobSpell
# 23 = witchMagic
# 22 = spell
# 20 = largeexplode	
# 19 = hugeexplosion
# 18 = crit
# 17 = depthsuspend
# 15 = heart	
# 14 = slime
# 13 = snowshovel
# 12 =snowballpoof
# 11 = reddust
# 10 = largesmoke
# 9 = droplet
# 8 = footstep
# 7 = lava
# 6 = flame
# 5 = explode
# 3 = portal
# 2 = note
# 0 = take

#************************************************#
#String Ids For AreaEffectCloud's Particles On PC#
#************************************************#
Smokeboxs = {
	"take": "take",
	"note": "note",
	"portal": "portal",
	"explode": "explode",
	"flame": "flame",
	"lava": "lava",
	"footstep": "footstep",
	"droplet": "droplet",
	"largesmoke": "largesmoke",
	"reddust": "reddust",
	"snowballpoof": "snowballpoof",
	"snowshovel": "snowshovel",
	"slime": "slime",
	"heart": "heart",
	"depthsuspend": "depthsuspend",
	"crit": "crit",
	"hugeexplosion": "hugeexplosion",
	"largeexplode": "largeexplode",
	"spell": "spell",
	"witchMagic": "witchMagic",
	"mobSpell": "mobSpell",
	"mobSpellAmbient": "mobSpellAmbient",
	"suspended": "suspended",
	"fallingdust": "fallingdust",
	"enchantmenttable": "enchantmenttable",
	"angryVillager": "angryVillager",
	"happyVillager": "happyVillager",
	"fireworksSpark": "fireworksSpark",
	"splash": "splash",
	"magicCrit": "magicCrit",
	"cloud": "cloud",
	"barrier": "barrier",
	"iconcrack": "iconcrack",
	"blockcrack": "blockcrack",
	"dragonbreath": "dragonbreath",
	"endRod": "endRod",
	"damageIndicator": "damageIndicator",
	}

#********************#
#Color INT Values Ids#
#********************#
Smokeboxs2 = {
	"(Black)": 177,
	"(Dark Blue)": 170,
	"(Dark Green)": 1700,
	"(Dark Aqua)": 170170,
	"(Dark Red)": 17000,
	"(Purple)": 1700170,
	"(Gold)": 2551700,
	"(Grey)": 170170170,
	"(Dark Gray)": 858585,
	"(Blue)": 8585255,
	"(Green)": 8525585,
	"(Aqua)": 85255255,
	"(Red)": 2558585,
	"(Light Purple)": 25585255,
	"(Yellow)": 25525585,
	"(White)": 255255255,
	}

#******************#
#Keys For Color Ids#
#******************#
EffectKeys = ()
for key in Smokeboxs2.keys():
	EffectKeys = EffectKeys + (key,)
	
#*************#
#Inputs GUI/UI#
#*************#
inputs = [
	(
		("MAIN", "title"),
		("(AreaEffectCloud MCEdit Filter)", "label"),
		("Radius", (0.5,-1.17549E-38,3.40282347E+38)),
		("RadiusOnUse", (0,-1.17549E-38,3.40282347E+38)),
		("RadiusPerTick", (0,-1.17549E-38,3.40282347E+38)),
		("Particle", tuple(Smokeboxs.keys())),
		("Duration", (1200,-2147483648,2147483647)),
	), (
		("EFFECTS", "title"),
		("(Custom Potion Effects Settings)", "label"),
		("Effect ID", (0,0,27)),
		("Effect Amplifier", (0,-128,127)),
		("ShowParticles", (0,0,1)),
		("Effect Duration", (1200,0,2147483647)),
	), (
		("SETTINGS", "title"),
		("(Filter Settings)", "label"),
		("Custom ColorValue", False),
		("ColorValue", EffectKeys),
		("ReapplicationDelay", (0,-2147483648,2147483647)),
		("WaitTime", (0,-2147483648,2147483647)),
		("Age", (1,-2147483648,2147483647)),
		("ParticleParam1", 0),
		("ParticleParam2", 0),
		("Console Edtition", False),
		("Invulnerable", False),
		("Last-Forever/No-Despawn", False),
		("1.11-1.12+Plus", False),
	), (
		("ABOUT", "title"),
		("((Contact Information))", "label"),
		("This filter was created by StealthyExpert", "label"),
		("You can follow me on Twitter", "label"),
		("twitter.com/RedstonerLabs  @RedstonerLabs", "label"),
		("You can also subscribe to my channel on YouTube", "label"),
		("youtube.com/channel/UCfSCq4Al4Bx7geFdbkLxMxw", "label"),
		("You can also join my server on Discord", "label"),
		("discord.gg/67cbdEj", "label"),
	),
]

def perform(level, box, options):

	#**************#
	#Define Options#
	#**************#
	ItemsSmokeBox = Smokeboxs[options["Particle"]]
	colorvalue = dict([(trn._(a), b) for a, b in Smokeboxs2.items()])[options["ColorValue"]]

	#****************#
	#Define Selection#
	#****************#
	for x in xrange(box.minx, box.maxx):
	
		for z in xrange(box.minz, box.maxz):
		
			for y in xrange(box.miny, box.maxy):

				#********************************#
				#Checks If Console Edtion Is True#
				#********************************#
				chunk = level.getChunk(x/16, z/16)
				
				#*******************************#
				#Define & Create AreaEffectCloud#
				#*******************************#
				areaEffectCloud = TAG_Compound()
				areaEffectCloud["Radius"] = TAG_Float(options["Radius"])
				areaEffectCloud["DurationOnUse"] = TAG_Int(0)
				areaEffectCloud["Invulnerable"] = TAG_Byte(options["Invulnerable"])
				areaEffectCloud["PortalCooldown"] = TAG_Int(0)
				
				#*********************************************************************#
				#Checks If Console Edtion Is True And Converts Particle Ids To Console#
				#*********************************************************************#
				if options["Console Edtition"] and ItemsSmokeBox == "take":
					areaEffectCloud["Particle"] = TAG_Int(0)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "take":
					areaEffectCloud["Particle"] = TAG_String("take")
					
				if options["Console Edtition"] and ItemsSmokeBox == "note":
					areaEffectCloud["Particle"] = TAG_Int(2)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "note":
					areaEffectCloud["Particle"] = TAG_String("note")
					
				if options["Console Edtition"] and ItemsSmokeBox == "portal":
					areaEffectCloud["Particle"] = TAG_Int(3)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "portal":
					areaEffectCloud["Particle"] = TAG_String("portal")
					
				if options["Console Edtition"] and ItemsSmokeBox == "explode":
					areaEffectCloud["Particle"] = TAG_Int(5)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "explode":
					areaEffectCloud["Particle"] = TAG_String("explode")
					
				if options["Console Edtition"] and ItemsSmokeBox == "flame":
					areaEffectCloud["Particle"] = TAG_Int(6)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "flame":
					areaEffectCloud["Particle"] = TAG_String("flame")
					
				if options["Console Edtition"] and ItemsSmokeBox == "lava":
					areaEffectCloud["Particle"] = TAG_Int(7)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "lava":
					areaEffectCloud["Particle"] = TAG_String("lava")
					
				if options["Console Edtition"] and ItemsSmokeBox == "footstep":
					areaEffectCloud["Particle"] = TAG_Int(8)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "footstep":
					areaEffectCloud["Particle"] = TAG_String("footstep")
					
				if options["Console Edtition"] and ItemsSmokeBox == "droplet":
					areaEffectCloud["Particle"] = TAG_Int(9)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "droplet":
					areaEffectCloud["Particle"] = TAG_String("droplet")
					
				if options["Console Edtition"] and ItemsSmokeBox == "largesmoke":
					areaEffectCloud["Particle"] = TAG_Int(10)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "largesmoke":
					areaEffectCloud["Particle"] = TAG_String("largesmoke")
					
				if options["Console Edtition"] and ItemsSmokeBox == "reddust":
					areaEffectCloud["Particle"] = TAG_Int(11)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "reddust":
					areaEffectCloud["Particle"] = TAG_String("reddust")
					
				if options["Console Edtition"] and ItemsSmokeBox == "snowballpoof":
					areaEffectCloud["Particle"] = TAG_Int(12)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "snowballpoof":
					areaEffectCloud["Particle"] = TAG_String("snowballpoof")
					
				if options["Console Edtition"] and ItemsSmokeBox == "snowshovel":
					areaEffectCloud["Particle"] = TAG_Int(13)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "snowshovel":
					areaEffectCloud["Particle"] = TAG_String("snowshovel")
					
				if options["Console Edtition"] and ItemsSmokeBox == "slime":
					areaEffectCloud["Particle"] = TAG_Int(14)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "slime":
					areaEffectCloud["Particle"] = TAG_String("slime")
					
				if options["Console Edtition"] and ItemsSmokeBox == "heart":
					areaEffectCloud["Particle"] = TAG_Int(15)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "heart":
					areaEffectCloud["Particle"] = TAG_String("heart")
					
				if options["Console Edtition"] and ItemsSmokeBox == "depthsuspend":
					areaEffectCloud["Particle"] = TAG_Int(17)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "depthsuspend":
					areaEffectCloud["Particle"] = TAG_String("depthsuspend")
					
				if options["Console Edtition"] and ItemsSmokeBox == "crit":
					areaEffectCloud["Particle"] = TAG_Int(18)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "crit":
					areaEffectCloud["Particle"] = TAG_String("crit")
					
				if options["Console Edtition"] and ItemsSmokeBox == "hugeexplosion":
					areaEffectCloud["Particle"] = TAG_Int(19)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "hugeexplosion":
					areaEffectCloud["Particle"] = TAG_String("hugeexplosion")
					
				if options["Console Edtition"] and ItemsSmokeBox == "largeexplode":
					areaEffectCloud["Particle"] = TAG_Int(20)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "largeexplode":
					areaEffectCloud["Particle"] = TAG_String("largeexplode")
					
				if options["Console Edtition"] and ItemsSmokeBox == "spell":
					areaEffectCloud["Particle"] = TAG_Int(22)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "spell":
					areaEffectCloud["Particle"] = TAG_String("spell")
					
				if options["Console Edtition"] and ItemsSmokeBox == "witchMagic":
					areaEffectCloud["Particle"] = TAG_Int(23)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "witchMagic":
					areaEffectCloud["Particle"] = TAG_String("witchMagic")
					
				if options["Console Edtition"] and ItemsSmokeBox == "mobSpell":
					areaEffectCloud["Particle"] = TAG_Int(24)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "mobSpell":
					areaEffectCloud["Particle"] = TAG_String("mobSpell")
					
				if options["Console Edtition"] and ItemsSmokeBox == "mobSpellAmbient":
					areaEffectCloud["Particle"] = TAG_Int(25)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "mobSpellAmbient":
					areaEffectCloud["Particle"] = TAG_String("mobSpellAmbient")
					
				if options["Console Edtition"] and ItemsSmokeBox == "suspended":
					areaEffectCloud["Particle"] = TAG_Int(27)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "suspended":
					areaEffectCloud["Particle"] = TAG_String("suspended")
					
				if options["Console Edtition"] and ItemsSmokeBox == "fallingdust":
					areaEffectCloud["Particle"] = TAG_Int(28)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "fallingdust":
					areaEffectCloud["Particle"] = TAG_String("fallingdust")
					
				if options["Console Edtition"] and ItemsSmokeBox == "enchantmenttable":
					areaEffectCloud["Particle"] = TAG_Int(29)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "enchantmenttable":
					areaEffectCloud["Particle"] = TAG_String("enchantmenttable")
					
				if options["Console Edtition"] and ItemsSmokeBox == "angryVillager":
					areaEffectCloud["Particle"] = TAG_Int(31)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "angryVillager":
					areaEffectCloud["Particle"] = TAG_String("angryVillager")
					
				if options["Console Edtition"] and ItemsSmokeBox == "happyVillager":
					areaEffectCloud["Particle"] = TAG_Int(32)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "happyVillager":
					areaEffectCloud["Particle"] = TAG_String("happyVillager")
					
				if options["Console Edtition"] and ItemsSmokeBox == "fireworksSpark":
					areaEffectCloud["Particle"] = TAG_Int(33)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "fireworksSpark":
					areaEffectCloud["Particle"] = TAG_String("fireworksSpark")
					
				if options["Console Edtition"] and ItemsSmokeBox == "splash":
					areaEffectCloud["Particle"] = TAG_Int(34)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "splash":
					areaEffectCloud["Particle"] = TAG_String("splash")
					
				if options["Console Edtition"] and ItemsSmokeBox == "magicCrit":
					areaEffectCloud["Particle"] = TAG_Int(35)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "magicCrit":
					areaEffectCloud["Particle"] = TAG_String("magicCrit")
					
				if options["Console Edtition"] and ItemsSmokeBox == "cloud":
					areaEffectCloud["Particle"] = TAG_Int(37)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "cloud":
					areaEffectCloud["Particle"] = TAG_String("cloud")
					
				if options["Console Edtition"] and ItemsSmokeBox == "barrier":
					areaEffectCloud["Particle"] = TAG_Int(38)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "barrier":
					areaEffectCloud["Particle"] = TAG_String("barrier")
					
				if options["Console Edtition"] and ItemsSmokeBox == "iconcrack":
					areaEffectCloud["Particle"] = TAG_Int(39)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "iconcrack":
					areaEffectCloud["Particle"] = TAG_String("iconcrack")
					
				if options["Console Edtition"] and ItemsSmokeBox == "blockcrack":
					areaEffectCloud["Particle"] = TAG_Int(40)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "blockcrack":
					areaEffectCloud["Particle"] = TAG_String("blockcrack")
					
				if options["Console Edtition"] and ItemsSmokeBox == "Invisible":
					areaEffectCloud["Particle"] = TAG_Int(43)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "Invisible":
					areaEffectCloud["Particle"] = TAG_String("Invisible")
					
				if options["Console Edtition"] and ItemsSmokeBox == "dragonbreath":
					areaEffectCloud["Particle"] = TAG_Int(44)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "dragonbreath":
					areaEffectCloud["Particle"] = TAG_String("dragonbreath")
					
				if options["Console Edtition"] and ItemsSmokeBox == "endRod":
					areaEffectCloud["Particle"] = TAG_Int(45)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "endRod":
					areaEffectCloud["Particle"] = TAG_String("endRod")
					
				if options["Console Edtition"] and ItemsSmokeBox == "damageIndicator":
					areaEffectCloud["Particle"] = TAG_Int(46)
					
				if options["Console Edtition"] != True and ItemsSmokeBox == "damageIndicator":
					areaEffectCloud["Particle"] = TAG_String("damageIndicator")

				customPotionEffects = TAG_List()
				customPotionEffect = TAG_Compound()
				customPotionEffect["ShowParticles"] = TAG_Byte(options["ShowParticles"])
				customPotionEffect["Duration"] = TAG_Int(options["Effect Duration"])
				customPotionEffect["Id"] = TAG_Int(options["Effect ID"])
				customPotionEffect["Amplifier"] = TAG_Int(options["Effect Amplifier"])
				customPotionEffects.append(customPotionEffect)
				areaEffectCloud["Effects"] = customPotionEffects
				
				areaEffectCloud["FallDistance"] = TAG_Float(0.0)
				
				#**************************************#
				#1.11+ Support Changes ID To New Format#
				#**************************************#				
				if options["1.11-1.12+Plus"]:
					AreaEffectCloud["id"] = TAG_String(u'area_effect_cloud')
					
				else:
					areaEffectCloud["id"] = TAG_String(u'AreaEffectCloud')

				areaEffectCloud["ParticleParam1"] = TAG_Int(options["ParticleParam1"])
				areaEffectCloud["ParticleParam2"] = TAG_Int(options["ParticleParam2"])
				areaEffectCloud["Age"] = TAG_Int(options["Age"])
				
				#********************************************#
				#Custom ColorValue Option Aplies To Particles#
				#********************************************#	
				if options["Custom ColorValue"]:
				
					areaEffectCloud["Color"] = TAG_Int(colorvalue)
				
				else:
					areaEffectCloud["Color"] = TAG_Int(0)
				
				motion = TAG_List()
				motion.append(TAG_Double(0))
				motion.append(TAG_Double(0))
				motion.append(TAG_Double(0))
				areaEffectCloud["Motion"] = motion
				
				areaEffectCloud["ReapplicationDelay"] = TAG_Int(options["ReapplicationDelay"])
				areaEffectCloud["Potion"] = TAG_String("minecraft:potion")
				
				#********************************************#
				#Changes Durantion To The Max Value When True#
				#********************************************#
				if options["Last-Forever/No-Despawn"]:
					areaEffectCloud["Duration"] = TAG_Int(2147483647)
					
				else:
					areaEffectCloud["Duration"] = TAG_Int(options["Duration"])
					
				areaEffectCloud["Air"] = TAG_Short(300)
				areaEffectCloud["OnGround"] = TAG_Byte(0)
				areaEffectCloud["Dimension"] = TAG_Int(0)
				rotation = TAG_List()
				rotation.append(TAG_Float(0.0))
				rotation.append(TAG_Float(0.0))
				areaEffectCloud["Rotation"] = rotation
				areaEffectCloud["RadiusPerTick"] = TAG_Float(options["RadiusPerTick"])
				pos = TAG_List()
				pos.append(TAG_Double(x+0.5))
				pos.append(TAG_Double(y))
				pos.append(TAG_Double(z+0.5))
				areaEffectCloud["Pos"] = pos
				areaEffectCloud["Fire"] = TAG_Short(0)
				areaEffectCloud["RadiusOnUse"] = TAG_Float(options["RadiusOnUse"])
				areaEffectCloud["WaitTime"] = TAG_Int(options["WaitTime"])
				chunk.Entities.append(areaEffectCloud)
				
				#********************************************#
				#Marks The Chunks As Dirty/ReLights Selection#
				#********************************************#
				chunk.dirty = True
				
				#********************************************************#
				#Prints Out Particle ID & Coordinates That Were Generated#
				#********************************************************#
				print "Created AreaEffectCloud " + str(ItemsSmokeBox) + " At X:" + str(x) + " Y:" + str(y) + " Z:" + str(z)

	#***************************************#
	#Prints Out Completed Generation Message#
	#***************************************#
	print "Completed Generation" 
