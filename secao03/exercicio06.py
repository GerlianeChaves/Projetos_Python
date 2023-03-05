h = float(input("Quanto você ganha por hora? "))
h_m = float(input("Quantas horas você trabalha por mês? "))

money = h*h_m

print("Seu salário desse mês é de R$ {0:.2f}".format(money))