#Clase abstracta es una clase que no podemos instanciar, es una reseta, modelo, o plantilla para crear clases apartir de esa plantilla, se parece a la herencia de clases, pero en el caso de la clase abstracta, si creamos nuevas clases obligamos a que si o si debamos implementar los métodos definidos en la clase abstracta, esto fomenta el polimorfismo.

#Implementar un método significa definir cómo va a funcionar

#abc es una clase auxiliar, ABC es una metaclase (la clase de la clase) y abstractclassmethod es un decorador que nos permite indicarle a la clase que estamos utilizando un metodo abstracto (un metodo que está declarado en esta clase pero que no tiene ninguna implementación para que cuando crea una clase que hereda de esta clase abstracta lo pueda implementar)
from abc import ABC, abstractclassmethod 

#Esto es una clase abstracta, sin ABC no sería una clase abstracta y el método abstracto perdería todo su poder
class Persona(ABC):
    
    #esto es un método abstracto
    @abstractclassmethod
    #init es un método especial
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    #esto también es un método abstracto        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    #el abstract method class hace que obligatoriamente debas crear una implementación para ese método 
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    #el abstract method class hace que obligatoriamente debas crear una implementación para ese método 
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    #el abstract method class hace que obligatoriamente debas crear una implementación para ese método 
    def hacer_actividad(self):
        print(f"Estoy trabajando actualmente en el rubro de: {self.actividad}")
        
lucas = Estudiante("Lucas",21,"Masculino","programación")
lucas.presentarse()
lucas.hacer_actividad()
pedro = Trabajador("Pedro",30,"Masculino","programación")
pedro.presentarse()
pedro.hacer_actividad()
