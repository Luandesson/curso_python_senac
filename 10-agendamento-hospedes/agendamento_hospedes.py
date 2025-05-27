## Criar um programa de agendamento para hospedes 
# Regra 1 - O numero total de pessoas (adulto + kids) não pode passar de 4 pessoas
# Regra 2 - Máximo de 30 dias de hospedagem 

print("Bem-vindo à rede de hoteis Senac RJ")

# Entrada de dados da acomodação
tipo = input(" Tipo de acomodação  (Standard ou Luxo) ?? ")
adulto = int(input("Quantos adultos? "))
kids = int(input("Quantas crianças? "))
dias = int(input("Quantos dias? "))

#Entruturas de repetição - validação das regras
if adulto + kids > 4:
    print("Máximo de 4 pessoas por acomodação.")
elif dias > 30:
    print("Máximo 30 dias de hospedagem.")
else:
    # Preços das acomodações
    if tipo == "standard" or tipo == "Standard":
        preco_adulto = 150
        preco_kids = 75
    elif tipo == "luxo" or tipo == "Luxo":
        preco_adulto = 200
        preco_kids = 100
    else:
        print("Tipo acomodação inválida.")
        exit()

valor_total = (adulto * preco_adulto + kids * preco_kids)* dias # Cálculo do valor total antes do desconto 

# Calculo para o desconto
if dias > 10:
    desconto = valor_total * 0.10
elif dias > 6:
    desconto = valor_total * 0.08
else:
    desconto = valor_total * 0.05

valor_desconto = valor_total - desconto #calculo com desconto
valor_desconto_br = f"{valor_desconto:,.2f}".replace(",","_").replace(".",",").replace("_",".")


# Cadastro do hóspede 
nome = (input("Olá, informe seu nome completo: "))
email = (input("Informe o seu e-mail:  "))

# Resumo da hóspedagem
print("\nAQUI ESTA O RESUMO RESERVA DE HOSPEDAGEM")
print(f"TIPO ACOMODAÇÃO:............: {tipo.title()}")
print(f"QUANTIDADE DE ADULTOS:......: {adulto}")
print(f"QUANTIDADE DE CRIANÇAS:.....: {kids}")
print(f"QUANTIDADE DE DIAS:.........: {dias}")
print(f"VALOR TOTAL:..............: R${valor_desconto_br}")
