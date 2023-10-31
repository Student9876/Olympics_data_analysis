import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path1 = "dataset/athlete_events.csv"
file_path2 = "dataset/noc_regions.csv"

df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)


# Enter year here 
year = 2016



dictionary_1 = {
}
dictionary_2 ={
}

Country_list=[]


for index,row in df2.iterrows():
    Country_list.append(row['NOC'])

for index, row in df1.iterrows():
    if row['NOC'] in Country_list:
        dictionary_1[row['NOC']]={}


for index, row in df1.iterrows():
    if row['NOC'] in Country_list:
        dictionary_1[row['NOC']][row['Year']]=0

for index, row in df1.iterrows():
    if row['NOC'] in Country_list:
        if row['Medal'] != 'NA':
            dictionary_1[row['NOC']][row['Year']]+=1


dictionary_1=dict(sorted(dictionary_1.items()))

for keys, value in dictionary_1.items():
    for key, val in value.items():
        if(key==year):
            dictionary_2[keys]=val


items = list(dictionary_2.items())
# Split the list of dictionary in half
first_ = items[:len(items)//2]
second_ = items[len(items)//2:]

# Dividing further in 4 parts
first_half  = first_[:len(first_)//2]
second_half  = first_[len(first_)//2:]
third_half  = second_[:len(second_)//2]
forth_half  = second_[len(second_)//2:]


# Create four separate dictionaries
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


# Initialise the subplot function using number of rows and columns 
figure, axis = plt.subplots(4)
figure.suptitle(f"Olympics medal winner of year {year}")

# axis[0].set_title("1st") 
axis[0].bar(range(len(first_half)), values1, tick_label=names1)
  

# axis[1].set_title("2nd") 
axis[1].bar(range(len(second_half)), values2, tick_label=names2)
  

# axis[2].set_title("3rd") 
axis[2].bar(range(len(third_half)), values3, tick_label=names3)
  
 
# axis[3].set_title("4th")
axis[3].bar(range(len(forth_half)), values4, tick_label=names4)



# plt.bar(range(len(first_half)), values1, tick_label=names1)
plt.show()
# plt.bar(range(len(second_half)), values2, tick_label=names2)
# plt.show()
# plt.bar(range(len(third_half)), values3, tick_label=names3)
# plt.bar(range(len(forth_half)), values4, tick_label=names4)