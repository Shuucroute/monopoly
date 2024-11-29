from propriete import Propriete

class Gare(Propriete):
    LOYERS = [25, 50, 100, 200]
    PRIX_ACHAT = 200

    def __init__(self, nom, quartier):
        super().__init__(Gare.PRIX_ACHAT, nom, quartier)

    def calculerLoyer(self, nbGaresPossedees):
        return Gare.LOYERS[nbGaresPossedees - 1]

    @property
    def type(self):
        return "Gare"



