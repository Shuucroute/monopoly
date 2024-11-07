class Propriete:
    def __init__(self, prixAchat, nom):
        self.prixAchat = prixAchat
        self.nom = nom
        self.hypotheque = False
        #self.prixHypotheque = self.prixAchat / 2


    def __str__(self):
        return (f"{self.nom} : ({self.prixAchat} €)")

ruePaix = Propriete(400, "Rue de la paix")
print(ruePaix)
        
