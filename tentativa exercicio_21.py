#21) Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte. 

inicio_hora = int(input(" Digite a hora de início do jogo: "))
fim_hora = int(input(" Digite a hora de fim do jogo: "))
print(" O jogo inicia às: ", inicio_hora, "hs")
print(" O jogo termina às: ", fim_hora, "hs")

if inicio_hora > fim_hora:
    duracao = fim_hora - inicio_hora
    print(" O jogo durou", duracao, "hs" )
else:
    duracao = 24 - inicio_hora + fim_hora
    print(" O jogo durou", duracao, "hs" )
    
