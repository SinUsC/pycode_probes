from PIL import Image, ImageEnhance
import numpy as np
from config import DEFAULT_SIGNATURE, DEFAULT_PALETTE

def image_to_ascii(image_path, width=100, contrast=2.0, signature=DEFAULT_SIGNATURE, palette=DEFAULT_PALETTE):
    img = Image.open(image_path).convert("L")
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)

    aspect_ratio = img.height / img.width
    height = int(aspect_ratio * width * 0.55)
    img = img.resize((width, height))

    pixels = np.array(img)
    ascii_img = [
        "".join(palette[int(pixel) * len(palette) // 256] for pixel in row)
        for row in pixels
    ]
    ascii_img.append(" " * (width - len(signature)) + signature)
    return "\n".join(ascii_img)
