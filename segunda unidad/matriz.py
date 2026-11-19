matriz = [[10, 20, 30],
          [40, 50, 60],
          [70, 80, 90]]
print(matriz[1][2])
matriz[0][0]=50
for fila in matriz:
    for elemento in fila:
        print(elemento,end=" ")
    print()