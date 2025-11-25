from abc import ABC, abstractmethod
from enum import Enum 

class Cor(Enum):
    VERMELHO = "Vermelho"
    AZUL = "Azul"
    VERDE = "Verde"
    AMARELA = "Amarela"

class Forma(ABC):
    __cor:Cor
    @abstractmethod
    def area(self) ->float:
        pass

class Circulo(Forma):
    __raio:float

    @property
    def _raio(self) -> float:
        return self.__raio
    
    @_raio.setter
    def _raio(self, raio:float) -> float:
        self.__raio = raio

        def __init__(self, raio:float, cor:Cor):
            self._raio = raio
            self.__cor = cor

        def area (self) -> float:
            from math import pi
            return pi * (self._raio ** 2)
        