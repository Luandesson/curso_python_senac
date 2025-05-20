#Programa para calcular a média de duas notas de um estudante. Para estar APTO, média>=70 e frequência>=75. 
# Caso contrário, NÃO APTO. 

# Entrada de dados
nome = input("Olá! Estudante, informe o seu nome: ")
nota1 = float(input("Informe a sua 1ª nota: "))
nota2 = float(input("Informe a sua 2ª nota: "))
frequencia = int(input("Qual a sua frequencia de 0 a 100 (%): "))

# Processamento dos dados
media_nota = (nota1 + nota2)/2

# Saida dos dados
if media_nota >= 70 and frequencia >= 75:
    print(f"Olá! {nome}, parabéns! Você esta apto. A media da sua nota é {media_nota}, sua frequencia {frequencia}%.")
else:
    print(f"Olá, {nome}, infelizmente você não esta apto aos requisitos, sua nota é: {media_nota}, e sua frequencia é {frequencia}%.")