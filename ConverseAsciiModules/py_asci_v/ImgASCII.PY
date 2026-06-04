from PIL import Image
from PIL import ImageEnhance
import numpy as np

# Paleta de caracteres ordenados por densidad visual (de oscuro a claro)
ASCII_CHARS = "#01 "





def image_to_ascii(image_path, width=100):
    # Abrir imagen y convertir a escala de grises
    img = Image.open(image_path).convert("L")
    
    # Redimensionar manteniendo proporción
    aspect_ratio = img.height / img.width
    height = int(aspect_ratio * width * 0.5)  # 0.5 ajusta proporción vertical
    img = img.resize((width, height))

    # Convertir imagen a matriz NumPy
    pixels = np.array(img)

    # Normalizar y mapear cada valor de brillo a un carácter ASCII
    ascii_img = [
        "".join(ASCII_CHARS[int(pixel) * len(ASCII_CHARS) // 256] for pixel in row)
        for row in pixels
    ]

    # Unir líneas en un solo string
    return "\n".join(ascii_img)

img = Image.open("ascii-art-hacker-760x380.jpg").convert("L")
# Mejora el contraste
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(1.0)  # Prueba con valores entre 1.5 y 3.0

# Guardar en archivo .txt
ascii_art = image_to_ascii("ascii-art-hacker-760x380.jpg", width=100)
with open("HackerASCII1", "w") as f:
    f.write(ascii_art)


