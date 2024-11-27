from propriete import Propriete

class Terrain(Propriete):
    def __init__(self, prixAchat, nom, loyers, quartier):
        super().__init__(prixAchat, nom, quartier)
        self.loyers = loyers
        self.nbMaisons = 0

    def calculerLoyer(self):
        return self.loyers[self.nbMaisons]

    @property
    def type(self):
        return "Terrain"
