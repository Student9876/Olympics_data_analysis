# Target 
''' 
1.
''' 



import pandas as pd
import matplotlib.pyplot as plt


file_path1 = "dataset/athlete_events.csv"
file_path2 = "dataset/noc_regions.csv"


df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)
column_name1 = "Name"
column_name2 = "Year"
column_name3 = "Team"
column_name_1 = "region"


dictionary_1 = {

}

Country_list=[]


for index,row in df2.iterrows():
    Country_list.append(row['region'])

for index, row in df1.iterrows():
    if row['Team'] in Country_list:
        dictionary_1[row['Team']]={}


for index, row in df1.iterrows():
    if row['Team'] in Country_list:
        dictionary_1[row['Team']][row['Year']]=0

for index, row in df1.iterrows():
    if row['Team'] in Country_list:
        if row['Medal'] != 'NA':
            dictionary_1[row['Team']][row['Year']]+=1


dictionary_1=dict(sorted(dictionary_1.items()))


# df_outputCSV = pd.DataFrame(dictionary_1)
# df_outputCSV.to_csv('output.csv', index=False)

for keys, value in dictionary_1.items():
   print(keys,value)
