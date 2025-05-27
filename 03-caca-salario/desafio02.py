## O bjetivo é descobrir quem é o funcionário mais bem pago daequipe.
# 1. Você deve entrevistar 5funcionários e registrar: nomee salário
#  2. Pergunte o nome.
# 3. Pergunte o valor do salário
# 4. Oprograma deve revelar o nome do funcionário com o maior salário.

# Entrda dos dados
print("Olá! colaboradores, escolhemos 5 funcionários, pois estamos fazendo uma entrevista interna.")
print("Vamos precisar de alguns dados de vocês, desde já agradecemos pela colaboração de todos.")
print("Let's go!")
funcionario = []
for i in range (5):
    nome = input("Informe o seu nome: ")
    salario_str = input("Qual o seu salário? ")
    salario = float(salario_str.replace(",","").replace(",","."))
    funcionario.append((nome, salario))

# Processamento dos dados
salario_maior = 0
funcionario_maior = ""

for nome, salario in funcionario:
    if salario > salario_maior:
        salario_maior = salario
        funcionario_maior = nome

# Saída dos dados
print(f"O funcionário mais bem pago é: {funcionario_maior}, com o salário maior de R${salario_maior}.")
