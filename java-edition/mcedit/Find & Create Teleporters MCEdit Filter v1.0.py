#Find And Create Teleporters Filter! :)
#filter created by StealthyExpert AKA @RedstonerLabs, iPxD Mods AKA @iPxD_Official follow us on twitter.
#NOTE: this filter will only work in these versions and anything btw these versions, 1.9, 1.10, 1.11, 1.12, 1.12.2+.

#mcedit imports
from pymclevel import TAG_Byte, TAG_Int, TAG_Compound, TAG_String, TileEntity, TAG_Long
from pymclevel.materials import alphaMaterials

#system imports
import os, sys

#message list array
tpms = []
bkms = []

#teleport destination coordinates and teleport block coordinates dict arrays.
tp = {}
bk = {}

#counter for teleport block coordinates array.
cnt = 0

#block ids dict array of tilentities that work with this filter.
idsdict = {
    "(Banner Standing)": 177,
    "(Banner Wall)": 176,
    "(Bed 1.12 Only)": 26,
    "(Beacon)": 138,
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

#barrowed from setblings potion effect filter credits to you! ;)
#keys for idsdict to render in ui/gui user interface.
EffectKeys = ()
for key in idsdict.keys():
	EffectKeys = EffectKeys + (key,)

#ui/gui user interface.
inputs = [
    (
        ("Main", "title"),
        ("(Find And Create Teleporters MCEdit Filter)", "label"),
        ("EndGateway Block: ", EffectKeys),
        ("EndGateway Data: ", (0,0,15)),
        ("Start = Teleporter: ", alphaMaterials.LightGreenWool),
        ("End = Destination: ", alphaMaterials.RedWool),
        ("Invisible Teleporter: ", False),
        ("ExactTeleport: ", True),
        ("1.11+: ", True),
    ), (
        ("About", "title"),
        ("(Contact Information)", "label"),
        ("", "label"),
        ("This filter was created by StealthyExpert & IPxD Mods", "label"),
        ("follow me on twitter", "label"),
        ("twitter.com/RedstonerLabs  @RedstonerLabs", "label"),
        ("subscribe to my channel on YouTube", "label"),
        ("youtube.com/channel/UCfSCq4Al4Bx7geFdbkLxMxw", "label"),
        ("join my server on Discord", "label"),
        ("discord.gg/67cbdEj", "label"),
    ),
]

#check if its other+.
def callerOne(clearlinux):

    if clearlinux == "1":
        return "1"

    else:
        return "0"

#check if its windows.
def callerTwo(clearwindows):

    if clearwindows == "1":
        return "1"

    else:
        return "0"

#clear console ouput
def clearConsole():

    #the reason I did it like this is because when clearing the console it returns a int value based on the operating system type.
    #this finds the text and replaces it with "" A blank space so that it doesnt show in the console and leaves it as A cleared console.

    clearlinux = str(os.system('clear'))
    clearlinux = clearlinux.replace((callerOne(clearlinux)), "")

    clearwindows = str(os.system('cls'))
    clearwindows = clearwindows.replace((callerTwo(clearlinux)), "")

    print clearwindows, clearlinux

#catches some extra tracebacks errors encase of missing .py's in the mcedit directory.
def excepthook(type, value, traceback):
    print(value)

#@abrightmoore's setBlock() method should be part of the official mcedit api honestly.
def setBlock(level, (block, data), x, y, z):
    level.setBlockAt(int(x), int(y), int(z), block)
    level.setBlockDataAt(int(x), int(y), int(z), data)

#stores endgateway x, y, z coordinates and you can get them with chs.get("x"), chs.get("y"), chs.get("z") #dict array.
def bkArray(x, y, z):
    global cnt

    cnt = cnt
    cnt += 1

    bk.update({cnt: {"x":x, "y":y, "z":z}})

#stores teleport x, y, z coordinates and you can get them with tp.get("x"), tp.get("y"), tp.get("z") #dict array.
def tpArray(x, y, z):
    global tp

    crs = {"x":x, "y":y, "z":z}

    tp.update(crs)

#creates endgateways at teleporter block x, y, z that teleport players to destination block x, y, z
def createEndGateway(level, options, block_ids, block_datas):

    for key in bk:
        chunk = level.getChunk(bk[key]["x"]/16, bk[key]["z"]/16)

        e = TAG_Compound()

        e["ExactTeleport"] = TAG_Byte(options["ExactTeleport: "])

        e["x"] = TAG_Int(bk[key]["x"])
        e["y"] = TAG_Int(bk[key]["y"])
        e["z"] = TAG_Int(bk[key]["z"])

        ep = TAG_Compound()
        ep["X"] = TAG_Int(tp.get("x"))
        ep["Y"] = TAG_Int(tp.get("y"))
        ep["Z"] = TAG_Int(tp.get("z"))
        e["ExitPortal"] = ep

        if options["1.11+: "]:
            e["id"] = TAG_String("minecraft:end_gateway")

        else:
            e["id"] = TAG_String("EndGateway")

        e["Age"] = TAG_Long(9223372036854775807)

        if options["Invisible Teleporter: "]:
            setBlock(level, (36, 0), bk[key]["x"], bk[key]["y"], bk[key]["z"])

        else:
            setBlock(level, (block_ids, block_datas), bk[key]["x"], bk[key]["y"], bk[key]["z"])

        chunk.TileEntities.append(e)

#main init script code.
def perform(level, box, options):

    #counters used for teleporter idsv for console ouput and also used for error detection.
    counter = 1
    counter2 = 1

    #clear console method.
    clearConsole()

    #tileentity block id and data value varibles.
    block_ids = dict([(trn._(a), b) for a, b in idsdict.items()])[options["EndGateway Block: "]]
    block_datas = options["EndGateway Data: "]

    #destination block varibles.
    end_block = options["End = Destination: "].ID
    end_data = options["End = Destination: "].blockData

    #teleporter block varibles.
    start_block = options["Start = Teleporter: "].ID
    start_data = options["Start = Teleporter: "].blockData

    #catch exception hook.
    sys.excepthook = excepthook

    #scan all blocks in the selection box by looping through x, y, z coordinates through the selection.
    for x in xrange(box.minx, box.maxx):

        for y in xrange(box.miny, box.maxy):

            for z in xrange(box.minz, box.maxz):

                #get block id and block data values in the current coordinate x, y, z.
                block_id = level.blockAt(x,y,z)
                block_data = level.blockDataAt(x, y, z)

                #check if destination block exist in the selection.
                if end_block == block_id and end_data == block_data and "x" not in tp:

                    #add destination block coordinates in the selection to the bk dict array.
                    tpArray(x, y, z)

                    #add destination block information in the selection to the bk tpms array.
                    tpms.append("(Destination) ID:" +  str(counter) + " (Coordinates) X: " + str(x) + " Y:" + str(y) + " Z:" + str(z))

                    #error detection counter and destination block instance id info.
                    counter += 1
                    counter = (counter)

                    #set air block id and block data at x, y z to be id:0, data:0.
                    setBlock(level, (0, 0), x, y, z)

                #check if teleporter block exist in the selection.
                if start_block == block_id and start_data == block_data:

                    #add teleporter block coordinates in the selection to the bk dict array.
                    bkArray(x, y, z)

                    #add teleporter block information in the selection to the bkms array.
                    bkms.append("(Teleporter) ID:" + str(counter2) + " (Coordinates) X: "+ str(x)+ " Y:"+ str(y)+ " Z:" + str(z))

                    #error detection counter and teleporter block instance id info.
                    counter2 += 1
                    counter2 = (counter2)

    #this is pretty straight foward so no need to explain its just basic error handling and completed successful messages.
    if counter2 == 1 and counter == 1:
        print "Error Values: BK:" + str(counter2) + " TP:" + str(counter)
        raise ValueError('No Teleporter Block Or Destination Block Found In Selection!')

    elif counter2 == 1:
        print "Error Values: BK:" + str(counter2) + " TP:" + str(counter)
        raise ValueError('No Teleporter Block Found In Selection!')

    elif counter == 1:
        print "Error Values: BK:" + str(counter2) + " TP:" + str(counter)
        raise ValueError('No Destination Block Found In Selection!')

    elif counter > 1 and counter2 > 1:
        for tpm in tpms:
            print tpm
        for bkm in bkms:
            print bkm
        print "Completed Successfully!"

    else:
        print "Error Values: BK:" + str(counter2) + " TP:" + str(counter)
        print "Unknown Error!"

    #create the endgateways if there are no errors detected.
    createEndGateway(level, options, block_ids, block_datas)