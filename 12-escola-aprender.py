import os
os.system("cls")

print("Atividade - Escola aprender")

nivel = int(input("Informe seu nível:"))
qtd_aulas_semanais = int(input("Informe a qtd de aulas semanais:"))

if (nivel == 1):
    salario_final = (qtd_aulas_semanais * 12) * 4
elif (nivel == 2):
    salario_final = (qtd_aulas_semanais * 17) * 4
elif (nivel == 3):
    salario_final = (qtd_aulas_semanais * 25) * 4
else:
    print("Nível do professor é invalido!")


print(f"O Salário do professor será:{salario_final:.1f}")
