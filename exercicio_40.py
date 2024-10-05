#40) Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 

produto = input("Digite o produto: ")
print(" O produto é: ", produto)
quantidade_adquirida = int(input("Digite a quantidade adquirida: "))
print(" A quantidade adquirida é: ", quantidade_adquirida)
preco_unitario = float(input("Digite o preço unitário: "))
print(" O preço unitário é: ", preco_unitario )
total = quantidade_adquirida * preco_unitario
print(" O total é: ", total)
'''
- Se quantidade <= 5 o desconto será de 2%
- Se quantidade > 5 e quantidade <=10 o desconto será de 3%
- Se quantidade > 10 o desconto será de 5%
'''
if quantidade_adquirida <= 5:
    desconto = 0.02 * preco_unitario
if quantidade_adquirida > 5 and quantidade_adquirida <=10:
    desconto = 0.03 * preco_unitario
if quantidade_adquirida >10:
    desconto = 0.05 * preco_unitario
    
totalPagar = total - desconto
print(" O total a pagar será de: ", totalPagar)
