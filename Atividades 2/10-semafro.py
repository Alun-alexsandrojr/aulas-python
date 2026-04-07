import os
os.system("cls")

cor = input("Digite a cor do semafro: ")

if cor == "verde":
    print("Pode passar")
elif cor == "amarelo":
    print("Atenção")
elif cor == "vermelho":
    print("pare")
else:
    print("Cor inválida")