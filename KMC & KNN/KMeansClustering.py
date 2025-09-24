import random
import math
# Function to calculate Euclidean distance between two points
def distance(point1, point2):
    total = 0
    # Loop through each dimension
    for i in range(len(point1)):
        total += (point1[i] - point2[i]) ** 2
    return math.sqrt(total)

# Function to calculate the mean (centroid) of a cluster
def mean(points):
    n = len(points)           # Number of points in the cluster
    dims = len(points[0])     # Number of dimensions
    result = []
    for i in range(dims):
        s = 0
        for j in range(n):
            s += points[j][i]   # Sum values of the i-th dimension
        result.append(s / n)     # Divide by number of points to get mean
    return result

# K-Means algorithm
def kmeans(data, k, max_iters=100):
    #Randomly select k initial centroids from the data
    centroids = random.sample(data, k)

    #Repeat until it reaches the max_iters
    for x in range(max_iters):
        #Create empty clusters
        clusters = []
        for i in range(k):
            clusters.append([])

        #Assign each point to the nearest centroid
        for point in data:
            distances = []
            for c in centroids:
                d = distance(point, c)
                distances.append(d)
            min_index = distances.index(min(distances))  # Index of nearest centroid
            clusters[min_index].append(point)

        #Recalculate centroids of each cluster
        new_centroids = []
        for cluster in clusters:
            if cluster:  # If cluster is not empty
                new_c = mean(cluster)
            else:        # If cluster is empty, pick a random point as centroid
                new_c = random.choice(data)
            new_centroids.append(new_c)

        # Check if centroids didn't change
        if new_centroids == centroids:
            break

        centroids = new_centroids

    return centroids, clusters

# Example usage
data = [
    [1, 2], [1.5, 1.8], [5, 8],
    [8, 8], [1, 0.6], [9, 11],
    [8, 2], [10, 2], [9, 3]
]
# Run K-Means with k=3 clusters
final_centroids, final_clusters = kmeans(data, k=3)

#Print final centroids
print("Centroids:")
for c in final_centroids:
    print(c)

#Print clusters
print("\nClusters:")
for i, cluster in enumerate(final_clusters):
    print("Cluster", i+1, ":", cluster)
