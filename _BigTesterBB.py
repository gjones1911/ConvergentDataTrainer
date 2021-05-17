import pandas as pd                           # import the pandas data frame moduel and call it pd
from _DeepSolarTools.__DEEPSOLAR_Resources import *
from _DeepSolarTools.__PAPER_RESOURCES import *


path_to_file = r'./_Data/_Mixed/US_set_all_OMEGA_1_24_21_Base.xlsx'

usecols = list(set(pd.read_excel(r'./_Data/MainUsecolumns/To_Add_to_model.xlsx', usecols=['Variables']).values.flatten().tolist() + model_varsD))
for v in not_in_bb:
    if v in usecols:
        del usecols[usecols.index(v)]
solar_drops = [
        'solar_system_count', 'solar_panel_area_divided_by_area', 'solar_panel_area_per_capita',
        'number_of_solar_system_per_household', 'solar_system_count_residential', 'solar_system_count_nonresidential',
        'total_panel_area', 'solar_system_count_nonresidential', 'total_panel_area_residential',
        'total_panel_area_nonresidential', 'Adoption',
    ]
usecols += solar_drops
usecols = list(set(usecols))
print(usecols)
print(len(usecols))


convergent_dfEX = pd.read_excel(path_to_file, usecols=usecols)
convergent_dfEX.rename(columns=label_translation_dict,inplace=True)
print(convergent_dfEX)


#convergent_dfEX.to_excel("ConvergentMini.xlsx")
convergent_dfEX.to_csv("ConvergentMini.csv")
