# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 20:44:24 2017

@author: muftring
"""

import csv
from collections import Counter

Title = 0
Year = 1
Rating = 2
Votes = 3

f = open('imdb.csv', 'r')
reader = csv.reader(f, delimiter='\t')
counter = Counter()
c = 0

for row in reader:
    c += 1
    print(c)
    if c > 1:
        counter[row[Year]] += 1

earliest = min(counter.keys())
latest = max(counter.keys())

print("The earliest is", earliest)
print("The latest is", latest)
