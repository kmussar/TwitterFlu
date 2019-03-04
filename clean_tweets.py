# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:36:02 2019

@author: kmuss
"""

import pickle
import pandas as pd
import numpy as np

filename = 'sick.pickle'

with open(filename, 'rb') as read_file:
    df = pickle.load(read_file)
print("opened df") # to check status of script
print(df.info())

# drop duplicates 
df= df.drop_duplicates(subset='text')
df= df.reset_index()
print("dropped duplicates")
print(df.info())
print(len(df['text']))

# remove retweets 
def remove_RT(df):
    # Remove retweets (RT)
    # Set RT to True (1) 
    length = len(df['text'])
    for x in range(length):
        if 'RT @' in df['text'][x]:
            df['retweeted'][x] = 1
            #print("found one!")
    # Create filter for RTs
    indexNames = df[df['retweeted'] == 1.0 ].index
    # Delete filtered row
    df.drop(indexNames , inplace=True)
    #with open('temp_df', 'wb') as to_write:
        #pickle.dump(df, to_write) 
    return df

remove_RT(df)
print(df.info())
df.reset_index(inplace=True, drop=True)
df.drop(columns=['retweeted'],axis=1, inplace=True)

# Remove hyperlinks and mentions
df = df.replace("(?:\@|https?\://)\S+", "", regex=True)

# Separate hashtags into their own column
df['hashtags'] = df['text'].apply(lambda x: x.split('#')[1:])
df['text']= df['text'].apply(lambda x: x.split('#')[0])

df= df.reset_index()
df.info()   

# Save pickle   
with open('sick_clean.pickle', 'wb') as to_write:
        pickle.dump(df, to_write)

