"""
Un carro está compuesto por un motor, un chasis, cuatro llantas y una carrocería. u Los

motores tienen un atributo para representan el volumen del motor en litros.

u El chasis tiene un atributo, el tipo de chasis, que es un valor enumerado con valores Independiente
o Monocasco. 

u La carrocería tiene un atributo que representa el tipo de carrocería,
enumerado con valores Independiente, Autoportante o Tubular y un color (tipo String). 

u
Las llantas tienen atributos como: marca (tipo String); diámetro del rin, altura y anchura (los
últimos tres son tipo int). 

Cada parte de un carro tiene su correspondiente constructor y un
método imprimir que muestra los valores de sus atributos en pantalla. Se requiere en una
clase de prueba, desarrollar un método main que cree un carro con un motor de 2 litros, un
chasis monocasco, una carrocería de color rojo y tipo tubular, 4 llantas de marca
“Goodyear”, diámetro del rin de 25 pulgadas, altura de 20 pulgadas y anchura de 15
pulgadas. Luego, se deben imprimir los datos del carro en pantalla.

"""


class Motor:
    def __init__(self, volLitros):
        self.vLitros = float(volLitros)

    def Mmotor(self):
        print(f"Motor: {self.vLitros} litros")


class Chasis:
    def __init__(self, tipoChasis):
        self.tchasis = str(tipoChasis)

    def Mchasis(self):
        print(f"Chasis: {self.tchasis}")


class Carroceria:
    def __init__(self, tipoCarroceria, color):
        self.tipoCarroceria = str(tipoCarroceria)
        self.color = str(color)

    def Mcarroceria(self):
        print(f"Carroceria: {self.tipoCarroceria}, Color: {self.color}")


class Llanta:
    def __init__(self, marca, dRin, altura, anchura):
        self.marca = str(marca)
        self.diametroRin = float(dRin)
        self.altura = float(altura)
        self.anchura = float(anchura)

    def Mllanta(self):
        print(
            f"Llanta: Marca {self.marca}, Diametro del Rin: {self.diametroRin} pulgadas, Altura: {self.altura} pulgadas, Anchura: {self.anchura} pulgadas"
        )


class Carro(Motor, Chasis, Carroceria, Llanta):
    def __init__(
        self,
        volLitros,
        tipoChasis,
        tipoCarroceria,
        color,
        marcaLlanta,
        dRin,
        altura,
        anchura,
    ):

        Motor.__init__(self, volLitros)
        Chasis.__init__(self, tipoChasis)
        Carroceria.__init__(self, tipoCarroceria, color)
        Llanta.__init__(self, marcaLlanta, dRin, altura, anchura)

    def main(self):
        # Llamamos el metodo Que nos mustra el resultado que cada clase instanciada
        self.Mmotor()
        self.Mchasis()
        self.Mcarroceria()
        self.Mllanta()


print("====================================")
print("=====SISTEMATIZACION DE CARROS======")
print("====================================")

try:
    volLitros = float(input("Ingrese el volumen del motor en litros: "))
    tipoChasis = input("Ingrese el tipo de chasis: ")
    tipoCarroceria = input("Ingrese el tipo de carroceria: ")
    color = input("Ingrese el color de la carroceria: ")
    marcaLlanta = input("Ingrese la marca de la llanta: ")
    dRin = float(input("Ingrese el diametro del rin en pulgadas: "))
    altura = float(input("Ingrese la altura de la llanta en pulgadas: "))
    anchura = float(input("Ingrese la anchura de la llanta en pulgadas: "))

    carro = Carro(
        volLitros, tipoChasis, tipoCarroceria, color, marcaLlanta, dRin, altura, anchura
    )
    carro.main()
except ValueError:
    print("Error al Ingresar valores")
