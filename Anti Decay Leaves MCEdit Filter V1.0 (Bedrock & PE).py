#Feel free to use this filter however you wish. 
#Follow me at @RedstonerLabs and my team Builders Horizon at @TheMCBuildTeam.

#Big credits to gentlegiantJGC, gentlegiantJGC#9219 for his fast chunk access with numpy.
#data[np.logical_and(chunk.Blocks[slices] == block, chunk.Data[slices] == value)] = new_value

#python imports
import time
import numpy as np

#display_name
displayName = "Anti Decay MCEdit Filter v1.0"

#user_inputs
inputs = (
	("Anti Decay MCEdit Filter", "label"),
	("This fither fixes leaves that decay.", "label"),
	("By StealthyExpertX - @RedstonerLabs", "label"),
	("Oak: ", False),
	("Birch: ", False),
	("Spruce: ", False),
	("Jungle: ", False),
	("Acaica: ", False),
	("Dark Oak: ", False),
)

#main preform
def perform(level, box, options):
	#start timer
	start = time.time()

	#empty dict
	blocks = {}

	#empty list
	leaves = {}

	#oak option
	if options["Oak: "]:
		blocks[(0,4)] = 8
		leaves[18] = 18

	#birch option
	if options["Birch: "]:
		blocks[(2,6)] = 10
		leaves[18] = 18

	#spruce option
	if options["Spruce: "]:
		blocks[(1,5)] = 9
		leaves[18] = 18

	#jungle option
	if options["Jungle: "]:
		blocks[(3,7)] = 11
		leaves[18] = 18

	#acacia option
	if options["Acaica: "]:
		blocks[(0,4)] = 8
		leaves[161] = 161

	#dark_oak option
	if options["Dark Oak: "]:
		blocks[(1,5)] = 9
		leaves[161] = 161

	#missing_options
	if len(blocks) == 0:
		raise ValueError("No options were selected, please try again!")

	#damage_value mapping
	data_map = blocks.keys()
	data_map = [x for t in data_map for x in t]

	#block_id mapping
	block_map = blocks.values()

	#block_mappings generator_list
	mappings = [
		(i_map, d_map, l_map) 
		for d_map in data_map
		for i_map in block_map
		for l_map in leaves
	]

	#scan_selection box
	for chunk, slices, _ in level.getChunkSlices(box):

		#data_values in_chunk
		data = chunk.Data[slices]

		#id_values in_chunk
		block = chunk.Blocks[slices]

		#block_&_values_&_ids from_mapping
		for (i_map, d_map, l_map) in mappings:

			#datavalue set_datavalue
			data[np.logical_and(block == l_map, data == d_map)] = i_map

		#mark_chunks to_relight
		chunk.dirty = True

	#end timer
	end = time.time()
	print "completion_time: " + str(end - start)