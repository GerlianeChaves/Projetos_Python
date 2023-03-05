#variaveis
v = []
#pos = []
maior50 = False

for n in range(0, 10):
    num = int(input("Informe {0}/10 valor para o vetor: ".format(n+1))) 
    v.append(num)
for n in v:    
    if n > 50:
        print("O numero {0} é maior que 50 e esta  na posicao {1}".format(n, v.index(n)))
        maior50 = True
#   pos = pos +1
if maior50 == False:
    print("Erro: nenhum numero maior que 50") 

    



