# Exercice 1
class MaClasse:
    def __init__(self):
        self.x = 23
        self.y = self.x + 5

    def affiche(self):
        print(f"x = {self.x}, y = {self.y}")

class Personne:
    def __init__(self, nom, prenom, adresse, age):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.age = age

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def setAge(self, age):
        self.age = age

    def setAdresse(self, adresse):
        self.adresse = adresse

    def affiche(self):
        print(f"Nom: {self.nom}, Prénom: {self.prenom}, Adresse: {self.adresse}, Âge: {self.age}")

class Voiture:
    def __init__(self, marque, modele, couleur, kilometrage):
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.kilometrage = kilometrage

    def setMarque(self, marque):
        self.marque = marque

    def setModele(self, modele):
        self.modele = modele

    def setCouleur(self, couleur):
        self.couleur = couleur

    def setKilometrage(self, kilometrage):
        self.kilometrage = kilometrage

    def affiche(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Couleur: {self.couleur}, Kilométrage: {self.kilometrage}")

# Exercice 2
class Maison:
    def __init__(self):
        self.adresse = ""
        self.nbrEtage = 0
        self.couleur = ""
        self.surface = 0.0

    def setAdresse(self, adresse):
        self.adresse = adresse

    def setNbrEtage(self, nbrEtage):
        self.nbrEtage = nbrEtage

    def setCouleur(self, couleur):
        self.couleur = couleur

    def setSurface(self, surface):
        self.surface = surface

    def affiche(self):
        print(f"Adresse: {self.adresse}, Nombre d'étages: {self.nbrEtage}, Couleur: {self.couleur}, Surface: {self.surface}")

# Exercice 3
class Forme:
    def __init__(self, nom):
        self.nom = nom

    def surface(self):
        pass

    def perimetre(self):
        pass

    def afficher_details(self):
        print(f"Forme: {self.nom}, Surface: {self.surface()}, Périmètre: {self.perimetre()}")

class Carre(Forme):
    def __init__(self, cote):
        super().__init__("Carré")
        self.cote = cote

    def surface(self):
        return self.cote ** 2

    def perimetre(self):
        return 4 * self.cote

class Rectangle(Forme):
    def __init__(self, largeur, longueur):
        super().__init__("Rectangle")
        self.largeur = largeur
        self.longueur = longueur

    def surface(self):
        return self.largeur * self.longueur

    def perimetre(self):
        return 2 * (self.largeur + self.longueur)

class Cercle(Forme):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def surface(self):
        return 3.14 * self.rayon ** 2

    def perimetre(self):
        return 2 * 3.14 * self.rayon

# Exercice 4
class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def afficher_details(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}")

    def se_deplacer(self):
        pass

class Avion(Vehicule):
    def __init__(self, marque, modele, ailes, nbrRoues):
        super().__init__(marque, modele)
        self.ailes = ailes
        self.nbrRoues = nbrRoues

    def se_deplacer(self):
        print("L'avion vole.")

class VoitureVehicule(Vehicule):
    def __init__(self, marque, modele, annee, nbrRoues):
        super().__init__(marque, modele)
        self.annee = annee
        self.nbrRoues = nbrRoues

    def se_deplacer(self):
        print("La voiture roule.")

class Velo(Vehicule):
    def __init__(self, marque, modele, nbrRoues):
        super().__init__(marque, modele)
        self.nbrRoues = nbrRoues

    def se_deplacer(self):
        print("Le vélo roule.")

# Test des exercices
print("=== Exercice 1 ===")
obj = MaClasse()
obj.affiche()

pers = Personne("Maryame", "Naciri", "Sale", 18)
pers.affiche()

car = Voiture("Toyota", "Corolla", "Rouge", 10000)
car.affiche()

print("\n=== Exercice 2 ===")
maison = Maison()
maison.setAdresse("Sale")
maison.setNbrEtage(2)
maison.setCouleur("Blanc")
maison.setSurface(120.5)
maison.affiche()

print("\n=== Exercice 3 ===")
c1 = Carre(4)
r1 = Rectangle(3, 6)
ce1 = Cercle(5)
c1.afficher_details()
r1.afficher_details()
ce1.afficher_details()

print("\n=== Exercice 4 ===")
v1 = Avion("Boeing", "747", 2, 12)
v2 = VoitureVehicule("Toyota", "Corolla", 2020, 4)
v3 = Velo("Giant", "Escape", 2)

v1.se_deplacer()
v2.se_deplacer()
v3.se_deplacer()

