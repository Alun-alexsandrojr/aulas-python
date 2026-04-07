import os 
os.system("cls")

print("Bolrtim Virtual")

aluno = input("Digite o nome do aluno:")
nota01 = float(input("Digite a primeira nota:"))
nota02 = float(input("Digite a Segunda nota:"))
nota03 = float(input("Digite a Terceira nota:"))

media = (nota01 + nota02 + nota03) / 3

if media >= 6:

    print(aluno,"Aprovado!")

elif media >= 4 and media <=5:
    print("Recuperação :/")
    
else:
    print(aluno,"Reprovado :(")
