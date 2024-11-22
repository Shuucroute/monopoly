from Propriete import Propriete
from Quartier import Quartier

class Terrain(Propriete):
    def __init__(self, prixAchat, nom, loyers, quartier):
        super().__init__(prixAchat, nom, quartier)
        self.__loyers=loyers
        self.__nbMaisons = 0

    def calculerLoyer(self):
        return self.__loyers[self.__nbMaisons]

    @property
    def nbMaisons(self):
        return self.__nbMaisons

    @nbMaisons.setter
    def nbMaisons(self,valeur):
        if valeur<5:
            self.__nbMaisons = valeur

    def type(self):
        return "Terrain"    
           
if __name__ == '__main__':
    quartierBleu = Quartier("Marron", 200)
    print(quartierBleu)

    # rue de la Paix
    rueDeLaPaix = Terrain(60, "Boulevard Belleville", [2,10,30,90,160,250], quartierBleu)
    print(rueDeLaPaix)
    
    # avenue des champs elysées
    avenueChampsElysees = Terrain(320, "Avenue des Champs Elysées", [35,175,500,1100,1300,1500], quartierBleu)
    print(avenueChampsElysees)

    print(quartierBleu)