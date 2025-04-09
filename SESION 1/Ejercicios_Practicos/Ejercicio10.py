print("Calculadora de masa")
presion = float(input("Ingrese la presión (en unidades adecuadas): "))
volumen = float(input("Ingrese el volumen (en unidades adecuadas): "))
temperatura = float(input("Ingrese la temperatura (en grados Fahrenheit): "))

masa = (presion * volumen) / (0.37 * (temperatura + 460))

print(f"\nLa masa calculada es: {masa:.2f}")