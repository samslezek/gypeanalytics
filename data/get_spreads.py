import requests
from bs4 import BeautifulSoup as bs
from collections import OrderedDict
import datetime
import csv
import os
import re

# This is the dict of team IDs on the sportsbook we're using 
numbers_dict={'1145': 'okc', '1170': 'nyk', '1159': 'atl', '1169': 'bkn', '1171': 'bos', '1162': 'cha', '1167': 'chi', '1166': 'cle', '1154': 'dal', '1147': 'den', '1164': 'det', '1152': 'gsw', '1155': 'hou', '1163': 'ind', '1148': 'lac', '1151': 'lal', '1156': 'mem', '1158': 'mia', '1165': 'mil', '1144': 'min', '1157': 'nop', '1161': 'orl', '1172': 'phi', '1149': 'phx', '1146': 'por', '1150': 'sac', '1153': 'sas', '1168': 'tor', '1143': 'uta', '1160': 'was'}

# This will be populated with all of the dates we will use for URLs in iter_dates()
date_list = []
all_spreads={}


def lookup_spreads():
	spreads_to_print=[]
	for date in date_list:
		url = "https://www.sportsbookreview.com/betting-odds/nba-basketball/?date=" + date 
		response = requests.get(url)
		if response.status_code == 200:
			soup = bs(response.content,'lxml')
			bovada_lines = soup.find_all('div', class_='eventLine-book-value', id=re.compile(r'/*999996*'))
			all_spreads[date] = {}
			for line in bovada_lines:
				print(line)
				try:
					team = numbers_dict[line.get('id').split('-')[3]]
					spread = line.get_text().split(u'\xa0')[0]
					all_spreads[date][team] = spread
					spreads_to_print.append([date,team,spread])
				except: 
					print('keyerror')
	to_write=open('spreads_list.csv','w')
	for item in spreads_to_print:
		to_write.write("%s\n" % item)
	return

def iter_dates(): 
	start_date = datetime.date(year = 2016, month = 10, day = 25)
	end_date = datetime.date(year = 2017, month = 4, day = 12)
	for n in range((end_date-start_date).days+1):
		current_date = (start_date+datetime.timedelta(n))
		if len(str(current_date.month))==1:
			month = "0"+str(current_date.month)
		else: 
			month = str(current_date.month)
		if len(str(current_date.day))==1:
			day = "0"+str(current_date.day)
		else: 
			day = str(current_date.day)	
		date_list.append((str(current_date.year) + month + day))

def add_spreads_column():
	my_full_stats = pd.read_csv('2017_stats.csv')
	my_full_stats['spread']=[0]*len(my_full_stats)
	for i in range(0,len(my_full_stats)):
		date = my_full_stats.loc[i,'Date']
		team = my_full_stats.loc[i,'Team']
		spread = all_spreads[date][team]
		print(team + " is favored by " + spread)



iter_dates()
lookup_spreads()
add_spreads_column()















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

