#!/bin/bash

# This is the clustalAlign.sh script that prepares a command to run clustal omega with the given parameters.

# The input file is specified as apoe_aa.fasta and the output file as apoe_alignment.fasta
# We are using default settings for all other parameters

clustalo -i apoe_aa.fasta -o apoe_alignment.fasta --force