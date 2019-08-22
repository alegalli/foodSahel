import numpy as np
import pandas as pd
import xlrd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style

bio = pd.read_excel('../data/Biomass Production/bio_adm2.xlsx')

# Features I'm interested in:
bio.rename(columns={'admin0Name':'adm0_name',
                    'admin1Name':'adm1_name',
                    'admin2Name':'adm2_name',
                    'BIO_2013':'2013',
                    'BIO_2014':'2014',
                    'BIO_2015':'2015',
                    'BIO_2016':'2016',
                    'BIO_2017':'2017',
                    'BIO_2018':'2018'}, inplace=True)
bio = bio[['adm0_name','adm1_name','adm2_name','Shape_Area','AREA',
        '2013','2014','2015','2016','2017','2018']]

# Manipulate data to create consistency with the other data
# adm2=='Gothaye' => adm2:'Gotheye'
bio['adm2_name'].replace('Gothaye','Gotheye',inplace=True)

# Countries I'm interested in:
bio = bio[bio.adm0_name.isin(['Mali','Burkina Faso','Niger'])]
# if you wanna drop these: bio[~bio.adm0_name.isin(['Mali','Niger'])] tilde

# Select adm1_name to work with
bio = bio[bio.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
bio = bio[bio.adm2_name.isin(['Bankass','Koro','Douentza','Djenne','Bandiagara','Tenenkou','Mopti','Youwarou',
                              'Gourma-Rharous','Dire','Niafunke',
                              'Gao','Ansongo','Menaka','Bourem',
                              'Yatenga','Loroum',
                              'Yagha','Seno','Soum','Oudalan',
                              'Komonjdjari',
                              'Tahoua','Tassara','Tillia',
                              'Banibangou','Filingue','Ouallam','Say','Tera','Tillaberi','Balleyara','Torodi','Bankilare','Abala','Ayerou','Gotheye'])]

bio = bio.reset_index(drop=True)


# Biomass production per AREA: Biomass Density biodens
biodens = pd.DataFrame(np.array([[2013,2014,2015,2016,2017,2018]]),columns=['2013','2014','2015','2016','2017','2018'])
biodens = biodens.append(bio[['2013','2014','2015','2016','2017','2018']])
biodens = biodens.reset_index(drop=True)

for i in biodens.index[1:len(biodens.index)-1]:
    for j in [['2013','2014','2015','2016','2017','2018']]:
        biodens.at[i,j] = biodens.loc[i,j] / bio.loc[i,'AREA']

# Prepare the DataFrame to be plotted
biodens = biodens.T
biodens = biodens.reset_index(drop=True)
# Rename the biodens with the respective adm2_name
biodens.columns = ['year']+bio.adm2_name.unique().tolist()

# Selecting the adm2_name with a certain criteria
biotry = biodens.loc[0,biodens.columns.isin(['Yatenga','Loroum','Yagha','Soum','Komonjdjari'])]

# Select plot style
# See more: https://github.com/matplotlib/matplotlib/blob/38be7aeaaac3691560aeadafe46722dda427ef47/lib/matplotlib/mpl-data/stylelib/fivethirtyeight.mplstyle
style.use('fivethirtyeight')
# Plot Biomass Density of the adm2_name tonnes/m^2
bio_graph = biodens.plot(x='year',y=biotry.index,figsize=(10,7))
bio_graph.tick_params(axis='both',which='major',labelsize=18)
bio_graph.set_yticklabels(labels = [-10, '0   ', '10   ', '20   ', '30   ', '40   ', '50   ', '60   ', '70   ', '80   '])
bio_graph.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)
# TODO: Set limits
#bio_graph.set_xlim(left = 1969, right = 2011) #mi da problemi
bio_graph.xaxis.label.set_visible(False)
# TODO: Below line
#bio_graph.text(x = 1965.8, y = -7,
#    s = ' ALESSANDRO GALLI                                                         Source: Action contre la Faim',fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey')
plt.show()


# Export data
bio.to_csv('../data/Biomass Production/biomass.csv', index=False)
