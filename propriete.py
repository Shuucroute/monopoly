import Quartier
from abc import ABC, abstractmethod

class Propriete:
    def __init__(self, prixAchat, nom, quartier):
        self.id = None
        self.__prixAchat = prixAchat
        self.__nom = nom
        self.__hypotheque = False
        self.leQuartier = quartier
        quartier.ajouterPropriete(self)
        
    @property
    def prixAchat(self):
        return self.__prixAchat

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, valeur):
        self.__nom = valeur

    @property
    def hypotheque(self):
        return self.__hypotheque
    @hypotheque.setter
    def hypotheque(self, nouvelleValeur):
        self.__hypotheque=nouvelleValeur
    
    @property
    def prixHypotheque(self):
        return self.prixAchat/2

    def __str__(self):
        return (f"{self.nom} ({self.prixAchat}€)")

    @abstractmethod
    def calculerLoyer(self):
        pass

    @abstractmethod
    def type(self):
        pass