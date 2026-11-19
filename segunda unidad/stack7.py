betetas_lista=[]
for i in range (1,11):
    betetas_lista.append(i)
lista_betetas=betetas_lista[-1]
for j in range(0,4):
    betetas_lista.pop()
tamaño_betetas=len(betetas_lista)
no_betetas=len(betetas_lista)==0

while len(betetas_lista)>0:
    betetas_lista.pop()

print(betetas_lista)
print(tamaño_betetas)
print(no_betetas)
print(lista_betetas)
