'''
Structures de données: Dictionnaires

dico = {}	Dictionnaire vide
dico = {<key>:<value>, <key2>:<value2>, <key3>:<value3>}
        paire (clé:valeur)

Lire une valeur : dico[<key>]
ajout/modification d'une valeur : dico[<key>] = <value>

pop     Supprimer une paire du dico
clear   Supprimer le dico
copy    Copier un dictionnaire

les boucles  
---------
for val in dico.values() -> pour parcourir toute les valeurs
for key in dico.keys()
'''

dico = {"prenom":"jean-philippe", "nom":"Tremblay", "age": 44}

print(dico)
print(type(dico))

print(dico["prenom"])
print(dico["age"])


dico["prenom"] = "luc"

print(dico["prenom"])
print(dico)

dico["taille"] = 1.82   #n'était pas dans la liste, mais on l'a rajouté
print(dico)



#dico.pop["taille"]
#print(dico)


#dico.clear()

#dico2 = dico.copy()
#print(dico2)

print("---------les valeurs---------------")
#pour parcourir le dictionnaire
for val in dico.values():
    print(val)

print("-----------les clés-------------")

#pour parcourir les clés
for key in dico.keys():
    print(key)


print("----------clé et valeur--------------")

#pour parcourir les clés
for key, value in dico.items():
    print(key, value)



#dictionnaire sur plusieurs lignes
dico2 = {
        "prenom":"Patrick",
        "nom":"Roy",
        "age": 22
        }

print("----------clé et valeur dico2--------------")

#pour parcourir les clés
for key, value in dico2.items():
    print(key, value)



print("----------vérifier si age est présente dico2--------------")
if "taille" in dico2:
    print("la clé age est présente")

else:
    print("la clé est absente")