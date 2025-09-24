import math
from collections import Counter

# Distance function
def distance(p1, p2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

# KNN function
def knn(train_data, test_point, k=3):
    distances = []
    for features, label in train_data:
        d = distance(features, test_point)
        distances.append((d, label))

    # Sort by distance
    distances.sort(key=lambda x: x[0])

    # Pick k nearest neighbors
    k_nearest = distances[:k]

    # Majority vote
    labels = [label for _, label in k_nearest]
    most_common = Counter(labels).most_common(1)[0][0]
    return most_common

def main():
    # Training data (features, label)
    train_data = [
        ([1, 2], "ClassA"),
        ([2, 3], "ClassA"),
        ([3, 3], "ClassA"),
        ([6, 8], "ClassB"),
        ([7, 7], "ClassB"),
        ([8, 9], "ClassB")
    ]

    # Test data with some tricky points
    test_data = [
        ([1.5, 2.0], "ClassA"),   # should be ClassA
        ([2.5, 3.0], "ClassA"),   # should be ClassA
        ([7.0, 8.0], "ClassB"),   # should be ClassB
        ([5.0, 5.0], "ClassA"),   # ambiguous → might get misclassified
        ([6.5, 6.5], "ClassA"),   # closer to ClassB cluster → will likely be wrong
    ]

    # Evaluate error rate
    k = 3
    errors = 0
    for features, true_label in test_data:
        pred = knn(train_data, features, k)
        print(f"Point {features} → Predicted: {pred}, Actual: {true_label}")
        if pred != true_label:
            errors += 1

    total = len(test_data)
    error_rate = errors / total

    print("\nTotal Test Points:", total)
    print("Errors:", errors)
    print("Error Rate:", error_rate)
    print("Accuracy:", 1 - error_rate)

if __name__ == "__main__":
    main()
