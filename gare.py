from propriete import Propriete

class Gare(Propriete):
    loyers = [25,50,100,200]
    prixAchatGare = 200
    def __init__(self,nom):
        super().__init__(nom,Gare.prixAchatGare)

    def calculerLoyer(self):    
        return self.loyers[self.nbGares]

if __name__ == '__main__':
    gareMontparnasse = Gare("Gare Montparnasse")
    print(gareMontparnasse)
    gareMontparnasse.nbGares += 1
    print(f"Le loyer est de {gareMontparnasse.calculerLoyer()}") 
    gareSaintLazare = Gare("Gare Saint-Lazare")
    print(gareSaintLazare)
    gareSaintLazare.nbGares += 1
    print(f"Le loyer est de {gareSaintLazare.calculerLoyer()}") 

