print("Calculadora de precio con descuento")
nombre_producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (por ejemplo, 15 para 15%): "))

descuento = precio * (porcentaje_descuento / 100)
precio_final = precio - descuento

print(f"\nProducto: {nombre_producto}")
print(f"Precio original: ${precio:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Precio final: ${precio_final:.2f}")