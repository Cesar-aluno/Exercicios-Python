    #36) Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e a soma das idades do homem mais novo com a mulher mais velha.

homem1 = int(input("Digite a idade do primeiro homem: "))
print(" O primeiro homem tem", homem1, 'anos.')
homem2 = int(input("Digite a idade do segundo homem: "))
print(" O segundo homem tem", homem2, 'anos.')
mulher1 = int(input("Digite a idade da primeira mulher: "))
print(" A primeira mulher tem", mulher1, 'anos.')
mulher2 = int(input("Digite a idade da segunda mulher: "))
print(" A segunda mulher tem", mulher2, 'anos.')

    #Qual é o homem mais velho?
if homem1 > homem2:
    homem_maior = homem1
else:
    homem_maior = homem2

    #Qual é a mulher mais nova?
if mulher1 < mulher2:
    mulher_menor = mulher1
else:
    mulher_menor = mulher2   

    #Qual é o homem mais novo?
if homem1 < homem2:
    homem_menor = homem1
else:
    homem_menor = homem2

    #Qual é a mulher mais velha?
if mulher1 > mulher2:
    mulher_maior = mulher1
else:
    mulher_maior = mulher2    

soma1 = homem_maior + mulher_menor
print(" O resultado da soma do homem mais velho com a mulher mais nova é: ", soma1)
soma2 = homem_menor + mulher_maior
print(" O resultado da soma do homem mais novo com a mulher mais velha é: ", soma2)
