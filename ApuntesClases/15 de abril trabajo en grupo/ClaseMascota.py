# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:33:18 2025

@author: lab
"""

class Mascota:
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad

    def jugar(self):
        print("jugar() ejecutado")

    def alimentar(self):
        print("alimentar() ejecutado")

# Ejemplo de uso:
mascota = Mascota("valor_0", "valor_1", "valor_2")
print(mascota.__dict__)