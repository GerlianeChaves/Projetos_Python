#variaveis
v = []

#entrada
cod = int(input("Informe o codigo numerico (1 ou 2): "))
 
#processamento 
if cod != 0:
    for n in range(0, 5):
        num = int(input("informe um valor real: "))
        v.append(num)
    if cod == 1:
        for n in v:
            print(n)
    if cod == 2:
        v.reverse()
        for n in v:
            print(n)
    else:
        print("Erro: código inválido, tente novamente.")
print("Programa encerrado!")