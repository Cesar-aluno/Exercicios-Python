#36) Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.

homem1 = int(input("Digite a idade do primeiro homem: "))
print(" O primeiro homem tem", homem1, 'anos.')
homem2 = int(input("Digite a idade do segundo homem: "))
print(" O segundo homem tem", homem2, 'anos.')
mulher1 = int(input("Digite a idade da primeira mulher: "))
print(" A primeira mulher tem", mulher1, 'anos.')
mulher2 = int(input("Digite a idade da segunda mulher: "))
print(" A segunda mulher tem", mulher2, 'anos.')

if homem1 > homem2 and mulher1 > mulher2:
    print(" O resultado é: ", soma)
elif homem2 > homem1 and mulher2 > mulher1:
    soma = homem2 + mulher1
    print(" O resultado é: ", soma)
