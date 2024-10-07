"""
Projet 1: Zorglangue 
Ah, vous parlez de la Zorglangue !
Il s'agit du langage inventé par le célèbre Zorglub, personnage de la bande dessinée Spirou et Fantasio.
Son principe est simple : 
On inverse l'ordre des lettres dans chaque mot, tout en conservant l'ordre des mots dans la phrase.
Exemples :
"Bonjour" devient "ruojnoB"
"Vive Zorglub !" devient "bulgroZ eviV!"
"Ceci est un message secret" devient "iceC tse un egassam terces"
Particularités :
La ponctuation est conservée à sa place.
Les majuscules restent des majuscules même après inversion (ex: "Zorglub" devient "bulgroZ").
"""

def switch(txt):
    ponct = [".","!","?"]
    newTxt = []
    for letter in txt:
        if letter in ponct:
            newTxt.append(letter)
    newTxt.append(txt[:-1])
    newTxt = "".join(newTxt)
    print(newTxt[::-1])

switch("Vive Zorglub !")

"""
def zorglangue(phrase):

  Traduit une phrase en Zorglangue.

  Args:
    phrase: La phrase à traduire.

  Returns:
    La phrase traduite en Zorglangue.


  # Séparer la phrase en mots
  mots = phrase.split()

  # Inverser les lettres de chaque mot
  mots_inverses = [mot[::-1] for mot in mots]

  # Reconstituer la phrase en Zorglangue
  phrase_zorglangue = " ".join(mots_inverses)

  return phrase_zorglangue

print(zorglangue("Vive Zorglub !"))
"""

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
