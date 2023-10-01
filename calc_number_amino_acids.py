""""use input number to calculate the number of amino acids and the estimate molecular weight."""
gene = input("\nEnter Gene Name:")#input gene name here
print('your sequence name is: {}'.format(gene))
nucleotide = int(input("Enter Number of Nucleotides: "))# input the number of nucleotides here
print('The length of DNA sequence is: {}'.format(nucleotide))
if nucleotide % 3 != 0:
    print("The number of nucleotides is not divisible by 3.")# alert user if not divisible by 3
else:
    amino_acids = nucleotide / 3
    molecular_weight = (amino_acids * 110) / 1000
    print('The length of decoded protein is:{}'.format(amino_acids))
    print('The average weight of the protein sequence is: {}'.format(molecular_weight))

