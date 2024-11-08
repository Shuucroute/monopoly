
class Quartier:
    def __init__(self, couleur, prixMaison=0):
        self.__couleur = couleur
        self.__prixMaison = prixMaison
        self.lesProprietesDuQuartier = []

    def ajouterPropriete(self, laPropriete):
        self.lesProprietesDuQuartier.append(laPropriete)
        
    def __str__(self):
        if self.__prixMaison == 0:
            resultat = f"Quartier {self.__couleur}"
        else:
            resultat = f"Quartier {self.__couleur} - Prix d'une maison : {self.__prixMaison}€"

        if len(self.lesProprietesDuQuartier) == 0:
            resultat = resultat + " - Aucune propriété"
        else:
            resultat = resultat + f" - {len(self.lesProprietesDuQuartier)} propriété(s):"
            for p in self.lesProprietesDuQuartier:
                resultat = resultat + '\n' + str(p)
            
        return resultat

# combien y a -t-il de proprietes dans le quartier ?

# combien un jour a-t-il de proprietes dans le quartier ?

if __name__ == '__main__':
    quartierBleu = Quartier("Bleu", 200)
    print(quartierBleu)
    quartierGares = Quartier("Noir")
    print(quartierGares)
