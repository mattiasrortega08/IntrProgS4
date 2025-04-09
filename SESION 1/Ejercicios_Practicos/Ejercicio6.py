# Solicitar los precios de los productos
print("Calculadora de total a pagar con IVA (15%)")
producto1 = float(input("Ingrese el precio del producto 1: "))
producto2 = float(input("Ingrese el precio del producto 2: "))
producto3 = float(input("Ingrese el precio del producto 3: "))

subtotal = producto1 + producto2 + producto3

iva = subtotal * 0.15

total = subtotal + iva

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"IVA (15%): ${iva:.2f}")
print(f"Total a pagar: ${total:.2f}")