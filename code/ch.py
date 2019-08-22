import pandas as pd
import xlrd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CH data from excel
ch = pd.read_excel('../data/Cadre Harmonise/cadre_harmonise.xlsx')

# Features I'm interested in:
ch = ch[['adm0_name','adm1_name','adm2_name','population','phase_class','phase35',
        'chtype','exercise_label','exercise_year','reference_label','reference_year']]

# Replace names to make consistent data: Tahoua, Tillaberi. THIS IS NOT WORKING, I take out Tillaberi and Tahoua to postpone the problem
#ch['adm2_name'].replace('Tahoua Department','Tahoua',inplace=True)
#ch['adm2_name'].replace('Tillaberi Department','Tillaberi',inplace=True)

# Select adm0_name to work with
ch = ch[ch.adm0_name.isin(['Mali','Burkina Faso','Niger'])]

# Select adm1_name to work with
ch = ch[ch.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]

# Select adm2_name to work with
ch = ch[ch.adm2_name.isin(['Bankass','Koro','Douentza','Djenne','Bandiagara','Tenenkou','Mopti','Youwarou',
                              'Gourma-Rharous','Dire','Niafunke',
                              'Gao','Ansongo','Menaka','Bourem',
                              'Yatenga','Loroum',
                              'Yagha','Seno','Soum','Oudalan',
                              'Komonjdjari',
                              'Tassara','Tillia', # I take out Tillaberi and Tahoua because of some values are in Tillaberi Department and Tahoua Department
                              'Banibangou','Filingue','Ouallam','Say','Tera','Balleyara','Torodi','Bankilare','Abala','Ayerou','Gotheye'])]

# Sorting ch by ['adm0_name','reference_year','chtype','reference_label','exercise_label','adm1_name','adm2_name']
ch = ch.sort_values(by=['adm0_name','reference_year','chtype','reference_label','exercise_label','adm1_name','adm2_name'])
ch = ch.reset_index(drop=True)


# We want to work just with the Lean Season data
# We need just the spring estimation: Select exercise_label=='Jan-May'
lean = ch[ch.exercise_label == 'Jan-May']
# Select reference_label='Jun-Aug'
lean = lean[lean.reference_label == 'Jun-Aug']
# Select chtype=='projected'
lean = lean[lean.chtype == 'projected']
lean = lean.reset_index(drop=True)
# Select featueres
lean = lean[['adm0_name','adm1_name','adm2_name','population','phase_class','phase35','reference_year']]

# Let's plot things out
# phase35 density between the population in Lean Season: (phase35%, reference_year)
lean['p35_density'] = lean['phase35'].div(lean['population'])
#lean_graph = lean[lean.adm2_name=='Gao'].plot(x='reference_year',y='p35_density',figsize=(12,8))


# I should create a DataFrame where a column is year, the other columns are the different areas (same as biomass)

# Create a DataFrame to plot population
pop1 = pd.DataFrame()
pop1['adm0_name'] = lean.adm0_name[lean.reference_year.isin([2014])]
pop1['adm1_name'] = lean.adm1_name[lean.reference_year.isin([2014])]
pop1['adm2_name'] = lean.adm2_name[lean.reference_year.isin([2014])]
pop1[2014] = lean.population[lean.reference_year.isin([2014])]
pop1 = pop1.sort_values(by=['adm0_name','adm1_name','adm2_name'])
pop1 = pop1.reset_index(drop=True)

for anno in range(2015,2020):
    pop2 = pd.DataFrame()
    pop2['adm0_name'] = lean.adm0_name[lean.reference_year.isin([anno])]
    pop2['adm1_name'] = lean.adm1_name[lean.reference_year.isin([anno])]
    pop2['adm2_name2'] = lean.adm2_name[lean.reference_year.isin([anno])]
    pop2[anno] = lean.population[lean.reference_year.isin([anno])]
    # NOTE: with nan all the sort will create wrong values
    # For the above reason I have to drop all NaN before sorting
    #pop1.dropna()
    # but it's easyer not to put Tillaberi and Tahoua from the beginning
    pop2 = pop2.sort_values(by=['adm0_name','adm1_name','adm2_name2'])
    pop2 = pop2.reset_index(drop=True)
    pop1[anno] = pop2[anno]

# Preapare DataFrame to plot population
p = pop1[[2014,2015,2016,2017,2018,2019]]
p.index = pop1['adm2_name']
p = p.T

# Select adm2_name to see
pop = p[['Bankass','Torodi','Gao','Yatenga']]

# Plot population
plt.style.use('fivethirtyeight')
graph = pop.plot(figsize=(10,7))
plt.show()



# Create a DataFrame to plot p35_density
p351 = pd.DataFrame()
p351['adm0_name'] = lean.adm0_name[lean.reference_year.isin([2014])]
p351['adm1_name'] = lean.adm1_name[lean.reference_year.isin([2014])]
p351['adm2_name'] = lean.adm2_name[lean.reference_year.isin([2014])]
p351[2014] = lean.p35_density[lean.reference_year.isin([2014])]
p351 = p351.sort_values(by=['adm0_name','adm1_name','adm2_name'])
p351 = p351.reset_index(drop=True)

for anno in range(2015,2020):
    p352 = pd.DataFrame()
    p352['adm0_name'] = lean.adm0_name[lean.reference_year.isin([anno])]
    p352['adm1_name'] = lean.adm1_name[lean.reference_year.isin([anno])]
    p352['adm2_name2'] = lean.adm2_name[lean.reference_year.isin([anno])]
    p352[anno] = lean.p35_density[lean.reference_year.isin([anno])]
    # NOTE: with nan all the sort will create wrong values
    # For the above reason I have to drop all NaN before sorting
    #p351.dropna()
    # but it's easyer not to put Tillaberi and Tahoua from the beginning
    p352 = p352.sort_values(by=['adm0_name','adm1_name','adm2_name2'])
    p352 = p352.reset_index(drop=True)
    p351[anno] = p352[anno]

# Preapare DataFrame to plot p35
phase35 = p351[[2014,2015,2016,2017,2018,2019]]
phase35.index = p351['adm2_name']
phase35 = phase35.T

# Select adm2_name to see
p35 = phase35[['Bankass','Torodi','Gao','Yatenga']]

# Plot p35
plt.style.use('fivethirtyeight')
graph = p35.plot(figsize=(10,7))
plt.show()




# Create a DataFrame to plot phase_class
phase_class1 = pd.DataFrame()
phase_class1['adm0_name'] = lean.adm0_name[lean.reference_year.isin([2014])]
phase_class1['adm1_name'] = lean.adm1_name[lean.reference_year.isin([2014])]
phase_class1['adm2_name'] = lean.adm2_name[lean.reference_year.isin([2014])]
phase_class1[2014] = lean.phase_class[lean.reference_year.isin([2014])]
phase_class1 = phase_class1.sort_values(by=['adm0_name','adm1_name','adm2_name'])
phase_class1 = phase_class1.reset_index(drop=True)

for anno in range(2015,2020):
    phase_class2 = pd.DataFrame()
    phase_class2['adm0_name'] = lean.adm0_name[lean.reference_year.isin([anno])]
    phase_class2['adm1_name'] = lean.adm1_name[lean.reference_year.isin([anno])]
    phase_class2['adm2_name2'] = lean.adm2_name[lean.reference_year.isin([anno])]
    phase_class2[anno] = lean.phase_class[lean.reference_year.isin([anno])]
    # NOTE: with nan all the sort will create wrong values
    # For the above reason I have to drop all NaN before sorting
    #phase_class1.dropna()
    # but it's easyer not to put Tillaberi and Tahoua from the beginning
    phase_class2 = phase_class2.sort_values(by=['adm0_name','adm1_name','adm2_name2'])
    phase_class2 = phase_class2.reset_index(drop=True)
    phase_class1[anno] = phase_class2[anno]

# Preapare DataFrame to plot phase_class
phase = phase_class1[[2014,2015,2016,2017,2018,2019]]
phase.index = phase_class1['adm2_name']
phase = phase.T

# Select adm2_name to see
phase_class = phase[['Bankass','Torodi','Gao','Yatenga']]

# NOTE: Should plot this with "dotplot"
# Plot phase_class
plt.style.use('fivethirtyeight')
graph = phase_class.plot(figsize=(10,7))
plt.show()

# bello ma vorrei visualizzare la stessa adm2_name con lo stesso colore e metterci una legenda
sns.swarmplot(x='reference_year',y='phase_class',data=phase_class)




# Visualize all the data available (year, phase_class)
sns.swarmplot(x='reference_year',y='phase_class',data=lean)




# Super interesting
# Visualize all the data available (year, p35_density)
sns.swarmplot(x='reference_year',y='p35_density',data=lean)
sns.swarmplot(x='reference_year',y='p35_density',data=lean[lean.adm2_name.isin(['Gao','Torodi','Yagha'])])




# Small linear regression model
sns.lmplot(x='population',y='p35_density',data=lean,figsize=(10,8))




# Export data
lean.to_csv('../data/Cadre Harmonise/lean.csv')
