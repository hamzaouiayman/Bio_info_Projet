from Bio import SeqIO
#for record in SeqIO.parse("../DATA/simulation/01/alignment_1.fas", "fasta"):
#    print(record)

#for record in SeqIO.parse("../DATA/simulation/01/alignment_1_TRUE.phy", "phylip"):
#    print(record)

from Bio import Phylo
tree = Phylo.read("../DATA/simulation/01/g_trees2.trees", "newick")
Phylo.draw_ascii(tree)