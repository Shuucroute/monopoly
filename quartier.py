class Quartier:
    def __init__(self, couleur, prixMaison=0):
        self.id = None
        self.couleur = couleur
        self.prixMaison = prixMaison
        self.proprietes = []

    def ajouterPropriete(self, propriete):
        self.proprietes.append(propriete)

    def __str__(self):
        description = f"Quartier {self.couleur}"
        if self.prixMaison > 0:
            description += f" - Prix d'une maison : {self.prixMaison}€"

        if not self.proprietes:
            description += " - Aucune propriété"
        else:
            description += f" - {len(self.proprietes)} propriété(s):"
            for propriete in self.proprietes:
                description += f'\n-> {propriete}'

        return description
