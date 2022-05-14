# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import shutil
import os

r = requests.get("https://ruleset.skk.moe/List/non_ip/stream.conf", stream=True)
d = requests.get("https://ruleset.skk.moe/List/non_ip/domestic.conf", stream=True)
rule_file = os.path.dirname(os.path.realpath(__file__))+"/rules.txt"
if os.path.isfile(rule_file):
    os.remove(rule_file)
shutil.copyfile("/home/wwwroot/network.tw/rules-model.txt", rule_file)
with open(rule_file, "r") as f:
    # Domestic
    rules = f.read()
with open(rule_file, "w") as f:
    toappend = ""
    for dline in d.iter_lines():
        if "DOMAIN" in dline.decode('utf-8') and "bili" not in dline.decode('utf-8') and "acg" not in dline.decode('utf-8') and "hdslb" not in dline.decode('utf-8') and "#" not in dline.decode('utf-8'):
            toappend += "  - "+dline.decode('utf-8')+",China\n"
    # Stream Media
    for line in r.iter_lines():
        if "DOMAIN" in line.decode('utf-8') and "youtube" not in line.decode('utf-8') and "google" not in line.decode('utf-8'):
            toappend += "  - "+line.decode('utf-8')+",海外流媒体\n"
    f.write(rules.format(rule=toappend))
