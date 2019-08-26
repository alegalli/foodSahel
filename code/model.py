import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

data = pd.read_csv('../data/Data/data.csv')


data.describe()
seabornInstance.distplot(data['p35_density'])
seabornInstance.distplot(data['millet_price'])
seabornInstance.distplot(data['millet_var'])
seabornInstance.distplot(data['conflicts'])
seabornInstance.distplot(data['fatalities'])
seabornInstance.distplot(data['biomass'])
plt.show()

data.isnull().any()
data.isna().any()

X = data[['millet_price','conflicts','fatalities','biomass']].values
y = data['p35_density'].values

plt.tight_layout()
seabornInstance.distplot(data['p35_density'])
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
coeff_df = pd.DataFrame(regressor.coef_, data[['millet_price','conflicts','fatalities','biomass']].columns, columns=['Coefficient'])
coeff_df

y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

df1 = df.head(25)
df1.plot(kind='bar',figsize=(10,8))
plt.grid(which='major',linestyle='-',linewidth='0.5',color='green')
plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')
plt.show()

print('Mean Absolute Error: ', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error: ', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error: ', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# No a really good fit: Root Mean Squared Error too big in spite of mean
print('Mean: ', data['p35_density'].mean())

# Root Mean Squared Error is 90% of Mean.
# That means the this algoritm is not accurate.
# Factors that may have contributed to this inaccurancy are:
# Need more data: huge amount of data to get the best possible prediction
# Bad assumptions: we made the assumption that this data has a linear relationship, but that might not be the case
# Poor features: the feature we used may not have had a high enought correlation to the values we were trying to predict
