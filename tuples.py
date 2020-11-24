'''
Structures de données : Tuples (séquences)
------------------------------------------
Les tuples sont immuables ----> Constantes: peut pas changer de valeur

monTuple = ()   ---> tuple vide
la () n'est pas obligatoire

'''

monTuple = ()

print(type(monTuple))



monAge = (44,)      #ajouter la "virgule" pour que ça soit un tuple

print(type(monAge))

print("---------tuple2-----------")


monTuple2 = 44,1.8, "jean"
print(type(monTuple2))
print(monTuple2)
print(monTuple2[2])



print("---------tuple3-----------")


(nombre1, nombre2, prenom) = (11,44, "luc")

nombre1 = 2000
prenom = "Martin"

print(nombre1, nombre2, prenom)