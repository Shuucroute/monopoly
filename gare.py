from Quartier import Quartier
from Propriete import Propriete
from Propriete import Propriete

class Gare(Propriete):
    loyers = [25,50,100,200]
    prixAchatGare = 200
    
    def __init__(self,nom, leQuartier):
        super().__init__(Gare.prixAchatGare, nom, leQuartier)
        
    def calculerLoyer(self):
        # à calculer ... en passant par quartier
        nbGares = 0
        return Gare.loyers[nbGares]

        super().__init__(nom,Gare.prixAchatGare)

    def calculerLoyer(self):    
        return self.loyers[self.nbGares]

if __name__ == '__main__':
    leQuartierGare = Quartier("Noir")
    # gare Montparnasse
    gareMontparnasse = Gare("Gare Montparnasse", leQuartierGare)

    # gare Saint Lazare
    gareSaintLazare = Gare("Gare Saint Lazare", leQuartierGare)

    # gare de Lyon
    gareDeLyon = Gare("Gare de Lyon", leQuartierGare)

    # gare du Nord
    gareDuNord = Gare("Gare du Nord", leQuartierGare)
    
    print(gareDuNord.leQuartier)