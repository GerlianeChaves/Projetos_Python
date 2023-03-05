#entrada
p  = float(input("Informe o peso de peixes pescado (kg): "))

#processamento
if p>50:
    e = p-50
    m = e*4
else:
    e = 0
    m = 0

#saida
print("Foram pescados {0:.2f}kg de peixe, {1:.2f}kg exece o valor padrão e por isso a multa é de R${2:.2f}".format(p, e, m))