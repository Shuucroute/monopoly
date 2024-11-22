from Quartier import Quartier
from Propriete import Propriete
from propriete import Propriete

class Gare(Propriete):
    loyers = [25,50,100,200]
    prixAchatGare = 200
    quartierGare = Quartier("Noir")
    
    def __init__(self,nom):
        super().__init__(Gare.prixAchatGare, nom, Gare.quartierGare)
        
    def calculerLoyer(self):
        # à calculer ... en passant par quartier
        nbGares = 0
        return Gare.loyers[nbGares]

        super().__init__(nom,Gare.prixAchatGare)

    def calculerLoyer(self):    
        return self.loyers[self.nbGares]

if __name__ == '__main__':
    # gare Montparnasse
    gareMontparnasse = Gare("Gare Montparnasse")
    print(gareMontparnasse)

    # gare Saint Lazare
    gareSaintLazare = Gare("Gare Saint Lazare")
    print(gareSaintLazare)

    # gare de Lyon
    gareDeLyon = Gare("Gare de Lyon")
    print(gareDeLyon)

    # gare du Nord
    gareDuNord = Gare("Gare du Nord")
    print(gareDuNord)
    
    print(Gare.quartierGare)
    gareMontparnasse = Gare("Gare Montparnasse")
    print(gareMontparnasse)
    gareMontparnasse.nbGares += 1
    print(f"Le loyer est de {gareMontparnasse.calculerLoyer()}") 
    gareSaintLazare = Gare("Gare Saint-Lazare")
    print(gareSaintLazare)
    gareSaintLazare.nbGares += 1
    print(f"Le loyer est de {gareSaintLazare.calculerLoyer()}") 

