import csv
from itertools import combinations

data = []

with open("E:\\5th SEM CODING\\ML\\transactions.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row[1:])
        
print("Transactions:")
print(data)

min_support = 2
min_confidence = 0.6

items = []
for transaction in data:
    for product in transaction:
        if product not in items:
            items.append(product)
            
print("\nAll unique items: ", items)

def count_frequency(itemset):
    count = 0
    for transaction in data:
        present = True
        for product in itemset:
            if product not in transaction:
                present = False
                break
        if present:
            count += 1
    return count

count_combination_freq = {}

print("\nAll item combinations and their frequencies:")
for k in range(1, len(items) + 1):
    for combo in combinations(items, k):
        freq = count_frequency(combo)
        print(combo, ":", freq)
        
        if freq >= min_support:
            count_combination_freq[combo] = freq

print("\nFrequent Itemsets (support >= min_support):")
for combo in count_combination_freq:
    if count_combination_freq[combo] == 1:
        print(f"{combo} was bought {count_combination_freq[combo]} time")
    else:
        print(f"{combo} were bought {count_combination_freq[combo]} times")
        
print("\nShopping pattern rules/ Association rules:")
for itemset in count_combination_freq:
    if len(itemset) >= 2:
        for k in range(1, len(itemset)):
            for left in combinations(itemset, k):
                right = tuple(sorted(set(itemset) - set(left)))
                if left in count_combination_freq and right in count_combination_freq:
                    confidence = count_combination_freq[itemset] / count_combination_freq[left]
                    if confidence >= min_confidence:
                        print(left, "--->", right, ":", confidence)
