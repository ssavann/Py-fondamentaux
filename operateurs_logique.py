'''
Opérateurs logique

not		n'est pas
and		et logique
or 		ou logique

'''


homme = False
#homme = True



if homme==True:
	print("Bonjour monsieur!")


#cette version fonctinne aussi: ça sous-entend que homme est toujours "True"
if homme:
	print("Bonjour monsieur!")


#si la valeur était fausse
if homme==False:
	print("Bonjour madamme!")

#ajouter "not" devant la variable
if not homme:
	print("Bonjour madamme!")
	
'''
username = "jean"
password = "1234"


print("Interface de connexion de la NASA")
print("_________________________________")

userInput = input("Login:")
passInput = input("password:")

#avec l'opérateur "and"
if userInput == username and passInput == password:
	print("Bienvenue", userInput, "à la NASA...")

else:
	print("Authentification non valide...")

'''


username = "jean"
password = "1234"


print("Interface de connexion de la NASA")
print("_________________________________")

userInput = input("Login:")
passInput = input("password:")

#avec l'opérateur "or"
if userInput == username or passInput == password:
	print("Bienvenue", userInput, "à la NASA...")

else:
	print("Authentification non valide...")



