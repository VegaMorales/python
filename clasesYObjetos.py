class Humano:
    def __init__(self, edad) -> None:
        self.edad = edad

    def hablar(self, mensaje):
        print (self.edad)
        print (mensaje)

pedro = Humano(29)
raul = Humano (18)

raul.hablar('hola')
pedro.hablar('hola, Raul')