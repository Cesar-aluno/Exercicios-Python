#46) Acrescentar uma mensagem de 'VALOR INVÁLIDO' no exercício [44] caso o segundo valor informado seja ZERO.

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

while valor2 == 0:
    print ("VALOR INVÁLIDO")
    valor2 = int(input("Digite outro valor: "))
    
#Abaixo está o resultado
resultado = valor1/valor2
print(" O resultado é: ", resultado)
