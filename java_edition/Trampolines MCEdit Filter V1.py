#Filter Created By StealthyExpertX, @RedstonerLabs, Leader Of iPxD Mods

from pymclevel import TAG_Int_Array, TAG_Long, TAG_String, TAG_Float, TAG_Double, TAG_Short, TAG_Compound, TAG_Int, TAG_Int, TAG_Byte, TAG_List
from numpy import zeros

displayName = "Trampolines Filter"

Smokeboxs2 = {
	"(PC Minecraft)": "PC",
	"(Console Edition Minecraft)": "CONSOLE",
	}

inputs = (
("Creates Working Trampoline In A 1x1 Selection", "label"),
("After running the filter save in mcedit to see the missing blocks as this filter works outside of the selection", "label"),
("Use Slime Blocks", False),
("1.11+ or 1.11.2+", False),
("Minecraft Type", tuple(Smokeboxs2.keys())),
)


def perform(level, box, options):
	for x in xrange(box.minx, box.maxx):
		for y in xrange(box.miny, box.maxy):
			for z in xrange(box.minz, box.maxz):
				block =	level.blockAt(x, y, z)
				data =	level.blockDataAt(x, y, z)
				extrab = options["Use Slime Blocks"]
				ItemsSmokeBox2 = Smokeboxs2[options["Minecraft Type"]]
				
				chunk = level.getChunk(x / 16, z / 16)
				
				areaEffectCloud = TAG_Compound()
				if options["1.11+ or 1.11.2+"]:
					areaEffectCloud["id"] = TAG_String(u'area_effect_cloud')
				if options["1.11+ or 1.11.2+"] != True:
					areaEffectCloud["id"] = TAG_String(u'AreaEffectCloud')
				areaEffectCloud["ownerUUID"] = TAG_String(u'')
				areaEffectCloud["OnGround"] = TAG_Byte(0)
				areaEffectCloud["Dimension"] = TAG_Int(0)
				areaEffectCloud["Air"] = TAG_Short(300)
				areaEffectCloud["ParticleParam2"] = TAG_Int(0)
				areaEffectCloud["ParticleParam1"] = TAG_Int(0)
				if ItemsSmokeBox2 == "PC":
					areaEffectCloud["Particle"] = TAG_String(u"take")
				if ItemsSmokeBox2 != "PC":
					areaEffectCloud["Particle"] = TAG_Int(0)
				areaEffectCloud["ReapplicationDelay"] = TAG_Int(0)
				rotation = TAG_List()
				rotation.append(TAG_Float(0.0))
				rotation.append(TAG_Float(0.0))
				areaEffectCloud["Rotation"] = rotation
				areaEffectCloud["FallDistance"] = TAG_Float(0.0)
				effects = TAG_List()
				effect = TAG_Compound()
				effect["Amplifier"] = TAG_Byte(15)
				effect["Id"] = TAG_Byte(25)
				effect["Duration"] = TAG_Int(10)
				effect["Ambient"] = TAG_Byte(0)
				effect["ShowParticles"] = TAG_Byte(0)
				effects.append(effect)
				effect2 = TAG_Compound()
				effect2["Amplifier"] = TAG_Byte(100)
				effect2["Id"] = TAG_Byte(11)
				effect2["Duration"] = TAG_Int(100)
				effect2["Ambient"] = TAG_Byte(0)
				effect2["ShowParticles"] = TAG_Byte(0)
				effects.append(effect2)
				effect3 = TAG_Compound()
				effect3["Amplifier"] = TAG_Byte(20)
				effect3["Id"] = TAG_Byte(8)
				effect3["Duration"] = TAG_Int(40)
				effect3["Ambient"] = TAG_Byte(0)
				effect3["ShowParticles"] = TAG_Byte(0)
				effects.append(effect3)
				areaEffectCloud["Effects"] = effects
				areaEffectCloud["Fire"] = TAG_Short(0)
				areaEffectCloud["Invulnerable"] = TAG_Byte(0)
				areaEffectCloud["PortalCooldown"] = TAG_Int(0)
				areaEffectCloud["CustomName"] = TAG_String(u'')
				areaEffectCloud["createdOnHost"] = TAG_Byte(0)
				areaEffectCloud["Silent"] = TAG_Byte(1)
				areaEffectCloud["NoGravity"] = TAG_Byte(1)
				areaEffectCloud["Glowing"] = TAG_Byte(0)
				areaEffectCloud["Age"] = TAG_Int(1)
				areaEffectCloud["RadiusOnUse"] = TAG_Float(0.0)
				areaEffectCloud["Duration"] = TAG_Int(2147483647)
				areaEffectCloud["DurationOnUse"] = TAG_Int(0)
				areaEffectCloud["WaitTime"] = TAG_Int(0)
				areaEffectCloud["RadiusPerTick"] = TAG_Float(0.0)
				areaEffectCloud["Radius"] = TAG_Float(2.5)
				areaEffectCloud["Color"] = TAG_Int(0)
				areaEffectCloud["Potion"] = TAG_String(u'minecraft:leaping')
				pos = TAG_List()
				pos.append(TAG_Double(x+0.5))
				pos.append(TAG_Double(y+5))
				pos.append(TAG_Double(z+0.5))
				areaEffectCloud["Pos"] = pos
				motion = TAG_List()
				motion.append(TAG_Double(0.0))
				motion.append(TAG_Double(0.0))
				motion.append(TAG_Double(0.0))
				areaEffectCloud["Motion"] = motion
				
				areaEffectCloud2 = TAG_Compound()
				if options["1.11+ or 1.11.2+"]:
					areaEffectCloud2["id"] = TAG_String(u'area_effect_cloud')
				if options["1.11+ or 1.11.2+"] != True:
					areaEffectCloud2["id"] = TAG_String(u'AreaEffectCloud')
				areaEffectCloud2["ownerUUID"] = TAG_String(u'')
				areaEffectCloud2["OnGround"] = TAG_Byte(0)
				areaEffectCloud2["Dimension"] = TAG_Int(0)
				areaEffectCloud2["Air"] = TAG_Short(300)
				areaEffectCloud2["ParticleParam2"] = TAG_Int(0)
				areaEffectCloud2["ParticleParam1"] = TAG_Int(0)
				if ItemsSmokeBox2 == "PC":
					areaEffectCloud2["Particle"] = TAG_String(u"take")
				if ItemsSmokeBox2 != "PC":
					areaEffectCloud2["Particle"] = TAG_Int(0)
				areaEffectCloud2["ReapplicationDelay"] = TAG_Int(0)
				rotation2 = TAG_List()
				rotation2.append(TAG_Float(0.0))
				rotation2.append(TAG_Float(0.0))
				areaEffectCloud2["Rotation"] = rotation2
				areaEffectCloud2["FallDistance"] = TAG_Float(0.0)
				effects2 = TAG_List()
				effect4 = TAG_Compound()
				effect4["Amplifier"] = TAG_Byte(15)
				effect4["Id"] = TAG_Byte(25)
				effect4["Duration"] = TAG_Int(10)
				effect4["Ambient"] = TAG_Byte(0)
				effect4["ShowParticles"] = TAG_Byte(0)
				effects2.append(effect4)
				effect5 = TAG_Compound()
				effect5["Amplifier"] = TAG_Byte(100)
				effect5["Id"] = TAG_Byte(11)
				effect5["Duration"] = TAG_Int(100)
				effect5["Ambient"] = TAG_Byte(0)
				effect5["ShowParticles"] = TAG_Byte(0)
				effects2.append(effect5)
				effect6 = TAG_Compound()
				effect6["Amplifier"] = TAG_Byte(20)
				effect6["Id"] = TAG_Byte(8)
				effect6["Duration"] = TAG_Int(40)
				effect6["Ambient"] = TAG_Byte(0)
				effect6["ShowParticles"] = TAG_Byte(0)
				effects2.append(effect6)
				areaEffectCloud2["Effects"] = effects2
				areaEffectCloud2["Fire"] = TAG_Short(0)
				areaEffectCloud2["Invulnerable"] = TAG_Byte(0)
				areaEffectCloud2["PortalCooldown"] = TAG_Int(0)
				areaEffectCloud2["CustomName"] = TAG_String(u'')
				areaEffectCloud2["createdOnHost"] = TAG_Byte(0)
				areaEffectCloud2["Silent"] = TAG_Byte(1)
				areaEffectCloud2["NoGravity"] = TAG_Byte(1)
				areaEffectCloud2["Glowing"] = TAG_Byte(0)
				areaEffectCloud2["Age"] = TAG_Int(1)
				areaEffectCloud2["RadiusOnUse"] = TAG_Float(0.0)
				areaEffectCloud2["Duration"] = TAG_Int(2147483647)
				areaEffectCloud2["DurationOnUse"] = TAG_Int(0)
				areaEffectCloud2["WaitTime"] = TAG_Int(0)
				areaEffectCloud2["RadiusPerTick"] = TAG_Float(0.0)
				areaEffectCloud2["Radius"] = TAG_Float(2.5)
				areaEffectCloud2["Color"] = TAG_Int(0)
				areaEffectCloud2["Potion"] = TAG_String(u'minecraft:leaping')
				pos2 = TAG_List()
				pos2.append(TAG_Double(x+0.5))
				pos2.append(TAG_Double(y+1.1))
				pos2.append(TAG_Double(z+0.5))
				areaEffectCloud2["Pos"] = pos2
				motion2 = TAG_List()
				motion2.append(TAG_Double(0.0))
				motion2.append(TAG_Double(0.0))
				motion2.append(TAG_Double(0.0))
				areaEffectCloud2["Motion"] = motion2
				
				chunk.Entities.append(areaEffectCloud2)
				chunk.Entities.append(areaEffectCloud)
				print "Created Trampoline! Successfully"
				chunk.dirty = True
				
				#Blackwool #3x3
				
				level.setBlockAt(x, y+1, z, 171)
				level.setBlockDataAt(x, y+1, z, 15)
				
				level.setBlockAt(x+1, y+1, z, 171)
				level.setBlockDataAt(x+1, y+1, z, 15)
				
				level.setBlockAt(x, y+1, z+1, 171)
				level.setBlockDataAt(x, y+1, z+1, 15)
				
				level.setBlockAt(x+1, y+1, z+1, 171)
				level.setBlockDataAt(x+1, y+1, z+1, 15)
				
				level.setBlockAt(x, y+1, z-1, 171)
				level.setBlockDataAt(x, y+1, z-1, 15)
				
				level.setBlockAt(x-1, y+1, z, 171)
				level.setBlockDataAt(x-1, y+1, z, 15)
				
				level.setBlockAt(x-1, y+1, z-1, 171)
				level.setBlockDataAt(x-1, y+1, z-1, 15)
				
				level.setBlockAt(x+1, y+1, z-1, 171)
				level.setBlockDataAt(x+1, y+1, z-1, 15)
				
				level.setBlockAt(x-1, y+1, z+1, 171)
				level.setBlockDataAt(x-1, y+1, z+1, 15)
				
				#Blackwool #2 3x3 Empty Circle
				
				level.setBlockAt(x+2, y+1, z, 171)
				level.setBlockDataAt(x+2, y+1, z, 15)
				
				level.setBlockAt(x-2, y+1, z, 171)
				level.setBlockDataAt(x-2, y+1, z, 15)
				
				level.setBlockAt(x, y+1, z+2, 171)
				level.setBlockDataAt(x, y+1, z+2, 15)
				
				level.setBlockAt(x, y+1, z-2, 171)
				level.setBlockDataAt(x, y+1, z-2, 15)
				
				level.setBlockAt(x+2, y+1, z-1, 171)
				level.setBlockDataAt(x+2, y+1, z-1, 15)
				
				level.setBlockAt(x-1, y+1, z+2, 171)
				level.setBlockDataAt(x-1, y+1, z+2, 15)
				
				level.setBlockAt(x+1, y+1, z+2, 171)
				level.setBlockDataAt(x+1, y+1, z+2, 15)
				
				level.setBlockAt(x+2, y+1, z+1, 171)
				level.setBlockDataAt(x+2, y+1, z+1, 15)
				
				level.setBlockAt(x+1, y+1, z+-2, 171)
				level.setBlockDataAt(x+1, y+1, z-2, 15)
				
				level.setBlockAt(x-2, y+1, z+1, 171)
				level.setBlockDataAt(x-2, y+1, z+1, 15)
				
				level.setBlockAt(x-2, y+1, z-1, 171)
				level.setBlockDataAt(x-2, y+1, z-1, 15)
				
				level.setBlockAt(x-1, y+1, z-2, 171)
				level.setBlockDataAt(x-1, y+1, z-2, 15)
				
				#Blue Wool 5x5 / 3x3 
				
				level.setBlockAt(x+3, y+1, z, 171)
				level.setBlockDataAt(x+3, y+1, z, 11)
				
				level.setBlockAt(x-3, y+1, z, 171)
				level.setBlockDataAt(x-3, y+1, z, 11)
				
				level.setBlockAt(x, y+1, z+3, 171)
				level.setBlockDataAt(x, y+1, z+3, 11)
				
				level.setBlockAt(x, y+1, z-3, 171)
				level.setBlockDataAt(x, y+1, z-3, 11)
				
				level.setBlockAt(x+1, y+1, z-3, 171)
				level.setBlockDataAt(x+1, y+1, z-3, 11)
				
				level.setBlockAt(x-1, y+1, z-3, 171)
				level.setBlockDataAt(x-1, y+1, z-3, 11)
				
				level.setBlockAt(x+3, y+1, z-1, 171)
				level.setBlockDataAt(x+3, y+1, z-1, 11)
				
				level.setBlockAt(x-3, y+1, z-1, 171)
				level.setBlockDataAt(x-3, y+1, z-1, 11)
				
				level.setBlockAt(x+3, y+1, z+1, 171)
				level.setBlockDataAt(x+3, y+1, z+1, 11)
				
				level.setBlockAt(x-3, y+1, z+1, 171)
				level.setBlockDataAt(x-3, y+1, z+1, 11)
				
				level.setBlockAt(x+1, y+1, z+3, 171)
				level.setBlockDataAt(x+1, y+1, z+3, 11)
				
				level.setBlockAt(x-1, y+1, z+3, 171)
				level.setBlockDataAt(x-1, y+1, z+3, 11)
				#
				level.setBlockAt(x-2, y+1, z+2, 171)
				level.setBlockDataAt(x-2, y+1, z+2, 11)
				
				level.setBlockAt(x+2, y+1, z-2, 171)
				level.setBlockDataAt(x+2, y+1, z-2, 11)
				
				level.setBlockAt(x+2, y+1, z+2, 171)
				level.setBlockDataAt(x+2, y+1, z+2, 11)
				
				level.setBlockAt(x+2, y+1, z-2, 171)
				level.setBlockDataAt(x+2, y+1, z-2, 11)
				
				level.setBlockAt(x-2, y+1, z-2, 171)
				level.setBlockDataAt(x-2, y+1, z-2, 11)

				if extrab == True:
				
					#Slime Block #3x3
					
					level.setBlockAt(x, y, z, 165)
					level.setBlockDataAt(x, y, z, 0)
					
					level.setBlockAt(x+1, y, z, 165)
					level.setBlockDataAt(x+1, y, z, 0)
					
					level.setBlockAt(x, y, z+1, 165)
					level.setBlockDataAt(x, y, z+1, 0)
					
					level.setBlockAt(x+1, y, z+1, 165)
					level.setBlockDataAt(x+1, y, z+1, 0)
					
					level.setBlockAt(x, y, z-1, 165)
					level.setBlockDataAt(x, y, z-1, 0)
					
					level.setBlockAt(x-1, y, z, 165)
					level.setBlockDataAt(x-1, y, z, 0)
					
					level.setBlockAt(x-1, y, z-1, 165)
					level.setBlockDataAt(x-1, y, z-1, 0)
					
					level.setBlockAt(x+1, y, z-1, 165)
					level.setBlockDataAt(x+1, y, z-1, 0)
					
					level.setBlockAt(x-1, y, z+1, 165)
					level.setBlockDataAt(x-1, y, z+1, 0)
					
					
					
					#Part 2 Slime 3x3 Empty Circle
					
					level.setBlockAt(x+2, y, z, 165)
					level.setBlockDataAt(x+2, y, z, 0)
					
					level.setBlockAt(x-2, y, z, 165)
					level.setBlockDataAt(x-2, y, z, 0)
					
					level.setBlockAt(x, y, z+2, 165)
					level.setBlockDataAt(x, y, z+2, 0)
					
					level.setBlockAt(x, y, z-2, 165)
					level.setBlockDataAt(x, y, z-2, 0)
					
					level.setBlockAt(x+2, y, z-1, 165)
					level.setBlockDataAt(x+2, y, z-1, 0)
					
					level.setBlockAt(x-1, y, z+2, 165)
					level.setBlockDataAt(x-1, y, z+2, 0)
					
					level.setBlockAt(x+1, y, z+2, 165)
					level.setBlockDataAt(x+1, y, z+2, 0)
					
					level.setBlockAt(x+2, y, z+1, 165)
					level.setBlockDataAt(x+2, y, z+1, 0)
					
					level.setBlockAt(x+1, y, z+-2, 165)
					level.setBlockDataAt(x+1, y, z-2, 0)
					
					level.setBlockAt(x-2, y, z+1, 165)
					level.setBlockDataAt(x-2, y, z+1, 0)
					
					level.setBlockAt(x-2, y, z-1, 165)
					level.setBlockDataAt(x-2, y, z-1, 0)
					
					level.setBlockAt(x-1, y, z-2, 165)
					level.setBlockDataAt(x-1, y, z-2, 0)
					
					#Part 3 Slime Outer Ring
					
					level.setBlockAt(x+3, y, z, 165)
					level.setBlockDataAt(x+3, y, z, 0)
					
					level.setBlockAt(x-3, y, z, 165)
					level.setBlockDataAt(x-3, y, z, 0)
					
					level.setBlockAt(x, y, z+3, 165)
					level.setBlockDataAt(x, y, z+3, 0)
					
					level.setBlockAt(x, y, z-3, 165)
					level.setBlockDataAt(x, y, z-3, 0)
					
					level.setBlockAt(x+1, y, z-3, 165)
					level.setBlockDataAt(x+1, y, z-3, 0)
					
					level.setBlockAt(x-1, y, z-3, 165)
					level.setBlockDataAt(x-1, y, z-3, 0)
					
					level.setBlockAt(x+3, y, z-1, 165)
					level.setBlockDataAt(x+3, y, z-1, 0)
					
					level.setBlockAt(x-3, y, z-1, 165)
					level.setBlockDataAt(x-3, y, z-1, 0)
					
					level.setBlockAt(x+3, y, z+1, 165)
					level.setBlockDataAt(x+3, y, z+1, 0)
					
					level.setBlockAt(x-3, y, z+1, 165)
					level.setBlockDataAt(x-3, y, z+1, 0)
					
					level.setBlockAt(x+1, y, z+3, 165)
					level.setBlockDataAt(x+1, y, z+3, 0)
					
					level.setBlockAt(x-1, y, z+3, 165)
					level.setBlockDataAt(x-1, y, z+3, 0)
					
					level.setBlockAt(x-2, y, z+2, 165)
					level.setBlockDataAt(x-2, y, z+2, 0)
					
					level.setBlockAt(x+2, y, z-2, 165)
					level.setBlockDataAt(x+2, y, z-2, 0)
					
					level.setBlockAt(x+2, y, z+2, 165)
					level.setBlockDataAt(x+2, y, z+2, 0)
					
					level.setBlockAt(x+2, y, z-2, 165)
					level.setBlockDataAt(x+2, y, z-2, 0)
					
					level.setBlockAt(x-2, y, z-2, 165)
					level.setBlockDataAt(x-2, y, z-2, 0)
				else:
					#String Middle Block #3x3
					
					level.setBlockAt(x, y, z, 166)
					level.setBlockDataAt(x, y, z, 0)
					
					level.setBlockAt(x+1, y, z, 166)
					level.setBlockDataAt(x+1, y, z, 0)
					
					level.setBlockAt(x, y, z+1, 166)
					level.setBlockDataAt(x, y, z+1, 0)
					
					level.setBlockAt(x+1, y, z+1, 166)
					level.setBlockDataAt(x+1, y, z+1, 0)
					
					level.setBlockAt(x, y, z-1, 166)
					level.setBlockDataAt(x, y, z-1, 0)
					
					level.setBlockAt(x-1, y, z, 166)
					level.setBlockDataAt(x-1, y, z, 0)
					
					level.setBlockAt(x-1, y, z-1, 166)
					level.setBlockDataAt(x-1, y, z-1, 0)
					
					level.setBlockAt(x+1, y, z-1, 166)
					level.setBlockDataAt(x+1, y, z-1, 0)
					
					level.setBlockAt(x-1, y, z+1, 166)
					level.setBlockDataAt(x-1, y, z+1, 0)
					
					
					
					#String Block Inner #3x3
					
					level.setBlockAt(x+2, y, z, 166)
					level.setBlockDataAt(x+2, y, z, 0)
					
					level.setBlockAt(x-2, y, z, 166)
					level.setBlockDataAt(x-2, y, z, 0)
					
					level.setBlockAt(x, y, z+2, 166)
					level.setBlockDataAt(x, y, z+2, 0)
					
					level.setBlockAt(x, y, z-2, 166)
					level.setBlockDataAt(x, y, z-2, 0)
					
					level.setBlockAt(x+2, y, z-1, 166)
					level.setBlockDataAt(x+2, y, z-1, 0)
					
					level.setBlockAt(x-1, y, z+2, 166)
					level.setBlockDataAt(x-1, y, z+2, 0)
					
					level.setBlockAt(x+1, y, z+2, 166)
					level.setBlockDataAt(x+1, y, z+2, 0)
					
					level.setBlockAt(x+2, y, z+1, 166)
					level.setBlockDataAt(x+2, y, z+1, 0)
					
					level.setBlockAt(x+1, y, z+-2, 166)
					level.setBlockDataAt(x+1, y, z-2, 0)
					
					level.setBlockAt(x-2, y, z+1, 166)
					level.setBlockDataAt(x-2, y, z+1, 0)
					
					level.setBlockAt(x-2, y, z-1, 166)
					level.setBlockDataAt(x-2, y, z-1, 0)
					
					level.setBlockAt(x-1, y, z-2, 166)
					level.setBlockDataAt(x-1, y, z-2, 0)
					
					#Iron Fence Block #3x3 Outer
					
					level.setBlockAt(x+3, y, z, 101)
					level.setBlockDataAt(x+3, y, z, 0)
					
					level.setBlockAt(x-3, y, z, 101)
					level.setBlockDataAt(x-3, y, z, 0)
					
					level.setBlockAt(x, y, z+3, 101)
					level.setBlockDataAt(x, y, z+3, 0)
					
					level.setBlockAt(x, y, z-3, 101)
					level.setBlockDataAt(x, y, z-3, 0)
					
					level.setBlockAt(x+1, y, z-3, 101)
					level.setBlockDataAt(x+1, y, z-3, 0)
					
					level.setBlockAt(x-1, y, z-3, 101)
					level.setBlockDataAt(x-1, y, z-3, 0)
					
					level.setBlockAt(x+3, y, z-1, 101)
					level.setBlockDataAt(x+3, y, z-1, 0)
					
					level.setBlockAt(x-3, y, z-1, 101)
					level.setBlockDataAt(x-3, y, z-1, 0)
					
					level.setBlockAt(x+3, y, z+1, 101)
					level.setBlockDataAt(x+3, y, z+1, 0)
					
					level.setBlockAt(x-3, y, z+1, 101)
					level.setBlockDataAt(x-3, y, z+1, 0)
					
					level.setBlockAt(x+1, y, z+3, 101)
					level.setBlockDataAt(x+1, y, z+3, 0)
					
					level.setBlockAt(x-1, y, z+3, 101)
					level.setBlockDataAt(x-1, y, z+3, 0)
					
					level.setBlockAt(x-2, y, z+2, 101)
					level.setBlockDataAt(x-2, y, z+2, 0)
					
					level.setBlockAt(x+2, y, z-2, 101)
					level.setBlockDataAt(x+2, y, z-2, 0)
					
					level.setBlockAt(x+2, y, z+2, 101)
					level.setBlockDataAt(x+2, y, z+2, 0)
					
					level.setBlockAt(x+2, y, z-2, 101)
					level.setBlockDataAt(x+2, y, z-2, 0)
					
					level.setBlockAt(x-2, y, z-2, 101)
					level.setBlockDataAt(x-2, y, z-2, 0)
				
				
