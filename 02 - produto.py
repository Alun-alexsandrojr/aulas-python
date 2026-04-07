import os
os.system("cls")

nome_do_pruduto = input("Entre com nome do prudoto:")
preco = input("Entre com valor so pruduto:")
desconto = float(input("Entre com percentual de desconto:"))
valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto
print("O preço original: R$" , preco, "preço com desconto: R$",preco_final)