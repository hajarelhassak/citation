import tkinter as tk
from tkinter import messagebox
import json
import random

# Fichier des citations
FICHIER_CITATIONS = 'citations.json'

# Charger les citations
def charger_citations(fichier):
    try:
        with open(fichier, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Enregistrer les citations
def enregistrer(fichier, citations):
    with open(fichier, 'w') as f:
        json.dump(citations, f, indent=4)

# Afficher une citation aléatoire
def afficher():
    if citations:
        citation = random.choice(citations)
        messagebox.showinfo('Citation aléatoire', f'\'{citation['citation']}\' - {citation['auteur']}')
    else:
        messagebox.showwarning('Aucune citation', 'Aucune citation disponible.')

# Ajouter une nouvelle citation
def ajouter():
    texte = entree_citation.get()
    auteur = entree_auteur.get()
    if texte and auteur:
        citations.append({'citation': texte, 'auteur': auteur})
        enregistrer(FICHIER_CITATIONS, citations)
        messagebox.showinfo('Succès', 'Citation ajoutée avec succès !')
        
    else:
        messagebox.showwarning('Erreur', 'Veuillez remplir tous les champs.')

# Supprimer toutes les citations
def supprimer_toutes_les_citations():
    if messagebox.askyesno('Confirmation', 'Êtes-vous sûr de vouloir supprimer toutes les citations ?'):
        global citations
        citations = []  # Réinitialise la liste
        enregistrer(FICHIER_CITATIONS, citations)
        messagebox.showinfo('Succès', 'Toutes les citations ont été supprimées.')
    else:
        messagebox.showinfo('Annulé', 'Aucune citation n a été supprimée.')

# Initialisation des citations
citations = charger_citations(FICHIER_CITATIONS)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title('Hajalix - Gestion de Citations')
fenetre.geometry("600x500")

# Interface utilisateur
tk.Label(fenetre, text='Entrez une citation :').grid(row=0, column=0, padx=10, pady=5, sticky="e")
entree_citation = tk.Entry(fenetre, width=40)
entree_citation.grid(row=0, column=1, padx=10, pady=5)

tk.Label(fenetre, text='Entrez l auteur :').grid(row=1, column=0, padx=10, pady=5, sticky="e")
entree_auteur = tk.Entry(fenetre, width=40)
entree_auteur.grid(row=1, column=1, padx=10, pady=5)

# Boutons pour les actions
bouton_ajouter = tk.Button(fenetre, text='Ajouter la citation', command=ajouter)
bouton_ajouter.grid(row=2, column=1, pady=10)

bouton_afficher = tk.Button(fenetre, text='Afficher une citation aléatoire', command=afficher)
bouton_afficher.grid(row=3, column=1, pady=10)

# Bouton pour supprimer toutes les citations
bouton_supprimer_tout = tk.Button(fenetre, text='Supprimer toutes les citations', command=supprimer_toutes_les_citations)
bouton_supprimer_tout.grid(row=4, column=1, pady=10)


# Boucle principale
fenetre.mainloop()

