class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"Nome Titular: {self.titular} | Saldo: {self.saldo} | Status: {self.ativo}"

    @property
    def ativo(self):
        return "Ativo" if self._ativo == True else "Inativo"

    def ativar_conta(self):
        self._ativo = not self._ativo


murilo = ContaBancaria("Murilo", 300)
murilo.ativar_conta()
ricardo = ContaBancaria("Ricardo", 1600)

print(murilo)
print(ricardo)
