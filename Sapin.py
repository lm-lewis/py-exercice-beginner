# Exercice
symbole = "●"
taille = 10

for i in range(1, taille+1):
    print(f"{' ' * (taille - i)}{(symbole + ' ') * i}")

print()
print()
print()

inpt = ""
while not inpt.isdigit():
    inpt = input("Veillez entrer un nombre ")
taille = int(inpt)

for i in range(1, taille+1):
    print(f"{' ' * (taille - i)}{(symbole + ' ') * i}")


# ⚠️ Essai d'interpréter les lignes de code ci-dessus
# et expliqué c'est que vous comprenez.
