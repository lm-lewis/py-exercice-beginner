print('Exercice déterminant le nombre pair ou impair)

# On demande à l'utilisateur de saisir 
# un nombre 
n=int(input("Ecrire un entier : "))

# [facultatif] On affiche le nombre que l'utilisateur à saisir
print("n = ", n)

# Rappel: un nombre est dit pair si seulement 
# si le reste de la division entière donne zéro
if (n % 2 == 0):
    print(n, " est pair")
else:
    print(n, " est impair")


# ⚠️ fais gaffe si vous saisissez une lettre
# vous aurez une exception ☹️ ah oui.

# Maintenant pour pourvoir améliorer ça,
# il faut que vous vérifiez si l'entrée de saisir de l'utilisateur
# est un nombre avant de continuer le programme
# Si non, inutile de continuer car l'exception sera toujours au rendez-vous
# allez à vous.
