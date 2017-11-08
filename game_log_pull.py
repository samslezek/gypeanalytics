import pandas as pd
import numpy as np
import base64
import requests

#pull the csv with every game log from 2017
my_full_stats = pd.read_csv('data/201617_full_game_logs.csv')
print("Full is " + str(len(my_full_stats)))

#  Columns of the CSV are: 
#        ['GID', 'First  Last', 'Date', 'Team', 'Opp', 'H/A', 'GameID',
#        'GTime(ET)', 'Team pts', 'Opp pts', 'Start', 'Minutes', 'GP', 'active',
#        'FDP', 'DKP', 'DDP', 'YHP', 'Stats', 'DoubleD', 'TripleD', 'FD Sal',
#        'FD Change', 'DK Sal', 'DK Change', 'DD Sal', 'DD Change', 'YH Sal',
#        'YH Change', 'FD pos', 'DK pos', 'DD pos', 'YH pos']

# Get only the stats for November 2
my_filtered_stats = my_full_stats.query('Date==20161102')
my_filtered_stats=my_filtered_stats[['First  Last', 'DK pos', 'DK Sal', 'DKP']]

# Define a DataFrame to hold all players in our schema
players_df = pd.DataFrame(
	columns=[
		'Player',
		'Position',
		'Salary',
		'DKP',
		'Value'
	]
)

# Fill in our DataFrame in our schema
for i in range(0,len(my_filtered_stats)):
	positions_dict = {
		1.0:[1],
		12.0:[1,2],
		2.0:[2],
		23.0:[2,3],
		3.0:[3],
		34.0:[3,4],
		4.0:[4],
		45.0:[4,5],
		5.0:[5]
	}
	name = my_filtered_stats.iloc[i]['First  Last']
	pos = positions_dict[my_filtered_stats.iloc[i]['DK pos']]
	sal = my_filtered_stats.iloc[i]['DK Sal']
	dkp = my_filtered_stats.iloc[i]['DKP']
	value = dkp/sal
	new_player=[name,pos,sal,dkp,value]
	players_df.loc[i]=new_player

# Do a really bad job of selecting a lineup
lineup = [[1,2,3,4,5],[1,2],[3,4],[1],[2],[3],[4],[5]]
counter = 0
total_sal = 50000
positions_left = 8
our_lineup = pd.DataFrame(
	columns=[
		'Player',
		'Position',
		'Salary',
		'DKP',
		'Value'
	]
)
players_df = players_df.sort_values('Value', ascending=False)
for position in lineup:
	for i in range(0,len(players_df)):
		player=players_df.iloc[i]
		if set(position).intersection(player['Position']):
			if ((total_sal-player['Salary'])>(positions_left-1)*2999 and (total_sal-player['Salary'])<(positions_left-1)*7000):
				our_lineup.loc[counter]=player
				counter+=1
				positions_left+=-1
				total_sal=total_sal-player['Salary']
				break


# print our lineup
print(our_lineup)



