import time
import sys

boot_lines = [
    "[Initializing System...]",
    "[Loading Humor Module...]",
    "[Scanning for Errno13...]",
    "[Activating Virtual Env...]",
    "[Deploying Sarcasm & Patience...]",
    "[Finalizing Boot Sequence...]"
]

def progress_bar(line):
    for i in range(1, 21):
        bar = "█" * i + "▒" * (20 - i)
        sys.stdout.write(f"\r{line} {bar} {i*5}%")
        sys.stdout.flush()
        time.sleep(0.15)
    print()

for line in boot_lines:
    progress_bar(line)
    
mensaje = """
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
for letra in mensaje:
    print(letra, end='', flush=True)
    time.sleep(0.05)  # pausa de 50 milisegundos por letra