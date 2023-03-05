#entrada
n1 = int(input("Informe o n1: "))
n2 = int(input("Informe o n2: "))
n3 = int(input("Informe o n3: "))
n4 = int(input("Informe o n4: "))

#processamento
    #quadrados
q1 = n1**2
q2 = n2**2
q3 = n3**2
q4 = n4**2

if q3 >=1000:
    print("O q3 é: ", q3)
else:
    print("Os números são:", n1,n2,n3,n4)
    print("Os quadrados são: ", q1,q2,q3,q4)