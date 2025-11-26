from abc import ABC, abstractmethod

class Contribuintes(ABC):
    #1° Membro da classe - Atributos
    __nome: str
    __rendaAnual: float

    #2° Membro da classe - Propriedade
    #Propriedade do atributo nome
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    #Propriedade do atributo rendaAnual
    @property
    def rendaAnual(self) -> float:
        return self.__rendaAnual

    @rendaAnual.setter
    def rendaAnual(self, rendaAnual: float):
        self.__rendaAnual = rendaAnual

    #3° Membro - Construtor
    def __init__(self, nome: str, rendaAnual: float):
        self.nome = nome
        self.rendaAnual = rendaAnual

    # Método
    @abstractmethod
    def gastoTotalAnual(self) -> float:
        pass

#Subclasse
class PessoaFisica(Contribuintes):
    __gastosSaude: float

    @property
    def gastosSaude(self) -> float:
        return self.__gastosSaude

    @gastosSaude.setter
    def gastosSaude(self, valor: float):
        self.__gastosSaude = valor if valor >= 0 else 0

    def __init__(self, nome: str, rendaAnual: float, gastosSaude: float):
        super().__init__(nome, rendaAnual)
        self.gastosSaude = gastosSaude


    def gastoTotalAnual(self) -> float:
        if self.rendaAnual < 20000.0:
            imposto = self.rendaAnual * 0.15
        else:
            imposto = self.rendaAnual * 0.25

        desconto = self.gastosSaude * 0.5
        return imposto - desconto

#Subclasse
class PessoaJuridica(Contribuintes):
    __numFuncionarios: int

    @property
    def numFuncionarios(self) -> int:
        return self.__numFuncionarios

    @numFuncionarios.setter
    def numFuncionarios(self, valor: int):
        self.__numFuncionarios = valor  if valor >= 0 else 0

    def __init__(self, nome: str, rendaAnual: float, numFuncionarios: int):
        super().__init__(nome, rendaAnual)
        self.numFuncionarios = numFuncionarios

    # Polimorfismo
    def gastoTotalAnual(self) -> float:
        taxa = 0.14 if self.numFuncionarios > 10 else 0.16
        return self.rendaAnual * taxa
#----Fim sub sub classe Pessoa Juridica ----#

#----Inicio codigo principal-------
def main():
    contribuintes = []

    n = int(input("Quantos contribuintes deseja cadastrar? "))

    for i in range(1, n + 1):
        print(f"\nContribuinte #{i}:")
        tipo = input("Pessoa física ou jurídica (f/j)? ")

        nome = input("Nome: ")
        renda = float(input("Renda anual: "))

        if tipo == 'f':
            saude = float(input("Gastos com saúde: "))
            contribuintes.append(PessoaFisica(nome, renda, saude))
        else:
            funcionarios = int(input("Número de funcionários: "))
            contribuintes.append(PessoaJuridica(nome, renda, funcionarios))

    print("\nIMPOSTOS PAGOS:")
    total = 0

    for c in contribuintes:
        imposto = c.gastoTotalAnual()
        total += imposto
        print(f"{c.nome}: R$ {imposto:.2f}")

    print(f"\nTOTAL DE IMPOSTOS ARRECADADOS: R$ {total:.2f}")

if __name__ == "__main__":
    main()
