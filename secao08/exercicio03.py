#variaveis
v = []

#entradas
for n in range(0,10):
    num = int(input("Informe o valor do vetor: "))
    v.append(num)
    
#processamento
v.reverse() #inverte a lista

for n in v:
    print(n)