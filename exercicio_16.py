#16) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

compra = int(input( "Digite o número de maçãs compradas: "))
if compra <12:  
    valor = 1.30
else:
    valor = 1.00
calcular = compra * valor
print ("O custo total de maçãs é: ", calcular)
