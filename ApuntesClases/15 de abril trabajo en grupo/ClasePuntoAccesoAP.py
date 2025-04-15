# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:35:53 2025

@author: lab
"""

class PuntoAccesoAP:
    def __init__(self, ssid, mac, estado):
        self.ssid = ssid
        self.mac = mac
        self.estado = estado

    def activar(self):
        print("activar() ejecutado")

    def desactivar(self):
        print("desactivar() ejecutado")

# Ejemplo de uso:
puntoaccesoap = PuntoAccesoAP("valor_0", "valor_1", "valor_2")
print(puntoaccesoap.__dict__)