import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
"""
foodm = pd.read_csv('../data/Food Prices/wfp_food_prices_mali.csv',low_memory=False)
foodb = pd.read_csv('../data/Food Prices/wfp_food_prices_burkina-faso.csv',low_memory=False)
foodn = pd.read_csv('../data/Food Prices/wfp_food_prices_niger.csv',low_memory=False)

# Features I'm interested in:
foodm.rename(columns={'country':'adm0_name',
                      'admname':'adm1_name'}, inplace=True)
foodb.rename(columns={'country':'adm0_name',
                      'admname':'adm1_name'}, inplace=True)
foodn.rename(columns={'country':'adm0_name',
                      'admname':'adm1_name'}, inplace=True)
foodm = foodm[['date','adm0_name','adm1_name','mktname','category','cmname',
        'price','currency','unit']]
foodb = foodb[['date','adm0_name','adm1_name','mktname','category','cmname',
        'price','currency','unit']]
foodn = foodn[['date','adm0_name','adm1_name','mktname','category','cmname',
        'price','currency','unit']]

# Extract reference_year
foodm['reference_year'] = foodm.date.str.split('-',expand=True)[0]
foodb['reference_year'] = foodb.date.str.split('-',expand=True)[0]
foodn['reference_year'] = foodn.date.str.split('-',expand=True)[0]
foodm = foodm.drop(0)
foodb = foodb.drop(0)
foodn = foodn.drop(0)
# Adjusting variables dtypes
foodm['reference_year'] = foodm['reference_year'].astype(int)
foodb['reference_year'] = foodb['reference_year'].astype(int)
foodn['reference_year'] = foodn['reference_year'].astype(int)
foodm['price'] = foodm['price'].astype(float)
foodb['price'] = foodb['price'].astype(float)
foodn['price'] = foodn['price'].astype(float)

# Select data from 2014 to 2018
foodm = foodm[foodm.reference_year.isin([2014,2015,2016,2017,2018,2019])]
foodb = foodb[foodb.reference_year.isin([2014,2015,2016,2017,2018,2019])]
foodn = foodn[foodn.reference_year.isin([2014,2015,2016,2017,2018,2019])]

# Select adm1_name to work with
foodm = foodm[foodm.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
foodb = foodb[foodb.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
foodn = foodn[foodn.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]

# Find mean of food prices
foodm = foodm[foodm.cmname.isin(['Millet - Retail','Rice (local) - Retail','Rice (imported) - Retail','Sorghum - Retail'])]
foodb = foodb[foodb.cmname.isin(['Sorghum - Retail','Millet - Retail','Maize - Retail','Rice (local) - Retail'])]
foodn = foodn[foodn.cmname.isin(['Millet - Retail','Rice (imported) - Retail','Sorghum - Retail','Maize - Retail'])]
foodm = foodm.reset_index(drop=True)
foodb = foodb.reset_index(drop=True)
foodn = foodn.reset_index(drop=True)



meanm = foodm.groupby(['cmname','adm1_name','reference_year'])['price'].mean()
meanb = foodb.groupby(['cmname','adm1_name','reference_year'])['price'].mean()
meann = foodn.groupby(['cmname','adm1_name','reference_year'])['price'].mean()
print(str(meanm))
print(str(meanb))
print(str(meann))

"""


foodm = pd.read_csv('../data/Food Prices/wfp_food_prices_mali.csv',low_memory=False)
foodb = pd.read_csv('../data/Food Prices/wfp_food_prices_burkina-faso.csv',low_memory=False)
foodn = pd.read_csv('../data/Food Prices/wfp_food_prices_niger.csv',low_memory=False)
foodm = foodm.drop(0)
foodb = foodb.drop(0)
foodn = foodn.drop(0)
food = foodm.append(foodb.append(foodn)).reset_index()
food.rename(columns={'country':'adm0_name',
                     'admname':'adm1_name'}, inplace=True)
food = food[['date','adm0_name','adm1_name','mktname','category','cmname',
        'price','currency','unit']]
food['reference_year'] = food.date.str.split('-',expand=True)[0]
food = food.drop(0)
food['reference_year'] = food['reference_year'].astype(int)
food['price'] = food['price'].astype(float)
food = food[food.reference_year.isin([2013,2014,2015,2016,2017,2018,2019])]
food = food[food.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
food = food.reset_index(drop=True)



# Interested only on millet price variations
millet = food[food['cmname'] == 'Millet - Retail']
millet = millet[['reference_year','adm0_name','adm1_name','price']]

# Price mean
mmil = pd.DataFrame({'mean' : millet.groupby(['reference_year','adm1_name'])['price'].mean()}).reset_index()
# Price std
stmil = pd.DataFrame({'std' : millet.groupby(['reference_year','adm1_name'])['price'].std()}).reset_index()

# Difference of price mean
diffmil = pd.DataFrame(columns=['reference_year','adm1_name','mean_diff'])

for year in range(2013,2020):
    for elem in millet['adm1_name'].unique():
        diffmil = diffmil.append(pd.Series([year, elem, 0],index=diffmil.columns),ignore_index=True)

mmil = mmil.sort_values(['reference_year','adm1_name']).reset_index()
diffmil = diffmil.sort_values(['reference_year','adm1_name']).reset_index()

# Finally him:
for adm1 in diffmil.adm1_name.unique():
    diffmil.loc[diffmil.adm1_name == adm1,'mean_diff'] = mmil[mmil.adm1_name == adm1]['mean'].diff()

diffmil = diffmil[diffmil.reference_year.isin(range(2014,2020))]
diffmil.reset_index(inplace=True)
diffmil = diffmil[['reference_year','adm1_name','mean_diff']]


plt.style.use('fivethirtyeight')

# Plot millet price mean
graph = mmil[mmil.adm1_name.isin(['Mopti'])].plot(x='reference_year',y=['mean'],figsize=(10,7))

# Plot millet price std
graph = stmil[stmil.adm1_name.isin(['Mopti'])].plot(x='reference_year',y=['std'],figsize=(10,7))

# Plot millet price variations
graph = diffmil[diffmil.adm1_name.isin(['Mopti'])].plot(x='reference_year',y=['mean_diff'],figsize=(10,7))

plt.show()
