nombre = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
precio_por_hora = float(input("Ingrese el precio que cobra por hora: "))

sueldo_bruto = horas_trabajadas * precio_por_hora

descuento_renta = sueldo_bruto * 0.05
salario_neto = sueldo_bruto - descuento_renta

print(f"Nombre del trabajador: {nombre}")
print(f"Sueldo bruto: C${sueldo_bruto:.2f}")
print(f"Descuento por renta (5%): C${descuento_renta:.2f}")
print(f"Salario neto a pagar: C${salario_neto:.2f}")