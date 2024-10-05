#38) Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a mensagem ‘Usuário inválido!’. Caso o Código seja correto, deve ser lido outro valor que é a senha. Se esta senha estiver incorreta (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’. Caso a senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’.

#Login de usuário
codigo_usuario = input("Digite o código: ")

if codigo_usuario == '1234':
    senha = int(input("Digite a senha: "))
else:
    print(" Usuário inválido!")
if senha == '9999':
    print(" Acesso permitido!")
else:    
    print(" Senha incorreta!") 
