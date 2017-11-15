import pandas as pd
import numpy as np
import base64
import requests
import datetime


#  Columns of the CSV are: 
#        ['GID', 'First  Last', 'Date', 'Team', 'Opp', 'H/A', 'GameID',
#        'GTime(ET)', 'Team pts', 'Opp pts', 'Start', 'Minutes', 'GP', 'active',
#        'FDP', 'DKP', 'DDP', 'YHP', 'Stats', 'DoubleD', 'TripleD', 'FD Sal',
#        'FD Change', 'DK Sal', 'DK Change', 'DD Sal', 'DD Change', 'YH Sal',
#        'YH Change', 'FD pos', 'DK pos', 'DD pos', 'YH pos']

def add_season_avg():
	my_full_stats = pd.read_csv('master_stats_file.csv')
	# This will add a column of a player's season average to date
	# Add an empty column which will be filled with season averages
	my_full_stats['season_avg']=[0]*len(my_full_stats)
	# Create a list to store current player's dkp scores for the season
	season_avg_list=[]
	# Set which player we're on (initially null)
	current_player = ""
	# We then create a loop that goes through every game 
	for i in range(0,len(my_full_stats)):
		# Get players name for current game
		player = my_full_stats.iloc[i]['First  Last']
		minutes = my_full_stats.iloc[i]['Minutes']
		if minutes == 0:
			# skip over the game if the player didn't play
			continue
		if player == current_player:
			# Not a new player, calculate average of season dkp totals
			season_avg_value = sum(season_avg_list)/float(len(season_avg_list))
			dkp = my_full_stats.iloc[i]['DKP']
			# The below method is not preferred. Should use loc
			my_full_stats['season_avg'][i]=season_avg_value
			season_avg_list.append(dkp)
		else:
			# New player -> set average to the score of their first game
			print("now on " + player)
			current_player = player
			season_avg_list = []
			# Always use the below loc syntax to prevent accidentally creating a copy
			# e.g. my_full_stats['DKP'].iloc[i] would create a copy
			# if you used the above, you would not be able to change values on the original
			dkp = my_full_stats.loc[i,'DKP']
			# Add this game's DKP to the player's list of season DKP totals
			season_avg_list.append(dkp)
			# HACKED: since it's the first game, just set average equal to this game's DKP
			my_full_stats.loc[i,'season_avg']=dkp
	my_full_stats.to_csv('master_stats_file.csv')

def add_played():
	my_full_stats = pd.read_csv('master_stats_file.csv')
	# This will add a column of whether the player registered a minute
	my_full_stats['played']=[0]*len(my_full_stats)
	# Set which player we're on (initially null)
	current_player = ""
	# We then create a loop that goes through every game 
	for i in range(0,len(my_full_stats)):
		# If the player played, set to 1. otherwise, keep at zero
		minutes = my_full_stats.iloc[i]['Minutes']
		if minutes != 0:
			my_full_stats['played'][i]=1
	my_full_stats.to_csv('master_stats_file.csv')

def add_last_five():
	my_full_stats = pd.read_csv('master_stats_file.csv')
	# This will add a column of a player's season average over last 5 games
	# Add an empty column which will be filled with last five averages
	my_full_stats['last_five']=[0]*len(my_full_stats)
	# Create a list for the current player's dkp scores for last 5 games
	last_five_list=[]
	# Set which player we're on (initially null)
	current_player = ""
	# We then create a loop that goes through every game 
	for i in range(0,len(my_full_stats)):
		# Get player's name for currentgame
		player = my_full_stats.iloc[i]['First  Last']
		minutes = my_full_stats.iloc[i]['Minutes']
		if minutes == 0:
			# skip over the game if the player didn't play
			continue
		if player == current_player:
			# Not a new player, calculate last five 
			last_five_value = sum(last_five_list)/float(len(last_five_list))
			# Always use the below loc syntax to prevent accidentally creating a copy
			# e.g. my_full_stats['DKP'].iloc[i] would create a copy
			# if you used the above, you would not be able to change values on the original
			dkp = my_full_stats.loc[i,'DKP']
			my_full_stats.loc[i,'last_five']=last_five_value
			if len(last_five_list) < 5:
				# Fewer than 5 games played; add this game to last five
				last_five_list.append(dkp)
			else:
				# More than 5 games played
				# Add this game to last 5, but delete the oldest game in last 5
				last_five_list = last_five_list[1:4]
				last_five_list.append(dkp)
		else:
			# HACK: New player -> set average to the score of their first game
			# Set to new player
			current_player = player
			# Initialize this guy's non-existent last 5 list
			last_five_list = []
			# Get dkp of this game
			dkp = my_full_stats.loc[i,'DKP']
			# Add this game's dkp to last 5 list
			last_five_list.append(dkp)
			print("we're on " + player)
			# HACK: set average to this game's score
			my_full_stats.loc[i,'last_five']=dkp
	my_full_stats.to_csv('master_stats_file.csv')



# def remove_zero_minute_games():
# 	# Load all games
# 	df = pd.read_csv('201617_full_game_logs.csv')
# 	# Remove the games where player didn't play
# 	df = df[df.Minutes != 0]
# 	# Re-write csv
# 	df.to_csv('201617_nonzero_game_logs.csv')

def remove_playoff_games():
	df = pd.read_csv('master_stats_file.csv')
	playoff_start_date = datetime.date(year=2017,month=4,day=13)
	# for i in range(0,100):
	# 	df.drop(df.index[i])
	drop_list=[]
	for i in range(0,len(df)):
		# Get player's name for currentgame
		date = str(df.loc[i,'Date'])
		year = int(date[0:4])
		month = int(date[4:6])
		day = int(date[6:8])
		game_date = datetime.date(year=year,month=month,day=day)
		if (game_date>playoff_start_date):
			drop_list.append(i)
	df.drop(df.index[drop_list], inplace=True)
	df.to_csv('master_stats_file.csv')	
		


def reverse_rows():
	# Load all games
	df = pd.read_csv('master_stats_file.csv')
	# Reverse the order
	df = df.reindex(index=df.index[::-1])
	# Re-write csv
	df.to_csv('master_stats_file.csv')



