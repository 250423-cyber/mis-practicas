frutas=["manzana","guayaba","uva"]
#Actualizar
frutas[1]="pera"
#INSERT
frutas.append("sandía")
#Meter más de uno
frutas.extend(["Kiwi","Mango"])
#Eliminar
retirado=frutas.pop(2)

ultimo=frutas.pop()

frutas.remove("sandía")

del frutas[0]
print(frutas)
