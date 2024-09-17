#28) Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

valor1 = input(" Digite o primeiro valor: ")
valor2 = input(" Digite o segundo valor: ")
valor3 = input(" Digite o terceiro valor: ")

if valor1 > valor2 and valor1 > valor3:
    print(" O maior valor é ", valor1)
elif valor2 > valor1 and valor2 > valor3:
    print(" O maior valor é ", valor2)
else:
    print(" O maior valor é ", valor3)
