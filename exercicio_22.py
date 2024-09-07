#22) A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).



horas_semanais = int(input(" Quantas horas foram trabalhadas na semana? "))
salario_hora = float(input( " Digite o salário por hora:  "))
print(" O salário por hora é: ",salario_hora)
horasMensais = horas_semanais * 4 
print(" O número de horas trabalhadas no mês é: ",horasMensais, 'horas' )

if horas_semanais >40:
    acrescimo = 0.50 * salario_hora
    print(" O valor do acréscimo é: ",acrescimo)
    salario_total = horas_semanais + salario_hora + acrescimo
    print(" O salário total é: ",salario_total) 
else:
    salario_total = horas_semanais + salario_hora
    print(" O salário total é: ",salario_total) 
    

