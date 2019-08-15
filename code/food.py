import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Extract year
foodm['year'] = foodm.date.str.split('-',expand=True)[0]
foodb['year'] = foodb.date.str.split('-',expand=True)[0]
foodn['year'] = foodn.date.str.split('-',expand=True)[0]
foodm = foodm.drop(0)
foodb = foodb.drop(0)
foodn = foodn.drop(0)
# Adjusting variables dtypes
foodm['year'] = foodm['year'].astype(int)
foodb['year'] = foodb['year'].astype(int)
foodn['year'] = foodn['year'].astype(int)
foodm['price'] = foodm['price'].astype(float)
foodb['price'] = foodb['price'].astype(float)
foodn['price'] = foodn['price'].astype(float)

# Select data from 2014 to 2018
foodm = foodm[foodm.year.isin([2013,2014,2015,2016,2017,2018,2019])]
foodb = foodb[foodb.year.isin([2013,2014,2015,2016,2017,2018,2019])]
foodn = foodn[foodn.year.isin([2013,2014,2015,2016,2017,2018,2019])]

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
meanm = foodm.groupby(['cmname','adm1_name','year'])['price'].mean()
meanb = foodb.groupby(['cmname','adm1_name','year'])['price'].mean()
meann = foodn.groupby(['cmname','adm1_name','year'])['price'].mean()
print(str(meanm))
print(str(meanb))
print(str(meann))
