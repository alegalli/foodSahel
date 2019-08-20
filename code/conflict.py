import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

confm = pd.read_csv('../data/Conflict Data/Conflict Data for Mali.csv')
confb = pd.read_csv('../data/Conflict Data/Conflict Data for Burkina Faso.csv')
confn = pd.read_csv('../data/Conflict Data/Conflict Data for Niger.csv')

# Features I'm interested in:
confm.rename(columns={'country':'adm0_name',
                    'admin1':'adm1_name',
                    'admin2':'adm2_name',
                    'admin3':'adm3_name',
                    'event_date':'date',
                    'year':'reference_year'}, inplace=True)
confb.rename(columns={'country':'adm0_name',
                    'admin1':'adm1_name',
                    'admin2':'adm2_name',
                    'admin3':'adm3_name',
                    'event_date':'date',
                    'year':'reference_year'}, inplace=True)
confn.rename(columns={'country':'adm0_name',
                    'admin1':'adm1_name',
                    'admin2':'adm2_name',
                    'admin3':'adm3_name',
                    'event_date':'date',
                    'year':'reference_year'}, inplace=True)
confm = confm[['reference_year','date','adm0_name','adm1_name','adm2_name','adm3_name',
        'event_type','sub_event_type','fatalities']]
confb = confb[['reference_year','date','adm0_name','adm1_name','adm2_name','adm3_name',
        'event_type','sub_event_type','fatalities']]
confn = confn[['reference_year','date','adm0_name','adm1_name','adm2_name','adm3_name',
        'event_type','sub_event_type','fatalities']]

# Extract reference_year
confm = confm[confm.reference_year.isin([2013,2014,2015,2016,2017,2018,2019])]
confm = confm[confm.reference_year.isin([2013,2014,2015,2016,2017,2018,2019])]
confm = confm[confm.reference_year.isin([2013,2014,2015,2016,2017,2018,2019])]

# Select adm1_name to work with
confm = confm[confm.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
confm = confm.reset_index(drop=True)
confb = confb[confb.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
confb = confb.reset_index(drop=True)
confn = confn[confn.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
confn = confn.reset_index(drop=True)

# Manipulate data to create consistency with the other data
# adm3=='Ayorou' => adm2:'Ayerou'
# adm3=='Torodi' => adm2:'Torodi'
# adm3=='Abala' => adm2:'Abala'
for i in confn.index:
    if confn.loc[i,'adm3_name']=='Ayorou':
        confn.at[i,'adm2_name']='Ayerou'
    if confn.loc[i,'adm3_name']=='Torodi':
        confn.at[i,'adm2_name']='Torodi'
    if confn.loc[i,'adm3_name']=='Abala':
        confn.at[i,'adm2_name']='Abala'

#confm = confm.drop(['adm3_name'])
#confb = confb.drop(['adm3_name'])
#confn = confn.drop(['adm3_name'])

confm = confm[confm.adm2_name.isin(['Bankass','Koro','Douentza','Djenne','Bandiagara','Tenenkou','Mopti','Youwarou', 'Gourma-Rharous','Dire','Niafunke', 'Gao','Ansongo','Menaka','Bourem'])]
confb = confb[confb.adm2_name.isin(['Yatenga','Loroum', 'Yagha','Seno','Soum','Oudalan', 'Komonjdjari'])]
confn = confn[confn.adm2_name.isin(['Tahoua','Tassara','Tillia', 'Banibangou','Filingue','Ouallam','Say','Tera','Tillaberi','Balleyara','Torodi','Bankilare','Abala','Ayerou','Gotheye'])]
confm = confm.reset_index(drop=True)
confb = confb.reset_index(drop=True)
confn = confn.reset_index(drop=True)




# Plot number of conflicts per year per adm2_name
ncym = pd.DataFrame(columns=['reference_year','adm2_name','conflicts','fatalities'])
for year in confm['reference_year'].unique():
    for elem in confm['adm2_name'].unique():
        ncym = ncym.append(pd.Series([year, elem, 0, 0],index=ncym.columns),ignore_index=True)
# Esattamente questo!
# Counts number of conflicts in a year in a adm2_name
for idx, elem in confm.iterrows():
    ncym.set_value(ncym[(ncym.reference_year == elem.reference_year) & (ncym.adm2_name == elem.adm2_name)].index,'conflicts', ncym['conflicts']+1)
for idx, elem in confm.iterrows():
    ncym.set_value(ncym[(ncym.reference_year == elem.reference_year) & (ncym.adm2_name == elem.adm2_name)].index,'fatalities', ncym['fatalities']+ int(elem['fatalities']))
# Number of conflicts in Gao per reference_year
plt.style.use('fivethirtyeight')
graph = ncym[ncym.adm2_name.isin(['Gao'])].plot(x='reference_year',y=['fatalities','conflicts'],figsize=(10,7))
plt.show()
