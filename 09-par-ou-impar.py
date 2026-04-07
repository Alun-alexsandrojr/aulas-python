import os
os.system("cls")

print("Atividade - Par ou Ímpar")

numero = int(input("Informe um número:"))
resto = numero % 2

if (resto == 0):
    print("Par!")
else:
    print("Ímpar!")
