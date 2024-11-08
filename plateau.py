from propriete import *
class Terrain (Propriete):
    def __init__ (self, prixAchat, nom, loyers):
        super().__init__(prixAchat, nom)
        self.loyers = loyers
        self.__nbMaisonss = 0
