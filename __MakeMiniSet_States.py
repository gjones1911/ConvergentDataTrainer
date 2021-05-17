import pandas as pd                           # import the pandas data frame moduel and call it pd
from _DeepSolarTools.__DEEPSOLAR_Resources import *
from _DeepSolarTools.__PAPER_RESOURCES import *


df_m = pd.read_csv(r"C:\Users\gjone\ConvergentDataTrainer\ConvergentMini.csv", low_memory=False)

df_m = df_m.loc[df_m['State'].isin(['ca', 'wv', 'sd', 'az', 'nv', 'me' ]), :]
df_m.to_csv("ConvergentTopBottom.csv")
