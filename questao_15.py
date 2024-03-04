print('Preços da Frutaria')
print('-------------------')
print('Morango - R$ 2,50 por KG')
print('Maçã - R$ 1,80 por KG')
print('-------------------')

morango = int(input('Quantos Quilos de Morango Deseja? : '))
maça = int(input('Quantos Quilos de Maçã Deseja? : '))

#--------------------------------

def preço_final():
    def preço_morango():
        if morango <= 5:
            return 2.50 * morango
        else:
            return 2.20 * morango
    
    def preço_maça():
        if maça <= 5:
            return 1.80 * maça
        else:
            return 1.50 * maça
    
    valor_maça = preço_maça()
    valor_morango = preço_morango()
    preço = valor_maça + valor_morango
    
    if maça + morango > 8 or preço > 25:
        desconto = preço - (preço * 1/10)
        print(f'Valor = R$ {desconto:.2f} ')
    
    else:
        print(f'Valor = R$ {preço:.2f} ')
        
#----------------------------------
  
print('-------------------')
preço_final()
