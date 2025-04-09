print("Calculadora de calificación final")
tareas = float(input("Ingrese la calificación de tareas (0-100): "))
examen_parcial = float(input("Ingrese la calificación del examen parcial (0-100): "))
examen_final = float(input("Ingrese la calificación del examen final (0-100): "))

calificacion_final = (tareas * 0.30) + (examen_parcial * 0.30) + (examen_final * 0.40)

print(f"\nLa calificación final del estudiante es: {calificacion_final:.2f}")