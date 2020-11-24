print("---- Programme pour calculer la surface et volume ----------")

'''
-Calculer une surface en m2  	-> surface = longueur x largeur
-Calculer un volume en m3		-> volume = longueur x largeur x hauteur

-Devrait afficher la liste des commandes sur demande de l'utilisateur
-Une commande doit permettre de quitter le programme


'''

#déclarer un dictionnaire
dico = {"aide" : "Afficher les commandes du programme", 
		"surface" : "Calculer la surface en m2",
		"volume" : "Calculer le volume en m3",
		"quitter" : "Quitter le programme"}

print("Tapez aide pour afficher les commandes")

while True:
	com = input("com>")

	if com=="aide":
		print("Liste des commandes du programme")
		print("--------------------------------")

		for k, v in dico.items():
			print(k, ":", v)

	elif com=="surface":
		lon = input("Longueur ?")
		lar = input("Largeur ?")

		try:
			print(f"La surface est de {float(lon) * float(lar)}m2")

		except:
			print("Une erreur s'est produite...")
			continue

	elif com=="volume":
		lon = input("Longueur ?")
		lar = input("Largeur ?")
		hau = input("Hauteur ?")

		try:
			print(f"Le volume est de {float(lon) * float(lar) * float(hau)}m3")

		except:
			print("Une erreur s'est produite...")
			continue

	elif com=="quitter": break

		