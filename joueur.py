from propriete import Propriete
from db import DB
class Joueur:
    def __init__(self, nom, pion, proprietes=[], cash=1500, case=0):
        self.nom = nom
        self.pion = pion

    def encaisser(self, montant):
        self.cash += montant

    def decaisser(self, montant):
        if self.cash >= montant:
            self.cash -= montant
            return True  
        else:
            print("Vous n'avez pas assez d'argent.")
            return False

    def payer(self, montant, leJoueur):
        if self.decaisser(montant):
            leJoueur.encaisser(montant)
        else:
            print("Paiement annulé, pas assez de fonds.")

    def acheter(self, propriete=self.case):
        if propriete.id==None:
            propriete.proprietaire = self
            self.proprietes.append(propriete)
        else:
            print("Achat annulé, pas assez de fonds.")



