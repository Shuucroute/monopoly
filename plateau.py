from propriete import Propriete
from quartier import Quartier

class Terrain (Propriete):
    def __init__ (self, prixAchat, nom, loyers, quartier):
        super().__init__(prixAchat, nom, quartier)
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
    quartierBleu = Quartier("Bleu", 200)
    print(quartierBleu)

    rueDeLaPaix = Terrain(400, "Rue de la paix", [50,200,600,1400,1700,2000], quartierBleu)
    print(rueDeLaPaix)

    avenueChampsElysee = Terrain(320, "Avenue Champs Elysee", [35,175,500,1100,1300,1500], quartierBleu)
    print(avenueChampsElysee)

    print(quartierBleu)

