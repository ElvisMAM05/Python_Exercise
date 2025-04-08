"""
1. Dada una edad clasifique esa edad si es nino, adolecente, adulto o adulto mayor
2. Se debe de crear una funcion para cada una de las validaciones
3. Imprimir al final el resultado de la validacion

Condiciones
edad < 13 = niño
edad > = 13 && edad < 18 = Adolecente
edad > = 18 && edad < 60 = Adulto
edad > =60 = Adulto Mayor
"""


print("Hola bienvenido a mi programa para calcular mi edad")
Edad = int(input("Edad ingrese: "))

def edad_menor(Edad):
    return Edad<13

def edad_Adolecente(Edad):            
                return Edad>=13 and Edad<18
            
def edad_Adulto(Edad):
    return  Edad>=18 and Edad<60

def edad_Adulto_Mayor(Edad):
    return Edad>60

def calculo_edad():

    
    if(edad_menor(Edad)):
        print("Awww, eres un bebe todavía")
        return
    
    if(edad_Adolecente(Edad)):
        print("Bueno, ya casi tienes que trabajar jaja")
        return
        
    if(edad_Adulto(Edad)):
        print("Paga tus impuestos")
        return
    
    if(edad_Adulto_Mayor(Edad)):
        print("¿Disfrutaste tu vida?")
        return    
        
calculo_edad()