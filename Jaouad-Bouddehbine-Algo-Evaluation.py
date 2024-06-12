

################# Algo – Evaluation ##############################
# Les exercices 1 à 6 sont à réaliser :
#  En pseudo langage
#  Et en Python
# Les exercices 7 et 8 sont à réaliser en Python uniquement

################## 1 - Somme et moyenne ############################
####### Pseudo langage #######

#   Afficher "Somme et moyenne"
#   Demander N1 en tant qu'entier
#   Demander N2 en tant qu'entier
#   Demander N3 en tant qu'entier

#   Définir somme comme N1 + N2 + N3
#   Afficher "Somme =", somme

#   Définir moyenne comme somme / 3
#   Afficher "Moyenne =", moyenne

####### Python #######
print("Somme et moyenne")
N1 = int(input("Entrer un nombre: "))
N2 = int(input("Entrer un nombre: "))
N3 = int(input("Entrer un nombre: "))

somme = N1 + N2 + N3
print("Somme =", somme)

moyenne = somme / 3
print("Moyenne =",round(moyenne,2))

################## 2 - Elections ############################
####### Pseudo langage #######
#   Afficher("Élections")
#   PrVotesObtenu = LireFlottant("Entrer le pourcentage de votes obtenus")
#   Si PrVotesObtenu < 5 Alors
#       Afficher("Candidat éliminé")
#   Sinon si PrVotesObtenu < 50 Alors
#       Afficher("Candidat qualifié pour le second tour")
#   Sinon
#       Afficher("Candidat élu")
#   Fin

####### Python #######
print("Elections")
PrVotesObtenu = float(input("Entrer le pourcentage de votes obtenus: "))
if PrVotesObtenu < 5:
    print("Candidat elimine")
elif PrVotesObtenu < 50:
    print("candidat qualifie pour le second tour")
else:
    print("Candidat elu")


################## 3 – Pair ou impair ############################
####### Pseudo langage 'pour...fin pour #######
#   TAAB1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   afficher("Tableau", TAAB1)

#   pour chaque élément i dans la plage de 0 à 9:
#       si TAAB1[i] est divisible par 2:
#           afficher TAAB1[i], "est pair"
#       sinon:
#           afficher TAAB1[i], "est impair"


####### Python 'pour...fin pour #######

TAAB1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Tableau", TAAB1)

for i in range(10):
    if TAAB1[i] % 2 == 0:
        print(TAAB1[i], "est pair")
    else:
        print(TAAB1[i], "est impair")

####### Pseudo langage Tant que ... fin tant que #######
#  TAAB2 = [86, 2, 99, 74, 5, 6, 33, 8, 9, 27]`
# Afficher le tableau TAAB2

#i = 0
#Tant que le i est inférieur à la longueur du tableau TAAB2:
#   faire une vérification (ou un test) pour voir si la valeur actuelle dans le tableau TAAB2 est pair 
#       si la réponse est affirmative, alors
#           Afficher("La valeur", i, "est pair")`
#       sinon (c'est-à-dire que la valeur est impair), alors
#           imprimer("La valeur", i, "est impair")`

#   incrémente le i de 1 (pour aller à la prochaine valeur du tableau)



####### Python Tant que ... fin tant que #######

TAAB2 = [86, 2, 99, 74, 5, 6, 33, 8, 9, 27]
print("Tableau", TAAB2)

i = 0
while i < len(TAAB2):
    if TAAB2[i] % 2 == 0:
        print(TAAB2[i], "est pair")
    else:
        print(TAAB2[i], "est impair")
    i += 1


################## 4 - Notes ############################
####### Pseudo langage #######
#Notes = [6.5, 15, 7, 10, 18, 5.5, 11, 9, 13, 14]`
#Afficher les notes obtenues par les étudiants

#compteur des étudiants avec la moyenne = 0

#Pour chaque note qui fait partie de la liste "Notes":`
#    `faire une vérification (ou un test) pour voir si la valeur actuelle de "note" est supérieure ou égale à 10
#        `si la note est supérieure ou égale à 10, alors`
#            `augmenter le compteur des étudiants avec la moyenne de 1
# Afficher Le nombre d'étudiants qui ont obtenu une moyenne de 10 ou plus.

####### Python #######

Notes = [6.5, 15, 7, 10, 18, 5.5, 11, 9, 13, 14]
print("Notes:", Notes)

count = 0  

for note in Notes:
    if note >= 10:
        count += 1

print("le nombre d'etudiants avec la moyenne est de: ", count)
    

################## 5 – Le plus grand, le plus petit ############################
####### Pseudo langage #######
#TAAB3 = [87, 2, 96, 74, 5, 6, 34, 8, 9, 21]`
#imprimer("Afficher le tableau TAAB3:", TAAB3)`

#G (le plus grand) = valeur initiale du premier élément du tableau TAAB3`
#P (le plus petit) = valeur initiale du premier élément du tableau TAAB3`

#Pour chaque valeur (appelée "i" dans ce code) qui fait partie de la plage 1 à la longueur du tableau TAAB3:`
#   faire une vérification (ou un test) pour voir si la valeur actuelle est supérieure à G (le plus grand)`
#       si la réponse est affirmative, alors`
#           mettre à jour la valeur de G par la valeur actuelle`
#
#   faire une nouvelle vérification pour voir si la valeur actuelle est inférieure à P (le plus petit)`
#       si la réponse est affirmative, alors`
#           mettre à jour la valeur de P par la valeur actuelle`
#
#imprimer("Le plus grand élément du tableau est", G)`
#
#imprimer("Le plus petit élément du tableau est", P)`


####### Python #######

TAAB3 = [87, 2, 96, 74, 5, 6, 34, 8, 9, 21]
print("Tableau", TAAB3)

G = TAAB3[0]
P = TAAB3[0]

for i in range(1, len(TAAB3)):
    if TAAB3[i] > G:
        G = TAAB3[i]
    if TAAB3[i] < P:
        P = TAAB3[i]

print("Le plus grand est", G)
print("Le plus petit est", P)



################## 6 - Présence dans un tableau ############################
####### Pseudo langage #######

# pour chaque valeur dans le tableau
# si la valeur est égale à N
# alors incrémenter Nf de 1
# afficher le nombre de fois que N apparait dans le tableau

####### Python #######

TAAB4 = [1, 2, 3, 4, 2, 6, 2, 8, 2, 10]
print("Tableau", TAAB4)

N = int(input("Entrer un nombre: "))
Nf = 0
for NF in TAAB4:
    if NF == N: 
        Nf += 1
print("Le nombre", N, "apparait", Nf, "fois")


##################  Bubble sort algorithm ############################

Dancers = [99, 37, 34, 86, 1, 7, 2, 87, 3, 55]
print("debut de la dance :", Dancers)

n = len(Dancers)
for i in range(n):
    for j in range(0, n-i-1):
        if Dancers[j] > Dancers[j+1]:
            Dancers[j], Dancers[j+1] = Dancers[j+1], Dancers[j]
print("dance terminee :", Dancers)


##################  Calculator ############################
print("Calculator")

result = None

while True:
    if result is None:
        a = input("Enter a (or type 'end' to exit): ")
        if a.lower() == 'end':
            break
        result = int(a)
    
    cal = input("Enter operation (or type 'end' to exit): ")
    if cal.lower() == 'end':
        break
    
    b = input("Enter a number (or type 'end' to exit): ")
    if b.lower() == 'end':
        break
    b = int(b)
    
    if cal == "+":
        result += b
    elif cal == "-":
        result -= b
    elif cal == "*":
        result *= b
    elif cal == "/":
        result /= b
    else:
        print("Invalid operation")
        continue
    
    print(f"Result: {result}")


##################  Fin  ############################
