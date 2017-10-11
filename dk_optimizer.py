from ohmysportsfeedspy import MySportsFeeds
import pandas as pd
import numpy as np
import base64
import requests
# import pydfs-lineup-optimizer

#pull the csv with every game log from 2017
my_full_stats = pd.read_csv('data/201617_full_game_logs.csv')

#filter for players on a specific day
my_filtered_stats = my_full_stats.query('Date==20161102')

# set up the schema necessary for pydfs-lineup-optimizer
players_df = pd.DataFrame(
	columns=[
		'First Name',
		'Last Name',
		'Position',
		'Team',
		'Salary',
		'FPPG',
		'Injury Status'
	]
)

# fill the csv needed for pydfs-lineup-optimizer
for i in range(0, len(my_filtered_stats)):
	first = my_filtered_stats.iloc[i]['First  Last'].split(' ')[0]
	last = ' '.join(my_filtered_stats.iloc[i]['First  Last'].split(' ')[1:])
	positions_dict = {
		1.0:['PG'],
		12.0:['PG', 'SG'],
		2.0:['SG'],
		23.0:['SG','SF'],
		3.0:['SF'],
		34.0:['SF','PF'],
		4.0:['PF'],
		45.0:['PF','C'],
		5.0:['C']
	}
	pos = positions_dict[my_filtered_stats.iloc[i]['DK pos']]
	team = my_filtered_stats.iloc[i]['Team']
	sal = my_filtered_stats.iloc[i]['DK Sal']
	fppg = my_filtered_stats.iloc[i]['DKP']
	inj='0'
	new_player=[first,last,pos,team,sal,fppg,inj]
	print(len(players_df.columns))
	print(len(new_player))
	players_df.loc[i]=new_player

# players_df is now formatted to be put into pydfs-lineup optimizer
print(players_df)





