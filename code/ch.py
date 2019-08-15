import pandas as pd
import xlrd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CH data from excel
ch = pd.read_excel('../data/Cadre Harmonise/cadre_harmonise.xlsx')

# Features I'm interested in:
ch = ch[['adm0_name','adm1_name','adm2_name','population','phase_class','phase35',
        'chtype','exercise_label','exercise_year','reference_label','reference_year']]

# Select adm0_name to work with
ch = ch[ch.adm0_name.isin(['Mali','Burkina Faso','Niger'])]

# Select adm1_name to work with
ch = ch[ch.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
ch = ch.reset_index(drop=True)

# We want to work just with the Lean Season data
# We need just the spring estimation: Select exercise_label=='Jan-May'
lean = ch[ch.exercise_label == 'Jan-May']
# Select reference_label='Jun-Aug'
lean = lean[lean.reference_label == 'Jun-Aug']
# Select chtype=='projected'
lean = lean[lean.chtype == 'projected']
lean = lean.reset_index(drop=True)
# lean[['adm0_name','adm1_name','adm2_name','population','phase_class',
#         'phase35','reference_year']]
lean = lean.drop(['chtype','exercise_label','exercise_year','reference_label'],axis=1)


# Let's plot things out
# phase35 density between the population in Lean Season: (phase35%, reference_year)
lean['p35_density'] = lean['phase35'].div(lean['population'])
lean_graph = lean[lean.adm2_name=='Gao'].plot(x='reference_year',y='p35_density',figsize=(12,8))
