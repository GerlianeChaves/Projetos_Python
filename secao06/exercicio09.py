#entrada
indc = float(input("Informe o índice: "))

#processamento
if indc >= 0.3 and indc < 0.4:
    #saida
    print("Notificar Grupo 1")
    
elif indc >= 0.4 and indc < 0.5:
    #saida
    print("Notificar Grupos 1 e 2")
    
elif indc >= 0.5:
    #saida
    print("Notificar Grupos 1, 2 e 3")
    
else:
    print("Padrões Normais")