import matplotlib.pyplot as plt
datos = [42, 12, 88, 23, 7, 65, 34, 50]
def insercion(arr):
    a = arr.copy()
    comp = 0
    for i in range(1, len(a)):
        clave, j = a[i], i - 1
        while j >= 0 and a[j] > clave:
            comp += 1
            a[j+1] = a[j]
            j -= 1
        if j >= 0: 
            comp += 1
        a[j+1] = clave
    return a, comp

def seleccion(arr):
    a = arr.copy()
    n = len(a)
    comp = 0
    for i in range(n):
        min_idnx = i
        for j in range(i+1, n):
            comp += 1
            if a[j] < a[min_idnx]:
                min_idnx = j
        a[i], a[min_idnx] = a[min_idnx], a[i]
    return a, comp

lista_ordenada, comp_ins = insercion(datos)
_, comp_sel = seleccion(datos)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 3.5))

ax1.bar(range(len(datos)), datos, color="red")
ax1.set_title("1. Lista original")
ax1.set_ylabel("valor")

ax2.bar(range(len(lista_ordenada)), lista_ordenada, color="blue")
ax2.set_title("2. Lista ordenada")

ax3.bar(["insercion", "seleccion"], [comp_ins, comp_sel], color=["#11629c", "#b6733a"])
ax3.set_title("3. Comparaciones")
ax3.set_ylabel("cantidad")

plt.tight_layout()
plt.show()