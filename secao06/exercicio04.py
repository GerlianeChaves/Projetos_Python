#entrada
sx = input("Informe seu sexo: F(feminino) ou M(masculino)")
h = float(input("Informe sua altura em metros: "))

#processamento
if sx.lower() == 'f':
    peso = (62.1*h)-44.7
elif sx.lower() == 'm':
    peso = (72.7*h)-58
else:
    peso = 0
    print("Erro!Tente novamente mais tarde.")
#saida
print("Seu peso ideal é {0:.2f}".format(peso))