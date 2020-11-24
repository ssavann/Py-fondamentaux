'''
Modifier le type d'une variable (cast) = changer son type
int 	nombre entier
str		chaine de caractères
float	nombre flottant
bool	vrai ou faux
'''

nb = input("Nombre ? ")		
#malheureusement son type sera un "string" et non un nombre, je ne peux donc additionner les mots avec des chiffres

#print(nb + 5)
print(type(nb))

print(int(nb) + 5)      #a changé en nombre a ce stade ci, mais nb est toujours un "string" de son origine
print(type(nb))     


#pour pouvoir changer le "string" en nombre


nb2 = input("Nombre ? ") 
nb2 = int(nb2)              #en forçant un "int" nb2 devient un nombre
print(nb2 + 10)
print(type(nb2))


nb3 = input("Nombre ? ") 
nb3 = float(nb3) 
print(nb3 + 13)
print(type(nb3))


homme = 979808
homme = bool(homme)
print(homme)