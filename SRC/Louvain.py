import louvain
import igraph
import numpy as np

labels = np.load("../DATA/simulation2/1/labels.array.npy")
distance_matrix = np.load("../DATA/simulation2/1/identity_distance_graph.array.npy")


g = igraph.Graph.Adjacency((distance_matrix < 0.5).tolist())
#g.es['weight'] = distance_matrix[distance_matrix.nonzero()]
print(g)


partition = louvain.find_partition(g, louvain.ModularityVertexPartition)
print(partition)

#louvain = cm.best_partition(distance_matrix)


