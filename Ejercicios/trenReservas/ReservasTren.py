"""
Se quiere crear un programa que administre las reservas de un sistema de transporte férreo.
El tren cuenta con un número fijo de 100 sillas. De ellas, 20 son de clase ejecutiva, mientras
que el resto son de clase económica. Cada silla puede ser asignada a un pasajero que cuenta
con un nombre y una cédula. Este último dato es la entrada principal para poder consultar
una reserva o eliminarla del sistema. Cuando se asigna una silla es necesario conocer las
preferencias del usuario. Este puede elegir la posición de la silla, ventana o pasillo, y la clase,
ejecutiva o económica. Las sillas son asignadas   según su ubicación y su
clase. De igual forma, el programa permite buscar la reserva de un pasajero y visualizar los
datos de la reserva. El programa debe permitir al usuario: (valor:2,0)
• Asignar una silla en el tren
• Eliminar reserva
• Buscar pasajero
• Calcular el porcentaje de ocupación del tren

"""

import numpy as np
import os


class Tren:
    def __init__(self):
        self.sillas_ejecutivas = 20
        self.economicas = 80
        self.informacionReserva = {}
        self.reservas_ejecutivas = np.full((self.sillas_ejecutivas, 4), "D")
        self.reservas_economicas = np.full((self.economicas, 4), "D")


class SistemaReservas(Tren):
    def __init__(self):
        super().__init__()

    def _obtener_tipo_asiento(self, fila, numero_asiento):

        if reserva.clase == "Economico":
            if self.reservas_economicas[fila, numero_asiento - 1] == "D":
                return "No asignado"
            elif numero_asiento % 2 == 1:
                return "Ventana"
            else:
                return "Pasillo"
        elif reserva.clase == "Ejecutivo":

            if self.reservas_ejecutivas[fila, numero_asiento - 1] == "D":
                return "No asignado"
            elif numero_asiento % 2 == 1:
                return "Ventana"
            else:
                return "Pasillo"

    def _Get_Agregar_Reserva(self, reserva):
        if reserva.clase == "Economico":
            cedula = reserva.pasajero.cedula
            if cedula not in self.informacionReserva:
                self._agregar_reserva_economico(reserva)
                self.informacionReserva[cedula] = reserva
                print(self.informacionReserva)
            else:
                return print("Este este asiento ya esta ocupado")

        elif reserva.clase == "Ejecutivo":
            cedula = reserva.pasajero.cedula
            if cedula not in self.informacionReserva:
                self._agregar_reserva_ejecutiva(reserva)
                self.informacionReserva[cedula] = reserva
                print(self.informacionReserva)
            else:
                return print("Este este asiento ya esta ocupado")

    def _agregar_reserva_ejecutiva(self, reserva):
        try:
            fila = reserva.posicion
            columna = reserva.numero - 1
            if self.reservas_ejecutivas[fila, columna] == "D":
                self.reservas_ejecutivas[fila, columna] = "R"
                print("Se registro una reserva exitosamente")
            else:
                print("Este asiento ya esta ocupado")
        except IndexError as a:
            print(f"Descripcion del error: {a}")
            return print("Acabas de ingresar un valor erroneo para la asignacion")

    def _agregar_reserva_economico(self, reserva):

        fila = reserva.posicion
        columna = reserva.numero - 1

        if self.reservas_economicas[fila, columna] == "D":

            self.reservas_economicas[fila, columna] = "R"
        else:
            print("Este asiento ya está ocupado")

    def _mostrar_asientos(self):
        print("************************************")
        print("* Asientos de reservas economicas: *")
        print("************************************")
        print(self.reservas_economicas)
        print()
        print("***********************************")
        print("* Matriz de reservas ejecutivas:  *")
        print("***********************************")
        print(self.reservas_ejecutivas)

    def _buscar_pasajero(self, cedula):

        """
        [0,0][][][0,4]
        [1,0][][][1,4]
        [2,0][][][2,4]
        """

        if cedula in self.informacionReserva:
            reserva = self.informacionReserva[cedula]
            tipo_asiento = self._obtener_tipo_asiento(reserva.posicion, reserva.numero)
            print(
                f"El pasajero {reserva.pasajero.nombre} tiene un asiento de tipo {reserva.clase} en  {tipo_asiento}."
            )
            print(
                f"Hubicacion: fila {reserva.posicion + 1} de la columna {reserva.numero}"
            )
        else:
            print(f"No se encontro reserva para el pasajero con cedula {cedula}.")

    def _eliminar_reserva(self, cedula):
        if cedula in self.informacionReserva:
            reserva = self.informacionReserva[cedula]
            fila = reserva.posicion
            columna = reserva.numero - 1

            if reserva.clase == "Economico":
                if self.reservas_economicas[fila, columna] == "R":
                    self.reservas_economicas[fila, columna] = "D"
                    del self.informacionReserva[cedula]
                    print(f"Reserva eliminada para el pasajero con cédula {cedula}.")
                else:
                    print("Este asiento no está ocupado por la reserva")
            elif reserva.clase == "Ejecutivo":
                if self.reservas_ejecutivas[fila, columna] == "R":
                    self.reservas_ejecutivas[fila, columna] = "D"
                    del self.informacionReserva[cedula]
                    print(f"Reserva eliminada para el pasajero con cédula {cedula}.")
                else:
                    print("Este asiento no esta ocupado por la reserva.")
        else:
            print(f"No se encontro reserva para el pasajero con cedula {cedula}.")


class Reserva:
    def __init__(self, posicion_silla, numero_silla, clase, pasajero):
        self.posicion = posicion_silla
        self.numero = numero_silla
        self.clase = clase
        self.pasajero = pasajero


class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
