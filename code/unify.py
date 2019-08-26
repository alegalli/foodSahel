import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


food = pd.read_csv('../data/Food Prices/millet_price.csv')
conf = pd.read_csv('../data/Conflict Data/conflict_numb.csv')
bio = pd.read_csv('../data/Biomass Production/biomass.csv')
lean = pd.read_csv('../data/Cadre Harmonise/lean.csv')

food = food.sort_values(['reference_year','adm2_name']).reset_index()
conf = conf.sort_values(['reference_year','adm2_name']).reset_index()
bio = bio.sort_values(['reference_year','adm2_name']).reset_index()
lean = lean.sort_values(['reference_year','adm2_name']).reset_index()
food = food.drop(columns=['index'])
conf = conf.drop(columns=['index'])
bio = bio.drop(columns=['index'])
lean = lean.drop(columns=['index'])

data = lean
data['millet_price'] = food['mean']
data['millet_var'] = food['price_var']
data['conflicts'] = conf['conflicts']
data['fatalities'] = conf['fatalities']
data['biomass'] = bio['biomass']


corr = data.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm',vmin=-1,vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,10,1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(['population','phase_class','phase35','reference_year','p35_density','millet_price','millet_var','conflicts','fatalities','biomass'])
ax.set_yticklabels(['population','phase_class','phase35','reference_year','p35_density','millet_price','millet_var','conflicts','fatalities','biomass'])
plt.show()




data.to_csv('../data/Data/data.csv')
