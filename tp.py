# exercice 1
print("bonjour")
###############


# exercice 2
a=float(input("entrez le premier nombre:"))
b=float(input("entrez le deuxieme nombre:"))
print ("le produit des deux nombres est:",a * b)
##################################


# Exercice 3
a = int(input("Entrez le premier entier (A) : "))
b = int(input("Entrez le deuxième entier (B) : "))
a, b = b, a
print("Après échange : A =", a, ", B =", b)
###########################


# Exercice 4
n = int(input("Entrez un nombre entier : "))
if n % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")


#exercice 5
a = int(input("Entrez le premier entier : "))
b = int(input("Entrez le deuxième entier : "))
c = int(input("Entrez le troisième entier : "))
print("Le plus grand nombre est :", max(a,b,c))
############################


#exercice 6
note = float(input("Entrez une note (entre 0 et 20) : "))
if 0 <= note <= 20:
    if note >= 10:
        print("Validé")
    else:
        print("Non validé")
else:
    print("Note invalide, veuillez entrer une note entre 0 et 20.")
    ###########################################
    # Exercice 7
a= float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))
produit = a * b
if produit > 0:
    print("Le produit est positif.")
elif produit < 0:
    print("Le produit est négatif.")
else:
    print("Le produit est nul.")
    ##############################
    # Exercice 9
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))
c = float(input("Entrez le troisième nombre : "))
moyenne = (a + b + c) / 3
print("La moyenne est :", moyenne)
######################
# Exercice 8
n=int (input("entrez un entier"))

############################











