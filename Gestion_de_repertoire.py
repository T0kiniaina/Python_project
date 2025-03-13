import sys
from pathlib import Path
import json

# Initialisation des contenus du contact
class Contact:
    def __init__(self, nom, telephone, email):
        self.nom = nom
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return f"Nom: {self.nom}, Numéro téléphone: {self.telephone}, Adresse email: {self.email}"

    def to_dict(self):
        return {
            "Nom": self.nom,
            "Numéro téléphone": self.telephone,
            "Adresse email": self.email
        }

# Création des méthodes appliquées à la classe Contact
class Carnet_adresse:
    def __init__(self):
        self.contacts = []
        self.path = input("Entrez le chemin de fichier :\n")
        self.path = Path(self.path)
        self.json_file = self.path / "contact.json"
        self.json_file.touch(exist_ok=True)
        if self.json_file.stat().st_size == 0:
            with open(self.json_file, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)

    def Ajouter(self):
        print("Veuillez saisir les informations du contact !")
        nom = input("Nom : ")

        while True:
            numero = input("Numero : ")
            if not numero.isdigit() or len(numero) != 10:
                print("Le numero doit être 10 chiffres. Reessayez !")
            else:
                break

        while True:
            email = input("Email : ")
            if "@" not in email or "." not in email:
                print("Veuillez entrer une adresse email valide")
            else:
                break
        
        new_contact = Contact(nom, numero, email)
        self.contacts.append(new_contact)
        print(f"Contact ajouté : {new_contact}")

    def Sauvegarder(self):
        if self.json_file.exists() and self.json_file.stat().st_size > 0:
            with open(self.json_file, "r", encoding="utf-8") as f:
                existing_contact = json.load(f)
        else:
            existing_contact = []

        contacts_data = [contact.to_dict() for contact in self.contacts]
        existing_contact.extend(contacts_data)

        with open(self.json_file, "w", encoding="utf-8") as f:
            json.dump(existing_contact, f, indent=4, ensure_ascii=False)
        print("Contacts sauvegardés !")
    
    def Afficher(self):
        if self.json_file.exists() and self.json_file.stat().st_size > 0:
            try:
                with open(self.json_file, "r", encoding="utf-8") as f:
                    contacts = json.load(f)
                if contacts:
                    print("Liste des contacts :")
                    for contact in contacts:
                        print(contact)
                else:
                    print("Votre répertoire est vide !")
            except json.JSONDecodeError:
                print("Le fichier JSON est corrompu ou vide.")
        else:
            print("Votre répertoire est vide !")

    def Supprimer(self):
        name = input("Entrez le nom du contact à supprimer : ")
        initial_length = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact.nom != name]

        if len(self.contacts) < initial_length:
            with open(self.json_file, "w", encoding="utf-8") as f:
                json.dump([contact.to_dict() for contact in self.contacts], f, indent=4, ensure_ascii=False)
            print(f"Le contact {name} a été supprimé !")
        else:
            print(f"Le contact {name} n'a pas été trouvé !")

    def Quitter(self):
        print("Fermeture du carnet d'adresses...")
        sys.exit()

if __name__ == "__main__":
    Carnet = Carnet_adresse()
    while True:
        action = int(input("Veuillez entrer l'action à faire :\n(1) Ajouter\n(2) Afficher\n(3) Sauvegarder\n(4) Supprimer\n(5) Quitter\n"))
        if action == 1:
            Carnet.Ajouter()
        elif action == 2:
            Carnet.Afficher()
        elif action == 3:
            Carnet.Sauvegarder()
        elif action == 4:
            Carnet.Supprimer()
        elif action == 5:
            Carnet.Quitter()
        else:
            print("L'action spécifiée est invalide.")
