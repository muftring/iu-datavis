#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:58:20 2017

@author: uftringfamily
"""

import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt

# Q1: Calculate the following basic characteristics of ratings of movies 
# only in 1994: 10th percentile, median, mean, 90th percentile. 
df = pd.read_csv('imdb.csv', delimiter='\t')
selector =  df['Year'] == 1994
moviesFrom1994 = df[selector]
ratings = moviesFrom1994['Rating']

ratings10thPercentile = np.percentile(ratings, 10)
ratingsMedian = np.median(ratings)
ratingsMean = np.mean(ratings)
ratings90thPercentile = np.percentile(ratings, 90)

print("1994 movie ratings, \n\tmean: {} \n\tmedian: {} \n\t10th-percentile: {} \n\t90th-percentile: {}".format(ratingsMean, ratingsMedian, ratings10thPercentile, ratings90thPercentile))

# Q2: plot the histogram of ratings of the movies between 2000 and 2014
selector1 = df['Year'] >= 2010
selector2 = df['Year'] <= 2014
moviesFrom2010to2014 = df[selector1 & selector2]
moviesFrom2010to2014['Rating'].hist()

# Q3: plot the histogram of ratings using the pyplot.hist() function
# (1) change the color from blue to whatever you want
# (2) add labels of x and y axis
# (3) change the number of bins to 20

# Q4: use Seaborn...
