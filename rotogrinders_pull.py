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

# For the below line, you need to install chromedriver using Homebrew
# Get Homebrew from brew.sh, then in your terminal type brew install chromedriver


def get_position(position):
	browser = webdriver.Chrome()
	browser.get("https://rotogrinders.com/projected-stats/nfl-" + position + "?site=draftkings")
	soup = bs(browser.page_source, "html.parser")
	# Get player names
	players = soup.find_all('a', class_='player-popup')
	all_players=[]
	for player in players:
		all_players.append(player.string)
	# Get player point projections
	projection_parent = soup.find('div', attrs={"data-title": "Fantasy Points"}).parent
	player_projections = projection_parent.findChildren()
	player_projections=player_projections[2:len(player_projections)]
	all_projections=[]
	for projection in player_projections:
		all_projections.append(projection.string)
	# Get player salaries
	salary_parent_div=soup.find_all('div', text=re.compile(r'/*\$\d\.\dK*'))
	all_salaries = []
	for salary in salary_parent_div:
		all_salaries.append(salary.text)
	# Add all data to the player_data list
	for i in range(0,len(all_projections)):
		print("Appending " + all_players[i])
		my_player=([all_players[i],position,all_salaries[i],all_projections[i]])
		#players_df.append(my_player)
		print("Appended.")
		print(players_df)

# Create the dataframe to store the player data
players_df = pd.DataFrame(
	columns=[
		'Player',
		'Position',
		'Salary',
		'Projection'
	]
)
get_position('qb')
print(players_df)
