import pandas as pd
import xlrd
import seaborn as sns
import matplotlib.pyplot as plt

#Read CH data from excel
ch = pd.read_excel('../data/Cadre Harmonise/cadre_harmonise.xlsx')

# Features I'm interested in:
ch = ch[['adm0_name','adm1_name','adm2_name','population','phase_class','phase35',
        'chtype','exercise_label','excercise_year','reference_label','reference_year']]

# Select adm0_name to work with
ch = ch[ch.adm0_name.isin(['Mali','Burkina Faso','Niger'])]

# Select adm1_name to work with
ch = ch[ch.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
ch = ch.reset_index(drop=True)
