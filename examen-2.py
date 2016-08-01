# -*- coding: utf-8 -*-

import abc


class Animal(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def comer(self):
        print("Como como un animal")

    @abc.abstractmethod
    def caminar(self):
        print("Camino como un animal")
    
    @abc.abstractmethod
    def mirar(self):
        print("Miro como un animal")


class Gato(Animal):

    def __init__(self):
        Animal.__init__(self)

    def comer(self):
        super(Gato, self).comer()
        print("Como como un gato")
    
    def mirar(self):
        super(Gato, self).mirar()
        print("Miro como un gato")

    def mauyar(self):
        print("Maullo como un gato")

    def dormir(self):
        print("Duermo como un gato")

    def caminar(self):
        super(Gato, self).caminar()
        print("Camino como un gato")


class Perro(Animal):

    def __init__(self):
        Animal.__init__(self)

    def caminar(self):
        super(Perro, self).caminar()
        print("Camino como un perro")

    def mirar(self):
        super(Perro, self).mirar()
        print("Miro como un perro")
    
    def ladrar(self):
        print("Ladro como un perro")

    def dormir(self):
        print("Duermo como un perro")

    def comer(self):
        super(Perro, self).comer()
        print("Como com un perro")


gato = Gato()
perro = Perro()

gato.mauyar()
gato.dormir()
gato.caminar()

perro.ladrar()
perro.dormir()
perro.comer()
