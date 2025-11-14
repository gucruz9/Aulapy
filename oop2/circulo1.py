import calculadora as c

#Instânciação do objeto
circulo = c.calculadora1()

#Entrada de dados
raio = float(input("Digite o valor do raio: "))

#Processamento de dados
circunferencia = circulo.circunferencia(raio)
area = circulo.area(raio)

#Saída de dados
print(f''' Circunferência: {circunferencia::.2f}
      Area: {area:.2f}
      PI: {circulo.PI}    
''')