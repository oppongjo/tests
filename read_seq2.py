#!/usr/bin/env python3
# read_seq2.py
from Bio import SeqIO
import re

for record in SeqIO.parse("/work/courses/BINF6308/data_BINF6308/Module4/dmel-all-chromosome-r6.17.fasta", "fasta"):
    if re.match("^\d{1}\D*$", record.id):
        print(record.id)
 