# fah_scraper
Demo scraper for folding@home team stats webpages

## fah_scraper.py
Pulls data from banano folding at home team - https://apps.foldingathome.org/teamstats/team234980

Generates a csv containing rows of f@h username, points, and WUs into a folder called `logs` that is created in the directory the script is run from.

**Output style:**
```ID,Credit,WUs
vmiarc39yres,6055872957,43042
6m5khs4cnqq2,2499144190,22473
tkmrq8rmmql0,1750049359,8492
rv8fxr56dolc,1275514561,11510
tfgjdryn2a11,1251863199,10595
```

## generate_payout_data.py
Checks logs folder and if more than one csv file is found, compares the 2 most recent files, calculating differences in points and WU.

Generates a csv containing rows of f@h username, points, and WUs into a folder called `point_diffs` that is created in the directory the script is run from.
Output only includes non-zero rows.

**Output style:**
```ID,Credit,WUs
vmiarc39yres,6055872957,43042
6m5khs4cnqq2,2499144190,22473
tkmrq8rmmql0,1750049359,8492
rv8fxr56dolc,1275514561,11510
tfgjdryn2a11,1251863199,10595

