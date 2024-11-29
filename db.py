import mysql.connector
from quartier import Quartier
from Terrain import Terrain
from gare import Gare
from CompagnieEE import CompagnieEE


class DB:
    @staticmethod
    def connexionBase():
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="monopoly_ethan"
            )
        except mysql.connector.Error as err:
            print(f"Erreur lors de la connexion à la base de données : {err}")
            exit(1)

    @staticmethod
    def creationQuartiers():
        with DB.connexionBase() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS quartiers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                couleur VARCHAR(255) NOT NULL,
                prixMaison INT NOT NULL
            );
            """)

    @staticmethod
    def importerQuartier(id=None, nom=None):
        if id is None and nom is None:
            print("Erreur : Veuillez fournir un `id` ou un `nom` pour importer un quartier.")
            return None
        with DB.connexionBase() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT id, couleur, prixMaison
                FROM quartiers
                WHERE id = %s OR couleur = %s
            """, (id, nom))
            result = cursor.fetchone()
            if result:
                quartier = Quartier(result['couleur'], result['prixMaison'])
                quartier.id = result['id']
                return quartier
            return None

    @staticmethod
    def importerPropriete(id=None, nom=None):
        if id is None and nom is None:
            print("Erreur : Veuillez fournir un `id` ou un `nom` pour importer une propriété.")
            return None
        with DB.connexionBase() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT id, type, idQuartier, nom, prixAchat, loyers
                FROM proprietes
                WHERE id = %s OR nom = %s
            """, (id, nom))
            result = cursor.fetchone()
            if result:
                quartier = DB.importerQuartier(result['idQuartier'])
                if not quartier:
                    print(f"Erreur : Quartier ID {result['idQuartier']} introuvable.")
                    return None
                if result['type'] == "Terrain":
                    loyers = list(map(int, result['loyers'].split(',')))
                    return Terrain(result['prixAchat'], result['nom'], loyers, quartier)
                elif result['type'] == "Gare":
                    return Gare(result['nom'], quartier)
                elif result['type'] == "CompagnieEE":
                    return CompagnieEE(result['prixAchat'], result['nom'], quartier)
            return None
