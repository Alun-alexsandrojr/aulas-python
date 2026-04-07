import os
os.system("cls")

idade = int(input("Digite sua idade atual: "))
ano_atual = int(input("Digite o ano atual: "))
ano_futuro = int(input("Digite o ano do futuro: "))

idade_futura = idade +(ano_futuro - ano_atual)

print("Em:", ano_futuro, "Você terá", idade_futura, "anos")
