import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
input_filename = sys.argv[1]
output_filename = sys.argv[2]
with open(output_filename, 'wa') as handle:
    for rec in SeqIO.parse(input_filename, 'fasta'):
        handle.write(SeqRecord(id=rec.id, seq=rec.seq.reverse_complement()).format('fasta'))
