import mysql.connector
from quartier import Quartier
from propriete import Propriete
from Terrain import Terrain
from gare import Gare
from CompagnieEE import CompagnieEE


class DB:
    @classmethod
    def connexionBase(cls):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "monopoly_ethan"
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

# creation de la table - Next

# importerPropriete
    @classmethod
    def importerPropriete(cls, id=None, nom=None):
        maConnexion = DB.connexionBase()
        monCurseur = maConnexion.cursor(dictionary= True)

        requete = f"""
                SELECT id,
                       type,
                       idQuartier,
                       nom,
                       prixAchat,
                       loyers
                FROM   proprietes
                WHERE  (id = '{id}' OR nom like '{nom}');"""

        monCurseur.execute(requete)
        monResultat = monCurseur.fetchone()

        #récupérer le quartier correspondant
        #q=DB.importerQuartier(id=int(monResultat["idQuartier"]))
        #ou
        q=DB.Quartiers[int(monResultat["idQuartier"])]       
        if monResultat["type"] == "Terrain":           
            # je cree un Terrain
            p = Terrain(int(monResultat["prixAchat"]),
                        monResultat["nom"],
                        monResultat["loyers"],      # "2,10,30,90,160,250" => [2,10,30,90,160,250]
                        q)  # 1 => 

        elif monResultat["type"] == "Gare":
            # je cree une Gare
            p = Gare(monResultat["nom"],
                     q)
            
        else:
            # je cree une CompagnieEE - TODO
            p = None

        p.id = monResultat["id"]   
        return p
    
# Proprietes (importer toutes les proprietes)

# sauvegarder une propriete - Next

# suppression de la table - Next

if __name__ == '__main__':
    '''
    leQuartierJaune = DB.importerQuartier(id=8)
    print(leQuartierJaune)

    leQuartierMarron = DB.importerQuartier(nom='Marron')
    print(leQuartierMarron)

    print(f"il y a {len(DB.Quartiers)} quartiers:")
    for cle,valeur in DB.Quartiers.items():
        print(cle, "-", valeur)
    '''
    maPropriete0 = DB.importerPropriete(id=1)
    print(maPropriete0)

    maPropriete1 = DB.importerPropriete(id=3)
    print(maPropriete1)

    maPropriete2 = DB.importerPropriete(nom="Gare MontParnasse")
    print(maPropriete2)

    maPropriete3 = DB.importerPropriete(nom="Gare Saint-Lazare")
    print(maPropriete3)

    maPropriete4 = DB.importerPropriete(nom="Gare de Lyon")
    print(maPropriete4)

    maPropriete5 = DB.importerPropriete(nom="Gare du Nord")
    print(maPropriete5)

    q=maPropriete2.leQuartier
    print(q)
