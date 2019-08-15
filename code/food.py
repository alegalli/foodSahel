import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

foodm = pd.read_csv('../data/Food Prices/wfp_food_prices_mali.csv')
foodb = pd.read_csv('../data/Food Prices/wfp_food_prices_burkina-faso.csv')
foodn = pd.read_csv('../data/Food Prices/wfp_food_prices_niger.csv')

# Features I'm interested in:
foodm = foodm[['date','country','admname','mktname','category','cmname',
        'price','currency','unit']]
foodb = foodb[['date','country','admname','mktname','category','cmname',
        'price','currency','unit']]
foodn = foodn[['date','country','admname','mktname','category','cmname',
        'price','currency','unit']]

# Extract year
foodm['year'] = foodm.date.str.split('-',expand=True)[0]
foodb['year'] = foodb.date.str.split('-',expand=True)[0]
foodn['year'] = foodn.date.str.split('-',expand=True)[0]
foodm = foodm.drop(0)
foodb = foodb.drop(0)
foodn = foodn.drop(0)
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
foodm = foodm[foodm.admname.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tindilleri'])]
foodb = foodb[foodb.admname.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tindilleri'])]
foodn = foodn[foodn.admname.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tindilleri'])]

# Find mean of food prices
foodm = foodm[foodm.cmname.isin(['Millet - Retail','Rice (local) - Retail','Rice (imported) - Retail','Sorghum - Retail'])]
foodb = foodb[foodm.cmname.isin(['Sorghum - Retail','Millet - Retail','Maize - Retail','Rice (local) - Retail'])]
foodn = foodn[foodm.cmname.isin(['Millet - Retail','Rice (imported) - Retail','Sorghum - Retail','Maize - Retail'])]
foodm = foodm.reset_index(drop=True)
foodb = foodb.reset_index(drop=True)
foodn = foodn.reset_index(drop=True)
meanm = foodm.groupby(['cmname','admname','year'])['price'].mean()
meanb = foodb.groupby(['cmname','admname','year'])['price'].mean()
meann = foodn.groupby(['cmname','admname','year'])['price'].mean()
