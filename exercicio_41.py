#41) Faça um algoritmo para ler as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula abaixo e escrever o conceito do aluno de acordo com a tabela de conceitos mais abaixo:

#Média_de_aproveitamento = N1 + N2 * 2 + N3 * 3 /7 

nota1 = float(input("Digite a primeira nota: ")) 
nota2 = float(input("Digite a segunda nota: ")) 
nota3 = float(input("Digite a terceira nota: ")) 

media_aproveitamento = nota1 + (nota2 * 2 ) + (nota3 * 3 ) / 7
print('a média é {:.2f}'.format(media_aproveitamento))

if media_aproveitamento >=9:
    print("Nota A!")
elif media_aproveitamento >= 7.5 and media_aproveitamento < 9:
    print("Nota B!")
elif media_aproveitamento >= 6 and media_aproveitamento<7.5:
    print("Nota C!")
elif media_aproveitamento < 6:
    print("Nota D!")
