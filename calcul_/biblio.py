
# 1. Fonction pour remplir les données dans livres.txt
def remplir_livres():
    n = int(input("Combien de livres à enregistrer ? "))
    with open("livres.txt", "w") as f:
        for _ in range(n):
            isbn = input("ISBN : ")
            titre = input("Titre : ")
            auteur = input("Auteur : ")
            annee = int(input("Année de publication : "))
            statut = input("Statut (disponible, emprunté, réservé) : ").lower()
            ligne = f"{isbn};{titre};{auteur};{annee};{statut}\n"
            f.write(ligne)

# 2. Fonction pour lister les livres disponibles
def livres_disponibles():
    print(" Livres disponibles :")
    with open("livres.txt", "r") as f:
        for ligne in f:
            if "disponible" in ligne:
                print(ligne.strip())

# 3. Fonction pour enregistrer les livres empruntés dans un fichier
def enregistrer_empruntes():
    with open("livres.txt", "r") as f, open("empruntes.txt", "w") as out:
        for ligne in f:
            if "emprunté" in ligne:
                out.write(ligne)

# 4. Statistiques : pourcentage de livres disponibles
def statistiques_livres():
    total = dispo = 0
    with open("livres.txt", "r") as f:
        for ligne in f:
            total += 1
            if "disponible" in ligne:
                dispo += 1
    if total == 0:
        print("Aucun livre enregistré.")
    else:
        pourcentage = (dispo / total) * 100
        print(f"📈 {pourcentage:.2f}% des livres sont disponibles.")

# 5. Supprimer les livres publiés avant 2000
def supprimer_anciens_livres():
    with open("livres.txt", "r") as f:
        lignes = [ligne for ligne in f if int(ligne.strip().split(";")[3]) >= 2000]
    with open("livres.txt", "w") as f:
        f.writelines(lignes)
    print("📁 Livres publiés avant 2000 supprimés.")
