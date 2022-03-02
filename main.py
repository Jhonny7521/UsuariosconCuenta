from user import User

jhon = User("Jhon")
marcos = User("Marcos")

print(jhon.nombre)

jhon.cuentasUsuario['sueldos'].deposito(1500)
jhon.cuentasUsuario['ahorros'].deposito(800)

jhon.mostrarSaldoUsuario()

jhon.cuentasUsuario['sueldos'].retiro(100)
jhon.cuentasUsuario['ahorros'].retiro(200)

jhon.mostrarSaldoUsuario()

jhon.cuentasUsuario['sueldos'].generar_interés()
jhon.cuentasUsuario['ahorros'].generar_interés()

jhon.mostrarSaldoUsuario()

jhon.transferirDinero(100,marcos)

