import markov_clustering as mc
import numpy as np
import time

labels = np.load("../DATA/simulation30/1/labels.array.npy")
distance_matrix = np.load("../DATA/simulation30/1/identity_distance_graph.array.npy") 

distance_matrix = (distance_matrix <0.3).astype(int)

file = open("../DATA/Resultat/MCL30.txt","w") 
 


start = time.time()
#for inflation in [i / 10 for i in range(20, 35)]:
result = mc.run_mcl(distance_matrix, inflation=3)
clusters = mc.get_clusters(result)
end = time.time()

file.write("temps d'execution: %f \n" %(end-start)) 
file.write("nombre de cluster: %d \n" %len(clusters))

for i,cl in enumerate(clusters):
	file.write("[%d] : "%i)
	for j in cl:
		file.write("%s,"%labels[j])
	file.write("\n\n")
