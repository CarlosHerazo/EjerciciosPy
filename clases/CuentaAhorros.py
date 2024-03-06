"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Construye los siguientes métodos para la clase:

• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
• mostrar (): Muestra los datos de la cuenta.
• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.

"""

from random import randrange
from colorama import Fore, Style
import os


class Cuenta:
    _cuentasCreadas = {
        "111": {
            "Nombre": "Carlos Herazo",
            "Edad": 18,
            "cedula": 111,
            "Tipo": "PersonaNatural",
            "NumeroC": 1215121512,
            "Cantidad $": 1200,
        },
        "123": {
            "Nombre": "Maria Juliana",
            "Edad": 23,
            "cedula": 123,
            "Tipo": "CuentaJoven",
            "NumeroC": 11524522,
            "Cantidad $": 1200,
        },
    }

    def __init__(self, titular="", cantidad=0, edad=0, id_C=""):
        self._titular = titular
        self._edad = edad
        self.__id_c = id_C
        self.__cantidad = cantidad

    @classmethod
    def mostrar(cls, id_C):
        print(Fore.CYAN + "INFORMACION DE LA CUENTA" + Style.RESET_ALL)
        if id_C not in cls._cuentasCreadas[id_C]:
            for llave, val in cls._cuentasCreadas[id_C].items():
                print(f"{llave} : {val}")

    def ingresar(self, cant, id_C):
        cantidad = Cuenta._cuentasCreadas[id_C]["Cantidad $"]
        if cant > 0:
            cantidad += cant
            Cuenta._cuentasCreadas[id_C]["Cantidad $"] = cantidad
            return print(
                Fore.GREEN
                + f"Tu tarjeta se ha recargado a {Fore.YELLOW} ${cantidad}"
                + Style.RESET_ALL
            )
        else:
            print(
                +Fore.RED
                + "La cantidad ingresada debe ser mayor que cero."
                + Style.RESET_ALL
            )
            return None

    def retirar(self, cant, id_C):
        cantidad = Cuenta._cuentasCreadas[id_C]["Cantidad $"]
        if cant > 0 and cant < cantidad:
            cantidad -= cant
            Cuenta._cuentasCreadas[id_C]["Cantidad $"] = cantidad
            print(Fore.RED + f"- {cant}" + Style.RESET_ALL)
            return print(
                Fore.GREEN
                + f"Retirada exitosa.{Fore.YELLOW} Saldo actual:{Style.RESET_ALL} {Fore.GREEN}{cantidad}"
                + Style.RESET_ALL
            )
        else:
            print(
                Fore.RED
                + "Upps, hubo un error al poder retirar la cantidad solicitada."
                + Style.RESET_ALL
            )
            return None

    @classmethod
    def _Set_cuentaExistente(cls, cedula, valor):
        if valor == 1:
            if cedula in cls._cuentasCreadas:
                cuenta = cls._cuentasCreadas[cedula]
                if cuenta["Tipo"] == "CuentaJoven":
                    return True
                else:
                    return False
            return False
        else:
            if cedula in cls._cuentasCreadas:
                cuenta = cls._cuentasCreadas[cedula]
                if cuenta["Tipo"] == "PersonaNatural":
                    return True
                else:
                    return False
            return False


class Asesor(Cuenta):
    def __init__(self, usuario):
        super().__init__("Asesor", 0)
        self.__usuario = usuario

        if self._set_validar_asesor():
            print(Fore.GREEN + "Acceso Conseguido" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Acceso Denegado" + Style.RESET_ALL)

    def _set_validar_asesor(self):
        return self.__usuario.lower() == "asesor"

    def CrearCuenta(self, titular, tipo_cuenta, edad, cedula):
        while True:
            res = input("¿Desea ingresar alguna cantidad?: (s/n)")
            bonificacion = 20000
            if res.lower() == "s":
                cant = float(input("Ingrese el valor a Depositar:"))

                if tipo_cuenta == "CuentaJoven":
                    if cant > 0:
                        totalRecarga = cant + bonificacion
                        print(
                            f"Su cuenta a sido cargada con {cant} + {bonificacion} para un total de: {totalRecarga}"
                        )
                        break
                    else:
                        totalRecarga = cant + bonificacion
                        print(
                            f"Su cuenta a sido cargada con {cant} + {bonificacion} para un total de: {totalRecarga}"
                        )
                        break
                else:
                    if cant > 0:
                        print(f"Su cuenta a sido cargada con {cant}")
                        break
            elif tipo_cuenta == "CuentaJoven":
                cant = self._Cuenta__cantidad + bonificacion
                print(
                    f"Su cuenta a sido cargada con {self._Cuenta__cantidad} + {bonificacion} para un total de: {cant}"
                )
                break
            else:
                cant = self._Cuenta__cantidad
                break

        numeroC = randrange(10**15, 10**16)
        if tipo_cuenta == "PersonaNatural":
            nueva_cuenta = {
                "Nombre": titular,
                "Edad": edad,
                "cedula": cedula,
                "Tipo": tipo_cuenta,
                "Numero de cuenta": numeroC,
                "Cantidad $": cant,
            }
        elif tipo_cuenta == "CuentaJoven":

            nueva_cuenta = {
                "Nombre": titular,
                "Edad": edad,
                "cedula": cedula,
                "Bonificacion %": bonificacion,
                "Tipo": tipo_cuenta,
                "Numero de cuenta": numeroC,
                "Cantidad $": cant,
            }
            print(
                Fore.GREEN
                + "Felicidades, Por ser cuenta Joven tienes una bonificacion de $20000"
                + Style.RESET_ALL
            )
        else:

            return print("Tipo de cuenta no valido.")

        self._cuentasCreadas[cedula] = nueva_cuenta
        print(f"Cuenta creada con exito para {titular} - Tipo: {tipo_cuenta}")

    def ver_todas_las_cuentas(self):
        print("\nTodas las cuentas creadas:")
        for idn, cuenta in self._cuentasCreadas.items():
            print(f"Numero de Identificacion: {idn}")
            for llave, val in cuenta.items():
                print(f"{llave} : {val}")
            print("----")


class CuentaJoven(Cuenta):

    def __init__(self, cedula):
        self.cedula = cedula
        print(Cuenta._cuentasCreadas)
        if not self._Set_cuentaExistente(cedula, 1):
            print(Fore.RED + "Esta cuenta No esta Registrada" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Inicio Exitoso" + Style.RESET_ALL)

    def esTitularValido(self, id_C):
        edad = Cuenta._cuentasCreadas[id_C]["Edad"]
        return 18 <= edad < 25

    def retirar_menor(self, cant, id_C):
        cuenta_existente = self._Set_cuentaExistente(id_C, 1)

        if cuenta_existente:
            if self.esTitularValido(id_C):
                return super().retirar(cant, id_C)

            else:
                return print(
                    Fore.RED
                    + "No puedes retirar dinero. El titular es menor de edad."
                    + Style.RESET_ALL
                )
        else:
            return print(
                Fore.RED
                + "No hay una cuenta válida con el ID proporcionado."
                + Style.RESET_ALL
            )


class PersonaNatural(Cuenta):

    def __init__(self, cedula):
        self.cedula = cedula
        print(Cuenta._cuentasCreadas)
        if not self._Set_cuentaExistente(cedula, 2):
            print(Fore.RED + "Esta cuenta No esta Registrada" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Inicio Exitoso" + Style.RESET_ALL)
