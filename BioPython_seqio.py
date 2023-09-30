import sys
from Bio import SeqIO

def reverse_complement(seq):
  """Returns the reverse complement of a sequence."""
  complement_map = {"A": "T", "T": "A", "G": "C", "C": "G"}
  reversed_complement = ""
  for base in seq[::-1]:
    reversed_complement += complement_map[base]
  return reversed_complement


  def main():
  """Takes two arguments from the command line:
    * The name of the original multi-sequence FASTA file.
    * The desired name of the new multi-sequence FASTA file.
  """
  
  input_fasta_file = sys.argv[1]
  output_fasta_file = sys.argv[2]

  # Read the multi-sequence FASTA file.
  input_records = SeqIO.parse(input_fasta_file, "fasta")

  # Reverse the complements of the sequences.
  output_records = []
  for record in input_records:
    output_record = record.copy()
    output_record.seq = reverse_complement(record.seq)
    output_records.append(output_record)

  # Output the new multi-sequence FASTA file.
  SeqIO.write(output_records, output_fasta_file, "fasta")


if __name__ == "__main__":
  main()