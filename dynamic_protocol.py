""""use data from the user to dynamically change the results of the program"""
final_vol = int(input('\nenter the final volume of the solution(ml):'))
nacl_stock = int(input('enter the NaCl stock(mM):'))
nacl_final = int(input('enter the NaCl final(mM):'))
mg_stock = int(input('enter the MgCl2 stock(mM):'))
mg_final = float(input('enter the MgCl2 final(mM):'))
x = f"Add {str(final_vol * (nacl_final / nacl_stock))} m1 NaCl\n" #concentration of NaCl
y = f"Add {str(final_vol * (mg_final / mg_stock))} m1 MgCl2\n"
z = f"Add water to a final volume of {str(final_vol)} m1 and mix"
print(x+y+z)