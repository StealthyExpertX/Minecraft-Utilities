#note this filter only works correctly in PE/BEDROCK worlds, saves, maps.

#feel free to use this filter however you wish. 
#follow me at @RedstonerLabs and my team Builders Horizon at @TheMCBuildTeam.

#big credits to gentlegiantJGC, gentlegiantJGC#9219 for his fast block access.

#version 1.1

#python imports
import time
import numpy as np

#display_name
displayName = "PE BEDROCK Hidden Lights MCEdit Filter v1.1"

#user_inputs
inputs = (
	("Hidden Lights MCEdit Filter V1.1", "label"),
	("Finds and changes blocks to hidden light sources.", "label"),
	("Glow Stone: ", False),
	("Sea Lantern: ", False),
	("Torch: ", False),
	("Redstone Torch: ", False),
	("Redstone Lamp: ", False),
	("Beacon: ", False),
	("Fire: ", False),
	("Jack o'Lantern: ", False),
	("End Rod: ", False),
	("Glowing Obsidian: ", False),
	("All: ", False),
	("By StealthyExpertX - @RedstonerLabs", "label"),
	)

#main preform
def perform(level, box, options):
	#start timer
	start = time.time()

	#empty list.
	blocks = []

	#glowstone.
	if options["Glow Stone: "]:
		blocks.append(89)

	#sealantern.
	if options["Sea Lantern: "]:
		blocks.append(169)

	#torch.
	if options["Torch: "]:
		blocks.append(50)

	#redstonetorch.
	if options["Redstone Torch: "]:
		blocks.append(76)

	#redstonelamp.
	if options["Redstone Lamp: "]:
		blocks.append(124)

	#beacon.
	if options["Beacon: "]:
		blocks.append(138)

	#jackolantern
	if options["Jack o'Lantern: "]:
		blocks.append(91)

	#endrod.
	if options["End Rod: "]:
		blocks.append(208)

	#glowingobsidian.
	if options["Glowing Obsidian: "]:
		blocks.append(246)

	#fire.
	if options["Fire: "]:
		blocks.append(51)

	#all.
	if options["All: "]:
		blocks.extend([89, 169, 50, 76, 124, 138, 91, 208, 246, 51])

	#check if nothing was selected.
	if len(blocks) == 0:
		raise ValueError("No options were selected, please try again!")

	#scan_selection box
	for chunk, slices, _ in level.getChunkSlices(box):

		#id_values in_chunk
		block = chunk.Blocks[slices]

		#data_values in_chunk
		data = chunk.Data[slices]

		#find_ids from_list
		for findblock in blocks:

			#block set_blockid
			block[block == findblock] = 208

			#data set_datavalue
			data[np.logical_and(block == findblock, True)] = 6

		#mark_chunks to_relight
		chunk.dirty = True

	#end timer
	end = time.time()
	print "completion_time: " + str(end - start)
