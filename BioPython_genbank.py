from Bio import Entrez

Entrez.email = oppong.jo@northeastern.edu

from Bio import SeqIO

id_list = ["515056", "J01673.1"]
handle = Entrez.efetch(
        db = "nucleotide",
        rettype = "gb",
        retmode = "text",
        id = "515056")
record = SeqIO.read(handle, "gb")
handle.close()
print(record.seq)
print(record.features[0])