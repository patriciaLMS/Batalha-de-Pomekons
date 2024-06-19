import os
os.system("cls")
print("### Bem-Vindo ao Game PomeKon ###")

bonus =int(input("Informe o Bônus da Partida: "))
ataqueDabriel = int(input("Dabriel - Ataque: "))
defesaDabriel = int(input("Dabriel - Defesa: "))
levelDabriel = int(input("Dabriel - Level: "))
ataqueGuarte = int(input("Guarte - Ataque: "))
defesaGuarte = int(input("Guarte - Defesa: "))
levelGuarte = int(input("Guarte - Level: "))
valorGolpeDabriel = (ataqueDabriel + defesaDabriel)/2 
if levelDabriel % 2 == 0:
    valorGolpeGuarte = valorGolpeDabriel + bonus

valorGolpeGuarte = (ataqueGuarte + defesaGuarte)/2
if levelGuarte % 2 == 0:
    valorGolpeGuarte = valorGolpeGuarte + bonus

print(f"Valor do Golpe do Dabriel: {valorGolpeDabriel}")
print(f"Valor do Golpe do Guarte: {valorGolpeGuarte}")

if valorGolpeGuarte > valorGolpeDabriel:
    print("Guarte é o Ganhador :) ##### ")
elif valorGolpeDabriel > valorGolpeGuarte:
    print("Dabriel é o Ganhador :) #####")
else:
    print("Jogo Terminou Empatado :( #####")