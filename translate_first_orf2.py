#!/usr/bin/env python
"""Translate the first open reading frame (ORF) of RNA sequences in a FASTA file.

The ORF must start with the AUG, end with the UAA, UAG, or UGA, and have an even multiple of three RNA bases between.
"""

import argparse
import re
from Bio import SeqIO
from Bio.Seq import Seq

def find_first_orf(rna):
    """Return first open-reading frame of RNA sequence as a Bio.Seq object.

    Must start with AUG
    Must end with the UAA, UAG, or UGA
    Must have even multiple of 3 RNA bases between
    """
    start_codon = rna.find('AUG')
    if start_codon == -1:
        return Seq("")
    for i in range(start_codon, len(rna), 3):
        codon = rna[i:i+3]
        if codon in ['UAA', 'UAG', 'UGA']:
            return rna[start_codon:i]
    return Seq("")


def translate_first_orf(dna):
    """Return translated first ORF of DNA sequence as a string.

    Assumes input sequences is a Bio.Seq object.
    """
    rna = dna.transcribe()
    orf = find_first_orf(rna)
    if orf:
        protein = orf.translate()
        protein = str(protein).replace("Stop", "*")  # to replace the Stop with *
        return protein
    else:
        return ""


def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filename", metavar="FILE", help="Input FASTA file")
    parser.add_argument("pattern", metavar="PATTERN", help="Pattern for searching in the FASTA file IDs")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    for record in SeqIO.parse(args.filename, "fasta"):
        if re.search(args.pattern, record.id):
            orf = translate_first_orf(record.seq)
            if orf:
                print(record.id, orf + "*", sep='\t')
