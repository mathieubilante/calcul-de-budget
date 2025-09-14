  #Première partie
liste = []
def dimensions():
    long = float(input("\nEntrer la longueur(mètre) de la dalle: "))
    liste.append(long)
    larg = float(input("\nEntrer la largeur(mètre) de la dalle: "))
    liste.append(larg)
    haut = float(input("\nEntrer la hauteur(mètre) de la dalle: "))
    liste.append(haut)

    return  liste

#Deuxième partie
print("\nCALCUL DU VOLUME DE BETON NECESSAIRE POUR UNE DALLE")
dimensions()

vol = 1
for i in liste:
 vol *= i

print(f"\nLe volume nécessaire pour une dalle de {liste[0]} mètre(s) longuer, {liste[1]} mètre(s) de largeur et {liste[2]} mètre(s) de hauteur vaut: {vol} mètre cube")

#Troisième partie
prix = 100 * vol
print(f"\nLe coût total de votre projet vaut {prix} Euro")







































