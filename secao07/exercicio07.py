#entrada
cont = 0 
cont1 =0 
cont2 =0 
cont3 =0 
cont4 = 0

cod = int(input("Informe o código do objeto: "))

#processamento
while cod != 0:
    print("Informe o defeito apresetado: ")
    print("1- Necessita de esfera                    2- Necessita de limpeza ")
    print("3- Necessita de troca de cabo/conector    4- Quebrado/Inutilizado ")
    print("0 - para encerrar o programa")
    #entrada
    deft = input("Defeito: ")
        
    #processamento
    if deft == 1:
        cont1 = cont1+1
    elif deft == 2:
        cont2 = cont2+1
    elif deft == 3:
        cont3 = cont3+1
    elif deft == 4:
        cont4 = cont4+1
    cont = cont+1
    cod = int(input("Informe o código do objeto: "))
    #else:
     #  print("Erro: Tente novamente")  

print(cont1, cont2, cont3, cont4)        
quant = cont
p1 = cont1/(cont*100)
p2 = cont2/(cont*100)
p3 = cont3/(cont*100)
p4 = cont4/(cont*100)

#saida
print("Quantidade de Mouses: {0}".format(quant))
print("Situação:                              | Quantidade             | Percentual           ")
print("1- Necessita de esfera                 | {0}                    | {1}%           ".format(cont1, p1))   
print("2- Necessita de limpeza                | {0}                    | {1}%           ".format(cont2, p2))
print("3- Necessita de troca de cabo/conector | {0}                    | {1}%           ".format(cont3, p3))
print("4- Quebrado/Inutilizado                | {0}                    | {1}%           ".format(cont4, p4))
    