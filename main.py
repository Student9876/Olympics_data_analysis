# Target 
''' 
1.
''' 



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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

# for keys, value in dictionary_1.items():
#    print(keys,value)

dictionary_2 ={

}

for keys, value in dictionary_1.items():
    for key, val in value.items():
        if(key==2010):
            dictionary_2[keys]=val



items = list(dictionary_2.items())
# Split the list of tuples in half
first_ = items[:len(items)//2]
second_ = items[len(items)//2:]
# Create two separate dictionaries


first_half  = first_[:len(first_)//2]
second_half  = first_[len(first_)//2:]
third_half  = items[:len(second_)//2]
forth_half  = items[len(second_)//2:]


first_half_dict = dict(first_half)
second_half_dict = dict(second_half)
third_half_dict = dict(third_half)
forth_half_dict = dict(forth_half)


names1 = list(first_half_dict.keys())
values1 = list(first_half_dict.values())

names2 = list(second_half_dict.keys())
values2 = list(second_half_dict.values())

names3 = list(third_half_dict.keys())
values3 = list(third_half_dict.values())

names4 = list(forth_half_dict.keys())
values4 = list(forth_half_dict.values())

plt.bar(range(len(first_half)), values1, tick_label=names1)
plt.show()
# plt.bar(range(len(second_half)), values2, tick_label=names2)
# plt.show()
# plt.bar(range(len(third_half)), values3, tick_label=names3)
# plt.bar(range(len(forth_half)), values4, tick_label=names4)