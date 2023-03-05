#variáveis
maior = -999
menor = 999
soma = 0

#entrada/processamento
for n in range(1,11):
    v = int(input("Informe um valor: "))
    if v > 0:
        if v > maior:
            maior = v 
        if v < menor:
            menor = v
        soma = soma + v 
    else:
        v = int(input("Informe um valor: "))

med = soma/10

#saida
print("O Maior número é: {0}".format(maior))
print("O menor número é: {0}".format(menor))
print("A média é: {0}".format(med))
 
        
