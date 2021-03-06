#!/usr/bin/env python

"""fah_scraper.py: compares the 2 most recent fah_scraper outputs and
generates a csv containing f@h username, points, and WUs into a folder called point_diffs."""

__author__ = "stuckat6pm"

# python imports
import csv
import datetime
import math
import os
from pathlib import Path

# make data directory
if not os.path.isdir("point_diffs"):
    os.makedirs("point_diffs")

logs = Path("logs")
payouts = Path("point_diffs")
# Here I name the files a timestamp, but it can be called whatever
filename = str(math.floor(datetime.datetime.now().timestamp()))

# grab most recent files
comparison = sorted(Path(logs).iterdir(), key=os.path.getmtime, reverse=True)[:2]
print("COMPARING", comparison[0], comparison[1])

with open(comparison[0], "r") as new:
    next(new)
    new = {row[0]: [int(row[1]), int(row[2])] for row in csv.reader(new)}
with open(comparison[1], "r") as old:
    next(old)
    old = {row[0]: [int(row[1]), int(row[2])] for row in csv.reader(old)}

with open(payouts / ("%s.csv" % filename), "w+", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Credit", "WUs"])
    for key in new:
        if key in old:
            new_vals = new[key]
            old_vals = old[key]
            points = abs(new_vals[0] - old_vals[0])
            WU = abs(new_vals[1] - old_vals[1])
            if points:
                writer.writerow([key, points, WU])
