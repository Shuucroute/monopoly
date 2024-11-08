from propriete import Propriete

class Terrain (Propriete):
    def __init__ (self, prixAchat, nom, loyers):
        super().__init__(prixAchat, nom)
        self.__loyers = loyers
        self.__nbMaisons = 0

    def calculerLoyer(self):
        return self.__loyers[self.nbMaisons]

    @property
    def nbMaisons(self):
        return self.__nbMaisons

    @nbMaisons.setter
    def nbMaisons(self,valeur=None):
        if valeur <5:
            self.__nbMaisons = valeur

if __name__ == '__main__':
    rueDeLaPaix = Terrain(400, "Rue de la paix", [50,200,600,1400,1700,2000])
    print(rueDeLaPaix)
    rueDeLaPaix.nbMaisons = 2
    print(f"Le loyer est de {rueDeLaPaix.calculerLoyer()}") 
