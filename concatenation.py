'''
La concaténation: mettre bout à bout 2 ou 3 chaînes de caractères
'''



numCompte = 123
client = "Bob"

#avec des virgules
print("numéro:", numCompte, "appartient à", client)

#avec des signes "+", il faut spécifier le type pour que ça fonctionne
print("numéro: " + str(numCompte) + " appartient à " + client)

#avec des accolades
print("numéro: {0} appartient à {1}" .format (numCompte, client))

#accolade et variables, ne pas oublié le "f" au début
print(f"numéro: {numCompte} appartient à {client}")