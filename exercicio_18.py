#18) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).
ano_atual = int(input( "O ano atual é: "))
ano_nascimento = int(input( "Ano de nascimento: "))
idade_votar = ano_atual -ano_nascimento
if idade_votar >=18:
    print ("Permitido votar! ")
else:
    print("Não é permitido votar! ")
    
