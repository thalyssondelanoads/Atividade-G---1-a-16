def media():
    media = (nota1 + nota2) / 2
    
    if media == 10:
        print('MÉDIA = 10, Aprovado com Distinção')
    
    elif media >= 7:
        print(f'MÉDIA = {media}, Aprovado')
    
    else:
        print(F'MÉDIA = {media}, Reprovado')
    
#-------------------------------- 
    
print('Analisar Situação')
print('------------')

nota1 = float(input('Digite a Nota 1: '))
nota2 = float(input('Digite a Nota 2: '))
print('------------')

media()
