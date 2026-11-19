historial_navegacion=[]
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.org")
print("Historial cargado: ",historial_navegacion)
pagina_actual=historial_navegacion[-1]
print("pagina_actual en pantalla", pagina_actual)
pagina_cerrada=historial_navegacion.pop()
print("saliendo de: ",pagina_cerrada)
print("Historial después de presionar atras ",historial_navegacion)

total_paginas=len(historial_navegacion)
print("paginas previas guardadas",total_paginas)

sin_paginas=len(historial_navegacion)==0
print("El historial está vacio? ",sin_paginas)