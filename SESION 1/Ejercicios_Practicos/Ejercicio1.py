tasa_anual = 0.27  # 27%

prestamo = float(input("Ingrese el monto del préstamo: "))
anios = int(input("Ingrese la cantidad de años del préstamo: "))

interes_total = prestamo * tasa_anual * anios

print(f"\nEl interés total que se pagará en {anios} años es: ${interes_total:.2f}")