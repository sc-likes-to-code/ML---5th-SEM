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
