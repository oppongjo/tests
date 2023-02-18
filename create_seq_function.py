#!/usr/bin/env python3
# create_seq_function.py
"""Export a list of kmers in FASTA format."""

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


def kmers_to_SeqRecords(kmers):
    """Create SeqRecords for each kmer in list of kmers.

    IDs will be seq1, seq2, ..., seqN
    Descriptions will be kmer1, kmer2, ..., kmerN
    Molecule Type will be DNA
    """

    sequences = []

    for count, kmer in enumerate(kmers):
        sequences.append(SeqRecord(Seq(kmer),
                                   id=f"seq{count+1}",  # +1 so numbering starts at 1, not 0
                                   description=f"kmer{count+1}",
                                   annotations={"molecule_type": "DNA"}))
    return(sequences)


if __name__ == "__main__":
    my_sequences = kmers_to_SeqRecords(["AGTACACTGGT", "AGTACACTGGC"])

    # Write the SeqRecords within the list sequences as a fasta file
    SeqIO.write(my_sequences, "kmers.fasta", "fasta")
