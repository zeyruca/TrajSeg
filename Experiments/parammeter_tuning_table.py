import pandas as pd
df2=pd.read_csv('HurricanesDataset/Results_HurricanesDataset_CBSMoT.csv')
print(df2['best parameters'])
df2=pd.read_csv('FishingDataset/Results_FishingDataset_CBSMoT.csv')
print(df2['best parameters'])
df2=pd.read_csv('GeolifeDataset/Results_GeolifeDataset_CBSMoT.csv')
print(df2['best parameters'])

df2=pd.read_csv('HurricanesDataset/Results_HurricanesDataset_SPD.csv')
print(df2['best parameters'])
df2=pd.read_csv('FishingDataset/Results_FishingDataset_SPD.csv')
print(df2['best parameters'])
df2=pd.read_csv('GeolifeDataset/Results_GeolifeDataset_SPD.csv')
print(df2['best parameters'])

df2=pd.read_csv('HurricanesDataset/Results_HurricanesDataset_SWS_L.csv')
print(df2['best parameters'])
df2=pd.read_csv('FishingDataset/Results_FishingDataset_SWS_L.csv')
print(df2['best parameters'])
df2=pd.read_csv('GeolifeDataset/Results_GeolifeDataset_SWS_L.csv')
print(df2['best parameters'][0])