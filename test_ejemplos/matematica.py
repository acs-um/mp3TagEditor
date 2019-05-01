class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b


class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2


class Rectangulo:

    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def perimetro(self):
        return (self.lado_a * 2) + (self.lado_b * 2)

    def area(self):
        return self.lado_a * self.lado_b
