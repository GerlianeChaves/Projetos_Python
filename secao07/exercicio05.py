#entrada
usr = input("Informe o usuário: ")
senha = input("Informe a senha: ")
 
#processamento
while usr == senha:
    #saida
    print("Senha precisa ser diferente do nome de usuário. Tente novamente.")
    usr = input("Informe o usuário: ")
    senha = input("Informe a senha: ")
    if senha != usr:
        #saida
        print("Login efetuado com sucesso!") 

