from abc import ABC, abstractmethod

class Propriete(ABC):
    def __init__(self, prixAchat, nom, quartier):
        self.id = None
        self.nom = nom
        self.prixAchat = prixAchat
        self.hypotheque = False
        self.quartier = quartier
        quartier.ajouterPropriete(self)

    @property
    def prixHypotheque(self):
        return self.prixAchat / 2

    def __str__(self):
        return f"{self.nom} ({self.prixAchat}€)"

    @abstractmethod
    def calculerLoyer(self):
        pass

    @abstractmethod
    def type(self):
        pass
