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