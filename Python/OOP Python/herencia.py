# Herencia = pilar fundamental de la OOP que permite a la clase hija acceder a todos los métodos y propiedades de todos los padres. Por ejemplo, Persona y Estudiante.

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hola, estoy hablando un poco...")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"mi habilidad es: {self.habilidad}"

# Esta es una clase hija llamada Empleado que hereda características de las clases padre Persona y Artista (herencia múltiple).
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        # Constructor dentro de otro constructor
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def mostrar_habilidad(self):
        return "No tengo jajaja"  
      
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, trabajo en {self.empresa} y {super().mostrar_habilidad()}")
        
    # Aquí se podría sobrescribir el método hablar si se desea.

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, universidad, notas):
        # Constructor dentro de otro constructor
        super().__init__(nombre, edad, nacionalidad)
        self.universidad = universidad
        self.notas = notas

    # Aquí se podría sobrescribir el método hablar si se desea.

roberto = EmpleadoArtista("Roberto", 43, "Colombiano", "Cantar",1000000,"Marvy Systems")

#propiedad issubclass que permite ver si una clase es hija de otra
herencia = issubclass(EmpleadoArtista,Artista)
print(herencia)
#propiedad isinstance que permite ver si un objeto es una instancia de una clase
instancia= isinstance(roberto,Estudiante)
print(instancia)

roberto.hablar()
roberto.presentarse()
