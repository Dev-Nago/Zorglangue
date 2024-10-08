import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from cryptography.fernet import Fernet

"""
Projet 3-4 : Cryptage d’une image ou d’un texte
Le projet consiste à crypter une image ou un texte en utilisant une clé secrète. Pour l'image, la simplification proposée (somme sur la 3 ème dimension) permet de travailler avec une image en niveaux de gris, ce qui facilite le processus de cryptage. Le cryptage des pixels ou des caractères du texte peut être réalisé avec différentes méthodes comme celle de “cryptography” SAS IA - hash - cryptage
Pour une image, on va faire simple prenez la somme d’une image sur la 3 dimension:
np.sum(img, axis=2)
Pyplot possède la fonction imread pour lire les images, on la convertit en array 2D.


"""



# Ouvrir l'image
img = Image.open("image_2.JPG")

# Convertir en niveaux de gris
img_gray = img.convert('RGB')

# Convertir en tableau NumPy
img_array = np.array(img_gray)

#plt.imshow(img_gray, cmap='gray')
#plt.show()


def encrypt_array(data, key):
    """Chiffre un tableau NumPy en utilisant l'algorithme Fernet.

    Args:
        data (np.ndarray): Le tableau à chiffrer.
        key (bytes): La clé de chiffrement.

    Returns:
        bytes: Les données chiffrées.
    """

    # Convertir les données en bytes
    data_bytes = data.tobytes()

    # Créer un objet Fernet
    cipher_suite = Fernet(key)

    # Chiffrer les données
    encrypted_data = cipher_suite.encrypt(data_bytes)

    return encrypted_data

def decrypt_array(encrypted_data, key):
    """Déchiffre un tableau NumPy chiffré avec Fernet.

    Args:
        encrypted_data (bytes): Les données chiffrées.
        key (bytes): La clé de chiffrement.

    Returns:
        np.ndarray: Le tableau déchiffré.
    """

    # Créer un objet Fernet
    cipher_suite = Fernet(key)

    # Déchiffrer les données
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    # Convertir les données déchiffrées en tableau NumPy
    decrypted_array = np.frombuffer(decrypted_data, dtype=data.dtype)

    return decrypted_array


def save_decrypted_image(decrypted_data, filename, shape):
    """Enregistre un tableau NumPy déchiffré sous forme d'image.

    Args:
        decrypted_data (np.ndarray): Le tableau déchiffré.
        filename (str): Le nom du fichier de sortie.
        shape (tuple): Les dimensions de l'image originale.
    """

    # Reshape le tableau pour correspondre aux dimensions de l'image originale
    image_array = decrypted_data.reshape(shape)

    # Créer une image PIL à partir du tableau
    img = Image.fromarray(image_array)

    # Enregistrer l'image
    img.save(filename)


key = Fernet.generate_key()
data = img_array

# Chiffrement
encrypted_data = encrypt_array(data, key)

# Déchiffrement
decrypted_data = decrypt_array(encrypted_data, key)

# garde en imagen
decrypted_data = save_decrypted_image(decrypted_data, "papi_decrypter.jpg",data.shape)