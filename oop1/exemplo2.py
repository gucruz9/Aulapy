import produtoOOP as p #Importar modulo
p1 = p.Produto() #Instaciar o objeto

#Entrada de dados
print("Digite os dados do produto:")
p1.nome = input("\tNome:")
p1.preco = float(input("\tPreço: R$"))
p1.saldo = int(input("\Quantidade: "))

#Saída de dados
print (p1.dadosDoProduto())

#Adicionar produtos 
q = int(input ("Digite o número de produtos a ser adicionado ao estoque: "))
p1.adicionarProdutos(q)

#Saída de dados 2
print ("---Dados atualizados---")
print (p1.dadosDoProduto)

#Remover produtos
q = int(input ("Digite o número de produtos a ser removido do estoque: "))
p1.removerProdutos(q)
#Saída de dados 3
print ("---Dados atualizados---")
print (p1.dadosDoProduto)