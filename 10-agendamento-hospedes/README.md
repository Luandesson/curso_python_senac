# 🏨 Sistema de Agendamento de Hóspedes - Rede de Hotéis Senac RJ

Este programa auxilia os atendentes a calcular o valor total da hospedagem, garantindo que o número total de pessoas (adultos + crianças) não ultrapasse 4 e que a estadia não exceda 30 dias.

## 🎯 Propósito

- Validar as regras de hospedagem (máximo de 4 pessoas e 30 dias).
- Calcular o valor total da hospedagem com base na modalidade escolhida (Standard ou Luxo).
- Aplicar descontos progressivos conforme a quantidade de dias.
- Gerar um resumo da reserva com dados do hóspede.

```python
# Criar um programa de agendamento para hospedes 
# Regra 1 - O número total de pessoas (adulto + kids) não pode passar de 4 pessoas
# Regra 2 - Máximo de 30 dias de hospedagem 

print("Bem-vindo à rede de hoteis Senac RJ")

# Entrada de dados da acomodação
tipo = input(" Tipo de acomodação  (Standard ou Luxo) ?? ")
adulto = int(input("Quantos adultos? "))
kids = int(input("Quantas crianças? "))
dias = int(input("Quantos dias? "))

# Estruturas de repetição - validação das regras
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
        print("Tipo de acomodação inválida.")
        exit()
        
    valor_total = (adulto * preco_adulto + kids * preco_kids) * dias  # Cálculo do valor total antes do desconto 
    
    # Cálculo para o desconto
    if dias > 10:
        desconto = valor_total * 0.10
    elif dias > 6:
        desconto = valor_total * 0.08
    else:
        desconto = valor_total * 0.05
        
    valor_desconto = valor_total - desconto  # Cálculo com desconto
    valor_desconto_br = f"{valor_desconto:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    
    # Cadastro do hóspede 
    nome = input("Olá, informe seu nome completo: ")
    email = input("Informe o seu e-mail:  ")
    
    # Resumo da hospedagem
    print("\nAQUI ESTÁ O RESUMO DA RESERVA DE HOSPEDAGEM")
    print(f"TIPO ACOMODAÇÃO:............: {tipo.title()}")
    print(f"QUANTIDADE DE ADULTOS:......: {adulto}")
    print(f"QUANTIDADE DE CRIANÇAS:.....: {kids}")
    print(f"QUANTIDADE DE DIAS:.........: {dias}")
    print(f"VALOR TOTAL:..............: R${valor_desconto_br}")
```
❓ Como o programa funciona?

Entrada de dados: O sistema coleta a modalidade da acomodação, o número de adultos, crianças e dias de hospedagem.

Validação: Verifica se o total de pessoas não ultrapassa 4 e se a estadia não excede 30 dias.

Cálculo: Define preços para acomodações Standard e Luxo, calcula o valor total e aplica desconto conforme a duração da hospedagem.

Resumo: Exibe um resumo detalhado da reserva, incluindo os dados cadastrados do hóspede.

🔍 Exemplo de Execução

Bem-vindo à rede de hoteis Senac RJ

 Tipo de acomodação  (Standard ou Luxo) ?? Standard
Quantos adultos? 2
Quantas crianças? 1
Quantos dias? 8
Olá, informe seu nome completo: Maria Silva
Informe o seu e-mail: maria@mail.com


AQUI ESTÁ O RESUMO DA RESERVA DE HOSPEDAGEM

TIPO ACOMODAÇÃO:............: Standard
QUANTIDADE DE ADULTOS:......: 2
QUANTIDADE DE CRIANÇAS:.....: 1
QUANTIDADE DE DIAS:.........: 8
VALOR TOTAL:..............: R$XXXX,XX

💡 Possíveis Melhorias
Adicionar validação de dados de entrada.

Expandir o cardápio de tipos de acomodação.

Implementar interface gráfica para facilitar o agendamento.

Desenvolvido por Luandesson Alves 🇧🇷
