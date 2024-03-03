def situaçao():
    def mostrar():
        print('----------------')
        print(f' Nota 1 = {nota1:.1f}')
        print(f' Nota 2 = {nota2:.1f}')
        print(f' Média = {media:.1f}')
        print(f' Conceito = {conceito}')
        
    nota1 = float(input('Digite sua Nota 1: '))
    nota2 = float(input('Digite sua Nota 1: '))
    media = (nota1 + nota2)/2
    
    if 0 < media <= 4:
        conceito = 'E'
        mostrar()
        if conceito == 'E':
            print('__________________')
            print('--> Situação Final = REPROVADO')
            
    elif 4 < media <= 6:
        conceito = 'D'
        mostrar()
        if conceito == 'D':
            print('__________________')
            print('--> Situação Final = REPROVADO')
            
    elif 6 < media <= 7.5:
        conceito = 'C'
        mostrar()
        if conceito == 'C':
            print('__________________')
            print('--> Situação Final = APROVADO')
    
    elif 7.5 < media <= 9:
        conceito = 'B'
        mostrar()
        if conceito == 'B':
            print('__________________')
            print('--> Situação Final = APROVADO')
            
    else:
        conceito = 'A'
        mostrar()
        if conceito == 'A':
            print('__________________')
            print('--> Situação Final = APROVADO')
            
#---------------------------------

print('Situação Escolar')
print('----------------')

situaçao()
