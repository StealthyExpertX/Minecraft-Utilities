#Created By StealthyExpertX and also known as AKA @RedstonerLabs and iPxD Mods

#Also You can support us by visiting our website www.ipxdhosting.com and trying out one of our three great web hosting plans we offer as low as 3.99$ per month :)

from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_Float
from pymclevel import TAG_String
from pymclevel import TAG_Long
from pymclevel import TAG_Int_Array
import math

Smokeboxs = {
	"(Oak Boat)": "oak",
	"(Spruce Boat)": "spruce",
	"(Birch Boat)": "birch",
	"(Jungle Boat)": "jungle",
	"(Acacia Boat)": "acaica",
	"(Glitched Boat)": "glitched",
	"(Dark Oak Boat)": "dark_oak",
	}
	
	
Smokeboxs2 = {
	"(PC Minecraft)": "PC",
	"(Console Edition Minecraft)": "CONSOLE",
	}

inputs = (
	("Boater MCEdit Filter Creates Boat Entities", "label"),
	("Minecraft Type", tuple(Smokeboxs2.keys())),
	("Glitched Boat Works On Minecraft Console Type Only", "label"),
	("Boat Type", tuple(Smokeboxs.keys())),
	("Offset X", 0.5),
	("Offset Y", 0),
	("Offset Z", 0.5),
	("(1.11)(1.11.2)(1.11.2+)", False),
	("NoGravity", False),
	("Invuneable", False),
	("Silent", False),
	("Glowing", False),
	("CustomNameVisible", False),
	("CustomName", "string"),
	("Rotation", 0),
	("Fire", 0),
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


def perform(level, box, options):
	print "Follow Me On Twitter At @RedstonerLabs"
	for x in xrange(box.minx, box.maxx):
		for z in xrange(box.minz, box.maxz):
			for y in xrange(box.miny, box.maxy):
			
				invun = options["Invuneable"]
			
				float = options["NoGravity"]

				silent = options["Silent"]
				
				ROTX = options["Rotation"]
				
				Text2 = options["CustomName"]
				
				glowing = options["Glowing"]
				
				fire = options["Fire"]
				
				off1 = options["Offset X"]
				
				off2 = options["Offset Y"]
				
				off3 = options["Offset Z"]
				
				vis = options["CustomNameVisible"]
				
				ItemsSmokeBox = Smokeboxs[options["Boat Type"]]
				
				ItemsSmokeBox2 = Smokeboxs2[options["Minecraft Type"]]
				
				chunk = level.getChunk(x/16, z/16)
				
				Boat = TAG_Compound()
				
				if options["(1.11)(1.11.2)(1.11.2+)"]:
					Boat["id"] = TAG_String(u'boat')
					
				else:
					Boat["id"] = TAG_String(u'Boat')
					
				pos = TAG_List()
				pos.append(TAG_Double(x+off1))
				pos.append(TAG_Double(y+off2))
				pos.append(TAG_Double(z+off3))
				Boat["Pos"] = pos
				Boat["OnGround"] = TAG_Byte(0)
				Boat["NoGravity"] = TAG_Byte(float)
				Boat["Silent"] = TAG_Byte(silent)
				motion = TAG_List()
				motion.append(TAG_Double(0.0))
				motion.append(TAG_Double(0.0))
				motion.append(TAG_Double(0.0))
				Boat["Motion"] = motion
				Boat["Dimension"] = TAG_Int(0)
				Boat["Air"] = TAG_Short(300)
				rotation = TAG_List()
				rotation.append(TAG_Float(ROTX))
				rotation.append(TAG_Float(0.0))
				Boat["Rotation"] = rotation
				Boat["FallDistance"] = TAG_Float(0.0)
				Boat["Invulnerable"] = TAG_Byte(invun)
				Boat["PortalCooldown"] = TAG_Int(0)
				Boat["Glowing"] = TAG_Byte(glowing)
				Boat["CustomNameVisible"] = TAG_Byte(vis)
				Boat["CustomName"] = TAG_String(Text2)
				Boat["Fire"] = TAG_Short(fire)
				
				if ItemsSmokeBox == "oak" and ItemsSmokeBox2 == "CONSOLE":
					Boat["Type"] = TAG_Int(0)
					
				if ItemsSmokeBox == "birch" and ItemsSmokeBox2 == "CONSOLE":
					Boat["Type"] = TAG_Int(1)
					
				if ItemsSmokeBox == "spruce" and ItemsSmokeBox2 == "CONSOLE":
					Boat["Type"] = TAG_Int(2)
					
				if ItemsSmokeBox == "jungle" and ItemsSmokeBox2 == "CONSOLE":
					Boat["Type"] = TAG_Int(3)
					
				if ItemsSmokeBox == "acaica" and ItemsSmokeBox2 == "CONSOLE":
					Boat["Type"] = TAG_Int(4)
					
				if ItemsSmokeBox == "dark_oak" and ItemsSmokeBox2 == "CONSOLE":
					Boat["Type"] = TAG_Int(5)
					
				if ItemsSmokeBox == "glitched" and ItemsSmokeBox2 == "CONSOLE":
					Boat["Type"] = TAG_Int(-1)
					
				if ItemsSmokeBox2 == "PC":
					Boat["Type"] = TAG_String(ItemsSmokeBox)
					
				chunk.Entities.append(Boat)
	print "Completed Work"
