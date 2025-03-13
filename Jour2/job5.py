import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Laura21!',
    database = 'laplateforme'
)

if mydb.is_connected():
    db_info = mydb.get_server_info()

cursor = mydb.cursor()

cursor.execute("SELECT superficie FROM etage;")
results = cursor.fetchall()
superficie_totale = sum(result[0] for result in results)
print(f"La superficie de La plateforme est de {superficie_totale} m2")