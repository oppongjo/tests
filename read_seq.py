#!/usr/bin/env python3
# read_seq.py
from Bio import SeqIO

infile = "/work/courses/BINF6308/data_BINF6308/Module4/dmel-all-chromosome-r6.17.fasta"

for record in SeqIO.parse(infile, "fasta"):
    print(record.id) 