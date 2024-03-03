print('Preço do Combustível')
print('------------------')
print('G - Gasolina = R$ 2,50/L')
print('A - Álcool = R$ 1,90/L')
print('------------------')

combustivel = str(input('Escolha o Tipo de Combustível: '))
litros = int(input('Quantos Litros? : '))

#-------------------------------------

def valor():
    if combustivel == 'A':
        if litros <= 20:
            preço = (1.90 - (1.90 * 3/100)) * litros
            print(f' Preço = R$ {preço:.2f} ')
        elif litros > 20:
            preço = (1.90 - (1.90 * 5/100)) * litros
            print(f' Preço = R$ {preço:.2f} ')
            
    elif combustivel == 'G':
        if litros <= 20:
            preço = (2.50 - (2.50 * 4/100)) * litros
            print(f' Preço = R$ {preço:.2f} ')
        
        elif litros > 20:
            preço = (2.50 - (2.50 * 6/100)) * litros
            print(f' Preço = R$ {preço:.2f} ')
    
    else:
        print('Valor Inválido!')
    
#------------------------------------------------

print('------------------')
valor()
