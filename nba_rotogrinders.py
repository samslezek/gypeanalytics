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

def get_players():
	# Open a Chrome browser for rotogrinders using selenium
	browser = webdriver.Chrome()
	browser.get("https://rotogrinders.com/projected-stats/nba-player?site=draftkings")
	soup = bs(browser.page_source, "html.parser")
	# Get player names and put in all_players
	players = soup.find_all('a', class_='player-popup')
	all_players=[]
	for player in players:
		all_players.append(player.string)
	# Get player point projections and put in all_projections
	projection_parent = soup.find('div', attrs={"data-title": "Fantasy Points"}).parent
	player_projections = projection_parent.findChildren()
	player_projections=player_projections[2:len(player_projections)]
	all_projections=[]
	for projection in player_projections:
		all_projections.append(projection.string)
	# Get player salaries and put in all_salaries
	salary_parent_div=soup.find_all('div', text=re.compile(r'/*\$[\d]+\.\dK*'))
	all_salaries = []
	for salary in salary_parent_div:
		salary_number = float(salary.text[1:len(salary.text)-1])*1000
		all_salaries.append(salary_number)
	# Get player positions and put in all_positions
	position_parent = soup.find('div', attrs={"data-title": "Position"}).parent
	player_positions = position_parent.findChildren()
	player_positions=player_positions[2:len(player_positions)]
	all_positions=[]
	for position in player_positions:
		all_positions.append(position.string)
	# Get player teams and put in all_teams
	team_parent = soup.find('div', attrs={"data-title": "Team"}).parent
	player_teams = team_parent.findChildren()
	player_teams=player_teams[2:len(player_teams)]
	all_teams=[]
	for team in player_teams:
		all_teams.append(team.string)
	# Add all data to the players_df DataFrame (created below)
	for i in range(0,len(all_projections)-1):
		my_player=([all_players[i],all_positions[i],all_teams[i],all_salaries[i],all_projections[i]])
		players_df.loc[i]=my_player
	browser.close()


# Create the dataframe to store the player data
players_df = pd.DataFrame(
	columns=[
		'Name',
		'Position',
		'teamAbbrev',
		'Salary',
		'AvgPointsPerGame'
	]
)

#get_players()


#players_df.to_csv('data/2017_10_18_rotogrinders_pull.csv')
optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASKETBALL)
optimizer.load_players_from_CSV('data/2017_10_18_rotogrinders_pull.csv')
bids = [
	'Marcus Smart',
	'Kemba Walker',
	'Jaylen Brown',
	'Robert Covington',
	'Andre Drummond'
]
cuts = [
	'Jason Smith',
	'Dario Saric',
	'Chris Paul',
	'Trevor Ariza',
	'James Harden',
	'Al Horford',
	'Kelly Olynyk',
	'Marqueese Chriss',
]

for guy in bids:
	player = optimizer.get_player_by_name(guy)
	optimizer.add_player_to_lineup(player)

for gype in cuts:
	player = optimizer.get_player_by_name(gype)
	optimizer.remove_player(player)

lineup_generator = optimizer.optimize(10)
for lineup in lineup_generator:
	print(lineup)