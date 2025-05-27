## Programa que determina se um funcionário esta apto ou não a se aposentar

# Inporta calendario
from datetime import date

# Entrada dos dados
nome = input("Olá qual o seu nome? ")
ano_nascimento = int(input("Qual o ano do seu nascimento? "))
ano_entrada_empresa = int(input("Em que ano você entrou na empresa? "))

# Processamento e saída dos dados
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
tempo_servico = ano_atual - ano_entrada_empresa

if idade >= 65 and tempo_servico >= 30:
    print(f"Parabén, {nome}!! Você esta apto a aposentadoria. Sua idade é: {idade}. Tempo de trabalho é: {tempo_servico}.")
elif idade >= 60 and tempo_servico >=25:
    print(f"Parabén, {nome}!! Você esta apto a aposentadoria. Sua idade é: {idade}. Tempo de trabalho é: {tempo_servico}.")
else:
    print(f"Você não cumpri os critérios da aposentadoria")