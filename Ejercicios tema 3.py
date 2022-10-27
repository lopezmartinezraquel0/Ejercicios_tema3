'''PRIMERA PARTE'''

#Crear una función con tres parámetros que sean números que se suman entre sí.
def suma(n1,n2,n3):
    return n1+n2+n3

#Llamar a la función en el main y darle valores.
suma(1,2,3)

'''SEGUNDA PARTE'''

#Crear una clase coche.
class Coche():
    def __init__(self):
        pass
    
#Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
class Coche():
    def __init__(self):
        self.puertas=5
        
#Una función que incremente el número de puertas que tiene el coche.
class Coche():
    def __init__(self):
        self.puertas=5
    
    def incremento(self,puerta):
        if (self.puertas==5):
            self.puertas+=puerta
        return 'El número de puertas incrementó a:' ,self.puertas
    
#Crear un objeto miCoche en el main y añadirle una puerta.
miCoche=Coche()
miCoche.incremento(3)

#Mostrar el número de puertas que tiene el objeto.
miCoche=Coche()
miCoche.incremento(3)