from propriete import Propriete

class CompagnieEE(Propriete):
    def __init__(self, prixAchat, nom, quartier):
        super().__init__(prixAchat, nom, quartier)

    def calculerLoyer(self, facteur):
        return 4 * facteur 

    @property
    def type(self):
        return "CompagnieEE"
