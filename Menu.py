import Ahorcado
import Agendaescolar
import Apporiobject
import joc
import scrapping
import webdjango

def menu():
    op = 0
    while op<1 or op>7:
        print("""
            Menu principal:
            1. Listas y números aleatorios (Ahorcado)
            2. Trabajar con ficheros(Agenda escolar)
            3. Juego Sky Jump Mario
            4. App orientada a objetos (Clases de familia)
            5. Scrapping (De la web pokemon)
            6. Server DJANGO
            7. Salida 
            \n
            """)
        op = int(input("Introduce una opción: "))
        if op<1 or op>7:
            print("Opción inválida, vuelve a elegir una opción: \n")
    return op


# Programa principal:
op = 1
while op != 7:
    op = menu()
    match op:
        case 1:
            Ahorcado.jugar_ahorcado()
        case 2:
            Agendaescolar.agenda_escolar()
        case 3:
            joc.joc() 
        case 4:
            Apporiobject.app_orientada_objetos()
        case 5:
            scrapping.funscrapping()
        case 6:
            webdjango.start_server()
        case other:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")


