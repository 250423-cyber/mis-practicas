from collections import deque
import time
cola_reproduccion=deque()
cola_reproduccion.append("1. Remolineando")
cola_reproduccion.append("2. Música del cielo")
cola_reproduccion.append("3. Fiesta en el desierto")
print("Cancion en espera")
for cancion in cola_reproduccion:
    print("_",cancion)
print("inicio reproduccion")

while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"sonando ahora: {cancion_actual}")
    time.sleep(1)
print(f"Finalizo:{cancion_actual}")
print(f"Quedan: {len(cola_reproduccion)} canciones en la cola")
print("La cola de reproduccion finalizado") 