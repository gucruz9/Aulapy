class Produto:
    #Atributos
    nome: str
    preco: float
    saldo: int

    #Contrutor
    def __init__(self, nome:str, preco:float,):
        self.nome = nome
        self.preco = preco
        self.saldo = 0

    #Construtor
    def __init__(self, nome:str, preco:float, saldo:int = 0):
        self.nome = nome
        self.preco = preco
        self.saldo = saldo
    


    #Metodos
    def  valorTotalEmEstoque(self) -> float:
        return self.preco * self.saldo
    def adicionarProdutos(self, quantidade) -> int:
        self.saldo = self.saldo + quantidade
        return self.saldo
    def removerProdutos  (self, quantidade) -> int:
        self.saldo = self.saldo - quantidade
    def dadosDoProduto(self) -> str:
        saida = f'''
            Dados do produto:
            \tNome do produto: {self.nome}
            \tValor de compra do produto; R$ {self.preco}
            \tQuantidade em estoque: {self.saldo}
            \tValor total em estoque: R$ {self.valorTotalEmEstoque():.2f}
            '''
        return saida