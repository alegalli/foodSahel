adm1_nameimport pandas as pd
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
confm = confm[confm.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tindilleri'])]
confm = confm.reset_index(drop=True)
confb = confb[confb.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tindilleri'])]
confb = confb.reset_index(drop=True)
confn = confn[confn.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tindilleri'])]
confn = confn.reset_index(drop=True)
