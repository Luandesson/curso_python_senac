## Operação Salário família 
# Desenvolver um programa que calcule corretamente o salario dos colaboradores com base no salário família.
# Automatizar o processo com logica de programação e entregar resultados formatados valores brasileiro 
# 3. Calcule o salário família: R$300,00 por filho.

# Entrda dos dados
nome = input("Olá! colaborador, me informe seu ultimo nome: ")
salario_bruto_str = (input("Me informe o seu salário bruto: "))
salario_bruto = float(salario_bruto_str.replace(".","").replace(",","."))
filho = int(input("Ok, agora me informe a quantidade de filhos você possui: "))

# Processamento dos dados
if filho > 0:
    salario_liquido = salario_bruto + (filho * 300)
    salario_liquido_br = f"{salario_liquido:,.2f}".replace(",","_").replace(".",",").replace("_",".")
    print(f"{nome}. O seu salário liquído é de: R${salario_liquido_br}")
else:
    salario_bruto_br = f"{salario_bruto:,.2f}".replace(",","_").replace(".",",").replace("_",".")
    print(f"{nome}, você não possui filhos! Seu salário liquido é de: R${salario_bruto_br}")