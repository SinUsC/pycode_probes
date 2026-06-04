import time


"""
-------------------------------------------------------------------
|   Variables movHorizontal -- movHorizontal("Hola1",10,10,0.2)    |
-------------------------------------------------------------------
|   mensaje = "Hola"                                               |
|   ancho = 20                                                     |
|   rebote = 10                                                    |
|   velocidad = 0.5                                                |
------------------------------------------------------------------"""

def movHorizontal(mensaje, ancho, rebote, velocidad):

    i = 0
    direccion = 1  # 1 para derecha, -1 para izquierda
    contador = 0

    while contador < rebote:
        espacios = " " * i
        print("\r" + espacios + mensaje + " " * (ancho - i), end='', flush=True)
        time.sleep(velocidad)
        #print(i)
        
        i += direccion

        if i == ancho or i == 0:
            direccion *= -1  # invierte la dirección
            contador +=1
            #print(contador)
            
movHorizontal("Hola1",10,10,0.2)
print()








