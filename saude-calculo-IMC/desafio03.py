## Saúde digital - Cálculo do IMC
# você é um agente da Saúde Tech e sua missão é ajudar os usuários a descobrirem se estão com o peso ideal usando um programa.

# Entrada dos dados
nome = input("Olá, para sabermos o seu peso ideal, me informe o seu nome: ")
peso = float(input("Me informe o seu peso em (kg): "))
altura = float(input("Qual a sua altura? "))

# Processamento e saída dos dados
IMC = peso / altura
if IMC > 25:
    print(f"Ops! {nome}, Acima do peso.")
else:
    print(f"OBA! {nome}, seu peso esta OK, seu IMC é: {IMC}. Você está no caminho certo! ")