FILENAME = "contact.txt"
# une fonction qui permet d'afficher les contacts
def Afficher_Contact(contacts):
    if not contacts:
        return
    print(f"vos {len(contacts)} contacts:")
    for i,(nom,telephone) in enumerate(contacts):
        print(f"{i+1}.{nom} - {telephone}")
#sauvegarde de contacts
def sauvegarder_contact(contacts):
    with open(FILENAME,"w") as fichier:
        for nom,telephone in contacts:
            fichier.write(f"{nom};{telephone}")

        print(f"{len(contacts)} contacts sauvegarde")


#chargement de contacts
def charger_contact():
    contacts = []
    try:
        with open(FILENAME, "r",encoding="utf-8") as fichier:
            for line in fichier:
                line = line.strip()
                if line:
                    nom,telephone, *reste = line.split(";")
                    contacts.append([nom,telephone])
            print(f"{len(contacts)} contacts charge")

    except FileNotFoundError:
        print("Nouveau fichier de contacts")

    return contacts
#creation de contact

def Ajouter_contact(contacts):
    print("Ajouter un contact : ")
    nom = input("Nom : ").strip()
    telephone = input("Telephone : ").strip()
    if nom and  telephone:
        contacts.append([nom,telephone])
        print(f"{nom} a  ete ajouter")
    else:
        print("Nom et Telephone obligatoire")

def menu():
    contacts = charger_contact()
    print("======Gestionnaire de Contacts======")
    while True:
        print("\n1. Voir les contacts ")
        print("2. Ajouter un contact ")
        print("3. Sauver un contact")

        choix = int(input("Votre choix :"))
        if choix == 1:
            Afficher_Contact(contacts)
        elif choix == 2:
            Ajouter_contact(contacts)
        elif choix == 3:
            sauvegarder_contact(contacts)
            print("Au revoir !!")
            break
        else:
            print("choix invalide")


print("Gestionnaire de contact")



menu()