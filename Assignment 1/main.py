import pandas as pd
import math

# ==========================
# Configurable Parameters
# ==========================

DATASET_PATH = "E:/COLLEGE/ML/weather.csv"
TARGET_COLUMN = "Played football" # Change if your dataset target column name is different

# ==========================
# Load the dataset
# ==========================

data = pd.read_csv(DATASET_PATH)
print("\n=== Dataset ===")
print(data)

# ==========================
# Function to calculate entropy
# ==========================

def calculate_entropy(yes_count, no_count):
    """
    Calculate entropy for a given number of 'Yes' and 'No' values.
    """
    total = yes_count + no_count
    if total == 0:
        return 0
    
    p_yes = yes_count / total
    p_no = no_count / total
    entropy = 0
    
    if p_yes > 0:
        entropy -= p_yes * math.log2(p_yes)
    if p_no > 0:
        entropy -= p_no * math.log2(p_no)
    
    return entropy

# ==========================
# Step 1: Calculate total dataset entropy
# ==========================

total_yes = len(data[data[TARGET_COLUMN] == "Yes"])
total_no = len(data[data[TARGET_COLUMN] == "No"])
total_entropy = calculate_entropy(total_yes, total_no)
total_records = total_yes + total_no

print(f"\nTotal Yes: {total_yes}, Total No: {total_no}")
print(f"Total Entropy of dataset: {total_entropy:.4f}")

# ==========================
# Step 2: Calculate Information Gain for each feature
# ==========================

features = [col for col in data.columns if col != TARGET_COLUMN]
ig_results = {}

for feature in features:
    feature_values = data[feature].unique()
    feature_entropy = 0
    print(f"\nCalculating Information Gain for feature: {feature}")
    
    for value in feature_values:
        subset = data[data[feature] == value]
        yes_count = len(subset[subset[TARGET_COLUMN] == "Yes"])
        no_count = len(subset[subset[TARGET_COLUMN] == "No"])
        entropy = calculate_entropy(yes_count, no_count)
        weight = (yes_count + no_count) / total_records
        feature_entropy += weight * entropy
        
        print(f"  {value} → Yes: {yes_count}, No: {no_count}, "
              f"Entropy: {entropy:.4f}, Weight: {weight:.4f}")
    
    ig = total_entropy - feature_entropy
    ig_results[feature] = ig
    print(f"Information Gain for {feature}: {ig:.4f}")

# ==========================
# Step 3: Find the feature with the highest IG
# ==========================

best_feature = max(ig_results, key=ig_results.get)

print("\n--- Summary of Information Gains ---")
for feature, ig in ig_results.items():
    print(f"{feature} : {ig:.4f}")

print(f"\n Root node should be: {best_feature} "
      f"(Highest IG: {ig_results[best_feature]:.4f})")
