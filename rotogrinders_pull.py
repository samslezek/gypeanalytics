import requests
from bs4 import BeautifulSoup as bs
from collections import OrderedDict
import datetime
import csv
import os
import re
import json
from selenium import webdriver
import pandas as pd
import numpy as np
from pydfs_lineup_optimizer import Site, Sport, get_optimizer
# To run this, you need to install chromedriver using Homebrew
# Get Homebrew from brew.sh, then in your terminal type brew install chromedriver
counter=0

# def get_position(position,counter):
# 	# Open a Chrome browser for rotogrinders using selenium
# 	browser = webdriver.Chrome()
# 	browser.get("https://rotogrinders.com/projected-stats/nfl-" + position + "?site=draftkings")
# 	soup = bs(browser.page_source, "html.parser")
# 	# Get player names and put in all_players
# 	players = soup.find_all('a', class_='player-popup')
# 	all_players=[]
# 	for player in players:
# 		all_players.append(player.string)
# 	# Get player point projections and put in all_projections
# 	projection_parent = soup.find('div', attrs={"data-title": "Fantasy Points"}).parent
# 	player_projections = projection_parent.findChildren()
# 	player_projections=player_projections[2:len(player_projections)]
# 	all_projections=[]
# 	for projection in player_projections:
# 		all_projections.append(projection.string)
# 	# Get player salaries and put in all_salaries
# 	salary_parent_div=soup.find_all('div', text=re.compile(r'/*\$\d\.\dK*'))
# 	all_salaries = []
# 	for salary in salary_parent_div:
# 		salary_number = float(salary.text[1:len(salary.text)-1])*1000
# 		all_salaries.append(salary_number)
# 	# Add all data to the players_df DataFrame (created below)
# 	for i in range(0,len(all_projections)):
# 		my_player=([all_players[i],position_lookup[position],'team',all_salaries[i],all_projections[i]])
# 		players_df.loc[counter]=my_player
# 		counter+=1

# # Create the dataframe to store the player data
# players_df = pd.DataFrame(
# 	columns=[
# 		'Name',
# 		'Position',
# 		'teamAbbrev',
# 		'Salary',
# 		'AvgPointsPerGame'
# 	]
# )
# positions=['qb','rb','wr','te','defense']
# position_lookup={
# 	'qb':'QB',
# 	'rb':'RB',
# 	'wr':'WR',
# 	'te':'TE',
# 	'defense':'DST'
# }
# for position in positions:
# 	get_position(position,len(players_df))
# print(players_df)

# players_df.to_csv('data/2017_w7_nfl_roto.csv')
optimizer = get_optimizer(Site.DRAFTKINGS, Sport.FOOTBALL)
optimizer.load_players_from_CSV('data/2017_w7_nfl_roto.csv')
cuts = [
	'Chris Thompson',
	'Kareem Hunt',
	'Evan Engram',
	'JuJu Smith-Schuster',
	'Devonta Freeman',
	'Jay Ajayi'
]
for cut in cuts:
		player = optimizer.get_player_by_name(cut)
		optimizer.remove_player(player)
bids = [
	'Alshon Jeffery'
]
for bid in bids:
		player = optimizer.get_player_by_name(bid)
		optimizer.add_player_to_lineup(player)
lineup_generator = optimizer.optimize(10)
for lineup in lineup_generator:
	print(lineup)
