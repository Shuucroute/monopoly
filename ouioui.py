import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = "monopoly",
)

print(mydb)

monCurseur = mydb.cursor()
monCurseur.execute("""
CREATE TABLE IF NOT EXISTS quartiers 
(
    id INT NOT NULL AUTO_INCREMENT,
    couleur VARCHAR(255),
    prixMaison INT,
    CONSTRAINT PK_quartiers PRIMARY KEY (id)
);
""")

print("table créée !")