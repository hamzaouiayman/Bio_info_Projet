from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO
import numpy as np

aln = AlignIO.read("../DATA/simulation/01/merge_file_alignement.aln", "clustal")
print(aln)
labels = np.array([ALN.id for ALN in aln])

np.save('../DATA/simulation/01/labels.array',labels)

calculator = DistanceCalculator('identity')
dm = calculator.get_distance(aln)
print(dm)
distance_graph = np.array([lign for lign in dm])

np.save('../DATA/simulation/01/identity_distance_graph1.array',distance_graph)