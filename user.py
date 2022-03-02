from cuentaBancaria import CuentaBancaria

class User:

    listaCuentasBancarias = []

    def __init__(self, nombre):
        
        self.nombre = nombre
        self.cuentasUsuario = {
            "sueldos" : CuentaBancaria(8,0),
            "ahorros" : CuentaBancaria(6,0)
        }

    # def hacerRetiro(self, cantidad):
    #     self.cuenta.retiro(cantidad)
    #     return self

    # def hacerDeposito(self, cantidad):
    #     self.cuenta.deposito(cantidad)
    #     return self

    # def mostrarBalanceUsuario(self):
    #     # return f"Usuario: {self.nombre}, Balance: {self.pesos}"
    #     # print(f"Usuario: {self.nombre}, Balance: {self.pesos}")
    #     self.cuenta.mostrar_info_cuenta()

    # # def transferirDinero(self, otroUsuario, monto):
    # #     self.pesos -= monto
    # #     otroUsuario.pesos += monto

    @classmethod
    def mostrarCuentasUsuario(cls):
        for i in cls.listaCuentasBancarias:
                # cuenta.mostrar_balance_usuario()
                print(f"Nombre: {i.nombre}, Dinero en cuenta: {i.cuenta.dineroCuenta}, Tasa de interes: {i.cuenta.tasaInteres}")

    
    # @staticmethod
    # def existeCuenta(nombre, cuentaNum):
    #     for i in User.listaCuentasBancarias:
    #         if i.nombre == nombre and i.cuentaNumero == cuentaNum:
    #             return True
    #         else:
    #             return False

    def mostrarSaldoUsuario(self):
        print(f"Usuario: {self.nombre}, Sueldo: {self.cuentasUsuario['sueldos'].mostrar_info_cuenta()}")
        print(f"Usuario: {self.nombre}, Ahorros: {self.cuentasUsuario['ahorros'].mostrar_info_cuenta()}")
        return self

    def transferirDinero(self,montoDinero,Usuario):
        self.montoDinero -= montoDinero
        Usuario.montoDinero += montoDinero
        self.mostrarSaldoUsuario()
        Usuario.mostrarSaldoUsuario()
        return self

