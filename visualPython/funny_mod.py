import time
import sys

# Texto de boot
boot_lines = [
    "[Initializing System...]",
    "[Loading Humor Module...]",
    "[Scanning for Errno13...]",
    "[Activating Virtual Env...]",
    "[Deploying Sarcasm & Patience...]",
    "[Finalizing Boot Sequence...]"
]

# Estado del sistema final
final_status = """
========================================
|   WELCOME, Mr. User! SYSTEM READY    |
|   CPU Emotional: 40%                 |
|   Humor: 100%                        |
|   Alias 'pycode': ONLINE             |
|   Virtual Env: ACTIVE                |
|   Caffeine Status: CRITICAL ☕       |
========================================
SYSTEM TIP: 
“Si el mundo te da errores, haz print('todo bien') y sigue compilando tu vida 😎”
"""

# Función de barra de carga
def progress_bar(line):
    for i in range(1, 21):
        bar = "█" * i + "▒" * (20 - i)
        sys.stdout.write(f"\r{line} {bar} {i*5}%")
        sys.stdout.flush()
        time.sleep(0.15)
    print()  # salto de línea al terminar la barra

# Simulación de boot
for line in boot_lines:
    progress_bar(line)

# Mostrar pantalla final
print(final_status)