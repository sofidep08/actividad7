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
        if cantidad <= 0 :
            print("Ingreso un dato incorrecto")
        else :
            for i in range(cantidad) :
                print(f"\nEstudiante {i+1}")
                carne = int(input("Ingrese el carné: "))
                nombre = input("Ingrese el nombre completo: ")
                edad = int(input("Ingrese la edad: "))
                carrera = input("Ingrese la carrera: ")
                cantidad_cursos = int(input("\nIngrese la cantidad de cursos que desea registrar[Max 10]: "))
                if cantidad_cursos > 10 :
                    print("Ingreso un dato incorrecto")
                else:
                    for j in range(cantidad_cursos) :
                        nombre_curso=input("Ingrese el nombre del curso: ")
                        nota_tarea=int(input("Ingrese la nota de la tarea [0 a 100]: "))
                        if nota_tarea < 0 or nota_tarea > 100 :
                            print("Ingreso un dato incorrecto")
                        else:
                            nota_parcial = int(input("Ingrese la nota del parcial [0 a 100]: "))
                            if nota_tarea < 0 or nota_tarea > 100:
                                print("Ingreso un dato incorrecto")
                            else:
                                nota_proyecto = int(input("Ingrese la nota  del proyecto [0 a 100]: "))
                                if nota_tarea < 0 or nota_tarea > 100:
                                    print("Ingreso un dato incorrecto")
                                else:
                                    estudiantes[carne] = {
                                        "nombre" : nombre,
                                        "edad" : edad,
                                        "carrera" : carrera,
                                        "nombre_curso" : {
                                            "nota_tarea" : nota_tarea,
                                            "nota_parcial" : nota_parcial,
                                            "nota_proyecto" : nota_proyecto
                                        }
                                    }

    elif opcion == 2 :
        print("\nEstudiantes registrados")
        promedio=0
        for carnet, datos in estudiantes.items():
            print(f"\nCarnet: {carnet}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Edad: {datos['edad']}")
            print(f"Carrera: {datos['carrera']}")
            print("\nCursos")
            print(f"Nombre curso: {datos['nombre_curso']}")
            print(f"Nota de tarea: {datos["nombre-curso"],["nota_tarea"]}")
            print(f"Nota de parcial: {datos["nombre-curso"], ["nota_parcial"]}")
            print(f"Nota de proyecto: {datos["nombre-curso"], ["nota_proyecto"]}")
            promedio= (nota_parcial + nota_proyecto + nota_parcial)/3

