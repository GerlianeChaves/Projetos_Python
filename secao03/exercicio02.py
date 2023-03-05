#entradas
input("Informe a peça: ")
estq_min = int(input("Informe a quantidade minina: "))
estq_max = int(input("Informe a quantidade maxima: "))

#processamento
estq = (estq_min+estq_max)/2

#saida
print("A quantidade de peças em estoque é: {0}".format(estq))