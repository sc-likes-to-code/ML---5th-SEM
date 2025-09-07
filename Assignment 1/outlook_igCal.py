#importing libraries
import pandas as pd
import math

#loading dataset
data = pd.read_csv("E:\\5th SEM CODING\\ML\\analyzing weather dataset\\weather.csv")
print(data)

# Count total number of Yes and No present in the dataset
total_yes = len(data[data["Played football"] == "Yes"])
total_no = len(data[data["Played football"] == "No"])
total = total_yes + total_no
print("Total yes: ",total_yes)
print("Total no: ",total_no)
print("Total no. of tuples in the dataset: ",total)

#Count Outlook-wise Yes/No

#sunny
sunny_yes = len(data[(data["Outlook"] == "Sunny") & (data["Played football"] == "Yes")])
print("Sunny Yes :",sunny_yes)
sunny_no = len(data[(data["Outlook"]=="Sunny") & (data["Played football"]=="No")])
sunny_total = sunny_yes + sunny_no
print("Sunny No :",sunny_no)

# Overcast
overcast_yes = len(data[(data["Outlook"]=="Overcast") & (data["Played football"]=="Yes")])
print("Overcast Yes :",overcast_yes)
overcast_no = len(data[(data["Outlook"]=="Overcast") & (data["Played football"]=="No")])
overcast_total = overcast_yes + overcast_no
print("Overcast No :",overcast_no)

# Rain
rain_yes = len(data[(data["Outlook"]=="Rain") & (data["Played football"]=="Yes")])
print("Rain Yes :",rain_yes)
rain_no = len(data[(data["Outlook"]=="Rain") & (data["Played football"]=="No")])
print("Rain No:",rain_no)
rain_total = rain_yes + rain_no

def cal_entropy(y,n):
    total = y + n
    p_yes = y/total
    p_no = n/total
    
    if total == 0:
        return 0
    
    entropy = 0
    if (p_yes > 0):
        entropy -= p_yes * math.log2(p_yes)
    if (p_no > 0):
        entropy -= p_no * math.log2(p_no)
        
    return entropy

entropy_total = cal_entropy(total_yes, total_no)
print("Entropy of total dataset: ",entropy_total)

entropy_sunny = cal_entropy(sunny_yes,sunny_no)
entropy_overcast = cal_entropy(overcast_yes,overcast_no)
entropy_rain = cal_entropy(rain_yes,rain_no)

IG_Outlook = entropy_total - ((sunny_total/total) * entropy_sunny + (overcast_total/total) * entropy_overcast + (rain_total/total) * entropy_rain)
print("Information Gain for Outlook: ",IG_Outlook)

#output
'''
     Outlook Temperature Humidity   Windy Played football
0      Sunny         Hot     High    Weak              No
1      Sunny         Hot     High  Strong              No
2   Overcast         Hot     High    Weak             Yes
3       Rain        Mild     High    Weak             Yes
4       Rain        Cool   Normal    Weak             Yes
5       Rain        Cool   Normal  Strong              No
6   Overcast        Cool   Normal  Strong             Yes
7      Sunny        Mild     High    Weak              No
8      Sunny        Cool   Normal    Weak             Yes
9       Rain        Mild   Normal    Weak             Yes
10     Sunny        Mild   Normal  Strong             Yes
11  Overcast        Mild     High  Strong             Yes
12  Overcast         Hot   Normal    Weak             Yes
13      Rain        Mild     High  Strong              No
Total yes:  9
Total no:  5
Total no. of tuples in the dataset:  14
Sunny Yes : 2
Sunny No : 3
Overcast Yes : 4
Overcast No : 0
Rain Yes : 3
Rain No: 2
Entropy of total dataset:  0.9402859586706311
Information Gain for Outlook:  0.24674981977443933
'''
