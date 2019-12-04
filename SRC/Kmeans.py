from sklearn.cluster import KMeans
import numpy as np
import time

labels = np.load("../DATA/simulation2/1/labels.array.npy")
distance_matrix = np.load("../DATA/simulation2/1/identity_distance_graph.array.npy")

file = open("../DATA/Resultat/Kmeans15.txt","w")
nb_cl = 3
start = time.time()
kmeans = KMeans(n_clusters=nb_cl, random_state=0).fit(distance_matrix)

end = time.time()
file.write("temps d'execution: %f \n" %(end-start)) 

for i in range(nb_cl):
	file.write("[%d] : "%i)
	file.write(str(labels[kmeans.labels_==i]))
	file.write("\n")
	#for k in range(len(labels)):
	#	print(labels[i],':',kmeans.labels_[i])
