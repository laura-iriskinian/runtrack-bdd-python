import mysql.connector

# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'Laura21!',
#     database = 'laplateforme'
# )

# if mydb.is_connected():
#     db_info = mydb.get_server_info()

# cursor = mydb.cursor()

# cursor.execute('SELECT employe.nom, employe.prenom, employe.salaire, service.nom AS service FROM employe JOIN service ON employe.id_service = service.id;')
# results = cursor.fetchall()
# print(results)

class Employe:
    def __init__(self, host = 'localhost', user = 'root', password = 'Laura21!', database = 'laplateforme'):
        """Connexion à la bdd"""
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()

    def ajouter_employe(self, nom, prenom, salaire, id_service):
        """Ajouter un nouvel employé à la bdd"""
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)" 
        self.cursor.execute(query, (nom, prenom, salaire, id_service))
        self.conn.commit()
        print(f"Employé {nom} {prenom} ajouté avec succès !")

    def lire_employes(self):
        """Affiche tous les employés"""
        query = "SELECT employe.id, employe.nom, employe.prenom, employe.salaire, service.nom AS service FROM employe JOIN service ON employe.id_service = service.id"
        self.cursor.execute(query)
        for employe in self.cursor.fetchall():
            print(employe)

    def mettre_a_jour_employe(self, id, salaire):
        """Mettre à jour le salaire d'un employé"""
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        self.cursor.execute(query, (salaire, id))
        self.conn.commit()
        print(f"Salaire de l'employé ID {id} mis à jour à {salaire}€")

    def supprimer_employe(self,id):
        """Supprime un employé de la bdd"""
        query = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(query, (id,))
        self.conn.commit()
        print(f"Employé ID {id} supprimé avec succès !")
    
    def fermer_connexion(self):
        """Fermer la connexion à la dbb"""
        self.cursor.close()
        self.conn.close()
        print("Connexion fermée")

if __name__ == "__main__":
    db = Employe()

    #Ajouter un employé
    db.ajouter_employe("Doe", "John", 3400, 1)

    #Lire les employés
    print("\n Liste des employés: ")
    db.lire_employes()

    #Mettre à jour un salaire
    db.mettre_a_jour_employe(1, 4500)

    #Supprimer un employé
    db.supprimer_employe(1)

    #fermer la connexion
    db.fermer_connexion()

