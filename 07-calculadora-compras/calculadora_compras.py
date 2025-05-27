# Mercado TECH: Calculadora de compras
# Entrada dos dados

produto = input("Qual o produto? ")
quantidade_produto = int(input("Quantidade? "))
valor_uni = float(input("Qual o valor unitário do produto? R$"))

# Processar os dados e calculos do desonto
total_bruto = quantidade_produto * valor_uni
if quantidade_produto > 10:
    desconto = total_bruto * 0.05
elif quantidade_produto > 6:
    desconto = total_bruto * 0.03
else:
    desconto = total_bruto * 0.02
total_desconto = total_bruto - desconto

# Saída dos dados
print(f"Nota da compra")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade_produto}")
print(f"Preço un.: R${valor_uni:.2f}.")
print(f"Total bruto: R${total_bruto:.2f}")
print(f"Desconto de: R${desconto:.2f}")
print(f"Total ficou: de: R${total_desconto:.2f}")

