def reajuste():
    def resultados():
        print(f'Salário Inicial = R$ {salario:.2f} ')
        print(f'Percentual de Aumento = {aumento} ')
        print(f'Valor do Aumento = R$ {valor_aumento:.2f} ')
        print(f'Salário com Aumento = R$ {reajuste:.2f} ')
    
    salario = float(input('Digite o seu Salário: ')) 
    
    if salario <= 280:
        aumento = '20%'
        valor_aumento = salario * 2/10
        reajuste = (salario * 2/10) + salario
        print('---------------')
        resultados()
        
    elif 280 < salario <= 700:
        aumento = '15%'
        valor_aumento = salario * 15/100
        reajuste = (salario * 15/100) + salario
        print('---------------')
        resultados()
    
    elif 700 < salario <= 1500: 
        aumento = '10%'
        valor_aumento = salario * 1/10
        reajuste = (salario * 1/10) + salario
        print('---------------')
        resultados()
    
    else:
        aumento = '5%'
        valor_aumento = salario * 1/20
        reajuste = (salario * 1/20) + salario
        print('---------------')
        resultados()
        
#-----------------------------

print('Reajuste de Salário')
print('---------------')

reajuste()
