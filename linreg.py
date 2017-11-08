# Basic data analysis imports
import pandas as pd
import numpy as np
import base64
import requests

# Imports for linear regression
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

# Imports for data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Pull CSV with all (non-zero) game logs
my_full_stats = pd.read_csv('data/2017_stats.csv')

#  my_full_stats.columns: 
#        ['GID', 'First  Last', 'Date', 'Team', 'Opp', 'H/A', 'GameID',
#        'GTime(ET)', 'Team pts', 'Opp pts', 'Start', 'Minutes', 'GP', 'active',
#        'FDP', 'DKP', 'DDP', 'YHP', 'Stats', 'DoubleD', 'TripleD', 'FD Sal',
#        'FD Change', 'DK Sal', 'DK Change', 'DD Sal', 'DD Change', 'YH Sal',
#        'YH Change', 'FD pos', 'DK pos', 'DD pos', 'YH pos']

# Get our independent variables (X) and dependent variable (y)
X=my_full_stats[['season_avg','last_five','Team pts', 'Minutes']]
y = my_full_stats['DKP']

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=42)

# Instantiate linear regression model
lm = LinearRegression()

# Train/fit model on training data
lm.fit(X_train,y_train)

# Create a dataframe for coefficeints. 
coefs = pd.DataFrame(lm.coef_,X.columns,columns=['Coeff'])
print(coefs)
print('')

# Print correlations
factors = ['season_avg','last_five','Team pts', 'Minutes']
for factor in factors:
	corr = my_full_stats['DKP'].corr(my_full_stats[factor])
	print(factor + ": " + str(corr))

# Print the y intercept. Does it matter that this intercept isn't close to 0?
print('')
print('Intercept is ' + str(lm.intercept_))

# Create predictions for the test set of independent variables
predictions=lm.predict(X_test)
# Visually compare predictions to results on test set
plt.scatter(y_test,predictions)
# You have to type plt.show() to get the visualization from the terminal
plt.show()


