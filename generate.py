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
filter = ["youtube", "google", "porn", "twitch", "soundcloud", "dmm", "jtvnw", "ttvnw"]
domefilter = ["bili", "acg", "b23", "hdslb"]
shutil.copyfile("rules-model.txt", rule_file)
with open(rule_file, "r") as f:
    # Domestic
    rules = f.read()
with open(rule_file, "w") as f:
    toappend = ""
    for dline in d.iter_lines():
        ds = dline.decode('utf-8')
        if "DOMAIN" in dline.decode('utf-8') and not any(f in ds for f in domefilter):
            toappend += "  - "+dline.decode('utf-8')+",China\n"
    # Stream Media
    for line in r.iter_lines():
        ls = line.decode('utf-8')
        if "DOMAIN" in ls and not any(f in ls for f in filter):
            toappend += "  - "+line.decode('utf-8')+",海外流媒体\n"
    f.write(rules.format(rule=toappend))
