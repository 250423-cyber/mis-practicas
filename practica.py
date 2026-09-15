inventario_tech=["laptop","tarjeta de video","procesador","memoria RAM"]
inventario_tech.append("disco SSD")
inventario_tech.insert(2,"fuente de poder")
inventario_tech.extend(["gabinete","monitor 4K","teclado mecanico","mouse gamer"])
inventario_tech[4]="memoria RAM DDR5"
equipo_despachado = inventario_tech.pop()
inventario_tech.remove("tarjeta de video")
print("El monitor esta en la posición: ",inventario_tech.index("monitor 4K"))
print("La ultima posicion es: ",equipo_despachado)
print(inventario_tech)