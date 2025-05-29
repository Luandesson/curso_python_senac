# ⚕️ Saúde Digital - Cálculo do IMC

Neste projeto, você atuará como um agente da Saúde Tech com a missão de ajudar os usuários a descobrirem se estão com o peso ideal usando um programa simples em Python.

## 🎯 Propósito

- Coletar dados do usuário relacionados à saúde (peso e altura).
- Calcular o IMC (Índice de Massa Corporal).
- Informar ao usuário se ele está acima do peso ou com peso ideal.
- Promover consciência sobre hábitos saudáveis por meio da tecnologia.

```python
# Exemplo de execução em Python
nome = input("Olá, para sabermos o seu peso ideal, me informe o seu nome: ")
peso = float(input("Me informe o seu peso em (kg): "))
altura = float(input("Qual a sua altura? "))

IMC = peso / altura
if IMC > 25:
    print(f"Ops! {nome}, Acima do peso.")
else:
    print(f"OBA! {nome}, seu peso esta OK, seu IMC é: {IMC}. Você está no caminho certo! ")

🧮 Como o cálculo funciona?
IMC = peso ÷ altura

O resultado é comparado com a faixa padrão de IMC. Se for superior a 25, o usuário é considerado acima do peso.

🧪 Exemplo de execução
Olá, para sabermos o seu peso ideal, me informe o seu nome: João  
Me informe o seu peso em (kg): 85  
Qual a sua altura? 1.70  
Ops! João, Acima do peso.

🌱 Benefício
Essa ferramenta básica pode ser expandida para soluções maiores de monitoramento de saúde e bem-estar no futuro.
