#entrada
idade = int(input("Informe a idade do nadador: "))

#processamento
if idade<=7 and idade >=5:
    #saida
    print("Catergoria Infantil-a")
elif idade<=11 and idade>=8:
    #saida
    print("Caterogia Intanfil-b")
elif idade<=13 and idade>=12:
    #saida
    print("Categoria Juvenil-a")
elif idade<=17 and idade>=14:
    #saida
    print("Categoria Juvenil-b")
elif idade>=18:
    #saida
    print("Categoria Adulto")    
else:
    print("Erro ao informar idade: esta pessoa é muito jovem para comeptir.")
