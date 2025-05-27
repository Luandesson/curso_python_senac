## Criar um programa que ajude os atendente a calcular o valor do pedido dos clientes

## CARDAPIO
print("")
print("")
print(" LANCHONETE TECHFOOD ")
print("")
print("         MENU        ")
print("")
print("150-XTudo - R$10,00")
print("151-xBacon - R$11,00")
print("")
print("BEBIDAS:")
print("100-Refresco - R$2,50")
print("101-Refri - R$8,00")
print("")

# Entrada dos dados
lanche = input("Qual o lanche (cód.) que vocÊ quer? ")
qtd_lanche = int(input("Quantos lanche? "))

bebida = input("Informe a sua bebida (cód.):")
qtd_bebida = int(input("Quantas bebidas? "))

# Preço
preco_lanche = 0
preco_bebida = 0

# Verificar o cód do lanche 
if lanche == "150":
    preco_lanche = 10
elif lanche == "151":
    preco_lanche = 11
else:
    print("CÓD lanche inválido!")

# Verificar o cód da bebida
if bebida == "100":
    preco_bebida = 2.50
elif bebida == "101":
    preco_bebida = 8
else:
    print("CÓD bebida inválido!")

# Cálculo 
total = (preco_lanche * qtd_lanche) + (preco_bebida * qtd_bebida)
print("")
print("      RESUMO PEDIDO     ")
print(f"Lanche: ({lanche}) x{qtd_lanche} = R${preco_lanche * qtd_lanche:.2f}")
print(f"Bebida: ({bebida}) x{qtd_bebida} = R${preco_bebida * qtd_bebida:.2f}")
print(f"Total à pagar: R$ {total:.2f}.")