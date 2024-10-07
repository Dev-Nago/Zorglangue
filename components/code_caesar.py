"""Projet 2: Code Caesar

Le code Caesar est le plus simple algorithme de cryptage possible, il est basé sur un décalage des lettres par une valeur donnée. Exemple avec un décalage de 3
clair : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : DEFGHIJKLMNOPQRSTUVWXYZABC
-Objectif : 

Implémenter un programme Python qui chiffre et déchiffre du texte en utilisant le chiffrement de César.

Fonctionnalités :

Chiffrement d'un texte avec une clé donnée (décalage des lettres de l'alphabet).
Déchiffrement d'un texte chiffré avec la même clé.
Gestion des lettres majuscules et minuscules.
Gestion des caractères non alphabétiques (ponctuation, espaces, etc.).
Tests unitaires avec Pytest pour vérifier le bon fonctionnement du chiffrement et du déchiffrement.

Amélioration:
prendre en compte les majuscules, les espaces et la ponctuation.
"""
mdp = "ab,ceFGHjklmwx"
mdp_a_dechiffre= "FGHjklmwxab,ce"
def code_caesar(cle,txt):
  prefix=txt[cle:]
  suffix=txt[:cle]
  return print(f"votre mot de passe chiffre est:{prefix+suffix}")

def dechif_caesar(cle,txt):
  prefix=txt[:-cle]
  suffix=txt[-cle:]
  return print(f"votre mot de passe dechiffre est:{suffix+prefix}")
code_caesar(5, mdp)
dechif_caesar(5, mdp_a_dechiffre)