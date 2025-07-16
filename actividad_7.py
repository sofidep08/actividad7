estudiantes = {}
opcion = 0
while opcion!=4 :
    print("[1] Registrar estudiantes")
    print("[2] Mostrar todos los estudiantes y sus cursos")
    print("[3] Buscar estudiantes por carnet")
    print("[4] Salir")
    opcion = int(input("Elija una opción: "))
    if opcion <= 0 or opcion >4 :
        print("Ingreso un dato incorrecto")