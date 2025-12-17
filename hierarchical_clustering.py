import math

def distance(p1, p2):
    total = 0
    for i in range(len(p1)):
        total += (p1[i] - p2[i]) ** 2
    return math.sqrt(total)

def cluster_distance(c1, c2, linkage):
    distances = []
    for p1 in c1:
        for p2 in c2:
            distances.append(distance(p1, p2))
    if linkage == 'single':
        return min(distances)
    elif linkage == 'complete':
        return max(distances)
    
def hierarchical_clustering(data, linkage):
    clusters = [[p] for p in data]
    step = 1
    while (len(clusters) > 1):
        min_dist = float('inf')
        merge_a, merge_b = 0, 0
        
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                d = cluster_distance(clusters[i], clusters[j], linkage)
                if d < min_dist:
                    min_dist = d
                    merge_a, merge_b = i, j
        
        new_cluster = clusters[merge_a] + clusters[merge_b]
        print(f"Step{step} : Merging {clusters[merge_a]} and {clusters[merge_b]} ---> Distance = {round(min_dist, 2)}")
        step += 1
        
        clusters.pop(max(merge_a, merge_b))
        clusters.pop(min(merge_a, merge_b))
        clusters.append(new_cluster)
        
    print("\nFinal cluster: ", clusters[0])
    
data =[[1, 2], [2, 3], [5, 8], [6, 9], [3, 2]]

print("SINGLE LINKAGE")
hierarchical_clustering(data, 'single')
print("\nCOMPLETE LINKAGE")
hierarchical_clustering(data, "complete")
