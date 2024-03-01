def produto():
    if produto1 < produto2 and produto1 < produto3:
        print('O Produto 1 é o mais Barato')
    
    elif produto2 < produto1 and produto2 < produto3:
        print('O Produto 2 é o mais Barato')
        
    else:
         print('O Produto 3 é o mais Barato')
    
#-------------------------------- 
    
print('Escolher Produto')
print('------------')

produto1 = float(input('Digite o Valor do Produto 1: '))
produto2 = float(input('Digite o Valor do Produto 2: '))
produto3 = float(input('Digite o Valor do Produto 3: '))
print('------------')

produto()
