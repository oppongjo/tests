from Bio.Seq import Seq
#SeqRecord to create SeqRecord
from Bio.SeqRecord import SeqRecord
#SeqIO to write file
from Bio import SeqIO
#generic_dna from package Alphabet
from Bio.Alphabet import generic_dna
#creating Sequence Record using SeqRecord
my_seq = SeqRecord(Seq("aaaatgggggggggggccccgtt",generic_dna),"#12345","","example 1",)
#printing the Sequence record to verify
print(my_seq)
#writing the the Sequence record to the file using SeqIO modules write() method
SeqIO.write(my_seq, "BioPython_seq.gb", "genbank")
