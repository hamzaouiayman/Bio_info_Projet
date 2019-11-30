from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO
import numpy as np

aln = AlignIO.read("../DATA/simulation2/1/merge_alignement.phy", "phylip")
print(aln)
labels = np.array([ALN.id for ALN in aln])

np.save('../DATA/simulation2/1/labels.array',labels)

calculator = DistanceCalculator('identity')
dm = calculator.get_distance(aln)
print(dm)
distance_graph = np.array([lign for lign in dm])

np.save('../DATA/simulation2/1/identity_distance_graph.array',distance_graph)