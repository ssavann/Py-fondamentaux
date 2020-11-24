'''
Erreurs et exceptions
---------------------
erreur d'exécution de code: problème dans le code ou problème extérieur (lien ou connexion)

try:		Tester un bloc de code
except:		le bloc est executé en cas d'erreur
except<NomException>:
except(<NomException1>, <NomException2>):
except Exception as err:
else:		Executer si aucune exeption n'est levée
finally:	Block exécuté après que tous les autres blocs aient été exécutés
pass		si on a rien à afficher
'''


nb1 =  input("nb1?")
nb2 =  input("nb2?")

try:
	print(int(nb1) / int(nb2))

#dans le cas où on divise par zéro
except ValueError:
	print("Attention il y a erreur")

except ZeroDivisionError:
	print("Vous ne pouvez pas faire de division par 0")



'''
except Exception as err:
	print(err)
'''	
'''
except:
	pass
'''	

'''
else:
	print("Tout va bien votre code est ok.")
'''

'''
finally:
	print("Essayer une nouvelle fois!")
'''

print("Fin du programme")


