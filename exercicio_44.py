#44) Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero e imprimir o resultado da divisão do primeiro valor lido pelo segundo valor lido. (utilizar a estrutura REPITA).

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

while valor2 == 0:
    valor2 = int(input("Digite outro valor: "))
#if valor2 != 0 and valor2 >0:
resultado = valor1/valor2
print(" O resultado é: ", resultado)
