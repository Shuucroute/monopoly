import mysql.connector
from Quartier import Quartier
from Propriete import Propriete
import Terrain
import Gare
import CompagnieEE


class DB:
    @classmethod
    def connexionBase(cls):
        mydb = mysql.connector.connect(
          host="localhost",
          user="mmaldo",
          password="aDHp8P6?2/6]",
          database = "monopoly_prod"
        )
        return mydb

# TABLE QUARTIERS -------------------------------------------------------
    @classmethod
    def creationQuartiers(cls):
        maConnexion = DB.connexionBase()
        monCurseur = maConnexion.cursor()
        monCurseur.execute("""
        CREATE TABLE IF NOT EXISTS quartiers 
        (
            id INT NOT NULL AUTO_INCREMENT,
            couleur VARCHAR(255),
            prixMaison INT,
            CONSTRAINT PK_quartiers PRIMARY KEY(id)
        );
        """)

    @classmethod
    def importerQuartier(cls, id=None, nom=None):
        maConnexion = DB.connexionBase()
        monCurseur = maConnexion.cursor(dictionary= True)

        requete = f"""
                SELECT id,
                       couleur,
                       prixMaison
                FROM   quartiers
                WHERE  (id = '{id}' OR couleur like '{nom}');"""

        monCurseur.execute(requete)
        monResultat = monCurseur.fetchone()

        q = Quartier(monResultat["couleur"], int(monResultat["prixMaison"]))
        q.id = int(monResultat["id"])
        
        return q

    __Quartiers = {}
    
    @classmethod
    @property
    def Quartiers(cls):
        if DB.__Quartiers == {}:
            maConnexion = DB.connexionBase()
            monCurseur = maConnexion.cursor(dictionary= True)
 
            monCurseur.execute(f"""
                SELECT id,
                       couleur,
                       prixMaison
                FROM   quartiers;""")
            mesResultats = monCurseur.fetchall()
            DB.__Quartiers = {}
            for r in mesResultats:
                q = Quartier(r["couleur"], int(r["prixMaison"]))
                q.id = int(r["id"])
                DB.__Quartiers[q.id] = q
            
        return DB.__Quartiers

    @classmethod
    def sauvegarderQuartier(cls, q):
        # si id n'a pas de valeur => insert
        # si id a une valeur => update
        maConnexion = DB.connexionBase()
        monCurseur = maConnexion.cursor()

        if q.id is None:
            print("inserting...")
            monCurseur.execute("""
               INSERT INTO quartiers (couleur, prixMaison)
               VALUES (%s, %s);""", (q.couleur, q.prixMaison))

            # recuperer l'id généré dans la base
            q.id = monCurseur.lastrowid
        else:
            print("updating...")
            monCurseur.execute("""
               UPDATE quartiers
               SET couleur = %s,
                   prixMaison = %s
               WHERE id = %s;""", (q.couleur, q.prixMaison, q.id))
 
        maConnexion.commit()
        
    @classmethod
    def suppressionTable(cls):
        maConnexion = DB.connexionBase()
        monCurseur = maConnexion.cursor()
        monCurseur.execute("DROP TABLE quartiers;")


# TABLE PROPRIETES -------------------------------------------------------
# to do ...

if __name__ == '__main__':
    leQuartierJaune = DB.importerQuartier(id=8)
    print(leQuartierJaune)

    leQuartierMarron = DB.importerQuartier(nom='Marron')
    print(leQuartierMarron)

    print(f"il y a {len(DB.Quartiers)} quartiers:")
    for cle,valeur in DB.Quartiers.items():
        print(cle, "-", valeur)

