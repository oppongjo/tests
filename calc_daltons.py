"""Calculate the estimated molecular weight of the protein and write the results on the screen"""
num_of_aminoacids_per_protein = 671
molecular_weight_of_amino_acid_in_daltons = 110
molecular_weight_of_protein_in_daltons = (num_of_aminoacids_per_protein)*(molecular_weight_of_amino_acid_in_daltons)
molecular_weight_of_protein_in_kilodaltons = (molecular_weight_of_protein_in_daltons)/1000
print('\nThe length of "protein Kinase C beta type" is : {}'.format(num_of_aminoacids_per_protein))

print('The average weight in kilodaltons is : {}'.format(molecular_weight_of_protein_in_kilodaltons))
