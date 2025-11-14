import produtoOOP as p #Importar modulo
p1 = p.Produto() #Instaciar o objeto

#Entrada de dados
print("Digite os dados do produto:")
p1.nome = input("\tNome:")
p1.preco = float(input("\tPreço: R$"))
p1.saldo = int(input("\Quantidade: "))

#Saída de dados
print ("Dados do produto")
print (f"\tNome do produto: {p1.nome}")
print (f"\tValor de compra: {p1.preco}")
print (f"\tQuantidade em estoque {p1.saldo}")
print (f"\tValor total em estoque: R$ {p1.valorTotalEmEstoque()}")