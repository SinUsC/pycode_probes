import pandas as pd

def asiento(cuenta_debe, nombre_debe, importe, cuenta_haber, nombre_haber):
    return [
        {"cuenta": cuenta_debe, "nombre": nombre_debe, "debe": importe, "haber": 0},
        {"cuenta": cuenta_haber, "nombre": nombre_haber, "debe": 0, "haber": importe},
    ]

diario = []
print("Introduce tus asientos. Escribe 'fin' para terminar.\n")

while True:
    cuenta_debe = input("Cuenta DEBE (o 'fin' para salir): ")
    if cuenta_debe.lower() == "fin":
        break
    nombre_debe = input("Nombre cuenta DEBE: ")
    importe = float(input("Importe: "))
    cuenta_haber = input("Cuenta HABER: ")
    nombre_haber = input("Nombre cuenta HABER: ")

# descripcion = input("Descripción (opcional): ")
    diario += asiento(cuenta_debe, nombre_debe, importe, cuenta_haber, nombre_haber)
    print("Asiento registrado.\n")

    for fila in diario:
        print(f"{fila['cuenta']:>5} | {fila['nombre']:<15} | Debe: {fila['debe']:>8.2f} | Haber: {fila['haber']:>8.2f}")
# Exportar a CSV
pd.DataFrame(diario).to_csv("libro_diario.csv", index=False)
print("Archivo 'libro_diario.csv' creado.")

# Convertimos el diario en un DataFrame
df = pd.DataFrame(diario)

# Agrupamos por cuenta y nombre, sumando Debe y Haber
mayor = df.groupby(["cuenta", "nombre"], as_index=False)[["debe", "haber"]].sum()

# Calculamos el saldo
mayor["saldo"] = mayor["debe"] - mayor["haber"]

# Guardamos en CSV
mayor.to_csv("libro_mayor.csv", index=False, encoding="utf-8-sig")


print(mayor)