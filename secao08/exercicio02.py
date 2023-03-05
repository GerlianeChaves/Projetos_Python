#variaveis
v1 = []
v2 = []
soma = []

#entrada/processamento
for n in range(0, 10):
    n1 = int(input("Informe o valor do vetor 1: "))
    v1.append(n1)
    n2 = int(input("Informe o valor do vetor 2: "))
    v2.append(n2)
    soma.append(n1+n2)
    
for n in soma:
    print(n)
