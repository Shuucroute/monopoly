import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
)

print(mydb)

monCurseur = mydb.cursor()
monCurseur.execute("CREATE")
