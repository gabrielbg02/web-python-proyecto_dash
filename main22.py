import os 
import math

#os.system ('cls')
saluda = 'hola capataz' # str 

while True:
    print ("MENU")
    print ("1-SUMAR")
    print ("2-RESTAR")
    print ("3-MULTIPLICAR")
    print ("4-DIVIDIR")
    opcion = int(input ("opcion a elegir: "))
               
    if opcion == 1:
        numero1 = float(input ("ingrese el primer numero: "))
        numero2 = float(input ("ingrese el segundo numero: "))
        suma = numero1 + numero2
      #hola 
        print (f"el numero sumado es: {suma:.0f}"  )
        break

print ("terminandooo")
os.system ('pause')


"""import os 

while True:
    try:
       
        opcion = int(input("Ingrese una opción: "))
        if opcion < 1 or opcion > 5: # Ajusta el rango según tus opciones
            print("Opción inválida. Ingrese un número entre 1 y 5.")
        else:
            break # Si la opción es válida, salimos del bucle
    except ValueError:
        print("Por favor, ingrese un número entero.")

# Ahora, ejecutamos la acción según la opción seleccionada
if opcion == 1:
    print("Hola, mundo!")"""
