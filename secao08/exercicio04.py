#variaveis
v = []
#soma = []

#entradas
for n in range(0, 20):
    num = int(input("Informe {0}/20 valor para o vetor: ".format(n+1)))
    v.append(num)
#   soma = soma + num
    
print("A soma do vetor e {0}".format(sum(v)))
    
    