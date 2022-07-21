#respuestaUsuario=input("¿Necesitas enviar algún paquete? (Ingresa si o no)")

#if respuestaUsuario == "si":
    #print("¡Podemos ayudar a enviar ese paquete!")
#else:
    #print("Regresa cuando necesites enviar un paquete. ¡Gracias!")

ingreso = input("¿Que te gustaria comprar: dulces, juguetes o comida?") 
respuesta=ingreso.lower()
print(respuesta)

if respuesta=="dulces":
    print("Bienvenido a la tienda de dulces!!")
elif respuesta=="juguetes":
    print("Bienvenido a la tienda de juguetes!!")
elif respuesta=="comida":
    print("Bienvenido al menu de comida!!")
else:
    print("Introduce una opción válida")













