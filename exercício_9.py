#9) Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.
salarioMensal_atual = float(input('o salário mensal atual é: '))
reajuste = float(input('o reajuste percentual do salário é: '))

calculando = salarioMensal_atual * (reajuste/100)
novoSalario = salarioMensal_atual + calculando
print ("o novo salário é: ", novoSalario)