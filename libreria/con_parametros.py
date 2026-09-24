from datetime import datetime
import matplotlib.pyplot as plt

def obtener_fecha(formato):
    """Devuelve la fecha y hora actual con el formato indicado."""
    return datetime.now().strftime(formato)

def crear_grafica(x, y, titulo):
    """Dibuja una gráfica de líneas con los datos recibidos."""
    plt.plot(x, y, marker="o")
    plt.title(titulo)
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")

def guardar_grafica(nombre_base, formato_fecha):
    """Guarda la gráfica con la fecha en el nombre del archivo."""
    marca = obtener_fecha(formato_fecha)
    archivo = f"{nombre_base}_{marca}.png"
    plt.savefig(archivo)
    return archivo

# Uso
meses = ["Ene", "Feb", "Mar", "Abr"]
ventas = [100, 150, 130, 180]

crear_grafica(meses, ventas, "Ventas mensuales")
archivo = guardar_grafica("ventas", "%Y%m%d_%H%M%S")
print(f"Gráfica guardada como: {archivo}")
plt.show()