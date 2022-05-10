# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests

r = requests.get("https://ruleset.skk.moe/List/non_ip/stream.conf", stream=True)
d = requests.get("https://ruleset.skk.moe/List/non_ip/domestic.conf", stream=True)
with open("stream.conf", "a") as f:
    # Domestic
    for dline in d.iter_lines():
        if "DOMAIN" in dline.decode('utf-8'):
            f.write("  - "+dline.decode('utf-8')+",China\n")
    # Stream Media
    for line in r.iter_lines():
        if "DOMAIN" in line.decode('utf-8') and "youtube" not in line.decode('utf-8') and "google" not in line.decode('utf-8'):
            f.write("  - "+line.decode('utf-8')+",Media\n")

