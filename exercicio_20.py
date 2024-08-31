#20) Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

print( "        Lendo valores !")
primeiro_valor = int(input( "O primeiro valor é: "))
segundo_valor = int(input( "O segundo valor é: "))

if primeiro_valor < segundo_valor:
    print (segundo_valor, primeiro_valor)
else:
    print (primeiro_valor, ',' ,segundo_valor)
