import random

# Función que muestra paneles de dinujos de la horca según los intentos.
def Dibujo_horca(intentos, palabra):
    if intentos == 0:
        print("  ________    ")
        print(" |/      |    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif intentos == 1:
        print("  ________    ")
        print(" |/      |    ")
        print(" |       😯  Este es Tommy ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")

    elif intentos == 2:
        print("  ________    ")
        print(" |/      |    ")
        print(" |       😦    Tommy esta sorprendido")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")

    elif intentos == 3:
        print("  ________    ")
        print(" |/      |    ")
        print(" |       😧   Tommy esta preocupado ")
        print(" |      /|    ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")

    elif intentos == 4:
        print("  ________    ")
        print(" |/      |    ")
        print(" |       😨    Tommy esta asustado")
        print(" |      /|\   ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")

    elif intentos == 5:
        print("  ________    ")
        print(" |/      |    ")
        print(" |       😰   Tommy esta en peligro ")
        print(" |      /|\   ")
        print(" |      /     ")
        print(" |            ")
        print("_|___         ")

    else:
        print("  ________    ")
        print(" |/      |    ")
        print(" |       😵   Tommy a muerto")
        print(" |      /|\   ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        
    # Para cada nivel de intento, se muestra un dibujo diferente de la horca y una descripción del estado de Tommy

# Función principal del juego del ahorcado
def jugar_ahorcado():
    # Lista de palabras de cuatro letras
    listpalabras = ["nata","casa", "gato", "luna", "pato", "pelo"]
    # Elige una palabra aleatoria de la lista
    palabra_a_adivinar = random.sample(listpalabras, 1)[0]
    # Lista que guarda las letras adivinadas hasta el momento
    letras_adivinadas = ["_"] * len(palabra_a_adivinar)
    # Número máximo de intentos permitidos
    intentos_maximos = 6
    # Contador de intentos
    intentos = 0
    # Lista de letras incorrectas ingresadas por el jugador
    letras_erroneas = []

    print("¡Bienvenido al juego del ahorcado! ¿Serás capaz de salvara Tommy de la horca?")
    print("Adivina la palabra de cuatro letras")
    print(" ".join(letras_adivinadas))  # Muestra las letras adivinadas hasta el momento

    # Bucle que permite al jugador ingresar letras hasta que adivine la palabra o agote los intentos
    while intentos < intentos_maximos:
        # El jugador introduce una letra
        letra = input("Introduce una letra: ")

        # Verifica si se ingresó una única letra minúscula del alfabeto
        if len(letra) != 1 or not letra.islower():
            print("Error, introduce solo una letra minúscula.")
            continue

        # Verifica si la letra ingresada está en la palabra a adivinar
        if letra in palabra_a_adivinar:
            # Actualiza las letras adivinadas con la letra correcta
            for i, a in enumerate(palabra_a_adivinar):
                if a == letra:
                    letras_adivinadas[i] = letra
            print(" ".join(letras_adivinadas))  # Muestra las letras adivinadas hasta el momento
        else:
            # Incrementa el contador de intentos y guarda la letra incorrecta
            intentos += 1
            letras_erroneas.append(letra)
            print("¡Incorrecto! Letras incorrectas:", ", ".join(letras_erroneas))  # Muestra las letras incorrectas
            Dibujo_horca(intentos, palabra_a_adivinar)  # Muestra el dibujo correspondiente a los intentos

        # Verifica si se han adivinado todas las letras de la palabra
        if "_" not in letras_adivinadas:
            print("""  
                       😀
                      / | 👍 !Has salvado a Tommy!
                       ] [
                  ¡Pero bueno estas en tu prime! Has adivinado la palabra, es:""", palabra_a_adivinar)
            return

    # Si se agotan los intentos, muestra el dibujo final de la horca y la palabra correcta
    Dibujo_horca(intentos, palabra_a_adivinar)
    print("\n¡Has agotado tus intentos papanatas! La palabra era:", palabra_a_adivinar)


