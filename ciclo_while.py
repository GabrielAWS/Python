#Programa que utiliza while y if para el juego "Adivina el número"
import random

print("Bienvenido al juego: ADIVINA EL NÚMERO!")
print("Las reglas son simple: piensa en un número y trata adivinar en cual esta pensando el programa")

numAleatorio = random.randint(1,10) #genera un numero aleatorio entre 1 y 10
valorCorrecto = False #indicador para romper el ciclo

while valorCorrecto != True: # Compara el indicar 
    datoUsuario=input("Adivina un numero entre 1 y 10: ") #se solicita un numero
    if int(datoUsuario)==numAleatorio: #Compara el numero ingresado con el numero aleatorio
        print("Adivinaste {}. Es correcto! Ganaste!".format(datoUsuario)) #imprimir Si es correcto
        valorCorrecto=True#cambia el indicador para romper el ciclo
    else:
        print("Incorrecto. El numero {} no es el que penso la maquina".format(datoUsuario))
        

    
        