print("Calculadora de tiempo promedio de recorrido")
lunes = float(input("Ingrese el tiempo del lunes (en minutos): "))
miercoles = float(input("Ingrese el tiempo del miércoles (en minutos): "))
viernes = float(input("Ingrese el tiempo del viernes (en minutos): "))

promedio = (lunes + miercoles + viernes) / 3

print(f"\nEl tiempo promedio que tarda en recorrer la ruta es: {promedio:.2f} minutos")