lista=[10.0,9.5,8.6,7.6,8.1,9.9,6.7,7.6,8.4,9.2,10.0,7.2,8.4,6.6,9]
n=len(lista)
swapped=True
while swapped:
    swapped=False
    for i in range(n-1):
        if lista[i]< lista[i+1]:
            lista[i],lista[i+1]= lista[i+1], lista[i]
            swapped=True
print("Lista ordenada descendente: ",lista)

n=len(lista)
swapped=True
while swapped:
    swapped=False
    for i in range(n-1):
        if lista[i]> lista[i+1]:
            lista[i],lista[i+1]= lista[i+1], lista[i]
            swapped=True
print("Lista ordenada ascendente: ",lista)