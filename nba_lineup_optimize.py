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