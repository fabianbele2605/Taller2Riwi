# Ingreso de credenciales del estudiante

estudianteNombre = "Noah"
estudianteCorrecto = ""
contraseñaCorrecta = "Noah123"
contraseñaEstudiante = ""

while estudianteCorrecto != estudianteNombre:
    estudianteCorrecto = str(input("Introducir nombre de estudiante=>"))
else:
    print("Nombre de estudiante correcto!")
    print()
    print()
    
while contraseñaEstudiante != contraseñaCorrecta:
    contraseñaEstudiante = str(input("Introducir contraseña=>"))
else:
    print("Contraseña correcta!")
print("Bienvenido estudiante!", estudianteNombre)
print()
print()

# Ingreso de calificacion del estudainte

tuCalificacion = int(input("Ingresar tu calificacion=>"))

if tuCalificacion >0 or tuCalificacion <59:
    print("Tu calificacion es reprobatoria, estas reprobado!")
    
elif tuCalificacion >60 or tuCalificacion <69:
    print("Tu calificación de aprobación es mínima!")
    
elif tuCalificacion >70 or tuCalificacion <79:
    print("Tienes una calificacion buena!")
    
elif tuCalificacion >80 or tuCalificacion <89:
    print("Tu calificacion es muy buena!")
    
elif tuCalificacion >90 or tuCalificacion <100:
    print("Tu calificacion es excelente!")
    
else:
    print("Tu calificacion no esta en el rango de (0-100).")
    


tuCalificacion = tuCalificacion
tuCalificacionMinimaParaAprobar = 70

if tuCalificacion>=tuCalificacionMinimaParaAprobar:
    print(f"Aprobaste, {estudianteNombre}!")
    
else:
    print(f"No aprobaste, {estudianteNombre}!")
    