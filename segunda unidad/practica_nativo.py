A = [[10, 15], [20, 5]]
B = [[5, 12], [15, 8]]
suma = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
ingreso = [[50 * suma[i][j] for j in range(2)] for i in range(2)]
print("Total de precios vendidos(Sábado y Domingo:)")
print(suma)
print("\nIngreso total en pesos (a 50 pesos por producto)")
print(ingreso)
