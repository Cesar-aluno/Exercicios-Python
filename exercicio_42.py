'''
42) Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito: 

- Ter no mínimo 65 anos de idade.
- Ter trabalhado no mínimo 30 anos.
- Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
'''

pessoa = input("Digite o sexo da pessoa: ")
idade = int(input("Digite a idade: "))
tempoTrabalhado = float(input("Digite o tempo trabalhado: "))

if pessoa == "Homem" or pessoa == 'H' or pessoa == 'h':
    print(" Um homem solicita aposentadoria!")
elif pessoa == "Mulher" or pessoa == 'M' or pessoa == 'm':
    print(" Uma mulher solicita aposentadoria!")
else:
    print(" Valor inválido!")
if idade >= 65:
    print(" Candidato para aposentadoria!")
else:
    print(" Rejeitado para aposentadoria!")
if tempoTrabalhado >= 30:
    print(" Aprovado para aposentadoria!")

if idade >= 60:
    print(" Candidata para aposentadoria!")
if tempoTrabalhado >= 25:
    print(" Aprovada para aposentadoria!")

