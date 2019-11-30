from sklearn.cluster import AgglomerativeClustering
import numpy as np

labels = np.load("../DATA/simulation/01/labels.array.npy")
distance_matrix = np.load("../DATA/simulation/01/distance_graph1.array.npy")

clustering = AgglomerativeClustering(n_clusters=3).fit(distance_matrix)

for i in range(len(labels)):
	print(labels[i],':',clustering.labels_[i])