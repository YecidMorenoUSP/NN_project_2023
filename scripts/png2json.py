import json
import os
import sys
import glob

_path = "database/out/"

info_json = {}

for file in glob.glob(_path+"*.png"):
    f = file.split("/")[-1]
    info_json[f] = {"type":"suspected"}

with open("database/out/info.json", "w") as outfile:
    to_txt = json.dumps(info_json,indent=4)
    outfile.write(to_txt)