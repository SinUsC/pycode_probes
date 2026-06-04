import argparse
import os
from converter import image_to_ascii
from config import PALETTES

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="🎨 Convierte una imagen en arte ASCII con firma personalizada estilo GRX."
    )

    parser.add_argument("-i", "--image", type=str, required=True,
                        help="Ruta de la imagen a convertir (ej. imagen.jpg)")
    parser.add_argument("-w", "--width", type=int, default=100,
                        help="Ancho del arte ASCII en caracteres (ej. 80, 100, 120)")
    parser.add_argument("-c", "--contrast", type=float, default=2.0,
                        help="Nivel de contraste (ej. 1.5, 2.0, 3.0)")
    parser.add_argument("-s", "--signature", type=str, default="GRX",
                        help="Firma personalizada que se añade al final del arte")
    parser.add_argument("-o", "--output", type=str, default="ascii_output.txt",
                        help="Nombre del archivo de salida (ej. arte.txt)")
    parser.add_argument("-v", "--show", action="store_true",
                    help="Muestra el arte ASCII en consola además de guardarlo")
    parser.add_argument("-p", "--palette", type=str, default="classic",
                    choices=["classic", "dense", "minimal", "blocks", "dots"],
                    help="Paleta de caracteres ASCII (classic, dense, minimal, blocks, dots)")

    args = parser.parse_args()

    ascii_art = image_to_ascii(
        args.image,
        width=args.width,
        contrast=args.contrast,
        signature=args.signature,
        palette=PALETTES.get(args.palette, PALETTES["classic"])
    )

    # Verificar si el archivo por defecto ya existe
    if args.output == "ascii_output.txt" and os.path.exists(args.output):
        respuesta = input(f"⚠️ El archivo '{args.output}' ya existe. ¿Quieres sobrescribirlo? (s/n): ").strip().lower()
        if respuesta != "s":
            nuevo_nombre = input("📝 Escribe el nuevo nombre para guardar el archivo (ej. arte_grx.txt): ").strip()
            args.output = nuevo_nombre

#Guarda el archivo
with open(args.output, "w") as f:
    f.write(ascii_art)
print("✅ Arte ASCII generado y guardado en ascii_output.txt")


if args.show:
    print("\n🖼️ Arte ASCII:\n")
    print(ascii_art)
