import os
os.system("cls")

print("Atividades - positivo ou Negativo")

numero = int(input("Informe um número:"))

if (numero > 0):
    print("Número positivo")
elif(numero < 0):
    print("Número negativo")
else:
    print("Número neutro")
