presupuesto_total = float(input("Ingrese el presupuesto anual del hospital: "))

presupuesto_urgencias = presupuesto_total * 0.37
presupuesto_prediatria = presupuesto_total * 0.42
presupuesto_traumatologia = presupuesto_total * 0.21

print("\nDistribucion del presupuesto anual:")
print(f"Urgencias: C${presupuesto_urgencias:.2f}")
print(f"Prediatria: C${presupuesto_prediatria:.2f}")
print(f"Traumatologia: C${presupuesto_traumatologia:.2f}")