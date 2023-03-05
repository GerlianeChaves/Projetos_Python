#entrada
n = int(input("Informe um número: "))
p = 0
i = 0

#processamento
if n%2==0:
    p = n
else:
    i = n
    
#saida
print("O valor par é {0} e o valor impar é {1}".format(p,i))