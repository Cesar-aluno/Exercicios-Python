#11) Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa de R$700,00 para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.

quantidade = int(input ('A quantidade de carros vendidos é: '))
print (quantidade)
vendas = float(input('Qual o valor das vendas?: '))
print ('O valor das vendas é: R$', vendas)
total_vendas = vendas * quantidade
print ('o valor total de vendas é:', total_vendas)

salario_fixo = float(input('Qual o salário fixo? '))
print ("O salário fixo é: R$", salario_fixo)
porcentagemVenda = 5
comissao = 700 
salario_final = quantidade + comissao + (vendas/porcentagemVenda) + salario_fixo
print ('O salário final é: R$', salario_final)
