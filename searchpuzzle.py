from hashlib import sha1, sha256
import hmac
import json


# pour sauvegarder les donner en fichier json
def save_in_json(data):
    with open("save.json", "w") as outfile:
        json.dump(data, outfile)


# donne un hashage a partir d un text et key et function de hashage sha1 ou sha256
def hash_function(text, key, hash_name):
    encoded_text = text.encode()  # coder le text
    encoded_key = str(key).encode()  # coder la clé

    if (hash_name == "sha1"):  # si la fonction de hashage est sha1
        hash_result = hmac.new(encoded_text, encoded_key, sha1)
    else:  # sinon en prend sha256 comme une fonction de hashage
        hash_result = hmac.new(encoded_text, encoded_key, sha256)

    hex_result = hash_result.hexdigest()  # la resultat en hexadecimal

    return hex_result


# la fonction de search_puzzle permet de donner un inconnu x a partir d un id et y et une fonction de hashage
def search_puzzle(id_, y, hash_algo):
    x = 0  # en prend x 0
    nombre_calcules = 0  # compter le nombre de calcule
    while True:  # calculer x jusque le hash de id et x est inférieur ou égal a y

        nombre_calcules += 1
        hash_ = hash_function(id_, x, hash_algo)
        save_in_json({"x": x, "nombre_calcules": nombre_calcules,
                      "hash_algo": hash_algo})  # sauvegarde les données dans chaque itération
        if hash_ <= y:
            return x, nombre_calcules

        x += 1


y_sha1 = "03b1663dda6549a0939ffdd712a852e0d4234e6b"  # le y pour sha
y_sh256 = "00005d10cc11e27bd8d4d1ce91bc725665ddbaa6ca2498ef38a88a58ad48cdb4"  # y pour sha256

id_ = input("saisir votre id: ")
hash_name = input("choisir le type de hashage \n 1: sha1 \n 2: sha256 \n")

if (int(hash_name) == 1):  # si utilisateur choisir 1 alors algo est sha1 sinon sha256
    hash_name = "sha1"
    y = y_sha1
else:
    hash_name = "sha256"
    y = y_sh256

print("l algorithme de hashage est: ", hash_name)
x, nombre_de_calcules = search_puzzle(id_, y, hash_name)
print("=======================\n")
print("la resultat x est: ", x)
print("le nombre de calcules est: ", nombre_de_calcules)
print("\n =======================")
