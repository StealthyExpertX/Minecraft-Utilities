#Credits: StealthyExpert - @RedstonerLabs

#Copies clipboard contents and generates all language files in the "texts" folder for Minecraft Bedrock Edition.
#Requires pyperclip, it's suguested that you use pip to install lastest version of pyperclip.

#Example Usage:
#python generate_langs.py
#Run from cmd.exe in administrator mode make sure to install python 2.7+ and not python 3.0.

#Required imports.
import pyperclip
import io
import os
import json
import shutil

#Get clipboard data.
clip_data = pyperclip.paste()

#Language list.
lang_list = [
	"en_US.lang",
	"en_GB.lang",
	"de_DE.lang",
	"es_ES.lang",
	"es_MX.lang",
	"fr_FR.lang",
	"fr_CA.lang",
	"it_IT.lang",
	"ja_JP.lang",
	"ko_KR.lang",
	"pt_BR.lang",
	"pt_PT.lang",
	"ru_RU.lang",
	"zh_CN.lang",
	"zh_TW.lang",
	"nl_NL.lang",
	"bg_BG.lang",
	"cs_CZ.lang",
	"da_DK.lang",
	"el_GR.lang",
	"fi_FI.lang",
	"hu_HU.lang",
	"id_ID.lang",
	"nb_NO.lang",
	"pl_PL.lang",
	"sk_SK.lang",
	"sv_SE.lang",
	"tr_TR.lang",
	"uk_UA.lang"
]

#Move file a to directory b.
def moveFile(a, b):
	shutil.move(a, b)

#Generate the "texts" folder if it doesn't exist.
try:
	os.mkdir("texts")

#Spit an error out the "texts" folder creation failed.
except OSError:
	print ("Creation of the directory /texts failed.")

#Display success message if "texts" folder creation suceeded.
else:
	print ("Successfully created the /texts directory.")

#Generate a json file using the language list.
with open('languages.json', 'w') as json_file:
	json.dump(lang_list, json_file)

#Loop through each language in the language list.
for lang in lang_list:

	#Generate a text file with the extension ".lang" using utf-8 encoding.
	with io.open(lang, "w", encoding="utf-8") as output:

		#Loop through each line in the clipboard and write it to the text file.
		for line in clip_data:
			output.write(line)

	#Move language files that are generated to the "texts" folder.
	moveFile(lang, "texts/"+lang)

#Move languages.json that was generated to the "texts" folder.
moveFile('languages.json', 'texts/languages.json')