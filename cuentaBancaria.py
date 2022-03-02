
class CuentaBancaria:

    informacion_Cuentas = []

    def __init__(self, tasa_interés = 0, dineroCuenta = 0): 
        
        self.dineroCuenta = dineroCuenta
        self.tasaInteres = tasa_interés/100
        CuentaBancaria.informacion_Cuentas.append(self)

    def deposito(self, monto):
        self.dineroCuenta += monto
        return self

    def retiro(self, monto):
        if self.dineroCuenta - monto > 0 :
            self.dineroCuenta -= monto
        else:
            print('Montos Insuficientes: cobrando una tarifa de $5')
            self.dineroCuenta -= 5
        return self

    def mostrar_info_cuenta(self):
        print(self.dineroCuenta)

    def generar_interés(self):
        self.dineroCuenta += (self.dineroCuenta * self.tasaInteres)
        return self

    @classmethod
    def mostrar_cuentas(cls):
        numCuentas = 1
        if len(cls.informacion_Cuentas) > 0:
            for cuenta in cls.informacion_Cuentas:
                # cuenta.mostrar_balance_usuario()
                print(f"Cuenta {numCuentas} => Tasa: {cuenta.tasaInteres}, Balance: {cuenta.dineroCuenta}")
                numCuentas += 1
        
        else:
            print('No se tienen cuentas almacenadas')

    



    