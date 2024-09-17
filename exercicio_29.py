#29) Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

valor1 = int(input(" Digite o primeiro valor: "))
valor2 = int(input(" Digite o segundo valor: "))
valor3 = int(input(" Digite o terceiro valor: "))

if valor1 and valor2 > valor3:
    print(" Os maiores valores são ", valor1, 'e', valor2)
    soma = valor1 + valor2
    print(" A soma dos maiores valores é: ", soma)
elif valor2 and valor3 > valor1:
    print(" Os maiores valores são: ", valor2, 'e', valor3)
    soma = valor2 + valor3
    print(" A soma dos maiores valores é: ", soma)
else:
    print(" Os maiores valores são: ", valor1,'e',valor3)
    soma = valor1 + valor3
    print(" A soma dos maiores valores é: ", soma)
