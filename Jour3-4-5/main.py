import tkinter as tk
from tkinter import ttk
import mysql.connector

class Product:
    def __init__(self, host='localhost', user='root', password='Laura21!', database='store'):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()
        self.tree = None  # Initialisation du Treeview comme attribut de classe

    def print_products(self):
        # Supprimer l'ancien tableau s'il existe déjà (évite les doublons)
        if self.tree:
            self.tree.destroy()

        # Exécuter la requête SQL
        self.cursor.execute("SELECT * FROM product")
        rows = self.cursor.fetchall()

        # Créer le tableau uniquement après avoir cliqué sur le bouton
        self.tree = ttk.Treeview(root, columns=('id', 'name', 'description', 'price', 'quantity', 'id_category'), show="headings")
        self.tree.heading('id', text='ID')
        self.tree.heading('name', text='Name')
        self.tree.heading('description', text='Description')
        self.tree.heading('price', text='Price')
        self.tree.heading('quantity', text='Quantity')
        self.tree.heading('id_category', text='Category')
        self.tree.pack()

        # Insérer les données dans le tableau
        for row in rows:
            self.tree.insert("", "end", values=row)

# Création de la fenêtre Tkinter
root = tk.Tk()
root.title("Gestion des Produits")

# Création de l'objet Product
product = Product()

# Bouton pour afficher le tableau des produits
btn = tk.Button(root, text="Afficher les Produits", command=product.print_products)
btn.pack()

# Lancer la boucle Tkinter
root.mainloop()

# Fermer la connexion MySQL après fermeture de la fenêtre
product.cursor.close()
product.conn.close()
