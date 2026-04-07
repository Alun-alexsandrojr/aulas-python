import os
os.system("cls")

print("Atividade Produto e Vendas")

descricao = input("Digite a descrição do produto:")
preco = float(input("Informe o preço do produto:"))
qtd = int(input("Informe a quantidade de produto:"))

total_sem_desconto = preco * qtd

if (qtd <= 5):
    desconto = (total_sem_desconto *2) / 100
elif (qtd > 5 and qtd <= 10):
    desconto = (total_sem_desconto * 3) / 100
elif (qtd > 10):
    desconto = (total_sem_desconto *5) / 100

total_com_desconto = total_sem_desconto - desconto

print(f"=" * 40)
print(f"O Total bruto: {total_sem_desconto}")
print(f"Quantos de desconto: {desconto}")
print(f"Total com desconto: {total_com_desconto}")