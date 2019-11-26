from sklearn.cluster import KMeans
import numpy as np

labels = np.load("../DATA/simulation/01/labels.array.npy")
distance_matrix = np.load("../DATA/simulation/01/distance_graph1.array.npy")

kmeans = KMeans(n_clusters=3, random_state=0).fit(distance_matrix)

for i in range(len(labels)):
	print(labels[i],':',kmeans.labels_[i])
