# Importar las librerías necesarias
import pygame
import sys
import subprocess  # Necesario para ejecutar otro archivo Python

# Inicializar Pygame
pygame.init()  # Inicializa todos los módulos de Pygame.

# Configurar la pantalla
screen = pygame.display.set_mode((400, 600))  # Crea una ventana de 800x600 píxeles.
pygame.display.set_caption('Menú Principal')  # Establece el título de la ventana.

# Definir colores
WHITE = (255, 255, 255)  # Define el color blanco.
GRAY = (100, 100, 100)   # Define el color gris.

# Configurar la fuente
font = pygame.font.Font(None, 74)  # Carga una fuente con tamaño 74. 'None' usa la fuente por defecto.

# Cargar imagen de fondo
background_image = pygame.image.load('background.png')  # Carga una imagen llamada 'background.png'.

# Opciones del menú
menu_options = ['Start', 'Exit']  # Lista con las opciones del menú.

# Función para dibujar el menú
def draw_menu(selected_index):
    screen.blit(background_image, (0, 0))  # Dibuja la imagen de fondo en la posición (0, 0).
    for index, option in enumerate(menu_options):  # Itera sobre las opciones del menú.
        if index == selected_index:  # Si la opción está seleccionada...
            color = WHITE  # ...la dibuja en blanco.
        else:  # Si no...
            color = GRAY  # ...la dibuja en gris.
        label = font.render(option, True, color)  # Renderiza el texto de la opción.
        width = label.get_width()  # Obtiene el ancho del texto renderizado.
        height = label.get_height()  # Obtiene el alto del texto renderizado.
        pos_x = (screen.get_width() - width) // 2  # Calcula la posición x centrada.
        pos_y = (screen.get_height() - height) // 2 + index * 100  # Calcula la posición y, con separación vertical.
        screen.blit(label, (pos_x, pos_y))  # Dibuja el texto en la pantalla.

# Bucle principal
def main():
    selected_index = 0  # Índice de la opción actualmente seleccionada.
    running = True  # Variable para mantener el bucle corriendo.

    while running:  # Bucle principal del juego.
        for event in pygame.event.get():  # Itera sobre los eventos.
            if event.type == pygame.QUIT:  # Si el evento es cerrar la ventana...
                pygame.quit()  # ...cierra Pygame...
                sys.exit()  # ...y sale del programa.
            elif event.type == pygame.KEYDOWN:  # Si se presiona una tecla...
                if event.key == pygame.K_UP:  # Si la tecla es la flecha arriba...
                    selected_index = (selected_index - 1) % len(menu_options)  # ...mueve la selección hacia arriba.
                elif event.key == pygame.K_DOWN:  # Si la tecla es la flecha abajo...
                    selected_index = (selected_index + 1) % len(menu_options)  # ...mueve la selección hacia abajo.
                elif event.key == pygame.K_RETURN:  # Si la tecla es Enter...
                    if menu_options[selected_index] == 'Start':  # ...y la opción seleccionada es 'Start'...
                        subprocess.call(["python3", "skyjump.py"])  # Ejecuta el archivo skyjump.py
                    elif menu_options[selected_index] == 'Exit':  # ...y la opción seleccionada es 'Exit'...
                        pygame.quit()  # ...cierra Pygame...
                        sys.exit()  # ...y sale del programa.

        draw_menu(selected_index)  # Llama a la función para dibujar el menú.
        pygame.display.update()  # Actualiza la pantalla con lo que se ha dibujado.

if __name__ == "__main__":
    main()  # Llama a la función principal si el script se está ejecutando directamente.

