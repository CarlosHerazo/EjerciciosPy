from CuentaAhorros import *

print("* ****************************************** *")
print(
    "*"
    + Fore.GREEN
    + " BIENVENIDOS AL SISTEMA DE CUENTAS BANCARIAS"
    + Style.RESET_ALL
    + " *"
)
print("* ****************************************** *")


def interactuar_con_asesor(asesor):
    while True:
        print(Fore.YELLOW + "***********************************************")
        print("*    Seleccione una opcion como Asesor:       *")
        print("***********************************************")
        print(
            "* "
            + Fore.GREEN
            + "1. Crear nueva cuenta"
            + Fore.YELLOW
            + "                       *"
        )
        print(
            "* "
            + Fore.BLUE
            + "2. Ver todas las cuentas creadas"
            + Fore.YELLOW
            + "            *"
        )
        print(
            "* "
            + Fore.RED
            + "3. Volver al menu principal"
            + Fore.YELLOW
            + "                 *"
        )
        print("***********************************************" + Style.RESET_ALL)

        opcion = input("Ingrese el numero de la opcion: ")

        if opcion == "1":
            titular = input("Ingrese el titular de la cuenta: ")

            tipo_cuenta = input(
                "Ingrese el tipo de cuenta (PersonaNatural o CuentaJoven): "
            )
            edad = int(input("¿Cual es la edad del titular?"))
            identificacion = input("Ingrese su Cedula")

            if tipo_cuenta not in ["PersonaNatural", "CuentaJoven"]:
                print("Tipo de cuenta no válido. Inténtelo de nuevo.")
                input("Precione Enter para continuar")
                os.system("cls")
                continue

            asesor.CrearCuenta(titular, tipo_cuenta, edad, identificacion)

        elif opcion == "2":
            asesor.ver_todas_las_cuentas()
            input("Precione Enter para continuar")
            os.system("cls")

        elif opcion == "3":
            print("Volviendo al menú principal.")
            input("Precione Enter para continuar")
            os.system("cls")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")
            input("Precione Enter para continuar")
            os.system("cls")


def interactuar_con_cuenta(cuenta, id_c, valor):

    while True:
        print(
            Fore.LIGHTGREEN_EX
            + "***********************************************"
            + Style.RESET_ALL
        )
        print(
            Fore.LIGHTGREEN_EX
            + f"*{ Style.RESET_ALL}    Seleccione una opcion para la cuenta:    {Fore.LIGHTGREEN_EX}*"
        )
        print(
            Fore.LIGHTGREEN_EX
            + "***********************************************"
            + Style.RESET_ALL
        )
        print(
            Fore.LIGHTGREEN_EX
            + f"*{Style.RESET_ALL} 1. Mostrar informacion de la cuenta         {Fore.LIGHTGREEN_EX}*"
            + Style.RESET_ALL
        )
        print(
            Fore.LIGHTGREEN_EX
            + f"*{Style.RESET_ALL} 2. Ingresar dinero                          {Fore.LIGHTGREEN_EX}*"
        )
        print(
            f"*{Style.RESET_ALL} 3. Retirar dinero                           {Fore.LIGHTGREEN_EX}*"
        )
        print(
            f"*{Style.RESET_ALL} 4. Volver al menú principal                 {Fore.LIGHTGREEN_EX}*"
        )
        print("***********************************************" + Style.RESET_ALL)
        if valor == 1:
            opcion = input("Ingrese el numero de la opcion: ")
            if opcion == "1":
                print(id_c)
                cuenta.mostrar(id_c)
                input("Precione Enter para continuar")
                os.system("cls")

            elif opcion == "2":
                cantidad = float(input("Ingrese la cantidad a ingresar: "))
                cuenta.ingresar(cantidad, id_c)
                input("Precione Enter para continuar")
                os.system("cls")

            elif opcion == "3":
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta.retirar_menor(cantidad, id_c)
                input("Precione Enter para continuar")
                os.system("cls")

            elif opcion == "4":
                print("Volviendo al menú principal.")
                input("Precione Enter para continuar")
                os.system("cls")
                break

            else:
                print("Opción no válida. Inténtelo de nuevo.")
                input("Precione Enter para continuar")
                os.system("cls")

        else:
            opcion = input("Ingrese el numero de la opcion: ")
            if opcion == "1":
                print(id_c)
                cuenta.mostrar(id_c)
                input("Precione Enter para continuar")
                os.system("cls")

            elif opcion == "2":
                cantidad = float(input("Ingrese la cantidad a ingresar: "))
                cuenta.ingresar(cantidad, id_c)
                input("Precione Enter para continuar")
                os.system("cls")

            elif opcion == "3":
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta.retirar(cantidad, id_c)
                input("Precione Enter para continuar")
                os.system("cls")

            elif opcion == "4":
                print("Volviendo al menú principal.")
                input("Precione Enter para continuar")
                os.system("cls")
                break

            else:
                print("Opción no válida. Inténtelo de nuevo.")
                input("Precione Enter para continuar")
                os.system("cls")


while True:
    print(Fore.YELLOW + "* ****************************************** *")
    print("*           Seleccione una opcion:           *")
    print("* ****************************************** *")
    print(
        "* "
        + Fore.GREEN
        + "1. Acceder como Asesor"
        + Fore.YELLOW
        + "                     *"
    )
    print(
        "* "
        + Fore.GREEN
        + "2. Acceder como Usuario Natural"
        + Fore.YELLOW
        + "            *"
    )
    print(
        "* "
        + Fore.GREEN
        + "3. Acceder como Cuenta Joven"
        + Fore.YELLOW
        + "               *"
    )
    print(
        "* "
        + Fore.GREEN
        + "4. Salir"
        + Fore.YELLOW
        + "                                   *"
    )
    print(
        Fore.YELLOW + "* ****************************************** *" + Style.RESET_ALL
    )

    opcion = input("Ingrese el número de la opcion: ")

    if opcion == "1":
        usuario_asesor = input("Ingrese el nombre de usuario de Asesor: ")
        asesor = Asesor(usuario_asesor)
        input("Precione Enter para continuar")
        os.system("cls")
        if asesor._set_validar_asesor():
            interactuar_con_asesor(asesor)
        else:
            print("Intente nuevamente")

    elif opcion == "2":
        id_c = input("Ingrese su identificacion: ")
        usuario_natural = PersonaNatural(id_c)

        if usuario_natural._Set_cuentaExistente(id_c, 2):
            valor = 2
            interactuar_con_cuenta(usuario_natural, id_c, valor)
            os.system("cls")
        else:
            continue
            os.system("cls")

    elif opcion == "3":
        id_c = input("Ingrese identificacion: ")

        cuenta_joven = CuentaJoven(id_c)

        if cuenta_joven._Set_cuentaExistente(id_c, 1):
            valor = 1
            interactuar_con_cuenta(cuenta_joven, id_c, valor)
            os.system("cls")
        else:
            continue
            os.system("cls")

    elif opcion == "4":
        print("Saliendo del sistema.")
        break

    else:
        os.system("cls")
        print("Opcion no valida")
