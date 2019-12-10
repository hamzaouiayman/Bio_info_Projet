import numpy as np 

labels = np.load("../DATA/simulation15/1/labels.array.npy")
file = open("../DATA/simulation15/1/labels2.txt","w")

for i,l in enumerate(labels):
	file.write("%d " %i)
	file.write(": %s \n"%l)