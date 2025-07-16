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
    elif opcion == 1 :
        cantidad = int(input("¿Cuántos estudiantes desea ingresar? "))
        for i in range(cantidad) :
            print(f"\nEstudiante {i+1}")
            carne = int(input("Ingrese el carné: "))
            nombre = input("Ingrese el nombre completo: ")
            edad = int(input("Ingrese la edad: "))
            carrera = input("Ingrese la carrera: ")
            print(f"\nIngrese la cantidad de cursos que desea registrar: ")