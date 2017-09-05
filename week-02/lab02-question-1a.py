# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 21:25:59 2017

@author: muftring
"""

import pandas as pd

df = pd.read_csv('imdb.csv', sep='\t')
earliest = df.Year.min()
latest = df.Year.max()
print("The earliest year: ", earliest)
print("The latest year: ", latest)

years = df.Year
counts = years.groupby(years).size()
print("Year\tCount")
print("----\t-----")
for year in counts.index:
    print(year,"\t",counts[year])

avgRating = df.Rating.mean()
avgVotes = df.Votes.mean()
print("Average Rating: ", avgRating)
print("Average Votes: ", avgVotes)

top5byRating = df.sort_values(by='Rating',ascending=False).head(5)
print("Top 5 movies, by rating")
print(top5byRating)

top5byVotes = df.sort_values(by='Votes', ascending=False).head(5)
print("Top5 movies, by votes")
print(top5byVotes)