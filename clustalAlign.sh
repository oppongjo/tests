from Bio import SeqIO
from Bio.Seq import Seq

clustalo_cline = ClustalOmegaCommandline(infile=apoe_aa.fasta, outfile="aligned_sequences.fasta", verbose=True, auto=True)
stdout, stderr = clustalo_cline()

print("alignment complete.")
