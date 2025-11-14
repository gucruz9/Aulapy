from calculadora import calculadora1

#Entrada de dados
raio = float(input("Digite o valor do raio: "))

#Processamento de dados
circunferencia = calculadora1.circunferencia(raio)
area = calculadora1.area(raio)
6

#Saída de dados
print(f''' Circunferência: {circunferencia:.2f}
    Area: {area:.2f}
      PI: {calculadora1.PI}    
''')