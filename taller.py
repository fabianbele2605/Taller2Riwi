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

# calcular promedio de calificacciones
# Solicitar las calificaciones al usuario
Miscalificaciones = input("Ingresa las calificaciones separadas por comas: ")

# Convertir la entrada en una lista de números
calificaciones = [float(calificacion.strip()) for calificacion in Miscalificaciones.split(',')]

# Calcular el promedio
promedio = sum(calificaciones) / len(calificaciones)

print(f"El promedio de las calificaciones es: {promedio:.2f}")  
    
    

# Ingreso de calificacion del estudiante

tuCalificacion = promedio

if tuCalificacion >=0 or tuCalificacion <=59:
    print("")
    
elif tuCalificacion >=60 or tuCalificacion <=69:
    print("")
    
elif tuCalificacion >=70 or tuCalificacion <=79:
    print("")
    
elif tuCalificacion >=80 or tuCalificacion <=89:
    print("")
    
elif tuCalificacion >=90 or tuCalificacion <=100:
    print("")
    
# Error si no recono Int o legan str
else:
    print("Tu calificacion no esta en el rango de (0-100).")
    

# Si aprobo o no aprobo

tuCalificacion = tuCalificacion
tuCalificacionMinimaParaAprobar = 70

if tuCalificacion>=tuCalificacionMinimaParaAprobar:
    print(f"Aprobaste, {estudianteNombre}!")
    
else:
    print(f"No aprobaste, {estudianteNombre}!")
    
    


    
    
