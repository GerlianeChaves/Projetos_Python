#entrada
c = input("Informe o código: ")
n = int(input("Informe a quantidade de horas trabalhadas: "))

#processamento
if n > 50:
    e = (n-50)
    e_s = e*20
    s = e_s+((n-e)*10)
else:
    e = 0
    s = n*10

#saida
print("Foram trabalhadas {0}h, com {1}h extras e por isso o salário é R$ {2:.2f}".format(n, e, s))