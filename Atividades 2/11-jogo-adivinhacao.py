import os
import random 
os.system("cls")

numero = random.randint(1,10)

palpite = int(input("Digite um número de 1 a 10: "))

if palpite == numero: 
    print("Acertou!")
else:
    print("Errou! Número era: ", numero)
