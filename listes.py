'''
Structures de données: Listes

Les listes en Python peuvent contenir plusieurs types (int, float, str, double) 
dans la même liste, contrairement à d'autres langages qui contiendraient qu'un seul type par liste

append:		Ajouter un element à la fin de la liste
insert:		Ajouter un element selon un index
remove:		Supprimer un element par sa valeur
pop:		Supprimer un element par son index
index:		Afficher l'index selon une valeur
count:		Nombre de fois ou l'élément apparait
sort:		Trier par ordre croissant
reverse:	Inverser l'ordre de la liste
copy:		Copie d'une liste
extend:		Étendre une liste
clear:		Effacer une liste
'''


maListe = ["zoe", "marc", "alain", "adrien", 10, 44.5, "zoe", "zoe"]
maListe2 = ["zoe", "marc", "alain", "adrien", "zoe", "zoe"]
maListe4 = [1,2,33,4]


print(type(maListe))

maListe.append("lana")	#pour ajouter "lana" à la fin de ma liste

maListe.insert(1, "toto")	#va inserer "toto" à la position 1

maListe.remove("marc")

maListe.pop(3)




for element in maListe:
	print(element)

print("------------")

print(maListe.index("alain"))
print(maListe.count("zoe"))

maListe2.sort()

print("------sort------")

for element in maListe2:
	print(element)


maListe2.reverse()

print("------reverse------")

for element in maListe2:
	print(element)


maListe3 = maListe2.copy()

print("------copy------")

for element in maListe3:
	print(element)



#ça va ajouter la liste 4 à la liste 1
maListe4.extend(maListe)

print("------extend------")

for element in maListe4:
	print(element)


maListe3.clear()
print("------clear------")

for element in maListe3:
	print(element)

#nouvelle façon de faire une copy dans l'intégralité
maListe5 = maListe2[:]	