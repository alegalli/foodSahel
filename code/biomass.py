adm2_nameimport pandas as pd
import xlrd
import seaborn as sns
import matplotlib.pyplot as plt

bio = pd.read_excel('../data/Biomass Production/bio_adm2.xlsx')

# Features I'm interested in:
bio.rename(columns={'admin0Name':'adm0_name',
                    'admin1Name':'adm1_name',
                    'admin2Name':'adm2_name'}, inplace=True)
bio = bio[['adm0_name','adm1_name','adm2_name','Shape_Area','AREA',
        'BIO_2014','BIO_2015','BIO_2016','BIO_2017','BIO_2018']]

# Countries I'm interested in:
bio = bio[bio.adm0_name.isin(['Mali','Burkina Faso','Niger'])]
# se vuoi escluderli: bio[~bio.adm0_name.isin(['Mali','Niger'])] tilde

bio = bio[bio.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
bio = bio.reset_index(drop=True)



# Extract csv
ex = bio.to_csv('../data/biomass.csv', index=False)
