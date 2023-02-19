#!/usr/bin/env python3
# read_seq2.py
from Bio import SeqIO
import re

infile = "/work/courses/BINF6308/data_BINF6308/Module4/dmel-all-chromosome-r6.17.fasta"

for record in SeqIO.parse(infile, "fasta"):
    if re.match("^\d{1}\D*$", record.id):
        print(record.id)
 