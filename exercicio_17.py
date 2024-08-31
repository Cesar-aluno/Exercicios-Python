#17) Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

print ( "           Aluno 1")
nota1 = float(input( "Avaliando primeira nota: "))
nota2 = float(input( "Avaliando segunda nota: "))
nota3 = float(input( "Avaliando terceira nota: "))
nota4 = float(input( "Avaliando quarta nota: "))

total = nota1 + nota2 + nota3 + nota4
media = total / 4 
if media >= 6:
    print ('       Aprovado')
else:
    print ('      Reprovado')

    
print ( "           Aluno 2")
nota1 = float(input( "Avaliando primeira nota: "))
nota2 = float(input( "Avaliando segunda nota: "))
nota3 = float(input( "Avaliando terceira nota: "))
nota4 = float(input( "Avaliando quarta nota: "))

total = nota1 + nota2 + nota3 + nota4
media = total / 4 
if media >= 6:
    print ('       Aprovado')
else:
    print ('      Reprovado')
