import os
os.system("cls")

print("Atividade - IMC")

peso = float(input("Informe seu peso:"))
altura = float(input("Informe sua altura:"))

imc = peso / (altura * altura)

if (imc < 16.9):
    print("Muito abaixo do peso!")
elif (imc >17 and imc <= 18.4):
    print("Abaixo do peso")
elif (imc >= 18.5 and imc <=24.9):
    print("peso normal")
elif (imc >= 25 and imc <=29.9):
    print("Acima do peso")
elif (imc >=30 and imc <=34.9):
    print("Obecidade Grau 1")
elif (imc >35 and imc <=40):
    print("Obecidade Grau 2")
else:
    print("Obesidade Grau 3")

print(f"Seu imc é: {imc:.2}")