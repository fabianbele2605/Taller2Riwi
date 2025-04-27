# Ingreso de credenciales del estudiante

estudianteNombre = "Noah"
estudianteCorrecto = ""
contraseñaCorrecta = "Noah123"
contraseñaEstudiante = ""

while estudianteCorrecto != estudianteNombre:
    estudianteCorrecto = str(input("Introducir nombre de estudiante=>"))
else:
    print("Numero de identidad de estudiante correcto!")
    print()
    print()
    
while contraseñaEstudiante != contraseñaCorrecta:
    contraseñaEstudiante = str(input("Introducir contraseña=>"))
else:
    print("Contraseña correcta!")
print("Bienvenido estudiante!", estudianteNombre)
print()
print()