print("Calculadora de porcentajes en un aula")
mujeres = int(input("¿Cuántas mujeres hay en el aula? "))
varones = int(input("¿Cuántos varones hay en el aula? "))

total = mujeres + varones


if total > 0:
    porcentaje_mujeres = mujeres * 100 / total
    porcentaje_varones = varones * 100 / total

    print(f"\nPorcentaje de mujeres: {porcentaje_mujeres:.1f}%")
    print(f"Porcentaje de varones: {porcentaje_varones:.1f}%")
else:
    print("\nNo hay estudiantes en el aula.")