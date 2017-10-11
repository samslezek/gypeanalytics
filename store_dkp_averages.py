from ohmysportsfeedspy import MySportsFeeds
import pandas as pd
import numpy as np
import base64
import requests

#pull the csv with every game log from 2017
my_full_stats = pd.read_csv('data/201617_full_game_logs.csv')

# print(my_full_stats.columns)
# Index(['GID', 'First  Last', 'Date', 'Team', 'Opp', 'H/A', 'GameID',
#        'GTime(ET)', 'Team pts', 'Opp pts', 'Start', 'Minutes', 'GP', 'active',
#        'FDP', 'DKP', 'DDP', 'YHP', 'Stats', 'DoubleD', 'TripleD', 'FD Sal',
#        'FD Change', 'DK Sal', 'DK Change', 'DD Sal', 'DD Change', 'YH Sal',
#        'YH Change', 'FD pos', 'DK pos', 'DD pos', 'YH pos'],
#       dtype='object')

# Set up dictionary of players' draftkings totals
dkp_dict= {}

# Add all DraftKings totals to the dictionary
for i in range(0, len(my_full_stats)):
	name = my_full_stats.iloc[i]['First  Last']
	dkp = my_full_stats.iloc[i]['DKP']
	if name not in dkp_dict:
		dkp_dict[name]=[]
	if dkp > 0:
		dkp_dict[name].append(dkp)

# Replace all lists of dkp totals with averages
for player in dkp_dict:
	dkp_list = dkp_dict[player]
	if len(dkp_list)>0:
		average = sum(dkp_list)/float(len(dkp_list))
	else:
		average = 0
	dkp_dict[player]=average

print(dkp_dict)