#7) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
mes = 30
ano = 365
print ("Expressando a idade em anos: ")
idade_em_anos = int(input ("Minha idade em anos é: "))

print ("Expressando a idade em meses: ")
idade_em_meses = input ("Minha idade em meses é: " + str(mes * idade_em_anos))

print ("Expressando a idade em dias: ")
input ("Minha idade em dias é: " + str (idade_em_anos * ano))

