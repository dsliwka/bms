"""
BMS Exercises
@author: Dirk Sliwka
"""

# Import:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from statsmodels.iolib.summary2 import summary_col



## Determine path to download the data
path_to_data = 'https://raw.githubusercontent.com/dsliwka/bms/master/GiftExchangeData.csv'

## read data into a data frame which we call df
df = pd.read_csv(path_to_data)

## describe the data
df.describe()



## Regression
reg1 = smf.ols('effort ~ wage ', data=df).fit()
reg2 = smf.ols('effort ~ wage + period', data=df).fit()
print(reg1.summary())

## Regression: print summary
print(summary_col([reg1, reg2],stars=True))

## Scatter plots
sns.set_context("poster", font_scale=1)

sns.relplot(x='wage', y='effort', data=df)


## Plot equitable effort for each wage level
w = np.linspace(0,10,101)
plt.plot(w, 3.84 *(1.04*w + 2.25)**(0.5)-5.77)



## Clear plot
plt.clf()
## Swarmplot
sns.swarmplot(x='wage', y='effort', data=df)
plt.plot(w, 3.84 *(1.04*w + 2.25)**(0.5)-5.77)








