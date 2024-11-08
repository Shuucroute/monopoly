from abc import ABC, abstractmethod
class Propriete(ABC):
    def __init__(self, prixAchat, nom):
        self.__prixAchat = prixAchat
        self.__nom = nom
        self.__hypotheque = False


    @property
    def prixAchat(self):
        return self.__prixAchat

    @property
    def nom(self):
        return self.__nom

    @property
    def hypotheque(self):
        return self.__hypotheque
    @hypotheque.setter
    def hypotheque(self,NouvelleValeur):
        self.__hypotheque = NouvelleValeur


    @property
    def PrixHypotheque(self):
        return self.__prixAchat / 2

  

    def __str__(self):
        return (f"{self.__nom} : ({self.prixAchat} €)")
    

if __name__ == "__main__":
    rueDeLaPaix = Propriete(400, "Rue de la paix")
    print(rueDeLaPaix.prixAchat) 
    print(rueDeLaPaix.hypotheque)
    rueDeLaPaix.hypotheque = True
    print(rueDeLaPaix)