#31) Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo. OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados.

valorA = int(input(" Digite um número inteiro: ")) 
valorB = int(input(" Digite um número inteiro: ")) 
valorC = int(input(" Digite um número inteiro: ")) 


if valorA < valorB + valorC and valorB < valorA + valorC and valorC < valorA + valorB:
    print (" É um triângulo!")
else:
    print(" Não é um triângulo!")
