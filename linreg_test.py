import pandas as pd
import numpy as np
import base64
import requests
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

#pull the csv with every game log from 2017
my_full_stats = pd.read_csv('data/201617_full_game_logs.csv')

#  my_full_stats.columns: 
#        ['GID', 'First  Last', 'Date', 'Team', 'Opp', 'H/A', 'GameID',
#        'GTime(ET)', 'Team pts', 'Opp pts', 'Start', 'Minutes', 'GP', 'active',
#        'FDP', 'DKP', 'DDP', 'YHP', 'Stats', 'DoubleD', 'TripleD', 'FD Sal',
#        'FD Change', 'DK Sal', 'DK Change', 'DD Sal', 'DD Change', 'YH Sal',
#        'YH Change', 'FD pos', 'DK pos', 'DD pos', 'YH pos']

X=my_full_stats[['Team pts', 'Minutes']]
y = my_full_stats['DKP']

# x.info() gives you what types of variables you have
# y.describe() gives you some statistical analysis of those variables

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=42)

# Instantiate linear regression model
lm = LinearRegression()

# Train/fit model on training data
lm.fit(X_train,y_train)

# Create a dataframe for coefficeints. 
coefs = pd.DataFrame(lm.coef_,X.columns,columns=['Coeff'])
print(coefs)


