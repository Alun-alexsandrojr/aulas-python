import os
import random
os.system("cls")

nome = input("Digite seu nome: ")

print("Escolha seu pokemon: ")
print("1- Charmander 🔥")
print("2- Squirtle 💧")
print("3- Bulbasaur 🌱")

escolha = int(input("Escolha o número do pokémon: "))

inimigo = random.randint(1,3)

if escolha == 1:
    print(nome, "Escolheu Charmander!")
elif escolha == 2:
    print(nome, "Escolheu Squirtlr!")
elif escolha == 3:
    print(nome, "Escolheu Bulbasaur")
else:
    print("Escolha inválida")

if inimigo == 1:
    print("Inimigo escolheu Charmander!")
elif inimigo == 2:
    print("Inimigo esolheu Squirtle")
elif inimigo == 3:
    print("Inimigo escolheu Bulbasaur")

if escolha == inimigo:
    print("Empate!")
    print("Você vai ganhar na próxima")
elif escolha == 1 and inimigo == 3:
    print("Você ganhou:)")
elif escolha == 2 and inimigo == 1:
    print("Você ganhou:)")
elif escolha == 3 and inimigo == 2:
    print("Você ganhou:)")
else:
    print("Você perdeu:(")
    print(nome,"Tenta Novamente")
    

    