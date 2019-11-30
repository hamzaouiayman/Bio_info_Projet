from sklearn.cluster import KMeans
import numpy as np

labels = np.load("../DATA/simulation2/1/labels.array.npy")
distance_matrix = np.load("../DATA/simulation2/1/identity_distance_graph.array.npy")

kmeans = KMeans(n_clusters=15, random_state=0).fit(distance_matrix)

for i in range(len(labels)):
	print(labels[i],':',kmeans.labels_[i])
