import louvain
import igraph
import numpy as np
import time

labels = np.load("../DATA/simulation2/1/labels.array.npy")
distance_matrix = np.load("../DATA/simulation2/1/identity_distance_graph.array.npy")


g = igraph.Graph.Adjacency((distance_matrix < 0.5).tolist())
#g.es['weight'] = distance_matrix[distance_matrix.nonzero()]
#print(g)

file = open("../DATA/Resultat/Louvain15.txt","w")

start = time.time()
partition = louvain.find_partition(g, louvain.ModularityVertexPartition)
end = time.time()


file.write("temps d'execution: %f \n" %(end-start)) 
#file.write("nombre de cluster: %d \n" %len(clusters))

file.write(str(partition))




