#!/usr/bin/env python3
# translate.py
# Import Seq
from Bio.Seq import Seq
from BioAlphabet import IUPAC 
from Bio.SeqRecord import SeqRecord
dna = Seq("AGTACACTGGTA")
rna = dna.transcribe()
protein = rna.translate()
print(protein)

my_seq = seq("AGTACACTGGTA", IUPAC_dna)
my_seq_r = SeqRecord(my_Seq, id = "#12345",description = "example 1")


SeqIO.write(my_seq_r, "translate.fasta", "fasta")
