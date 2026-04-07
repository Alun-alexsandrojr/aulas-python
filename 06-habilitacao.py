import os 
os.system("cls")

print("Atividade - Habilitação")

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
possui_habilitacao = input("Você possui habilitação (Sim ou Não)?: ")


if idade >= 18:
    possui_habilitacao = input("Você possui habilitação (Sim ou Não)?: ").lower()

    if(possui_habilitacao == "Sim"):

         print(nome,"Você pode Dirigir")

    else:
        print("Você não possui habilitação, ou seja, não pode dirijir")     

else: 
    print(nome,"Não pode dirigir :/")


print("Fim do Programa!")
