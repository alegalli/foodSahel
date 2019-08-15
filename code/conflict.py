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
                    'event_date':'date'}, inplace=True)
confb.rename(columns={'country':'adm0_name',
                    'admin1':'adm1_name',
                    'admin2':'adm2_name',
                    'admin3':'adm3_name',
                    'event_date':'date'}, inplace=True)
confn.rename(columns={'country':'adm0_name',
                    'admin1':'adm1_name',
                    'admin2':'adm2_name',
                    'admin3':'adm3_name',
                    'event_date':'date'}, inplace=True)
confm = confm[['year','date','adm0_name','adm1_name','adm2_name','adm3_name',
        'event_type','sub_event_type','fatalities']]
confb = confb[['year','date','adm0_name','adm1_name','adm2_name','adm3_name',
        'event_type','sub_event_type','fatalities']]
confn = confn[['year','date','adm0_name','adm1_name','adm2_name','adm3_name',
        'event_type','sub_event_type','fatalities']]

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
