def saudaçao():
    if turno == 'M':
        print('Bom Dia!')
    elif turno == 'V':
        print('Boa Tarde!')
    elif turno == 'N':
        print('Boa Noite!')
    else:
        print('Valor Inválido')
        
#---------------------------------

print('Saudação')
print('-----------')

turno = str(input('Digite o seu Turno de Estudo ( M, V ou N ): '))
print('-----------')

saudaçao()
