import random

print("Generador de correo electrónico")
nombre = input("Ingrese su nombre: ").strip().lower()
apellido = input("Ingrese su apellido: ").strip().lower()

# Generar combinaciones posibles
dominio = "@gustambouniversity.edu"
opciones = [
    f"{nombre}.{apellido}{dominio}",
    f"{apellido}.{nombre}{dominio}",
    f"{nombre[0]}{apellido}{dominio}",
    f"{apellido}{nombre[0]}{dominio}",
    f"{nombre}{apellido[0]}{dominio}"
]

correo = random.choice(opciones)

print(f"\nSu correo electrónico podría ser: {correo}")