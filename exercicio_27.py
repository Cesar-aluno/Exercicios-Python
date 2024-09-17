#27) Ler um valor e escrever se é positivo, negativo ou zero.

valor = int(input("Digite o valor: "))
print(" O valor é: ", valor)

if valor >-1 or 0:
    print( valor, "é positivo")
elif valor == 0:
    print( valor, "é zero")
else:
    print( valor, "é negativo")
    
