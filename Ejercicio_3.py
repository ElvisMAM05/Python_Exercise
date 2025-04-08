""" 
Escribe un programa que solicite al usuario una lista de números y luego cuente cuántos de esos números
son pares y cuántos son impares.
• Pide al usuario que ingrese una lista de números separados por comas.
• Convierte la entrada en una lista de enteros.
• Recorre la lista y cuenta cuántos números son pares y cuántos son impares.
• Muestra el resultado al usuario.
"""

print("Hola, bienvenido a mi programa")
Numeros=input(("Por favor, digita varios numeros separados por comas: "))
Numeros_Pares=[]
Numeros_Impares=[]
Lista_Numeros=[int(i) for i in Numeros.split(",")]

for N in Lista_Numeros:
    if (N%2==0):
        Numeros_Pares.append(N)
    else:
        Numeros_Impares.append(N)
        
        
print("Numeros pares: ",Numeros_Pares)
print("Numeros Impares: ",Numeros_Impares)
        


