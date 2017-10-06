import requests
from bs4 import BeautifulSoup as bs
from collections import OrderedDict
import datetime
import csv
import os
import re

print('hello')

# # Pull the csv with every game log from 2017
# my_full_stats = pd.read_csv('full_2017.csv') 

numbers_dict={'1145': 'okc', '1170': 'nyk', '1159': 'atl', '1169': 'bkn', '1171': 'bos', '1162': 'cha', '1167': 'chi', '1166': 'cle', '1154': 'dal', '1147': 'den', '1164': 'det', '1152': 'gsw', '1155': 'hou', '1163': 'ind', '1148': 'lac', '1151': 'lal', '1156': 'mem', '1158': 'mia', '1165': 'mil', '1144': 'min', '1157': 'nop', '1161': 'orl', '1172': 'phi', '1149': 'phx', '1146': 'por', '1150': 'sac', '1153': 'sas', '1168': 'tor', '1143': 'uta', '1160': 'was'}


#Lookup the Charlotte Spread
def lookup_spreads():
	info = {}
	dates=["20161103", "20161104", "20161105", "20161106"]
	all_spreads={}
	for date in dates:
		url = "https://www.sportsbookreview.com/betting-odds/nba-basketball/?date=" + date 
		response = requests.get(url)
		if response.status_code == 200:
			soup = bs(response.content,'lxml')
			bovada_lines = soup.find_all('div', class_='eventLine-book-value', id=re.compile(r'/*999996*'))
			all_spreads[date] = {}
			for line in bovada_lines:
				team = numbers_dict[line.get('id').split('-')[3]]
				spread = line.get_text().split(u'\xa0')[0]
				print(team + ": " + spread)
				all_spreads[date][team] = spread
	print(all_spreads)
	return

lookup_spreads()
















# def get_team_ids():
# 	city_dict={
# 	    "Atlanta": "ATL",
# 	    "Brooklyn" :"BKN",
# 	    "Boston": "BOS",
# 	    "Charlotte": "CHA",
# 	    "Chicago": "CHI",
# 	    "Cleveland": "CLE",
# 	    "Dallas": "DAL",
# 	    "Denver": "DEN",
# 	    "Detroit":"DET",
# 	    "Golden State": "GSW",
# 	    "Houston": "HOU",
# 	    "Indiana": "IND",
# 	    "L.A. Lakers": "LAC",
# 	    "L.A. Clippers": "LAL",
# 	    "Memphis": "MEM",
# 	    "Miami": "MIA",
# 	    "Milwaukee": "MIL",
# 	    "Minnesota": "MIN",
# 	    "New Orleans": "NOP",
# 	    "New York: "NYK",
# 	    "Oklahoma City": "OKC",
# 	    "Orlando": "ORL",
# 	    "Philadelphia": "PHI",
# 	    "Phoenix": "PHX",
# 	    "Portland":"POR",
# 	    "Sacramento": "SAC",
# 	    "San Antonio": "SAS",
# 	    "Toronto": "TOR",
# 	    "Utah": "UTA",
# 	    "Washington": "WAS"
# 	}
# 	numbers_dict = {}
# 	for team in city_dict:
# 		city_long = team
# 		city_short = city_dict[city_long]
# 		urls = ["https://www.sportsbookreview.com/betting-odds/nba-basketball/?date=20170101",
# 				"https://www.sportsbookreview.com/betting-odds/nba-basketball/?date=20170102",
# 				"https://www.sportsbookreview.com/betting-odds/nba-basketball/?date=20170103",
# 				"https://www.sportsbookreview.com/betting-odds/nba-basketball/?date=20170104",
# 				"https://www.sportsbookreview.com/betting-odds/nba-basketball/?date=20170105",
# 				"https://www.sportsbookreview.com/betting-odds/nba-basketball/?date=20170106"]
# 		for url in urls:
# 			response = requests.get(url)
# 			if response.status_code == 200:
# 				soup = bs(response.content,'lxml')
# 				bs_element = soup.find('span', text=city_long)
# 				if bs_element:
# 					print(city_long + " is " + bs_element.get('rel'))	
# 					numbers_dict[bs_element.get('rel')] = city_short.lower()
# 					break
# 	print(numbers_dict)

