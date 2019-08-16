import numpy as np
import pandas as pd
import xlrd
import seaborn as sns
import matplotlib.pyplot as plt

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


# Countries I'm interested in:
bio = bio[bio.adm0_name.isin(['Mali','Burkina Faso','Niger'])]
# if you wanna drop these: bio[~bio.adm0_name.isin(['Mali','Niger'])] tilde

# Select adm1_name to work with
bio = bio[bio.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
bio = bio.reset_index(drop=True)

# Manipulate data to create consistency with the other data
# adm2=='Gothaye' => adm2:'Gotheye'
bio['adm2_name'].replace('Gothaye','Gotheye',inplace=True)

# Biomass production per AREA: Biomass Density biodens
#biodens = pd.DataFrame(columns=[13,14,15,16,17,18])
biodens = pd.DataFrame(np.array([[2013,2014,2015,2016,2017,2018]]),columns=['2013','2014','2015','2016','2017','2018'])
biodens = biodens.append(bio[['2013','2014','2015','2016','2017','2018']])
biodens = biodens.reset_index(drop=True)

for i in biodens.index[1:len(biodens.index)-1]:
    for j in [['2013','2014','2015','2016','2017','2018']]:
        biodens.at[i,j] = biodens.loc[i,j] / bio.loc[i,'AREA']


biodens = biodens.T
biodens = biodens.reset_index(drop=True)
biodens.rename(columns={0:'year'},inplace=True)

biotry = biodens.loc[0, biodens.loc[0]<30]
#biotry.rename(columns={})'year'+'adm2_name'

bio_graph = biodens.plot(x='year',y=biotry.index,figsize=(12,8))



# Extract csv
ex = bio.to_csv('../data/biomass.csv', index=False)
