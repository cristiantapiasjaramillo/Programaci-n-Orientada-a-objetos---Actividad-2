print("Ingrese número de inscripcion")
numero_inscripcion=str(input())
print("Ingrese nombres")
nombres=str(input())
print("Ingrese patrimonio")
patrimonio=float(input())
print("Ingrese estrato social")
estrato_social=int(input())
pago_matricula=50000
if patrimonio>2000000 and estrato_social>3:
 pago_matricula=50000+0.03*patrimonio
print("El estudiante con número de inscripción", numero_inscripcion, "y nombre", nombres, "debe pagar: $", pago_matricula)
