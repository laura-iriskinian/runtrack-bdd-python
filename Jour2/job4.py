import mysql.connector

#permets de charger la BDD
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Laura21!',
    database = 'laplateforme'
)

if mydb.is_connected():
    db_info = mydb.get_server_info()
    print(f"connecté à MySQL, {db_info}")

#à placer pour exécuter une commande mysql
cursor = mydb.cursor()

#Job4
cursor.execute("SELECT nom, capacite FROM salle;")
#fetchall récupère les données du cursor
results = cursor.fetchall()
print(results)

