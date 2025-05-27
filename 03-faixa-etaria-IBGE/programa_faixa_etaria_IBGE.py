#CRIE UM PROGRAMA QUE MOSTRE A FAIXA ETÁRIA DO USUÁRIO, SEGUNDO IBGE  
# IBGE:
#jovem até os 20 anos
#adulto 21 até os 60 anos
#+60 idoso

# Importa as bibliotecas 
from datetime import date

# Entrada dos dados
nome = input("Olá! para identificar a sua faixa etária segundo IBGE, informe o seu nome: ")
dia = int(input("Agora, digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Em que ano você nasceu? "))

# Processamento dos dados
hoje = date.today()
idade = hoje.year - ano

# Verificar se o usuário já fez aniversário esse ano 
if (hoje.month, hoje.day) < (mes, dia):
    idade -= 1

# Saída dos dados
if idade >= 60:
    print(f"Olá! {nome}, a sua idade é {idade} anos e corresponde a faixa etária do IBGE: idoso.")
elif idade >= 20:
    print(f"Olá! {nome}, a sua idade é {idade} anos e corresponde a faixa etária do IBGE: adulto.")
else:
    print(f"Olá! {nome}, a sua idade é {idade} anos e corresponde a faixa etária do IBGE: jovem.")