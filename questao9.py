def dia():
    def mostrar():
        print(f'--> {dia}')
        
    dia = int(input('Digite o Dia da Semana: '))
    
    if dia == 1:
        dia = 'Domingo'
        mostrar()
    
    elif dia == 2:
        dia = 'Segunda'
        mostrar()
    
    elif dia == 3:
        dia = 'Terça'
        mostrar()
        
    elif dia == 4:
        dia = 'Quarta'
        mostrar()
    
    elif dia == 5:
        dia = 'Quinta'
        mostrar()
        
    elif dia == 6:
        dia = 'Sexta'
        mostrar()
        
    elif dia == 7:
        dia = 'Sábado'
        mostrar()
        
    else:
        print('--> Valor Inválido')

#----------------------------------

print('Dia da Semana')
print('---------------')
