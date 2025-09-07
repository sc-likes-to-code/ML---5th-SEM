#importing libraries
import pandas as pd
import math

#loading weather dataset
data = pd.read_csv("E:\\5th SEM CODING\\ML\\analyzing weather dataset\\weather.csv")
print(data)

#entropy function
def cal_entropy(yes,no):
    total = yes + no
    if (total == 0):
        return 0
    p_yes = yes / total
    p_no = no / total
    entropy = 0
    if (p_yes > 0):
        entropy -= p_yes * math.log2(p_yes)
    if (p_no > 0):
        entropy -= p_no * math.log2(p_no)
    return entropy

#calculating total entropy
total_yes = len(data[data["Played football"] == "Yes"])
total_no = len(data[data["Played football"] == "No"])
total_entropy = cal_entropy(total_yes, total_no)
total = total_yes + total_no

#calculating information gain or entropy of each feature
features = ["Outlook", "Temperature", "Humidity", "Windy"]
ig_results= {}

for feature in features:
    feature_values = data[feature].unique()
    feature_entropy = 0
    for value in feature_values:
        subset = data[data[feature] == value]
        yes = len(subset[subset["Played football"] == "Yes"])
        no = len(subset[subset["Played football"] == "No"])
        entropy = cal_entropy(yes, no)
        weight = (yes + no) / total
        feature_entropy += weight * entropy
    ig = total_entropy - feature_entropy
    ig_results[feature] = ig
    
#finding best feature
best_feature = max(ig_results, key = ig_results.get)

#printing all results
print("\n--- Information Gain values ---")
for feature, ig in ig_results.items():
    print(f"{feature}: {ig:.4f}")
print(f"\nRoot node should be: {best_feature} (Highest IG: {ig_results[best_feature]:.4f})")

#output:
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

--- Information Gain values ---
Outlook: 0.2467
Temperature: 0.0292
Humidity: 0.1518
Windy: 0.0481

Root node should be: Outlook (Highest IG: 0.2467)
'''
