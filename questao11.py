print('Casas de um Número')
print('--> O Número Precisa ser menor que 1000')
print('--------------------')

num = int(input('Digite o Número: '))
print('--------------------')

#-------------------------------------  
        
def num1():
    if 99 < num < 1000:
        alg1 = num // 100
        alg2 = num % 100 // 10
        alg3 = num % 10
        if alg1 == 1:
            print('1 Centena,', end=' ')
        elif alg1 != 1:
            print(f'{alg1} Centenas,', end=' ')
    
    elif 9 < num < 100:
        alg1 = num // 10
        alg2 = num % 10
        if alg1 == 1:
            print('1 Dezena e', end=' ')
        elif alg1 != 1:
            print(f'{alg1} Dezenas e', end=' ')
    
    elif num < 10:
        if num == 1:
            print('1 Unidade', end=' ')
        elif num != 1:
            print(f'{num} Unidades', end=' ')
    
    else:
        if num >= 1000:
            print('APENAS NÚMEROS INFERIORES A 1000!')
            
def num2():
    
    if 99 < num < 1000:
        alg1 = num // 100
        alg2 = num % 100 // 10
        alg3 = num % 10
        if alg2 == 1:
            print('1 Dezena e', end=' ')
        elif alg2 != 1:
            print(f'{alg2} Dezenas e', end=' ')
     
    elif 9 < num < 100:
        alg1 = num // 10
        alg2 = num % 10
        if alg2 == 1:
            print('1 Unidade', end=' ')
        elif alg2 != 1:
            print(f'{alg2} Unidades', end=' ')
            
def num3():
    if 99 < num < 1000:
        alg1 = num // 100
        alg2 = num % 100 // 10
        alg3 = num % 10
        if alg3 == 1:
            print('1 Unidade', end=' ')
        elif alg3 != 1:
            print(f'{alg3} Unidades', end=' ')
    
#-------------------------------------

num1()
num2()
num3()
