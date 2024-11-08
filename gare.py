from Propriete import Propriete

class Gare(Propriete) :
    loyers = [0,25,50,100,200]  # champ à portée classe : un seul pour tous les objets gares
    prixAchatGare = 200
    
    def __init__(self,nom):
        super().__init__(nom, Gare.prixAchatGare)
        
    def calculerLoyer(self):
        # à calculer ... en passant par quartier
        nbGares = 0
        return Gare.loyers[nbGares]

    @property
    def nbGares(self):
        return self.__nbGares

    @nbGares.setter
    def nbGares(self,value):
        self.__nbGares = value

if __name__ == '__main__':
    garemontparnasse = Gare("Gare Montparnasse")
    print(garemontparnasse)
    garesaintlazare = Gare("Gare Saint Lazare")
    print(garesaintlazare)

    print(f"Le loyer de la gare Montparnasse est de {garemontparnasse.calculerLoyer()}")
    print(f"Les loyers de la gare Montparnasse sont {Gare.loyers}")

