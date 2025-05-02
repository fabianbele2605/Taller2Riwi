# Ingreso de credenciales del estudiante

estudianteNombre = "Noah"
estudianteCorrecto = ""
contraseñaCorrecta = "Noah123"
contraseñaEstudiante = ""

while estudianteCorrecto != estudianteNombre:
    estudianteCorrecto = str(input("Introducir nombre de estudiante=>"))
else:
    print("Nombre de estudiante correcto!")
    print("'''''''''''''''''''''''''''''''''''''''''")
    
while contraseñaEstudiante != contraseñaCorrecta:
    contraseñaEstudiante = str(input("Introducir contraseña=>"))
else:
    print("Contraseña correcta!")
print("Bienvenido estudiante!", estudianteNombre)
print("'''''''''''''''''''''''''''''''''''''''''''''")

# calcular promedio de calificacciones
# Solicitar las calificaciones al usuario
Miscalificaciones = (input("Ingresa las calificaciones separadas por comas: "))

# Convertir la entrada en una lista de números
Listacalificaciones = [float(calif.strip()) for calif in Miscalificaciones.split(',')]

# Calcular el promedio
promedio_calificaciones = sum(Listacalificaciones) / len(Listacalificaciones)

print(f"El promedio de las calificaciones es: {promedio_calificaciones:.2f}")  
    
    

# Ingreso de calificacion del estudiante

tuCalificacion = promedio_calificaciones

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
    
    

# verificar las calificaciones que son mayores!


while True:
    cantidad = input("Ingresa la calificaciones para verificar cual es mayor a ella! => ")
    if cantidad.isdigit():
        cantidad = int(cantidad)
        conteo = 0
        for calificacion in Listacalificaciones:
           if calificacion > cantidad:
               conteo += 1
        print(f"hay una {conteo} calificacion mayor que {cantidad}")
        break
    else:
        print("Ingres un valor correcto!")
        
        
#Verifica cuantas veces se repite la calificacion!

while True:
    veces_repetida = input("Ingrese la calificacion para ver cuantas veces se repite! ")
    if veces_repetida.isdigit():
        veces_repetida = int(veces_repetida)
        conteo = 0
        for calificacion in Listacalificaciones:
            if calificacion < 0 or calificacion > 100:
                continue
            if calificacion == veces_repetida:
                conteo += 1
        print(f"la calificacion {veces_repetida} sale {conteo} veces")
        break
    else:
        print("Ingresa valores correcto!")
        
