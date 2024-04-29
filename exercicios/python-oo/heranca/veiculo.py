from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        return f"Marca: {self._marca}, Modelo {self._modelo}, Status: {self.ligado}"

    @property
    def ligado(self):
        return f"Ligado" if self._ligado == True else "desligado"

    @abstractmethod
    def ligar(self):
        pass
