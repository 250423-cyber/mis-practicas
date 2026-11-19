from datetime import datetime
import matplotlib.pyplot as plt

def grafica_ventas():
    meses = ["Ene", "Feb", "Mar", "Abr"]
    ventas = [100, 150, 130, 180]

    plt.plot(meses, ventas, marker="o")
    plt.title("Ventas mensuales")
    plt.xlabel("Mes")
    plt.ylabel("Ventas")

    marca = datetime.now().strftime("%Y%m%d_%H%M%S")
    plt.savefig(f"grafica_{marca}.png")
    plt.show()

grafica_ventas()