#25) Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

numero_conta = input("Número da conta do cliente: ")
print(numero_conta)
saldo = float(input("Saldo: "))
print(saldo)
debito = float(input("Débito: "))
print(debito)
credito = float(input("Crédito: "))
print(credito)

saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    print(" Saldo Positivo !")
else:
    print(" Saldo Negativo !")
