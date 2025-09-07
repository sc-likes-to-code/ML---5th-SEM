import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

# read csv
df = pd.read_csv("E:\\5th SEM CODING\\ML\\ASS 2_Gini Index\\data.csv")
print(df)

# Map categorical values
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# Features and target
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']
#X -> feature matrix
#y -> target column

# Train Decision Tree
dtree = DecisionTreeClassifier()
dtree.fit(X, y)

# plot
plt.figure(figsize=(10, 6))
tree.plot_tree(dtree, feature_names=features, filled=True)
plt.show()
