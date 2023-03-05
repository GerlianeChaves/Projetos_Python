#entrada
maior = 0

n = int(input("Informe um valor: "))

#processamento
while n != 0 :
    if n > maior: 
        maior = n 
    else:
        maio = maior
    
    n = int(input("Informe um valor: "))
    
#saida
print("O maior número é: {0}".format(maior))