from ohmysportsfeedspy import MySportsFeeds
import pandas as pd
import numpy as np
import base64
import requests

my_full_stats = pd.read_csv('nbastats.csv')
my_stats = my_full_stats[['#LastName','#FirstName','#Position',
                        "#PtsPerGame", "#RebPerGame", '#AstPerGame',
                        '#StlPerGame', '#BlkPerGame', '#TovPerGame']]
my_stats['#DKP'] = 0

for i in range(0, len(my_stats)):
    last = my_stats.iloc[i]['#LastName']
    first = my_stats.iloc[i]['#FirstName']
    pos = my_stats.iloc[i]['#Position']
    pts = my_stats.iloc[i]['#PtsPerGame']
    reb = my_stats.iloc[i]['#RebPerGame']
    ast = my_stats.iloc[i]['#AstPerGame']
    stl = my_stats.iloc[i]['#StlPerGame']
    blk = my_stats.iloc[i]['#BlkPerGame']
    to = my_stats.iloc[i]['#TovPerGame']
    dkp = pts+reb+(2*ast)+stl+blk+to
    my_stats.iloc[i]['#DKP']=dkp
    print(my_stats.iloc[i]['#FirstName'] + " " +
         my_stats.iloc[i]['#LastName'] +  " - " + my_stats.iloc[i]['#Position'] +
         ": " + str(dkp))