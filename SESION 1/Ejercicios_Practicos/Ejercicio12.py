# Solicitar el precio de compra del artículo
print("Calculadora de precio de venta con ganancia del 30%")
precio_compra = float(input("Ingrese el precio de compra del artículo: "))

# Calcular el precio de venta
precio_venta = precio_compra * 1.30

# Mostrar el resultado
print(f"\nEl precio de venta para obtener una ganancia del 30% es: ${precio_venta:.2f}")