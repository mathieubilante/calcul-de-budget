from collections import Counter
import string
def analyser_texte(texte):
    texte = texte.lower()
    for ponct in string.punctuation:
        texte = texte.replace(ponct, '')
    mots = texte.split()
    nombre_mots = len(mots)
    frequence = Counter(mots)
    mot_plus_frequent = frequence.most_common(1)[0][0] if frequence else None
    return nombre_mots, mot_plus_frequent, dict(frequence)
texte_utilisateur = input("Veuillez entrer un texte : ")
nb_mots, mot_freq, freqs = analyser_texte(texte_utilisateur)
print("\n--- Résultats de l'analyse ---")
print("Nombre total de mots :", nb_mots)
print("Mot le plus fréquent :", mot_freq)
print("Fréquence de chaque mot :")
for mot, freq in freqs.items():
    print(f"  {mot} : {freq}")
