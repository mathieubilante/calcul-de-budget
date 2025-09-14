#message de bienvenue
print("=======================================================")
print("Bienvenue dans votrre calcule de budget personnel\n")
print("=======================================================")
print("ETAPE 1 : Vos revenue \n")

#Entrer votre salaire du mois
salaire1= int(input("Entrer votre salaire de revenue  mensuel(FCFA) : " ))
salaire2 = int(input("Entrer votre autrers revenue mensuel(FCFA) :"))

#les depenses
print("*********************************************************")
print("ETAPE 2 : Vos depenses\n")
depenses1= int(input("Veillez entrer le prix du Loyer/Location(FCFA) :\n"))
depenses2= int(input("♥Entrer le prix des depenses de la nouriture et marché(FCFA) :\n"))
depenses3= int(input("Entrer  le prix des depenses du transport(FCFA) :\n"))
depenses4= int(input("Entrer le prix du divertissement(FCFA) :\n"))
depenses5= int(input("Entrer le prix des autres depenses(santé, vetement,...[FCFA]) :\n"))

print("*********************************************************")

#calcul
totaux = salaire1 + salaire2
depenses = depenses1 + depenses2 +depenses3 +depenses4  + depenses5
budget= totaux -depenses
epargne  = (budget*100)/totaux
repar1 = float((depenses1*100)/totaux)
repar2 = float((depenses2*100)/totaux)
repar3 = float((depenses3*100)/totaux)
repar4 = float((depenses4*100)/totaux)
repar5 = float((depenses5*100)/totaux)
budget_jour = budget/30
economie_an = budget*12

#le resumé
print("=======================================================")
print("RESUME DE VOTRE BUDGET")
print("=======================================================")
print("Revenue totaux  :",totaux)
print("Depenses totales :",depenses)
print("Budget restant :",budget)
print("Pourcentage d'épargne :",epargne)

#repartition des depenses
print("*********************************************************")
print("REPARTITION DE VOS DEPENSES")
print("  **********************")
print(f"Loyer       :       {depenses1}({repar1} % du revenu )\n")
print(f"Nouritures  :       {depenses2}({repar2} % du revenu )\n")
print(f"Transport   :       {depenses3}({repar3} % du revenu )\n")
print(f"Loisirs     :       {depenses4}({repar4} % du revenu )\n")
print(f"Autres      :       {depenses5}({repar5} % du revenu )\n")

#CALcul utile
print("CALCUL UTILIES :")
print("=======================================================")
print(f"Budget disponible par jour : {budget_jour} FCFA ")
print(f"Economie potentielles par an  :  {economie_an} FCFA")
if budget < 0 or economie_an < 0:
    print("  Attention : votre budget est négatif, vous dépensez plus que vos revenus !")
