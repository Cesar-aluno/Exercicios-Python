'''
8) Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

Inputs

Qual a quantidade de votos brancos?
nulos?
válidos?
============================================
Output
Total de porcentagens

Total de votos válidos: x%
Total de votos em branco: y%
Total de votos nulos: t%
'''

votosValidos = int(input("quantos votos validos? "))
votosBrancos = int(input("quantos votos brancos? "))
votosNulos = int(input("quantos votos nulos? "))

totalDeVotos = votosValidos + votosBrancos + votosNulos

porcentagemValidos = (votosValidos / totalDeVotos ) * 100
porcentagemBrancos = (votosBrancos / totalDeVotos ) * 100
porcentagemNulos = (votosNulos / totalDeVotos) * 100

#x = float (((total * (52/100)) + (total * 0,52)))
#y = float (total * (30/100) + total * 0,32)
#t = float (total * (18/100) + total * 0,18)

print ("votos validos: ", porcentagemValidos, "%")
print ("votos brancos: ", porcentagemBrancos, "%")
print ("votos nulos: ", porcentagemNulos, "%")
#print ("votos brancos: ", y)
#print ("votos nulos: ", t)



 