print("Calculadora de nuevo salario")
salario_actual = float(input("Ingrese el salario actual del empleado: "))

incremento = salario_actual * 0.08

descuento = salario_actual * 0.025

nuevo_salario = salario_actual + incremento - descuento

print(f"\nIncremento aplicado: ${incremento:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"El nuevo salario del empleado es: ${nuevo_salario:.2f}")