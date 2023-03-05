#entrada
resp = 0
cont = 0

n = int(input("Informe o número que você quer ver a tabuada (de 1 a 10): "))

#processamento 
while n <=10:
    if cont <=10:
        resp = n*cont
        print("{0} x {1} = {2}" .format(n, cont, resp))
        cont = cont+1
    