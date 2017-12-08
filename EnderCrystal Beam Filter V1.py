#Created By StealthyExpertX and also known as AKA @RedstonerLabs Leader Of iPxD Mods
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

inputs = (
	("Create Custom EnderCrystal Beams", "label"),
	("X", 0),
	("Y", 0),
	("Z", 0),
	("Invulnerable", True),
	("ShowBottom", False),
	("Offset X,Y,Z Coordinates", False),
	("1.11-1.12+Worlds", False),
)

def perform(level, box, options):
	print "Follow Me On Twitter At @RedstonerLabs"
	ShowBottoms = options["ShowBottom"]
	Invun = options["Invulnerable"]
	target1 = options["Y"]
	target2 = options["X"]
	target3 = options["Z"]
	for x in xrange(box.minx, box.maxx):
		for y in xrange(box.miny, box.maxy):
			for z in xrange(box.minz, box.maxz):
				chunk = level.getChunk(x/16, z/16)
				enderCrystal = TAG_Compound()
				pos = TAG_List()
				pos.append(TAG_Double(x+0.5))
				pos.append(TAG_Double(y))
				pos.append(TAG_Double(z+0.5))
				enderCrystal["Pos"] = pos
				if options["1.11-1.12+Worlds"]:	
					enderCrystal["id"] = TAG_String(u'ender_crystal')
				else:
					enderCrystal["id"] = TAG_String(u'EnderCrystal')
					
				if options["Offset X,Y,Z Coordinates"]:	
					beamTarget = TAG_Compound()
					beamTarget["X"] = TAG_Int(x+target2)
					beamTarget["Y"] = TAG_Int(y+target1)
					beamTarget["Z"] = TAG_Int(z+target3)
					enderCrystal["BeamTarget"] = beamTarget				
				else:
					beamTarget = TAG_Compound()
					beamTarget["X"] = TAG_Int(target2)
					beamTarget["Y"] = TAG_Int(target1)
					beamTarget["Z"] = TAG_Int(target3)
					enderCrystal["BeamTarget"] = beamTarget

				enderCrystal["OnGround"] = TAG_Byte(0)
				motion = TAG_List()
				motion.append(TAG_Double(0.0))
				motion.append(TAG_Double(0.0))
				motion.append(TAG_Double(0.0))
				enderCrystal["Motion"] = motion
				enderCrystal["Dimension"] = TAG_Int(0)
				enderCrystal["Air"] = TAG_Short(300)
				rotation = TAG_List()
				rotation.append(TAG_Float(0.0))
				rotation.append(TAG_Float(0.0))
				enderCrystal["Rotation"] = rotation
				enderCrystal["FallDistance"] = TAG_Float(0.0)
				enderCrystal["Fire"] = TAG_Short(0)
				enderCrystal["Invulnerable"] = TAG_Byte(Invun)
				enderCrystal["PortalCooldown"] = TAG_Int(0)
				enderCrystal["Glowing"] = TAG_Byte(0)
				enderCrystal["ShowBottom"] = TAG_Byte(ShowBottoms)
				chunk.Entities.append(enderCrystal)