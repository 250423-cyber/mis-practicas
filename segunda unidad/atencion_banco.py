from collections import deque
import time
cola_datos=deque()
cola_datos.append("Betetas")
cola_datos.append("Memo Jarías")
cola_datos.append("Irma Mando")
print("Clientes en la fila: ")
for turnos in cola_datos:
    print("_ ",turnos)

while len(cola_datos)>0:
    cliente_actual=cola_datos.popleft()
    time.sleep(1)
    print("Es turno de: ",cliente_actual)
    print("Clientes esperando: " ,len(cola_datos))
   