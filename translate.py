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

my_seq = Seq("AGTACACTGGTA", IUPAC.protein)

My_seq_rec = SeqRecord(my_seq)
SeqIO.write(my_seq, "protein.fasta", "fasta")
