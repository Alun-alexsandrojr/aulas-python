import os
os.system("cls")

estoque = int(input("Digite a quantidade em estoque: "))

if estoque < 5:
    print("Estoque baixo!")
else:
    print("Estoque OK")