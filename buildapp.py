#!/usr/bin/python3
import json
with open('src.json', 'r') as f:
    src_list = json.load(f)

with open('data.json', 'r') as f:
    pkg_dic = json.load(f)

rebuilt_list = []
for pkg in pkg_dic:
    if pkg["name"] in src_list:
        print("%s depends on qt, should be rebuilt" % pkg["name"])
        rebuilt_list.append(pkg["name"])

if len(rebuilt_list):
    print(rebuilt_list)

with open('rebuild_list.json', 'w') as f:
    json.dump(rebuilt_list, f)
