import os
os.system("cls")

print("Atividade - Calculadora")
numero01 = float(input("Entre com Primeiro numero:"))
numero02 = float(input("Entre com Segundo numero:"))
print("Escolha uma das operações!")
print("+ -> Somar")
print("- -> Subtrair")
print("* -> Multiplicar")
print("/ -> Dividir")
operacao = input("informe a operações:")

if (operacao == "+"):
    resultado = numero01 + numero02

elif (operacao == "-"):
    resultado = numero01 - numero02

elif (operacao == "*"):
    resultado = numero01 * numero02
elif (operacao == "/"):
    resultado = numero01 / numero02

else:
    print("operação inválida!")

print(f"A Operação escolhida foi {operacao}")
print(f"O Resultado é: {resultado}")
    

