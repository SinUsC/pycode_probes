import json  # Importa el módulo JSON para poder guardar y cargar datos en formato JSON

# Ruta del archivo donde se guardarán los datos
ARCHIVO_OBJETIVOS = "objetivos_ahorro.json"  # Define el nombre del archivo donde se almacenarán los objetivos de ahorro

# Guardar la lista en un archivo
def guardar_objetivos(objetivos):  # Define una función que guarda la lista de objetivos en un archivo
    with open(ARCHIVO_OBJETIVOS, "w") as archivo:  # Abre el archivo en modo escritura ("w"), lo crea si no existe
        json.dump(objetivos, archivo)  # Convierte la lista de objetivos a formato JSON y la escribe en el archivo
    print("💾 Objetivos guardados correctamente.")  # Muestra un mensaje de confirmación

# Cargar la lista desde el archivo
def cargar_objetivos():  # Define una función que carga los objetivos desde el archivo
    try:  # Intenta abrir y leer el archivo
        with open(ARCHIVO_OBJETIVOS, "r") as archivo:  # Abre el archivo en modo lectura ("r")
            return json.load(archivo)  # Convierte el contenido JSON del archivo en una lista de Python y la devuelve
    except FileNotFoundError:  # Si el archivo no existe, captura el error
        return []  # Devuelve una lista vacía para evitar que el programa falle
