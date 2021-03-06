#!/usr/bin/env python

"""fah_scraper.py: generates a csv containing f@h username, points, and WUs into a folder called logs."""

__author__ = "stuckat6pm"


# python modules
import csv
import datetime
import os
import math
from pathlib import Path

# requires installation from pypi
import requests
import lxml.html

# make data directory
if not os.path.isdir("logs"):
    os.makedirs("logs")

# pull web page
html = requests.get("https://apps.foldingathome.org/teamstats/team234980")
doc = lxml.html.fromstring(html.content)
table = doc.xpath(".//body/table/tr[not(th)]")

# Here I name the files a timestamp, but it can be called whatever
filename = str(math.floor(datetime.datetime.now().timestamp()))

with open(
    Path("logs") / ("%s.csv" % filename), "w+", newline="", encoding="utf-8"
) as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Credit", "WUs"])
    for row in table:
        # Rank, Team Rank, Name, Credit, WUs
        writer.writerow([col.text for col in row[2:]])
