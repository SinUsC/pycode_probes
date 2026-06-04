#
#¿Quieres que ahora lo adaptemos para que el ahorro mensual cambie según el mes, o que se detenga si 
# se alcanza una meta? También podemos agregar gastos y calcular el saldo. Tú decides.
#

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "octubre", "noviembre", "Diciembre"]

Gastos = [
    {"gasto": "alquiler", "importe": 600},
    {"gasto": "suministros", "importe":120},
    {"gasto": "seguroCoche", "impore":60}
]


ahorro_mes = 0
total_ahorro = 0
resumen_ahorro =[]
objetivo_computer = True
objetivo_casa = True

for mes in meses:
    if total_ahorro >= 3000 and objetivo_computer == True :
        print("has logrado tu meta competer-ultra-gamer")
        objetivo_computer = False
    elif total_ahorro >= 8000 and objetivo_casa == True :
        print("meta entrada casa completada")
        objetivo_casa = False
    ahorro_mes = int(input("¿Cuanto quieres ingresar en tu cuenta de ahorro?"))
    total_ahorro += ahorro_mes
    print(f"has ingresado {ahorro_mes}: tienes un saldo de {total_ahorro}:")
    resumen_ahorro.append(f"a mes de {mes}: tienes ahorrado un total de {total_ahorro}")


print("Movimientos de la cuenta...\n")

for resumen in resumen_ahorro:
    print(resumen)
