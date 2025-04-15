# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:35:22 2025

@author: lab
"""

class Router:
    def __init__(self, nombre, ip, estado):
        self.nombre = nombre
        self.ip = ip
        self.estado = estado

    def conectar(self):
        print("conectar() ejecutado")

    def desconectar(self):
        print("desconectar() ejecutado")

# Ejemplo de uso:
router = Router("valor_0", "valor_1", "valor_2")
print(router.__dict__)