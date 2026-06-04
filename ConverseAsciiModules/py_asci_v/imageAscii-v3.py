from PIL import Image, ImageEnhance
import argparse
import numpy as np

# Paleta de caracteres ordenados por densidad visual (oscuro → claro)
ASCII_CHARS = "AMCJ;´¨"

def image_to_ascii(image_path, width=100, contrast=2.0, signature="GRX"):
    # Abrir imagen y convertir a escala de grises
    img = Image.open(image_path).convert("L")

    # Mejorar contraste
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)

    # Redimensionar manteniendo proporción vertical
    aspect_ratio = img.height / img.width
    height = int(aspect_ratio * width * 0.55)
    img = img.resize((width, height))

    # Convertir imagen a matriz NumPy
    pixels = np.array(img)

    # Mapear cada valor de brillo a un carácter ASCII
    ascii_img = [
        "".join(ASCII_CHARS[int(pixel) * len(ASCII_CHARS) // 256] for pixel in row)
        for row in pixels
    ]

    # Añadir firma al final
    ascii_img.append(" " * (width - len(signature)) + signature)

    return "\n".join(ascii_img)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, default="Diseno-sin-titulo-3.jpg")
    parser.add_argument("--width", type=int, default=100)
    parser.add_argument("--signature", type=str, default="GRX")
    parser.add_argument("--output", type=str)
    args = parser.parse_args()

    ascii_art = image_to_ascii(args.image, width=args.width, signature=args.signature)
    with open(args.output, "w") as f:
        f.write(ascii_art)
    print(f"✅ Arte ASCII generado y guardado en {args.output}")
