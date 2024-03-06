"""
Se tiene un curso universitario el cual contiene un array de estudiantes. Para cada
estudiante se tienen los datos: nombre y apellidos del estudiante, código, número de
semestre y nota final del estudiante. Se requiere implementar los siguientes métodos:

• Añadir un estudiante al curso: se ingresan por teclado los datos del estudiante.
El código del estudiante debe ser único, si el código ya existe se debe generar
el mensaje correspondiente.

• Buscar un estudiante de acuerdo con su código ingresado por teclado: si se
encuentra muestra los datos del estudiante. De lo contrario, debe mostrar el
mensaje correspondiente.

• Eliminar un estudiante de acuerdo con su código ingresado por teclado: si se
encuentra muestra los datos del estudiante y se solicita una confirmación de la
eliminación. Si no, debe mostrar el mensaje correspondiente.

• Calcular promedio del curso: sumar las notas de los estudiantes y dividirlas por
la cantidad de estudiantes que tiene el curso.

• Obtener la cantidad de estudiantes que aprobó el curso: calcular el número de
estudiantes que obtuvo un promedio mayor o igual a 3.0 y mostrarlo en
pantalla. También se debe calcular el porcentaje de estudiantes que aprobó el
curso


"""

from tabulate import tabulate
from colorama import Fore, Style
import os


class StudentCourse:

    def __init__(self):
        self.curse = curseUniversity = [
            {
                "1101445764": {
                    "name": "Carlos Alberto",
                    "lastname": "Herazo Paternina",
                    "code": "1101445764",
                    "semester": 3,
                    "finalGrade": 8.5,
                }
            },
            {
                "1102556890": {
                    "name": "María Fernanda",
                    "lastname": "Gómez Ramírez",
                    "code": "1102556890",
                    "semester": 2,
                    "finalGrade": 5,
                }
            },
        ]

    def display_menu(self):
        print(
            Fore.BLUE
            + Style.BRIGHT
            + "================================="
            + Style.RESET_ALL
        )
        print(
            Fore.BLUE
            + Style.BRIGHT
            + f"===== { Style.RESET_ALL} Student Course Menu {Fore.BLUE  + Style.BRIGHT }======"
            + Style.RESET_ALL
        )
        print(
            Fore.BLUE
            + Style.BRIGHT
            + "================================="
            + Style.RESET_ALL
        )
        print(
            Fore.BLUE
            + Style.BRIGHT
            + f"={Style.RESET_ALL} 1. Agregar Estudiante {Fore.BLUE +Style.BRIGHT}        ="
            + Style.RESET_ALL
        )

        print(
            Fore.BLUE
            + Style.BRIGHT
            + f"={Style.RESET_ALL} 2. Ver info Estudiante  {Fore.BLUE +Style.BRIGHT}      ="
            + Style.RESET_ALL
        )
        print(
            Fore.BLUE
            + Style.BRIGHT
            + f"={Style.RESET_ALL} 3. Ver Estudiantes  {Fore.BLUE +Style.BRIGHT}          ="
            + Style.RESET_ALL
        )
        print(
            Fore.BLUE
            + Style.BRIGHT
            + f"={Style.RESET_ALL} 4. Eliminar Estudiante {Fore.BLUE +Style.BRIGHT}       ="
            + Style.RESET_ALL
        )
        print(
            Fore.BLUE
            + Style.BRIGHT
            + f"={Style.RESET_ALL} 5. Calcular Promedio {Fore.BLUE +Style.BRIGHT}         ="
            + Style.RESET_ALL
        )
        print(
            Fore.BLUE
            + Style.BRIGHT
            + f"={Style.RESET_ALL} 6. Ver Estudiantes Aprobados {Fore.BLUE +Style.BRIGHT} ="
            + Style.RESET_ALL
        )
        print(
            Fore.BLUE
            + Style.BRIGHT
            + f"={Style.RESET_ALL} 7. Salir {Fore.BLUE +Style.BRIGHT}                     ="
            + Style.RESET_ALL
        )

        print(
            Fore.BLUE
            + Style.BRIGHT
            + "================================="
            + Style.RESET_ALL
        )

    def display_table(self, data):
        headers = ["Code", "Name", "Lastname", "Semester", "Final Grade"]
        table_data = []
        for student_dict in data:
            for key, val in student_dict.items():
                row_data = [
                    val["code"],
                    val["name"],
                    val["lastname"],
                    val["semester"],
                    val["finalGrade"],
                ]
                table_data.append(row_data)
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    """Añadir un estudiante al curso: se ingresan por teclado los datos del estudiante.
    El código del estudiante debe ser único, si el código ya existe se debe generar
    el mensaje correspondiente"""

    def add_student(self, name, lastname, code, semester, finalGrade):
        # Verificar si el código del estudiante ya existe en la lista
        for student_dict in self.curse:
            for _, data in student_dict.items():
                if data["code"] == code:
                    print(f"El estudiante con código {code} ya existe.")
                    return False
                else:
                    # añadir al estudiante a la lista si no existe
                    new_student = {
                        code: {
                            "name": name,
                            "lastname": lastname,
                            "code": code,
                            "semester": semester,
                            "finalGrade": finalGrade,
                        }
                    }
                    self.curse.append(new_student)
                    print(f"Estudiante {name} añadido correctamente.")
                    return True

    """
        Buscar un estudiante de acuerdo con su código ingresado por teclado: si se
        encuentra muestra los datos del estudiante. De lo contrario, debe mostrar el
        mensaje correspondiente.
    """

    def view_student(self, code):
        headers = ["Field", "Value"]
        table_data = []

        for student_dict in self.curse:
            for key, data in student_dict.items():
                if key == code:
                    for val, dat in data.items():
                        table_data.append([val, dat])

        if table_data:
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        else:
            print(f"No se encontro un estudiante con el codigo:  {code}")

    """
        Eliminar un estudiante de acuerdo con su código ingresado por teclado: si se
        encuentra muestra los datos del estudiante y se solicita una confirmación de la
        eliminación. Si no, debe mostrar el mensaje correspondiente.
    """

    def delate_student(self, code):
        for student_dict in self.curse:
            for key in student_dict:
                if key == code:
                    self.curse.remove(student_dict)
                    print(f"Estudiante con código {code} eliminado correctamente.")
                    return True

    """
        Calcular promedio del curso: sumar las notas de los estudiantes y dividirlas por
        la cantidad de estudiantes que tiene el curso.
    """

    def calculate_prom(self):
        accumulated = 0
        cant_student = len(self.curse)
        for student_dict in self.curse:
            for _, val in student_dict.items():
                for key, data in val.items():
                    if key == "finalGrade":
                        accumulated += data

        average = accumulated / cant_student
        print("El promedio de notas calculadas seria: ", average)

    """
        Obtener la cantidad de estudiantes que aprobó el curso: calcular el número de
        estudiantes que obtuvo un promedio mayor o igual a 3.0 y mostrarlo en
        pantalla. También se debe calcular el porcentaje de estudiantes que aprobó el
        curso
    """

    def approved_curse(self):
        headers = ["Code", "Name", "Lastname", "Semester", "Final Grade"]
        table_data = []
        cont = 0
        for student_dict in self.curse:
            for key, val in student_dict.items():
                if val["finalGrade"] > 3.0:
                    row_data = [
                        val["code"],
                        val["name"],
                        val["lastname"],
                        val["semester"],
                        val["finalGrade"],
                    ]
                    table_data.append(row_data)
                    cont += 1

        if  len(self.curse) > 0:
            percentage_passed = (cont / len(self.curse)) * 100
            print(f"Estudiantes que aprovaron: {cont}")
            print(f"Porcentaje de estudiantes que aprobaron: {percentage_passed:.2f}%")
            if table_data:
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
        else:
            print("No se encontraron estudiantes que aprobaron.")


while True:
    estudiante = StudentCourse()
    estudiante.display_menu()
    option = input("Ingrese el numero de la opcion deseada: ")

    if option == "1":
        name = input("Ingrese el nombre del estudiante: ")
        lastname = input("Ingrese el apellido del estudiante: ")
        code = input("Ingrese el código del estudiante: ")
        semester = int(input("Ingrese el semestre del estudiante: "))
        finalGrade = float(input("Ingrese la nota final del estudiante: "))
        estudiante.add_student(name, lastname, code, semester, finalGrade)
        estudiante.display_table(estudiante.curse)
        input("Presione Enter para continuar")
        os.system("cls")

    elif option == "2":
        code = input("Ingrese el código del estudiante: ")
        estudiante.view_student(code)
        input("Presione Enter para continuar")
        os.system("cls")
    elif option == "3":
        estudiante.display_table(estudiante.curse)
        input("Presione Enter para continuar")
        os.system("cls")
    elif option == "4":
        code = input("Ingrese el código del estudiante: ")
        estudiante.delete_student(code)
        input("Presione Enter para continuar")
        os.system("cls")
    elif option == "5":
        estudiante.calculate_prom()
        input("Presione Enter para continuar")
        os.system("cls")
    elif option == "6":
        estudiante.approved_curse()
        input("Presione Enter para continuar")
        os.system("cls")
    elif option == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida. Por favor, ingrese un numero del 1 al 6")
        input("Presione Enter para continuar")
        os.system("cls")
