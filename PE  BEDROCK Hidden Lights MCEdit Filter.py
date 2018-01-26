#Hidden Lights MCEdit Filter created by StealthyExpertX , @RedstonerLabs , StealthyExpertX#8940
#Note this filter only works correctly in PE/BEDROCK worlds,saves,maps.

#You may use this filter and the code how ever you wish.

#user inputs / GUI / settings
inputs = (
    ("Hidden Lights MCEdit Filter", "label"),
    ("This filter finds and converts blocks to hidden light sources", "label"),
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
    )

#sets invisible end rod block
def setInvisibleBlock(level, x, y, z):

    #set the block id 250
    level.setBlockAt(x, y, z, 208)

    #set the block damage 250
    level.setBlockDataAt(x, y, z, 6)

#getBlock method gets block id of block at x, y, z
def getBlock(level, x, y, z):
    return level.blockAt(x, y, z)

def perform(level, box, options):

    #empty list
    idArray = []

    #if all is true it will convert all valid block types
    if options["All: "] == True:

        #extend list items to check if blocks exist and if they do then convert them to invisible end rods.
        idArray.extend([89, 169, 50, 76, 124, 138, 91, 208, 246, 51])

        #scan selection, x,y,z
        for x in xrange(box.minx, box.maxx):

            for y in xrange(box.miny, box.maxy):

                for z in xrange(box.minz, box.maxz):

                    #get block id and check if its in the idArray
                    if getBlock(level, x, y, z) in idArray:
                        #set invisible end rod 
                        setInvisibleBlock(level, x, y, z, True)

    #if all is false it will only convert selected valid block types
    else:
        
        #append list item to check if block exist and if it does convert it to invisible end rods.
        if options["Glow Stone: "]:
            idArray.append(89)

        if options["Sea Lantern: "]:
            idArray.append(169)

        if options["Torch: "]:
            idArray.append(50)

        if options["Redstone Torch: "]:
            idArray.append(76)

        if options["Redstone Lamp: "]:
            idArray.append(124)

        if options["Beacon: "]:
            idArray.append(138)

        if options["Jack o'Lantern: "]:
            idArray.append(91)

        if options["End Rod: "]:
            idArray.append(208)

        if options["Glowing Obsidian: "]:
            idArray.append(246)

        if options["Fire: "]:
            idArray.append(51)

        #scan selection, x,y,z
        for x in xrange(box.minx, box.maxx):

            for y in xrange(box.miny, box.maxy):

                for z in xrange(box.minz, box.maxz):

                    #get block id and check if its in the idArray
                    if getBlock(level, x, y, z) in idArray:
                    
                        #set invisible end rod 
                        setInvisibleBlock(level, x, y, z, False)