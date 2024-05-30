class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han depositado {cantidad} unidades.")
        self.mostrar_saldo()

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad} unidades.")
        else:
            print("Fondos insuficientes.")
        self.mostrar_saldo()

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

# Creando una instancia de la clase CuentaBancaria
mi_cuenta = CuentaBancaria("Juan Pérez", 1000)

# Operaciones en la cuenta
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
mi_cuenta.retirar(2000)
