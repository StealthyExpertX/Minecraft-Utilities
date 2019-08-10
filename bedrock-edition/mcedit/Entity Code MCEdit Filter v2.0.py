# coding unicode-escape
# Feel free to modify and use this filter however you wish. If you do,
# please give credit to SethBling and to StealthyExpert for updating this script for Bedrock Edition support.
# http://youtube.com/SethBling

from pymclevel import TAG_List, TAG_Byte, TAG_Int, TAG_Compound, TAG_Short, TAG_Double, TAG_Float, TAG_String, TAG_Long, TAG_Int_Array
import os

displayName = "Entity Code v2.0"

inputs = (
	("Entities: ", True),
	("TileEntities: ", True)
)

def getIdName(nbt):
	if "identifier" in nbt:
		return "identifier"
	return "id"

def getIdValue(nbt):
	if "identifier" in nbt:
		return nbt["identifier"].value
	return nbt["id"].value

def perform(level, box, options):
	os.system('cls||clear')
	print ("")
	print ("from pymclevel import TAG_Int, TAG_String, TAG_Compound, TAG_Byte TAG_Double, TAG_Float, TAG_Int_Array, TAG_Long, TAG_List, TAG_Short")
	print ("from numpy import zeros")
	print ("")

	identifiers = {}

	for (chunk, _, _) in level.getChunkSlices(box):
		if options["TileEntities: "]:
			for t in chunk.TileEntities:
				x = t["x"].value
				y = t["y"].value
				z = t["z"].value
				if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
					displayCode(t, identifiers, getIdValue(t))

		if options["Entities: "]:
			for e in chunk.Entities:
				x = int(e["Pos"][0].value-0.5)
				y = int(e["Pos"][1].value)
				z = int(e["Pos"][2].value-0.5)
				if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
					displayCode(e, identifiers, getIdValue(e))

def lowerFirst(s):
	return s[0].lower() + s[1:]

def getIdentifier(name, identifiers):
	if name in identifiers:
		identifiers[name] = identifiers[name]+1
		return lowerFirst(name + str(identifiers[name]))

	else:
		identifiers[name] = 1
		return lowerFirst(name)

def singularize(s):
	if s[len(s)-1] == "s" and s != "pos":
		return s[0:len(s)-1]
	else:
		return s

def displayCode(nbt, identifiers, tag):
	if type(nbt) is TAG_Int:
		return "TAG_Int({0})".format(nbt.value)

	elif type(nbt) is TAG_Short:
		return "TAG_Short({0})".format(nbt.value)

	elif type(nbt) is TAG_Byte:
		return "TAG_Byte({0})".format(nbt.value)

	elif type(nbt) is TAG_Long:
		return "TAG_Long({0})".format(nbt.value)

	elif type(nbt) is TAG_Double:
		return "TAG_Double({0})".format(nbt.value)

	elif type(nbt) is TAG_Float:
		return "TAG_Float({0})".format(nbt.value)

	elif type(nbt) is TAG_String:
		return "TAG_String(u'{0}')".format(nbt.value)

	elif type(nbt) is TAG_Compound:
		id_name = getIdName(nbt)

		if id_name in nbt and type(nbt[id_name]) is TAG_String:
			if "identifier" in nbt:
				identifier = getIdentifier(nbt["identifier"].value.replace(":", "_"), identifiers)
			elif "id" not in nbt:
				identifier = getIdentifier(nbt.value.replace(":", "_"), identifiers)
			else:
				identifier = getIdentifier(nbt["id"].value.replace(":", "_"), identifiers)
		else:
			identifier = getIdentifier(tag, identifiers)

		print('{0} = TAG_Compound()'.format(identifier))

		for subtag in nbt:
			print '{0}["{1}"] = {2}'.format(identifier, subtag, displayCode(nbt[subtag], identifiers, subtag))

		return identifier

	elif type(nbt) is TAG_List:
		identifier = getIdentifier(tag, identifiers)

		print('{0} = TAG_List()'.format(identifier))

		for i in range(len(nbt)):
			print "{0}.append({1})".format(identifier, displayCode(nbt[i], identifiers, singularize(tag)))

		return identifier

	elif type(nbt) is TAG_Int_Array:
		identifier = getIdentifier(tag, identifiers)
		print('{0} = zeros({1}, ">u4")'.format(identifier, len(nbt.value)))

		for i in range(len(nbt.value)):
			print('{0}[{1}] = {2}'.format(identifier, str(i), nbt.value[i]))

		return 'TAG_Int_Array({0})'.format(identifier)
	else:
		print nbt