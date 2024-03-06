"""
1. Enunciado: clase Cadena.
Se desea construir un programa que dado un String con valor inicial de: “Programación
Orientada a Objetos”, realice las siguientes operaciones:
a. Obtener la longitud de dicho String.
b. Eliminar los espacios en blanco del String obtenido en el paso anterior.
c. Pasar todos los caracteres del String (obtenido en el paso anterior) a mayúsculas.
d. Concatenar al String (obtenido en el paso anterior) el String“12345”.
e. Extraer del String (obtenido en el paso anterior), un Substring desde la posición 10 al
15.
f. Reemplazar en el String (obtenido en el paso anterior) el carácter “o” por “O”.
g. Comparar el String (obtenido en el paso anterior) con el String “Programación”.
Después de cada paso, se debe mostrar el resultado en pantalla.

"""


class Cadena:
    def __init__(self, cadena):
        self.cadena = cadena

    def obtenerLongitud(self):
        if self.cadena != "":
            return len(self.cadena)
        else:
            return print("Por favor escriba un texto")

    def eliminarEspacios(self):
        if self.cadena != "":
            val = self.cadena.replace(" ", "")
            return val
        else:
            return print("Por favor escriba un texto")

    def convertirMayus(self, val):
        if val != "":
            mayus = val.upper()
            return mayus
        else:
            return print("Por favor escriba un texto")

    def concatenar(self, val, mayus):
        if val != "" or mayus != "":
            return mayus + val
        else:
            return print("Por favor escriba un texto")

    def extraer(self, cont):
        if cont != "":
            return cont[9:15]
        else:
            return print("Por favor escriba un texto")

    def reemplazo(self, reem, caracter_a_reemplazar, nuevo_caracter):
        if reem != "":
            return reem.replace(caracter_a_reemplazar, nuevo_caracter)
        else:
            return print("Por favor escriba un texto")

    def comparacion(self, com):
        if com == "Programación":
            return "Igual"
        else:
            return "Diferente"

cadena = Cadena("Programación Orientada a Objetos")

longitud = cadena.obtenerLongitud()
print("Longitud:", longitud)

sin_espacios = cadena.eliminarEspacios()
print("Sin espacios:", sin_espacios)

mayusculas = cadena.convertirMayus(sin_espacios)
print("Mayusculas:", mayusculas)

concat = cadena.concatenar(sin_espacios, mayusculas)
print("Las cadenas unidas son: ", concat)

extraer = cadena.extraer(concat)
print("Nueva subcadena: ", extraer)

reemplazo = cadena.reemplazo(extraer, "O", "o").replace("Ó", "ó")
print("Reemplazo de palabras: ", reemplazo)

comparacion = cadena.comparacion(reemplazo)
print("La comparacion es: ", comparacion)
