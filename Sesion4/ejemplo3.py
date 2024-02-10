class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f'Se han depositado {cantidad} unidades.')
        else:
            print('La cantidad a depositar debe ser mayor que cero.')

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f'Se han retirado {cantidad} unidades.')
        else:
            print('Saldo insuficiente.')

    def consultar_saldo(self):
        print(f'Su saldo actual es: {self.__saldo}')