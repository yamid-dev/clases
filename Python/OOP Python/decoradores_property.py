
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad
    
    #property es un decorador especial porque es un decorador reservado para las clases, que le dice esto es un getter, usalo como una propiedad
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter 
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    @nombre.deleter 
    def nombre(self):
        del self.__nombre #esto va a eliminar valores

persona = Persona("Yamid",21)

#property le dice no trates el getter como una función sino como una propiedad, compara con el archivo de encapsulamiento
nombre = persona.nombre
print(nombre)

persona.nombre="Horacio"

nombre = persona.nombre
print(nombre)

#Aqui llamo al deleter para eliminar la propiedad especificada
del persona.nombre

print("¿Qué haces?")
