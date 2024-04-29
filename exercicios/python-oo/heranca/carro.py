from veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas

    def __str__(self):
        status = "Ligado" if self._ligado == True else "Desligado"
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Portas: {self._portas}, Status: {status}"
