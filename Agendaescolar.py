import os
import json

# Función para cargar la lista de asignaturas y tareas desde un archivo JSON
def cargar_lista_asignaturas():
    lista_asignaturas = []  # Inicializa una lista vacía para almacenar las asignaturas y tareas
    if os.path.exists("lista_asignaturas.json"):  # Verifica si el archivo JSON existe en el directorio actual
        with open("lista_asignaturas.json", "r") as file:  # Abre el archivo JSON en modo de lectura
            lista_asignaturas = json.load(file)  # Carga los datos del archivo JSON en la lista
    return lista_asignaturas  # Devuelve la lista de asignaturas y tareas


# Función para guardar la lista de asignaturas y tareas en un archivo JSON
def guardar_lista_asignaturas(lista_asignaturas):
    with open("lista_asignaturas.json", "w") as file:  # Abre el archivo JSON en modo de escritura
        json.dump(lista_asignaturas, file)  # Escribe la lista de asignaturas y tareas en el archivo JSON

# Función para mostrar la lista de asignaturas y tareas
def mostrar_lista_asignaturas(lista_asignaturas):
    print("\n ┗━━━━━༻  Lista de Asignaturas y Tareas ༺━━━━━┛ ")
    for i, asignatura in enumerate(lista_asignaturas, 1):  # Enumera las asignaturas y tareas con un índice
        print(f"{i}. Asignatura: {asignatura['asignatura']}, Tarea: {asignatura['tarea']}")
    print()

# Función para agregar una tarea a una asignatura
def agregar_tarea(lista_asignaturas, asignatura, tarea):
    lista_asignaturas.append({"asignatura": asignatura, "tarea": tarea})  # Agrega la nueva tarea a la lista de asignaturas y tareas
    guardar_lista_asignaturas(lista_asignaturas)  # Guarda la lista actualizada en el archivo JSON
    print("Tarea agregada correctamente.")

# Función para eliminar una tarea de una asignatura
def eliminar_tarea(lista_asignaturas, numero_orden):
    if numero_orden <= len(lista_asignaturas) and numero_orden > 0:  # Verifica si el número de orden está dentro del rango válido
        del lista_asignaturas[numero_orden - 1]  # Elimina la tarea correspondiente al número de orden
        guardar_lista_asignaturas(lista_asignaturas)  # Guarda la lista actualizada en el archivo JSON
        print("Tarea eliminada correctamente.")
    else:
        print("Número de orden no válido.")

# Función principal que muestra el menú y gestiona las opciones
def agenda_escolar():
    lista_asignaturas = cargar_lista_asignaturas()  # Carga la lista de asignaturas y tareas al iniciar el programa

    while True:
        print("\n ┗━━━━━༻  Lista de Asignaturas y Tareas ༺━━━━━┛ \n")
        print("1. Mostrar lista de asignaturas y tareas")
        print("2. Agregar tarea a una asignatura")
        print("3. Eliminar tarea de una asignatura")
        print("4. Salir\n")

        opcion = input("\nIngrese el número de su opción: ")

        if opcion == "1":
            mostrar_lista_asignaturas(lista_asignaturas)  # Muestra la lista actual de asignaturas y tareas

        elif opcion == "2":
            asignatura = input("Ingrese el nombre de la asignatura: \n")
            tarea = input("Ingrese la descripción de la tarea: \n")
            agregar_tarea(lista_asignaturas, asignatura, tarea)  # Agrega una nueva tarea a la asignatura especificada

        elif opcion == "3":
            numero_orden = int(input("Ingrese el número de orden de la tarea que desea eliminar:\n"))
            eliminar_tarea(lista_asignaturas, numero_orden)  # Elimina la tarea especificada por el número de orden

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número válido.")


