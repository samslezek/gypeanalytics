from ohmysportsfeedspy import MySportsFeeds
import pandas as pd
import numpy as np
import base64
import requests

#pull the csv with every game log from 2017
my_full_stats = pd.read_csv('full_2017.csv')

print(my_full_stats.columns)
# Index(['GID', 'First  Last', 'Date', 'Team', 'Opp', 'H/A', 'GameID',
#        'GTime(ET)', 'Team pts', 'Opp pts', 'Start', 'Minutes', 'GP', 'active',
#        'FDP', 'DKP', 'DDP', 'YHP', 'Stats', 'DoubleD', 'TripleD', 'FD Sal',
#        'FD Change', 'DK Sal', 'DK Change', 'DD Sal', 'DD Change', 'YH Sal',
#        'YH Change', 'FD pos', 'DK pos', 'DD pos', 'YH pos'],
#       dtype='object')

