lista = [15, 3, 8, 1, 4]
print("Lista original: ", lista)

def ordenar_lista(lista):
    copia = lista.copy()
    for i in range(len(copia)):
        for j in range(i + 1, len(copia)):
            if copia[i] > copia[j]:
                copia[i], copia[j] = copia[j], copia[i]
    return copia

def ordenar_lista2(lista):
    #"método sort()
    copia = lista.copy()
    copia.sort()
    return copia

def ordenar_lista3(lista):
    #Ordenamiento por burbuja
    copia = lista.copy()
    n = len(copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            if copia[j] > copia[j + 1]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
    return copia

def ordenar_lista4(lista):
    #Ordenamiento por inserción
    copia = lista.copy()
    for i in range(1, len(copia)):
        clave = copia[i]
        j = i - 1
        while j >= 0 and clave < copia[j]:
            copia[j + 1] = copia[j]
            j -= 1
        copia[j + 1] = clave
    return copia

def main():
    while True:
        print("\nElije una opción para ordenar:")
        print("1. Ordenar con intercambio directo")
        print("2. Ordenar con sort()")
        print("3. Ordenar con burbuja")
        print("4. Ordenar con inserción")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("Programa finalizado.")
            break
        if opcion == "1":
            print("Lista ordenada:", ordenar_lista(lista))
            break
        elif opcion == "2":
            print("Lista ordenada:", ordenar_lista2(lista))
            break
        elif opcion == "3":
            print("Lista ordenada:", ordenar_lista3(lista))
            break
        elif opcion == "4":
            print("Lista ordenada:", ordenar_lista4(lista))
            break
        else:
            print("Opción inválida, intenta de nuevo.")
if __name__ == "__main__":
    main()
