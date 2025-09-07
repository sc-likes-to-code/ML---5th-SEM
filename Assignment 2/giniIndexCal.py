import pandas as pd

# Load dataset
data = pd.read_csv("E:\\5th SEM CODING\\ML\\ASS 2_Gini Index\\weather.csv")
print(data)

# Gini index calculation function
def gini_index(yes, no):
    total = yes + no
    if total == 0:
        return 0
    p_yes = yes / total
    p_no = no / total
    return 1 - (p_yes**2 + p_no**2)

# Step 1: Calculate total dataset Gini index
total_yes = len(data[data["Played football"] == "Yes"])
total_no = len(data[data["Played football"] == "No"])
total_gini = gini_index(total_yes, total_no)
total = total_yes + total_no
print(f"Total Gini of dataset: {total_gini:.4f}")

# Step 2: Calculate Gini Gain for each feature
features = ["Outlook", "Temperature", "Humidity", "Windy"]
gini_results = {}

for feature in features:
    feature_values = data[feature].unique()
    feature_gini = 0
    print(f"\nCalculating Gini Gain for feature: {feature}")
    
    for value in feature_values:
        subset = data[data[feature] == value]
        yes = len(subset[subset["Played football"] == "Yes"])
        no = len(subset[subset["Played football"] == "No"])
        gini = gini_index(yes, no)
        weight = (yes + no) / total
        feature_gini += weight * gini
        print(f"  {value} → Yes: {yes}, No: {no}, Gini: {gini:.4f}, Weight: {weight:.4f}")
    
    gini_gain = total_gini - feature_gini
    gini_results[feature] = gini_gain
    print(f"Gini Gain for {feature}: {gini_gain:.4f}")

# Step 3: Find the feature with the highest Gini Gain
best_feature = max(gini_results, key=gini_results.get)
print("\n--- Summary ---")
for feature, gini_gain in gini_results.items():
    print(f"{feature} : {gini_gain:.4f}")

print(f"\nRoot node should be: {best_feature} (Highest Gini Gain: {gini_results[best_feature]:.4f})")

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
Total Gini of dataset: 0.4592

Calculating Gini Gain for feature: Outlook
  Sunny → Yes: 2, No: 3, Gini: 0.4800, Weight: 0.3571
  Overcast → Yes: 4, No: 0, Gini: 0.0000, Weight: 0.2857
  Rain → Yes: 3, No: 2, Gini: 0.4800, Weight: 0.3571
Gini Gain for Outlook: 0.1163

Calculating Gini Gain for feature: Temperature
  Hot → Yes: 2, No: 2, Gini: 0.5000, Weight: 0.2857
  Mild → Yes: 4, No: 2, Gini: 0.4444, Weight: 0.4286
  Cool → Yes: 3, No: 1, Gini: 0.3750, Weight: 0.2857
Gini Gain for Temperature: 0.0187

Calculating Gini Gain for feature: Humidity
  High → Yes: 3, No: 4, Gini: 0.4898, Weight: 0.5000
  Normal → Yes: 6, No: 1, Gini: 0.2449, Weight: 0.5000
Gini Gain for Humidity: 0.0918

Calculating Gini Gain for feature: Windy
  Weak → Yes: 6, No: 2, Gini: 0.3750, Weight: 0.5714
  Strong → Yes: 3, No: 3, Gini: 0.5000, Weight: 0.4286
Gini Gain for Windy: 0.0306

--- Summary ---
Outlook : 0.1163
Temperature : 0.0187
Humidity : 0.0918
Windy : 0.0306

Root node should be: Outlook (Highest Gini Gain: 0.1163)
'''
