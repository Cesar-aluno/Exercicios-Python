#22) A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).



horas_mensais = int(input( "Quantas horas foram trabalhadas no mês? "))
salario_hora = float(input( "Qual é o salário por hora? "))


if horas_mensais >40:
    acrescimo = 0.50 * salario_hora
    print(acrescimo)

salario_total = horas_mensais + salario_hora
print( "O salário total é: ",salario_total)    
