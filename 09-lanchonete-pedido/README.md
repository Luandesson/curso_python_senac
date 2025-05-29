# 🍔 Lanchonete TechFood - Calculadora de Pedidos

Este programa tem como objetivo ajudar os atendentes da Lanchonete TechFood a calcular rapidamente o valor total dos pedidos dos clientes, com base no cardápio da casa.

## 📋 Cardápio
LANCHONETE TECHFOOD
     MENU        
150 - X-Tudo - R$10,00
151 - X-Bacon - R$11,00

BEBIDAS:
100 - Refresco - R$2,50
101 - Refrigerante - R$8,00

## 🎯 Objetivo

- O atendente deve digitar o código do lanche e da bebida, além das quantidades.
- O sistema calcula o valor total do pedido.
- Mostra um resumo final com os itens, quantidades e total a pagar.

```python
# CARDÁPIO
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
lanche = input("Qual o lanche (cód.) que você quer? ")
qtd_lanche = int(input("Quantos lanches? "))

bebida = input("Informe a sua bebida (cód.): ")
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

💡 Exemplo de Execução
Qual o lanche (cód.) que você quer? 150  
Quantos lanches? 2  
Informe a sua bebida (cód.): 100  
Quantas bebidas? 1  

      RESUMO PEDIDO     
Lanche: (150) x2 = R$20.00  
Bebida: (100) x1 = R$2.50  
Total à pagar: R$ 22.50.

✅ Melhorias futuras
Adicionar mais itens ao cardápio.

Validar se o código digitado existe antes de continuar.

Interface gráfica para atendimento em balcão.

Desenvolvido por Luandesson 🚀
