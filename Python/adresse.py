#Section imports
import pickle as saumure
import os.path
import time

###Section constantes
NOMFIC_SAUVE="carnet2.pickle"
QUIT_CONFIRMER="Vous confirmez vouloir quitter (O/N) ?"
INSTRUCTIONS="""
****************************************************************************************
                                    Application carnet d'adresses
****************************************************************************************
Tapez une des 4 touches suivantes :
A pour Ajouter une personne,
L pour Lire la liste des personnes du carnet,
I pour relire ces Instructions,
Q pour Quitter."""
PATRON_LISTE="%s %s || Date de naissance: %s|| Email: %s|| Numero: %s"

###Section classes
class CarnetAdr(object):
    """Conteneur de fiches Methodes: __init__,ajouter_fiche(),sauver()"""
    def __init__(self):
        """Crée l'attribut gens comme liste vide"""
        self.gens = []

    def ajouter_fiche(self, fiche_nouvo):
        """Ajoute une fiche dans gens"""
        self.gens.append(fiche_nouvo)

    def sauver(self):
        with open(NOMFIC_SAUVE, 'wb') as ficow:
            saumure.dump(self, ficow)

class FicheAdr(object):
    """Fiche d'un contact METHODES: __init__,__repr__"""
    def __init__(self, prenom=None, nomfami=None, datenaiss=None, courriel=None, num=None):
        """Initialise les 4 attributs. Le format datenaiss est JJ/MM/AAAA"""
        self.prenom = prenom
        self.nomfami = nomfami
        self.datenaiss = datenaiss
        self.courriel = courriel
        self.num = num

    def __repr__(self):
        patron = "FicheAdr(prenom='%s', "+\
                 "nomfami='%s'" +\
                 "datenaiss='%s'" +\
                 "courriel='%s'" +\
                 "num='%s')"
        return patron%(self.prenom, self.nomfami, self.datenaiss, self.courriel, self.num)

class Kontroleur(object):
    """Pour gerer les données stockées dans une instance de CarnetAdr, le menu et le chargement des données du fichier.Methodes : __init__,charger(),gerer_menu(),ajouter_fiche(),lister_fiches()"""
    def __init__(self):
        """Initialise le controleur.Cherche un fichier.Si il le trouve, il le lit.Sinon, il crée un fichier vide. """
        self.carnet_adr = self.charger()
        if self.carnet_adr is None:
            self.carnet_adr = CarnetAdr()

        self.gerer_menu()

    def charger(self):
        """Charge un carnet depuis un fichier pickle"""
        if os.path.exists(NOMFIC_SAUVE):
            with open(NOMFIC_SAUVE, 'rb') as ficor:
                return saumure.load(ficor)
        else:
            return None

    def gerer_menu(self):
        #Boucle centrale de l'application
        #Obtient la commande clavier et lance l'action
        print(INSTRUCTIONS)
        while True:
            cmd = input("\n(a)jout, (l)iste, (i)nstructions, (q)uitter :")
            if cmd== "a" or cmd== "A":
                self.ajouter_fiche()
            elif cmd== "q" or cmd== "Q":
                if confirmer_quitter():
                    print("Sauvegarde....")
                    time.sleep(1.5)
                    self.carnet_adr.sauver()
                    print("Fin de l'application")
                    time.sleep(0.5)
                    print("A bientôt ;)")
                    time.sleep(0.5)
                    break
            elif cmd== "i" or cmd== "I":
                print(INSTRUCTIONS)
            elif cmd== "l" or cmd== "L":
                self.lister_fiches()
            else:
                modele = "*** Touche de commande inconnue (%s) !"
                print(modele%cmd)

    def ajouter_fiche(self):
        #Demande la saisie des champs de la nouvelle fiche
        print("Ajout d'une fiche dans le carnet")
        print("Description de la personne :")
        prenom = input("Son prenom ?")
        if prenom=="q":
            print("On abandonne ! :)")
            return
        nomfami = input("Son nom ?")
        if nomfami=="q":
            print("On abandonne ! :)")
            return
        datenaiss = input("Sa date de naissance (JJ/MM/AAAA)?")
        if datenaiss=="q":
            print("On abandonne ! :)")
            return
        courriel = input("Son @dresse ?")
        if courriel=="q":
            print("On abandonne ! :)")
            return
        num = input("Son numéro de téléphone ?")
        if num=="q":
            print("On abandonne ! :)")
            return

        nfiche = FicheAdr(prenom, nomfami, datenaiss, courriel, num)
        self.carnet_adr.ajouter_fiche(nfiche)
        ncontact = (prenom, nomfami)
        print("Nouvelle fiche faite pour %s %s.\n"%ncontact)

    def lister_fiches(self):
        """Afffiche la liste des fiches du carnet"""
        print("\nListe des personnes :")
        for indice,e in enumerate(self.carnet_adr.gens):
            contact = (e.prenom, e.nomfami, e.datenaiss, e.courriel, e.num)
            fiche = PATRON_LISTE%contact
            print("%s %s"%(indice+1, fiche))

###Sction fonctions
def confirmer_quitter():
    """On sort seulement si saisie de la lettre n minuscule par renvoi de false"""
    confi = input(QUIT_CONFIRMER)
    if confi=="n" or confi=="N":
        return False
    else:
        return True

###Section principale main
if __name__=="__main__":
    controleur = Kontroleur()
        
