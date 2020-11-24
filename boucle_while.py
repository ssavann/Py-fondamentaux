'''
Boucle while 	-> tant que

'''

i = 0
while i < 10:
	print(i, "Hello world")
	i+=1					
	#ne pas oublié l'incrémentation, sinon boucle infini



print("------------------")


while True:
	com = input(">")
	if com == "Hello":			
		#si l'utilisateur écrit "Hello" dans le terminal, le print va s'afficher
		print("Bonjour toi!")

