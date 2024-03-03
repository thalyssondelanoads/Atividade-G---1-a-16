def desconto():
    def resultados():
        print(f'Salário Bruto = R$ {bruto:.2f}')
        print(f' (-) IR({ir}) = R$ {ir_calculo:.2f}')
        print(f' (-) INSS(10%) = R$ {inss:.2f}')
        print(f' FGTS(11%) = R$ {fgts:.2f}')
        print(f' Total de Descontos = R$ {desconto:.2f}')
        print('________________________')
        print(f'--> Salário Líquido = R$ {salario:.2f}')
    
    hora = int(input('Horas Trabalhadas no Mês: '))
    valor_hora = float(input('Valor por Horas Trabalhadas: '))
    bruto = hora * valor_hora
    
    if bruto <= 900:
        ir = '0%'
        ir_calculo = bruto * 0
        inss = bruto * 1/10
        fgts = bruto * 11/100
        desconto = ir_calculo + inss
        salario = bruto - desconto
        print('----------------------')
        resultados()
    elif 900 < bruto <= 1500:
        ir = '5%'
        ir_calculo = bruto * 1/20
        inss = bruto * 1/10
        fgts = bruto * 11/100
        desconto = ir_calculo + inss
        salario = bruto - desconto
        print('----------------------')
        resultados()
        
    elif 1500 < bruto <= 2500:
        ir = '10%'
        ir_calculo = bruto * 1/10
        inss = bruto * 1/10
        fgts = bruto * 11/100
        desconto = ir_calculo + inss
        salario = bruto - desconto
        print('----------------------')
        resultados()
    
    else:
        ir = '20%'
        ir_calculo = bruto * 1/5
        inss = bruto * 1/10
        fgts = bruto * 11/100
        desconto = ir_calculo + inss
        salario = bruto - desconto
        print('----------------------')
        resultados()
        
#-----------------------------------

print('Desconto de Salário')
print('----------------------')

desconto()
