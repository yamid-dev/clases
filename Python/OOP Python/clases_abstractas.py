#Clase abstracta es una clase que no podemos instanciar, es una reseta, modelo, o plantilla para crear clases apartir de esa plantilla

#Implementar un método significa definir cómo va a funcionar

#abc es una clase auxiliar, ABC es una metaclase (la clase de la clase) y abstractclassmethod es un decorador que nos permite indicarle a la clase que estamos utilizando un metodo abstracto (un metodo que está declarado en esta clase pero que no tiene ninguna implementación para que cuando crea una clase que hereda de esta clase abstracta lo pueda implementar)
from abc import ABC, abstractclassmethod 

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        
    @abstractclassmethod
    def trabajar(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

persona = Persona("Yamid",21,"Masculino","Programador")