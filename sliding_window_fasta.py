import re
import sys
from Bio import SeqIO

def sliding_window(k,string):
    '''returns a list of all kmers in a given string'''
    kmers = []
    for start in range(0, len(string) - k + 1):
        kmers.append(string[start : start + k])

    return kmers

def gc_content(seq):
    """Returns [0,1], the fraction of GCs in the input string"""
    seq = seq.lower()
    #Count the gs and cs
    gc = 0
    for nucleotide in seq:
        if nucleotide in ["g","c"]:
            gc+=1

    return gc / float(len(seq))

def main():
    arg_counts = len(sys.argv)-1
    if arg_counts < 2:
        raise Exception("This script takes at least 2 arguments, a kmer length and a fasta file")

    for record in SeqIO.parse(sys.argv[2], "fasta"):
        print(">{}".format(record.description))
        for kmer in sliding_window(int(sys.argv[1]), record.seq):
            print("{}\t{:.2f}".format(kmer, gc_content(kmer)))

if __name__=="__main__":
    main()