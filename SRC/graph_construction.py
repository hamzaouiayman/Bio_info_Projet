from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO
import numpy as np

aln = AlignIO.read("../DATA/simulation30/1/merge_file_alignement.phy", "phylip")
print(aln)
labels = np.array([ALN.id for ALN in aln])

np.save('../DATA/simulation30/1/labels.array',labels)

calculator = DistanceCalculator('identity')
dm = calculator.get_distance(aln)
print(dm)
distance_graph = np.array([lign for lign in dm])

np.save('../DATA/simulation30/1/identity_distance_graph.array',distance_graph)