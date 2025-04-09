print("Calculadora de propina (10%)")
total_cuenta = float(input("Ingrese el total de la cuenta: "))

porcentaje_propina = 10
propina = total_cuenta * 0.10

print(f"\nTotal de la cuenta: ${total_cuenta:.2f}")
print(f"Porcentaje de propina: {porcentaje_propina}%")
print(f"Propina a dejar: ${propina:.2f}")