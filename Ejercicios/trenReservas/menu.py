from ReservasTren import *


sistema_reservas = SistemaReservas()


def menu():
    print("* ********************************** *")
    print("* Bienvenido al sistema de reservas: *")
    print("* ********************************** *")
    print("* 1. Agregar reserva                 *")
    print("* 2. Mostrar asientos                *")
    print("* 3. Buscar pasajero                 *")
    print("* 4. Eliminar reserva                *")
    print("* 5. Salir                           *")
    print("* ********************************** *")
    print("* ********************************** *")

    opcion = int(input("Ingrese el numero de la opcion deseada: "))

    return opcion


while True:

    opcion = menu()
    os.system("cls")
    input("Presione Enter para continuar")

    if opcion == 1:
        try:
            nombre = input("Ingrese su nombre: ")
            cedula = input("Ingrese su cédula: ")
            clase = input("Ingrese la clase (Economico/Ejecutivo): ")
            posicion = int(input("Ingrese la fila de la silla: "))
            numero = int(input("Ingrese el número de la silla: "))
        except ValueError as e:
            print(
                "Error: Ingrese un valor numérico válido para la fila y el número de la silla."
            )
            continue
        except Exception as e:
            print(f"Error inesperado: {e}")
            continue
        finally:
            print("***********************************")

        cliente = Usuario(nombre, cedula)
        reserva = Reserva(posicion - 1, numero, clase, cliente)
        sistema_reservas._Get_Agregar_Reserva(reserva)

    elif opcion == 2:
        sistema_reservas._mostrar_asientos()
        input("Presione Enter para continuar")
        os.system("cls")

    elif opcion == 3:
        cedula = input("Ingrese la cédula del pasajero: ")
        sistema_reservas._buscar_pasajero(cedula)
        input("Presione Enter para continuar")
        os.system("cls")
    elif opcion == 4:
        cedula = input("Ingrese la cédula del pasajero cuya reserva desea eliminar: ")
        sistema_reservas._eliminar_reserva(cedula)
        input("Presione Enter para continuar")
        os.system("cls")

    elif opcion == 5:
        print("Saliendo del sistema de reservas. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
        os.system("cls")
