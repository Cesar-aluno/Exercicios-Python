#24) Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

salario_fixo = float(input(" Qual é o salário fixo: "))
print("O salário fixo é: ", salario_fixo)
vendas = float(input(" Digite o valor das vendas: "))
print(" O valor das vendas é: ", vendas)
comissao = 0.03 * vendas
if vendas > 1500:
    comissao = 0.05 * vendas

salarioTotal = salario_fixo + vendas + comissao  
print(" O salário total é: ", salarioTotal)
