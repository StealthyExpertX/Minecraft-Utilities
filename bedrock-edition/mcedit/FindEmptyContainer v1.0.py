#By StealthyExpertX @RedstonerLabs

from pymclevel import TAG_Int, TAG_String, TAG_Compound, TAG_Byte
import numpy as np
import random, os, sys, directories, urllib2, json, albow

displayName = "Find Empty Contaners v1.0"

def perform(level, box, options):
	blocksSupported = {
		23 : "Dispenser",
		54 : "Chest",
		61 : "Furnace",
		62 : "Furnace",
		125 : "Dropper",
		130 : "EnderChest",
		138 : "Beacon",
		146 : "Chest",
		146 : "Barrel",
		154 : "Hopper",
		205 : "ShulkerBox",
		218 : "ShulkerBox"
	}
	for cx, cz in box.chunkPositions:
		try:
			chunk = level.getChunk(cx, cz)
		except:
			continue
		chunkBlockList = np.unique(chunk.Blocks)
		for block in chunkBlockList:
			if block not in blocksSupported:
				continue
			for coord in np.argwhere(chunk.Blocks == block):
				x,z,y = coord
				x += cx * 16
				z += cz * 16
				if (x,y,z) not in box:
					continue
				te = level.tileEntityAt(x,y,z)
				if 'Items' in te and len(te['Items']) == 0 and "LootTable" not in te:
					print "Found:" + str(te["id"].value) + " /tp @s " + str(x) + " " + str(y) + " " + str(z)