#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 11:43:36 2019
@author: kmussar
"""
# Imports
from TwitterSearch import TwitterSearch, TwitterSearchOrder, TwitterSearchException, TwitterUserOrder 
# import pandas as pd
from collections import defaultdict
import time
# import pickle
import json


# Authenticate - enter your developer keys here
ts = TwitterSearch(
    consumer_key = '',
    consumer_secret = '',
    access_token = '',
    access_token_secret = ''
 )

# add additional terms here 
search_terms = ['flu','cough','sick']

# to comply with TwitterAPI request restrictions
def my_callback_closure(current_ts_instance): # accepts ONE argument: an instance of TwitterSearch
        queries, tweets_seen = current_ts_instance.get_statistics()
        if queries > 0 and (queries % 5) == 0: # trigger delay every 5th query
            time.sleep(60) # sleep for 60 seconds
            print(tweet_count)
            
for term in search_terms:
    with open('tweets_'+term +'.json', 'a+') as outfile:
        tweet_count = 0 
        while tweet_count <100000:
            try:
                tso = TwitterSearchOrder() # create a TwitterSearchOrder object
                #tso.set_since_id=194380851
                tso.set_keywords([term]) 
                tso.set_language('en') # we want to see English tweets only
                tso.set_include_entities(True) # and do give us all those entity information

                for tweet in ts.search_tweets_iterable(tso, callback=my_callback_closure):
                    tweet_count += 1
                    #if tweet_count % 100:
                        #print(tweet_count)
                    user = defaultdict()
                    place = defaultdict()
                    geo = defaultdict
                    coordinates = defaultdict
                    tweet_unwind = defaultdict()
                    # print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
                    user = tweet['user']
                    place = tweet['place']
                    geo = tweet['geo']
                    coordinates = tweet['coordinates']
                    #unpack dictionaries and save them to lists
                    if user != None:
                        tweet.update(user)
                    if geo != None:
                        tweet.update(geo)
                    if place != None:
                        tweet.update(place)
                    if coordinates != None:
                        tweet.update(coordinates)
                    json.dump(tweet, outfile, sort_keys=True, indent=4)
                    outfile.write(", \n")
                    #df_sick2 = df_sick.append(tweet, ignore_index=True)

            except TwitterSearchException as e:
                print(e)            