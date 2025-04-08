"""
Cree una función de bienvenida para un usuario que se encargue de dar la bienvenida a un usuario X
debe solicitar el nombre del usuario.
"""

nombre= input("Bienvenido a mi programa, por favor digita tu nombre: ")

"""
Cree una funcion que se encargue de tomar dos notas y determine su promedio
"""

def promedio(a,b):
    
    Nota_Total= a+b
    
    
    return int( Nota_Total/2)


a=int(input("Digita la primera nota: "))
b=int(input("Digita la segunda nota: "))

resultado=promedio(a,b)



"""
Cree una funcion que permita mostrar el resultado del promedio al usuario, se debe mostrar el nombre
del usuario y el promedio
"""    

print("Hola ",nombre, "tu nota final es: ", resultado)


