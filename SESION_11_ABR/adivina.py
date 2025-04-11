#adivinar un numero
import random

numero_secreto = random.randint(1, 10)

numero_usuario = int(input("Adivina el número entre 1 y 10: "))

if(numero_secreto == numero_usuario):
    print("barbaro, 10 puntos extra!")
else:
    print("solo vara me debes un churro")