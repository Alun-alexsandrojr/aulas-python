import os
os.system("cls")

horas = float(input("Quantas horas por dia você estuda? "))

if horas < 2:
    print("pouco estudo")
elif horas <= 4:
    print("Estudo médio")
else:
    print("Muito estudo")




