#!/usr/bin/python3
import apt
import json
cache = apt.Cache()
app_list = open("pkg.list", 'r')
pkg_list = open("src.list", 'w')
src_list = []
for pkg in app_list.readlines():
    pkg_name = pkg.strip("\n")
    src = cache[pkg_name].candidate.source_name
    if src not in src_list:
        src_list.append(src)
        pkg_list.write(src)
        pkg_list.write("\n")

print(len(src_list))
with open('src.json','w') as fp:
    json.dump(src_list, fp)
