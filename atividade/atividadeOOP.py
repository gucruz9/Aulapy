
class pessoa:


    #Construtor
    def __init__(self, nome:str, idade: int):
        self.nome1 = nome
        self.idade1 = idade
        self.nome2 = nome
        self.idade2 = idade
    

    #Metodos
        def maior_idade(self, idade):
            if self.idade > idade:
                maior_idade = self.idade 
            elif self.idade < idade:
                maior_idade = self.idade
        maior_idade = "A idade das duas pessoas são iguais."

        def p_maior_idade(self, idade, nome):
            if self.idad1 > idade:
                p_maior_idade = self.idade 
            elif self.idade < idade:
                p_maior_idade = self.idade
                return nome 
            else: 
                return " p;"
        
        saida = f'''
            Dados das pessoas:
            \tNome da 1º Pessoa {self.nome}
            \tIdade da 1º Pessoa {self.idade}

            \tNome da 2º Pessoa {self.nome}
            \tIdade da 2º Pessoa {self.idade}
    
            \t Pessoa com a maior idade {self.p_maior_idade()}com {self.maior_idade()} anos.
            '''
        return saida