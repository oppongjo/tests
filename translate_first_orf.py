#!/usr/bin/env python3
# translate_first_orf
"""this is a code for processing DNA and RNA sequence in A FASTA file."""

    
"""The script uses Bio.Seq object to process the sequence in the file."""

import argparse
import re 
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord 
from Bio import SeqIO


def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="The script's main block gets the command-line arguments using argparse.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # get the FASTA file of sequences
    parser.add_argument('filename',  # variable to access this data later: args.filename
                        metavar='FASTA', # shorthand to represent the input value
                        help='Provide name and path to FASTA file to process.', # message to the user, it goes into the help menu
                        type=str)
    parser.add_argument('-p', '--pattern',  # access with args.pattern
                        help='Provide a regex pattern for filtering FASTA entries',
                        default='^\d{1}\D*$')  # default works for Drosophila chromosomes

    return(parser.parse_args())


def find_first_orf(rna):
    """Return first open-reading frame of RNA sequence as a Bio.Seq object."""

    rna = 'GGUCCGGGAUGCCUGAAUGGUACACUGGUAAGUACACUGUAAGUAAAAAAAA'
    orf = re.search('AUG([AUGC]{3})+(UAA|UAG|UGA)', rna).group() 
    
    try:
        """update regex to find the ORF"""
        orf = re.search('AUG([AUGC]{3})+(UAA|UAG|UGA)', str(rna)).group()
    except AttributeError:  # if no match found, orf should be empty
        orf = ""
    return(Seq(orf))


def translate_first_orf(dna):
    """ this function takes a DNA sequence as a Bio.Seq object and transcribes it into RNA """
    """ find_first_orf to find the first ORF in the RNA sequences"""
    """ translates the ORF into a protein sequence using translate() method"""

    dna = Seq("GGTCCGGGATGCCTGAATGGTACACTGGTAAGTACACTGTAAGTAAAAAAAA")
    rna = dna.transcribe() 
    orf = re.search('AUG([AUGC]{3})+(UAA|UAG|UGA)', rna).group()
    protein = rna.translate() 

    return(translated_orf)


if __name__ == "__main__":
    args = get_args()

    for record in SeqIO.parse(filename, "FASTA"):
        if re.match(r "^\d{1}\D*$", record.id):
            print (record.id   protein)

