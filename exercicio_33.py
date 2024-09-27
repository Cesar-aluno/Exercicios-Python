'''
33) Ler dois valores e imprimir uma das três mensagens a seguir:

‘Números iguais’, caso os números sejam iguais
‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
‘Segundo maior’, caso o segundo seja maior que o primeiro.
'''

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um valor: "))

if valor1 == valor2:
    print(" Números iguais!")
elif valor1 > valor2:
    print(" Primeiro é maior!")
elif valor2 > valor1:
    print(" Segundo é maior!")
