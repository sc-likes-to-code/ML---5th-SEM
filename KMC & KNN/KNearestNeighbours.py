import math
from collections import Counter

def distance(point1, point2):
    total = 0
    for i in range(len(point1)):
        total += (point1[i] - point2[i]) ** 2
    return math.sqrt(total)

def knn(train_data, train_labels, test_point, k=3):
    # Store distances (point, distance)
    distances = []
    for i in range(len(train_data)):
        d = distance(test_point, train_data[i])
        distances.append((d, train_labels[i]))

    # Sort by distance (smallest first)
    distances.sort(key=lambda x: x[0])

    # Pick the first k neighbors
    neighbors = [label for (_, label) in distances[:k]]

    # Return the most common class
    prediction = Counter(neighbors).most_common(1)[0][0]
    return prediction

train_data = [
    [1, 2], [2, 3], [3, 1],   # Class 0
    [6, 5], [7, 7], [8, 6]    # Class 1
]
train_labels = [0, 0, 0, 1, 1, 1]  # Corresponding labels

test_point = [5, 5]
prediction = knn(train_data, train_labels, test_point, k=3)
print("Test Point:", test_point, "=> Predicted Class:", prediction)

test_points = [[2, 2], [6, 6], [4, 4], [7, 5]]
for pt in test_points:
    pred = knn(train_data, train_labels, pt, k=3)
    print("Test Point:", pt, "=> Predicted Class:", pred)
