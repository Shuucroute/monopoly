from propriete import Propriete

class Gare(Propriete):
    def __init__(self,prixAchat,nom):
        super().__init__(prixAchat, nom)
        self.__loyers = [25,50,100,200]
        self.__nbGares = 0

    def calculerLoyer(self):
        return self.__loyers[self.nbGares]

    @property
    def nbGares(self):
        return self.__nbGares

    @nbGares.setter
    def nbGares(self,valeur):
        self.__nbGares = valeur

if __name__ == '__main__':
    gareMontparnasse = Gare(200, "Gare Montparnasse")
    print(gareMontparnasse)
    gareMontparnasse.nbGares = 1
    print(f"Le loyer est de {gareMontparnasse.calculerLoyer()}") 
