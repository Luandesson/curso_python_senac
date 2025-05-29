# 📊 Entrevista Interna: Funcionário Mais Bem Pago

Este projeto tem como objetivo identificar quem é o funcionário com o maior salário dentro de uma equipe de 5 entrevistados.

## 🎯 Propósito

- Praticar coleta de dados com entrada de múltiplos usuários.
- Trabalhar com listas e estruturas de repetição.
- Utilizar lógica condicional para encontrar valores máximos.
- Produzir uma saída personalizada e clara.

```python
# Exemplo de execução em Python
print("Olá! colaboradores, escolhemos 5 funcionários, pois estamos fazendo uma entrevista interna.")
print("Vamos precisar de alguns dados de vocês, desde já agradecemos pela colaboração de todos.")
print("Let's go!")

funcionario = []
for i in range(5):
    nome = input("Informe o seu nome: ")
    salario_str = input("Qual o seu salário? ")
    salario = float(salario_str.replace(",", "").replace(",", "."))
    funcionario.append((nome, salario))

salario_maior = 0
funcionario_maior = ""

for nome, salario in funcionario:
    if salario > salario_maior:
        salario_maior = salario
        funcionario_maior = nome

print(f"O funcionário mais bem pago é: {funcionario_maior}, com o salário maior de R${salario_maior}.")

❓ Por que este projeto importa?
Saber aplicar algoritmos simples para resolver problemas do dia a dia empresarial é fundamental. Este código simula um cenário real de RH ou liderança que precisa reconhecer os salários de sua equipe.

🔍 Entradas esperadas
Nome do funcionário (5 vezes)

Valor do salário de cada funcionário

🧪 Exemplo de execução
Olá! colaboradores, escolhemos 5 funcionários, pois estamos fazendo uma entrevista interna.  
Vamos precisar de alguns dados de vocês, desde já agradecemos pela colaboração de todos.  
Let's go!  
Informe o seu nome: Ana  
Qual o seu salário? 2500  
...  
Informe o seu nome: Bruno  
Qual o seu salário? 3700  
...  
O funcionário mais bem pago é: Bruno, com o salário maior de R$3700.0  
