def mostrar_encabezado_escuela():
    print("Universidad Tecnológica de Xicotepec de Juárez")
    print("Registro y Evaluación de calificaciones")
def obtener_nota_minima_aprobatoria():
    print("La nota mínima para aprobar es 7.0")
def evaluar_rendimiento(nota_final):
    if nota_final < 7.0: 
       return "Estás reprobado"    
    elif 7.0 <= nota_final < 9.5:
       return "Estás aprobado"     
    elif nota_final >= 9.5:
       return "Excelente"          
def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    promedio = (nota_examenes * .70) + (nota_tareas * .30)
    return round(promedio,1)                
def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)
    print(f"Alumno: {nombre_alumno}")
    print(f"Nota exámenes: {nota_examenes}")
    print(f"Nota tareas: {nota_tareas}")
    print(f"Calificación final: {nota_final}")
    print(f"Estado académico: {estado}")
nombre_alumno = input("Ingresa el nombre del alumno: ")
nota_examenes = float(input("Ingresa la nota de tu examen: "))
nota_tareas = float(input("Ingresa la nota de tus tareas: "))
mostrar_encabezado_escuela()
generar_boleta(nombre_alumno, nota_examenes, nota_tareas)