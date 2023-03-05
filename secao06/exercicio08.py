#entrada
n = int(input("Informe um número: "))

#processamento
if n%2 == 0:
    tipo = "par"
else:
    tipo = "impar"
    
if n>0:
    t1 = "positivo"
else:
    t1 = "negativo"
    
#saida
print("O valor {0} é número {1} e {2}".format(n, tipo, t1))