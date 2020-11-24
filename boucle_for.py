'''
Boucle for

range			PLage de valeur
range(6)		0 1 2 3 4 5
range(3,10)		3 4 5 6 7 8 9
range(10,20,2)	10 12 14 16 18 ça saute de 2
faire des sous-boucles: c'est possible
'''

for i in range(10):
	print(i, "hello world!")


print("-------------------")


for y in range(3,10):
	print(y, "hello world!")

print("-------------------")


for z in range(10,20, 2):
	print(z, "hello world!")

else:
	print("fin de Boucle")

print("-------------------")

for a in range(5):			#faire 5 passages de "a"
	for b in range(2):		#durant les 5 passages de "a", faire 2 passages de "b"
		print("a",a,"b",b)
