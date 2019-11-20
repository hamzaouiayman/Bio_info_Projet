from Bio import SeqIO

from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO

align = AlignIO.read("../DATA/simulation/01/merge_file_alignement.aln", "clustal")
print([id_.id for id_ in align])
# aln = AlignIO.read(open("../DATA/simulation/01/alignment_1_Test.phy"), "phylip")
# print(aln)

# calculator = DistanceCalculator('blosum62')
# dm = calculator.get_distance(aln)
# print(dm)

# print(dm)

# matr = [k for  k in dm]

# print(matr)

#for record in SeqIO.parse("../DATA/simulation/01/alignment_1_TRUE.phy", "phylip"):
#    print(record)

#from Bio import Phylo
#tree = Phylo.read("../DATA/simulation/01/g_trees2.trees", "newick")
#Phylo.draw_ascii(tree)