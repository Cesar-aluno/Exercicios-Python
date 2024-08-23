#10) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor. 

custo_fabrica = float(input('O custo de fábrica do carro é: R$ '))
print (custo_fabrica)
percentual = float(input ('Qual o percentual do distribuidor? '))
print ('O percentual é: ', percentual, '%')
impostos = float(input ('E quais os impostos?: '))
print ('Os impostos são: ', impostos, '%')

calcular_percentual = custo_fabrica * (percentual/100)
calcular_impostos = custo_fabrica * (impostos/100)

custo_final = custo_fabrica +  calcular_percentual + calcular_impostos
print ('O custo de um carro novo é: R$',custo_final)