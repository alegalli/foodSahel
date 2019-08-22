import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data
foodm = pd.read_csv('../data/Food Prices/wfp_food_prices_mali.csv',low_memory=False)
foodb = pd.read_csv('../data/Food Prices/wfp_food_prices_burkina-faso.csv',low_memory=False)
foodn = pd.read_csv('../data/Food Prices/wfp_food_prices_niger.csv',low_memory=False)

foodm = foodm.drop(0)
foodb = foodb.drop(0)
foodn = foodn.drop(0)


# Work on a single dataset
food = foodm.append(foodb.append(foodn)).reset_index()
# Select columns I'm interested in
food.rename(columns={'country':'adm0_name',
                     'admname':'adm1_name'}, inplace=True)
food = food[['date','adm0_name','adm1_name','mktname','category','cmname',
        'price','currency','unit']]
# Create column reference_year
food['reference_year'] = food.date.str.split('-',expand=True)[0]
food['reference_year'] = food['reference_year'].astype(int)

food['price'] = food['price'].astype(float)

# Select index I'm interested in
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
diffmil = pd.DataFrame(columns=['reference_year','adm1_name','price_var'])

for year in range(2013,2020):
    for elem in millet['adm1_name'].unique():
        diffmil = diffmil.append(pd.Series([year, elem, 0],index=diffmil.columns),ignore_index=True)

mmil = mmil.sort_values(['reference_year','adm1_name']).reset_index()
diffmil = diffmil.sort_values(['reference_year','adm1_name']).reset_index()
# Finally him:
for adm1 in diffmil.adm1_name.unique():
    diffmil.loc[diffmil.adm1_name == adm1,'price_var'] = mmil[mmil.adm1_name == adm1]['mean'].diff()

diffmil = diffmil[diffmil.reference_year.isin(range(2014,2020))]
diffmil.reset_index(inplace=True)
diffmil = diffmil[['reference_year','adm1_name','price_var']]


plt.style.use('fivethirtyeight')

# Plot millet price mean
graph = mmil[mmil.adm1_name.isin(['Mopti'])].plot(x='reference_year',y=['mean'],figsize=(10,7))

# Plot millet price std
graph = stmil[stmil.adm1_name.isin(['Mopti'])].plot(x='reference_year',y=['std'],figsize=(10,7))

# Plot millet price variations
graph = diffmil[diffmil.adm1_name.isin(['Mopti'])].plot(x='reference_year',y=['price_var'],figsize=(10,7))

plt.show()




# Export data
diffmil.to_csv('../data/Food Prices/millet_var.csv')
mmil.to_csv('../data/Food Prices/millet_price.csv')
