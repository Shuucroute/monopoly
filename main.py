from db import DB
from quartier import Quartier
from Terrain import Terrain
from gare import Gare
from CompagnieEE import CompagnieEE

def afficher_quartiers():
    """Exemple pour afficher tous les quartiers disponibles."""
    print("Chargement des quartiers...")
    quartiers = []
    for id in range(1,11): 
        quartier = DB.importerQuartier(id=id)
        if quartier:
            quartiers.append(quartier)
    for q in quartiers:
        print(q)

def afficher_proprietes():
    """Exemple pour afficher toutes les propriétés."""
    print("\nChargement des propriétés...")
    proprietes = []
    for id in range(1,39):  
        propriete = DB.importerPropriete(id=id)
        if propriete:
            proprietes.append(propriete)
    for p in proprietes:
        print(f"{p.nom} ({p.type}) - {p.prixAchat}€")

def main():
    """Point d'entrée principal du jeu."""
    print("Bienvenue dans le jeu Monopoly !\n")
    
    print("Initialisation de la base de données...")
    DB.creationQuartiers()

    afficher_quartiers()
    afficher_proprietes()

    # Simulation d'une boucle de jeu
    print("\nSimulation d'un tour de jeu...\n")

if __name__ == "__main__":
    main()
