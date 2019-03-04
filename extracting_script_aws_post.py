# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from collections import defaultdict
import pickle
import json

filenames = (['tweets_sore throat.json', 'tweets_runny nose.json',
              'tweets_sneezing.json'])

for file in filenames:
    with open(file) as data_file:    
        data = json.load(data_file)
        name = str(file.split('.')[0]).split('_')[1]
        picklename = name +'.pickle'
        csvname = name + '.csv'
        print("opened!" + name)        # to check status of script while running
        df = pd.DataFrame()
        tweet_dict = defaultdict()
        length = len(data)
        print(length)
        for i in range(length): 
            tweet_dict['id'] = data[i]['id']
            tweet_dict['text'] = data[i]['text']
            tweet_dict['screen_name'] = data[i]['screen_name']
            tweet_dict['name'] = data[i]['name']
            tweet_dict['location'] = data[i]['location']
            tweet_dict['coordinates'] = data[i]['coordinates']
            tweet_dict['geo'] = data[i]['geo']
            tweet_dict['place'] = data[i]['place']
            tweet_dict['created_at'] = data[i]['created_at']
            tweet_dict['description'] = data[i]['description']
            tweet_dict['retweeted'] = data[i]['retweeted']
            df = df.append(tweet_dict, ignore_index=True)
            if i % 100 == 0: 
                print(i)
        with open(picklename, 'wb') as to_write:
            pickle.dump(df, to_write) 
           

