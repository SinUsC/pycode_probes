import json

# Archivos para guardar datos
ARCHIVO_OBJETIVOS = "objetivos_ahorro.json"
ARCHIVO_PROGRESO = "progreso_mensual.json"

# Cargar datos desde archivos
def cargar_datos(ruta):
    try:
        with open(ruta, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

# Guardar datos en archivos
def guardar_datos(ruta, datos):
    with open(ruta, "w") as archivo:
        json.dump(datos, archivo)
    print(f"💾 Datos guardados en {ruta}")

# Inicializar listas
objetivos_ahorro = cargar_datos(ARCHIVO_OBJETIVOS)
progreso_mensual = cargar_datos(ARCHIVO_PROGRESO)

# Añadir nuevo objetivo
def añadir_objetivo():
    concepto = input("📝 Nombre del objetivo: ")
    meta_total = float(input("🎯 ¿Cuánto quieres ahorrar en total? "))
    mensual = float(input("💰 ¿Cuánto ahorrarás cada mes? "))
    objetivo = {"concepto": concepto, "meta_total": meta_total, "ahorro_mensual": mensual}
    objetivos_ahorro.append(objetivo)
    guardar_datos(ARCHIVO_OBJETIVOS, objetivos_ahorro)

# Registrar ahorro mensual
def registrar_ahorro():
    mes = input("📅 Mes actual: ")
    cantidad = float(input("💸 ¿Cuánto has ahorrado este mes? "))
    progreso_mensual.append({"mes": mes, "cantidad": cantidad})
    guardar_datos(ARCHIVO_PROGRESO, progreso_mensual)

# Mostrar progreso hacia cada objetivo
def mostrar_progreso():
    total_ahorrado = sum(item["cantidad"] for item in progreso_mensual)
    print(f"\n💼 Has ahorrado un total de {total_ahorrado:.2f}€")
    for objetivo in objetivos_ahorro:
        restante = objetivo["meta_total"] - total_ahorrado
        print(f"- {objetivo['concepto']}: faltan {max(restante, 0):.2f}€ para alcanzar los {objetivo['meta_total']}€")

# Menú interactivo
def menu():
    while True:
        print("\n📌 Menú principal:")
        print("1: Añadir objetivo de ahorro")
        print("2: Registrar ahorro mensual")
        print("3: Ver progreso hacia objetivos")
        print("4: Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            añadir_objetivo()
        elif opcion == "2":
            registrar_ahorro()
        elif opcion == "3":
            mostrar_progreso()
        elif opcion == "4":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida.")

# Ejecutar el programa
menu()
