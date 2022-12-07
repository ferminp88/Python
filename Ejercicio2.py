from pickle import *

class Vehiculo:

    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return self.color + " " + self.puertas


escort = Vehiculo("Azul", "4")
print(escort)

file = open('vehiculo_objeto', 'w+b')

dump(escort, file)

file.seek(0)
nuevo_escort = load(file)

print(nuevo_escort)
file.close()