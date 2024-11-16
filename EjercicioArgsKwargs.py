import threading #Librería threading para trabajar con hilos
import time #Librería time para simular la pausa
import random #Librería random para generar números aleatorios

#Función para procesar la información de un usuario
def procesarUsuario(id, **datos):
    #Sumulamos la pausa entre 0.2 y 2.5 segundos
    time.sleep(random.uniform(0.2, 2.5))
    #Imprimimos la información del usuario
    print(f"Usuario ID: {id}, Nombre: {datos.get("nombre")}, Edad: {datos.get("edad")}")

#Lisa de usuarios con sus datos
usuarios = [(1, "Ana", 30),
            (2, "Carlos", 22),
            (3, "Beatriz", 27),
            (4, "David", 35),
            (5, "Elena", 29),]

#Lista para almacenar los hilos
hilos = []

#Bucle para recorrer cada usuario
for usuario in usuarios:
    #Convertimos cada usuario en una lista para poder acceder a los elementos
    datosUsuario = list(usuario)

    #Creamos un hilo pasando como parámetros los datos del usuario
    hilo = threading.Thread(target=procesarUsuario, args=(datosUsuario[0],), kwargs={"nombre": datosUsuario[1], "edad": datosUsuario[2]})
    
    hilos.append(hilo) #Agregamos el hilo a la lista de hilos
    hilo.start() #Iniciamos el hilo

#Esperamos a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("Todos los hilos han finalizado")