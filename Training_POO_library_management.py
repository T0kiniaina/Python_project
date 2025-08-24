class Livre:
    def __init__(self, titre : str, auteur : str, annee : int, disponible : bool = True):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = disponible

    def emprunter(self):
        if self.titre:
            if self.disponible:
                self.disponible = False
                print(f"Vous avez emprunté le livre {self.titre}")
            else:
                print(f"Le livre {self.titre} n'est pas disponible")

    def retourner(self):
        if self.titre:
            if not self.disponible:
                self.disponible = True
                print(f"Vous avez retourné le livre {self.titre}")
            else:
                print(f"Le livre {self.titre} est déjà disponible")
    
class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Le livre {livre.titre} a été ajouté à la bibliothèque")
    
    def afficher_livres(self):
        for livre in self.livres:
            disponibilite = "Disponible" if livre.disponible else "Emprunté"
            print(f"Titre: {livre.titre}, Auteur: {livre.auteur}, Année: {livre.annee}, Statut: {disponibilite}")

def main():
    bibliotheque = Bibliotheque()

    livre1 = Livre("1984", "George Orwell", 1949)
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
    livre3 = Livre("Moby Dick", "Herman Melville", 1851)

    bibliotheque.ajouter_livre(livre1)
    bibliotheque.ajouter_livre(livre2)
    bibliotheque.ajouter_livre(livre3)

    bibliotheque.afficher_livres()
    livre1.emprunter()

if __name__ == "__main__":
    main()