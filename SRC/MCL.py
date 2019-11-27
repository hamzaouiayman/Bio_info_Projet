import markov_clustering as mc
import numpy as np

labels = np.load("../DATA/simulation/01/labels.array.npy")
distance_matrix = np.load("../DATA/simulation/01/identity_distance_graph1.array.npy") 

distance_matrix = (distance_matrix <0.5).astype(int)

for inflation in [i / 10 for i in range(11, 26)]:
    result = mc.run_mcl(distance_matrix, inflation=inflation)
    clusters = mc.get_clusters(result)
    print("inflation:", inflation,"clusters:", len(clusters))


print(clusters)