#32) Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time1 = int(input("Digite o número de gols: "))
time2 = int(input("Digite o número de gols: "))

if time1 > time2:
    print(" Time 1 é o vencedor!")
elif time2 > time1:
    print(" Time 2 é o vencedor!")
else:
    print("EMPATE!")
