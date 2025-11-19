class Terreno:
    #Membros da classe
    #1º Membro da classe
    __largura:float
    __comprimento:float

    #2º Membro da classe

    #Propriedades largura
    @property
    def largura (self):
        return self.__largura
    @largura.setter
    def largura (self, largura:float):
        self.__largura = largura

    #Propriedades do comprimento 
        @property
        def comprimento(self):
            return self.__comprimento
        @comprimento.setter
        def comprimento(self, comrpimento:float):
            self.__comprimento = comprimento

    #3º Membro - Construtor
    def __init__(self, largura:float, comprimento:float):
        self.comprimento = comprimento
        self.largura = largura 

    #4 Membro - Métodos 
    def __area (self) -> float:
        return self.comprimento * self.largura
    def __preco(self, preco:float) -> float:
        return self.area * preco
    def dadosTerreno(self, preco:float) -> str:
        saida = f'''
        Largua: {self.largura}
        Comprimento: {self.comprimento}
        Area: {self.__area():.2f}
        Preco: {self.__preco(preco):.2f}

'''