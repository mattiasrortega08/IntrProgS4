print("Calculadora de pulsaciones por cada 10 segundos de ejercicio")
edad = int(input("Ingrese su edad: "))

pulsaciones = (220 - edad) / 10

print(f"\nEl número de pulsaciones que debe tener por cada 10 segundos de ejercicio es: {pulsaciones:.2f}")