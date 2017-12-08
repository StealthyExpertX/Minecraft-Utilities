#Filter Created By StealthyExpert AKA @RedstonerLabs
#NOTE: This filter will only work in all btw these versions , 1.9, 1.10, 1.11, 1.12, 1.12.2, 1.13+?

#Imports pymclevel
from pymclevel import TileEntity, TAG_Byte, TAG_Int, TAG_Compound, TAG_String, TAG_Long
from pymclevel.materials import alphaMaterials

#Block Ids List Of TileEntities
Smokeboxs = {
	"(Banner Standing)": 177,
	"(Banner Wall)": 176,
	"(Bed 1.12 Only)": 26,
	"(Beacon)": 138,
	"(Block 36)": 36,
	"(Invisible)": 36,
	"(Brewing Stand)": 117,
	"(Cauldron)": 118,
	"(Chest)": 54,
	"(Command Block)": 137,
	"(Daylight Sensor)": 151,
	"(Dispenser)": 23,
	"(Dropper)": 158,
	"(Enchantment Table)": 116,
	"(End Portal)": 119,
	"(Ender Chest)": 130,
	"(EndGateWay)": 209,
	"(Flower Pot)": 140,
	"(Furnace Off)": 61,
	"(Furnace On)": 62,
	"(Hopper)": 154,
	"(Jukebox)": 84,
	"(Inverted Daylight Sensor)": 178,
	"(Mob Head)": 144,
	"(Mob Spawner)": 52,
	"(Note Block)": 25,
	"(Piston Block)": 33,
	"(Piston Head)": 34,
	"(Portal)": 90,
	"(Redstone Comparator Off)": 149,
	"(Redstone Comparator On)": 150,
	"(Repeating Command Block 1.10+ Only)": 210,
	"(Chain Command Block 1.10+ Only)": 211,
	"(Shulker Box 1.12+ Only)": 229,
	"(Standing Sign)": 63,
	"(Sticky Piston)": 29,
	"(Structure Block 1.11+ Only)": 255,
	"(Trapped Chest)": 146,
	"(Wall Sign)": 68,
	}
	
#Filter Operations
Ops = {
	"Create": "create",
	"Delete": "remove",
	"Modify": "edit",
	}

#Keys For Block IDs
EffectKeys = ()
for key in Smokeboxs.keys():
	EffectKeys = EffectKeys + (key,)

#User Inputs
inputs = [
	(
		("Main", "title"),
		("(TP Filter V4 Main Menu)", "label"),
		("This filter creates, edits, removes, Teleporters", "label"),
		("that are in the current selection box", "label"),
		("Operation: ", tuple(Ops.keys())),
		("GoTo X: ", (0,-9223372036854775808,9223372036854775807)),
		("GoTo Y: ", (0,-9223372036854775808,9223372036854775807)),
		("GoTo Z: ", (0,-9223372036854775808,9223372036854775807)),
	), (
		("Settings", "title"),
		("(Filter Settings)", "label"),
		("The block and data the endgateway will render as", "label"),
		("Block: ", EffectKeys),
		("Data: ", (0,0,15)),
		("Age of the endgateway", "label"),
		("Age: ", (9223372036854775807,-9223372036854775808,9223372036854775807)),
		("1x1 teleport = True or 20x20 teleport = False", "label"),
		("ExactTeleport: ", True),
		("If world/save version is 1.11 or higher 1.12.2+", "label"),
		("1.11+: ", True),
	), (
		("About", "title"),
		("(Contact Information)", "label"),
		("This filter was created by StealthyExpert", "label"),
		("You can follow me on Twitter", "label"),
		("twitter.com/RedstonerLabs  @RedstonerLabs", "label"),
		("You can also subscribe to my channel on YouTube", "label"),
		("youtube.com/channel/UCfSCq4Al4Bx7geFdbkLxMxw", "label"),
		("You can also join my server on Discord", "label"),
		("discord.gg/A8wgNyu", "label"),
	),
]
			
#Delete EndGateways Method 
def deleteAllEndGateWays(box, level):

	#Scan Selection Box
	for x5 in xrange(box.minx, box.maxx):

		for y5 in xrange(box.miny, box.maxy):
		
			for z5 in xrange(box.minz, box.maxz):
			
				#Define Chunk Accessor
				chunk3 = level.getChunk(x5/16, z5/16)
				
				#Get Data Of TileEntitiy
				tiles2 = level.tileEntityAt(x5, y5, z5)
				
				#Check If A TileEntity Exist In The Selection
				if tiles2 in chunk3.TileEntities and tiles2 != None:
				
					#Check If TileEntity Is A EndGateway Type TileEntity
					if tiles2["id"].value in ["EndGateway", "minecraft:end_gateway"]:
				
						#Remove TileEntitiy
						chunk3.TileEntities.remove(tiles2)

						#Place Air Block
						level.setBlockAt(x5, y5, z5, 0)
						level.setBlockDataAt(x5, y5, z5, 0)
						
	#Marks Chunks As Dirt For ReLighting				
	chunk3.dirty = True

#Main Code/Script
def perform(level, box, options):	
	
	#Block ID Selection
	blockids = dict([(trn._(a), b) for a, b in Smokeboxs.items()])[options["Block: "]]
	
	#Editing Operation
	editop = Ops[options["Operation: "]]

	#Create
	if editop == "create":
	
		#Scan Selection Box
		for x in xrange(box.minx, box.maxx):

			for y in xrange(box.miny, box.maxy):
			
				for z in xrange(box.minz, box.maxz):
				
					#Define Chunk Accessor
					chunk7 = level.getChunk(x/16, z/16)
		
					#Get Data Of TileEntitiy
					tiles2 = level.tileEntityAt(x, y, z)
					
					#Check If A TileEntity Exist In The Selection
					if tiles2 in chunk7.TileEntities and tiles2 != None:
						
						#Remove TileEntity
						chunk7.TileEntities.remove(tiles2)
					
					#Set Block From Input
					level.setBlockAt(x, y, z, blockids)
					level.setBlockDataAt(x, y, z, options["Data: "])
					
					#Create TileEntity NBT Data
					endGateway2 = TAG_Compound()
					endGateway2["ExactTeleport"] = TAG_Byte(options["ExactTeleport: "])
					
					endGateway2["x"] = TAG_Int(x)
					endGateway2["y"] = TAG_Int(y)
					endGateway2["z"] = TAG_Int(z)
					
					exitPortal2 = TAG_Compound()
					exitPortal2["X"] = TAG_Int(options["GoTo X: "])
					exitPortal2["Y"] = TAG_Int(options["GoTo Y: "])
					exitPortal2["Z"] = TAG_Int(options["GoTo Z: "])
					endGateway2["ExitPortal"] = exitPortal2
					
					endGateway2["Age"] = TAG_Long(options["Age: "])
					
					#If 1.11+ World Changes id
					if options["1.11+: "]:
					
						endGateway2["id"] = TAG_String("minecraft:end_gateway")
								
					else:
					
						endGateway2["id"] = TAG_String("EndGateway")

					#Add TileEntity
					chunk7.TileEntities.append(endGateway2)
					
					#Marks Chunks As Dirt For ReLighting
					chunk7.dirty = True

	#Edit
	elif editop == "edit":	
	
		#Scan Selection Box
		for (chunk, slices, point) in level.getChunkSlices(box):
		
			#Scan Chunks In Selection For TileEntities
			for te in chunk.TileEntities:
			
				#Get TileEntities X,Y,Z Coordinates
				x = te["x"].value
				y = te["y"].value
				z = te["z"].value
				
				#Check If TileEntities Are In Selection Box
				if (x,y,z) in box:
					
					#Check If Its An Endgateway
					if te["id"].value in ["EndGateway", "minecraft:end_gateway"]:
					
						#Place Block And Data
						level.setBlockAt(x, y, z, blockids)
						level.setBlockDataAt(x, y, z, options["Data: "])
						
						#Create TileEntity NBT Data
						te["ExactTeleport"] = TAG_Byte(options["ExactTeleport: "])
						
						te["Age"] = TAG_Long(options["Age: "])
						
						te["ExitPortal"]["X"] = TAG_Int(options["GoTo X: "])
						te["ExitPortal"]["Y"] = TAG_Int(options["GoTo Y: "])
						te["ExitPortal"]["Z"] = TAG_Int(options["GoTo Z: "])
						
						#If 1.11+ World Changes id
						if options["1.11+: "]:
						
							te["id"] = TAG_String("minecraft:end_gateway")
									
						else:
						
							te["id"] = TAG_String("EndGateway")

		#Marks Chunks As Dirt For ReLighting
		chunk.dirty = True
	
	#Remove
	elif editop == "remove":
		
		#Deleted EndGateWays In The Selection
		deleteAllEndGateWays(box, level)
		
	else:
		
		#Print Error Unknown Operation! Message To Console
		print "Error Unknown Operation!"
		raise ValueError('Error Unknown Operation! Tracingback: ')
		
	#Print Completed Sucessfully! Message To Console
	print "Completed Sucessfully!"