# Importar módulos necesarios
import pygame  # Biblioteca para desarrollar juegos
import sys  # Módulo para interactuar con el sistema
import random  # Módulo para generar números aleatorios
import os  # Módulo para interactuar con el sistema operativo
import time  # Módulo para funciones relacionadas con el tiempo

# Variables del juego
impulso_moneda = False  # Estado del impulso de la moneda
game_over = False  # Estado del juego
high_score = 0  # Inicializar la puntuación más alta
desplazamiento = 0  # Desplazamiento de la pantalla
desplazamiento_fondo = 0  # Desplazamiento del fondo
score = 0  # Puntuación del jugador
contador_final = 0  # Contador para el efecto de desvanecimiento
tiempo_inicio_impulso = 0  # Tiempo de inicio del impulso

def juegomario():
    # Inicializar Pygame
    pygame.init()

    # Inicializar mixer para música de fondo
    pygame.mixer.init()

    # Cargar y reproducir música de fondo
    pygame.mixer.music.load('ArchivosSkyjump/Overworld.mp3') # Cargar archivo de música
    pygame.mixer.music.play(-1)  # Reproducir en bucle infinito

    # Cargar música de game over
    try:
        game_over_music = pygame.mixer.Sound('ArchivosSkyjump/muerte.mp3')# Intentar cargar sonido de game over
    except pygame.error as e:
        print(f"Error al cargar la música de game over: {e}")# Imprimir error si no se puede cargar
        pygame.quit()# Salir de Pygame
        exit()# Salir del programa



    # Dimensiones de la ventana del juego
    ANCHO_PANTALLA = 400 
    ALTO_PANTALLA = 600

    # Crear ventana del juego
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption('Jumpy')

    # Establecer la tasa de fotogramas
    reloj = pygame.time.Clock()
    FPS = 60

    # Variables del juego
    UMBRAL_DESPLAZAMIENTO = 200  # Umbral para el desplazamiento de la pantalla
    GRAVEDAD = 1  # Fuerza de gravedad
    MAX_PLATFORMS = 10  # Número máximo de plataformas
    DURACION_IMPULSO = 1  # Duración del impulso en segundos
    velocidad_plataforma = 1  # Factor de velocidad de las plataformas

    # Cargar puntuación más alta desde un archivo
    if os.path.exists('score.txt'):  # Verificar si el archivo existe
        with open('score.txt', 'r') as archivo:  # Abrir el archivo en modo lectura
            high_score = int(archivo.read())  # Leer y convertir a entero



    # Definir colores
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    PANEL = (57, 86, 118)

    # Definir fuentes
    font_small = pygame.font.SysFont('Lucida Sans', 35)
    font_big = pygame.font.SysFont('Lucida Sans', 24)

    # Cargar imágenes
    jumpy_image = pygame.image.load('ArchivosSkyjump/Mario1.png').convert_alpha()  # Imagen del jugador
    jumpy_image_alt = pygame.image.load('ArchivosSkyjump/Mario2astronauta.png').convert_alpha()  # Imagen alternativa del jugador
    bg_images = [  # Lista de imágenes de fondo
        pygame.image.load('ArchivosSkyjump/Fondo0.png').convert_alpha(),
        pygame.image.load('ArchivosSkyjump/Fondoa1.jpg').convert_alpha(),
        pygame.image.load('ArchivosSkyjump/Fondoes2.jpg').convert_alpha(),
        pygame.image.load('ArchivosSkyjump/Fondoes3.jpg').convert_alpha()
    ]
    platform_image = pygame.image.load('ArchivosSkyjump/Suelo.webp').convert_alpha() # Imagen de la plataforma
    coin_image = pygame.image.load('ArchivosSkyjump/Monedalucky.png').convert_alpha() # Imagen de la moneda de salto

    # Función para dibujar texto en la pantalla
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col) # Con esto puedo renderizar el texto
        pantalla.blit(img, (x, y)) # Dibujar el texto en la pantalla

    # Función para dibujar el panel de información superior
    def draw_panel():
        pygame.draw.rect(pantalla, PANEL, (0, 0, ANCHO_PANTALLA, 30)) # Dibujar el fondo del panel
        pygame.draw.line(pantalla, BLANCO, (0, 30), (ANCHO_PANTALLA, 30), 2) # Dibujar la línea inferior del panel esa blanca
        draw_text('SCORE: ' + str(score), font_small, BLANCO, 0, 0) # Con esto dibujar la puntuación

    # Función para dibujar el fondo
    def draw_bg(desplazamiento_fondo):
        if score >= 7000:
            bg_index = 3  # Para cambiar al siguiente fondo si la puntuación llega a 7000
        elif score >= 5000: 
            bg_index = 2  # Para cambiar al siguiente fondo si la puntuación llega a 5000
        elif score >= 3200:
            bg_index = 1  # Para cambiar al siguiente fondo si la puntuación llega a 3200
        else:
            bg_index = 0 # Este ya es el fondo inicial

        pantalla.blit(bg_images[bg_index], (0, 0 + desplazamiento_fondo))
        pantalla.blit(bg_images[bg_index], (0, -600 + desplazamiento_fondo))

    # Función para actualizar la puntuación más alta
    def update_high_score():
        global high_score
        if score > high_score:  # Si la puntuación actual es mayor que la más alta
            high_score = score  # Actualizar la puntuación más alta
            with open('score.txt', 'w') as archivo:  # Abrir el archivo en modo escritura
                archivo.write(str(high_score))  # Escribir la nueva puntuación más alta



    # Clase Player para el jugador
    class Player():
        def __init__(self, x, y):
            self.images = { # Diccionario de imágenes del jugador 
                'default': pygame.transform.scale(jumpy_image, (45, 45)),  # Escalar imagen del jugador
                'alt': pygame.transform.scale(jumpy_image_alt, (45, 45))  # Escalar imagen alternativa del jugador
            }
            self.imagen_actual = 'default' # Imagen actual del jugador
            self.image = self.images[self.imagen_actual]  # Asignar imagen actual
            self.ancho = 25 # Ancho del rectángulo del jugador
            self.alto = 40 # Alto del rectángulo del jugador
            self.rect = pygame.Rect(0, 0, self.ancho, self.alto) # Determinar la hitbox del jugador
            self.rect.center = (x, y) # Posiconar la hitbox del jugador
            self.vel_y = 0 # Velocidad vertical del jugador
            self.flip = False

        # Función que sirve para cambiar la skin del personaje al llegar a los 7000(cuando sale con casco de astronauta Joan)
        def cambiar_imagen(self):
            if score >= 7000:
                self.imagen_actual = 'alt'
            else:
                self.imagen_actual = 'default' # Mantener la imagen por defecto
            self.image = self.images[self.imagen_actual] # Actualizar la imagen

        def mover(self):
            global impulso_moneda, tiempo_inicio_impulso, velocidad_plataforma
            desplazamiento = 0 #Inicializar desplazamiento del jugador
            dx = dy = 0 # Inicializar desplazamientos en x y y

            # Procesar teclas presionadas
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_a]:  # Si se presiona la tecla A
                dx = -10  # Mover a la izquierda
                self.flip = True  # Voltear la imagen
            if teclas[pygame.K_d]:  # Si se presiona la tecla D
                dx = 10  # Mover a la derecha
                self.flip = False  # No voltear la imagen

            # Gravedad
            self.vel_y += GRAVEDAD # Aplicar gravedad al jugador 
            dy += self.vel_y # Esto permite actualizar desplazamiento en y

            # Asegurarse de que el jugador no salga de la pantalla
            if self.rect.left + dx < 0: # Si el jugador va a salir por la izquierda
                dx = -self.rect.left # Ajustar desplazamiento
            if self.rect.right + dx > ANCHO_PANTALLA:  # Si el jugador va a salir por la derecha
                dx = ANCHO_PANTALLA - self.rect.right # Ajustar desplazamiento del jugador

            # Este apartado sirve para verificar  bien las colisiones con plataformas
            for platform in grupo_plataformas:
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.ancho, self.alto):
                    if self.rect.bottom < platform.rect.centery and self.vel_y > 0: # Aqui verifica si el jugador está cayendo sobre la plataforma
                        self.rect.bottom = platform.rect.top # Ajustar posición del jugador
                        dy = 0 # Ajustar desplazamiento en y
                        if impulso_moneda: # Aplicar impulso de salto con la moneda
                            self.vel_y = -30  
                        else:
                            self.vel_y = -20

            # Desplazar la pantalla hacia arriba si el jugador está en la parte superior
            if self.rect.top <= UMBRAL_DESPLAZAMIENTO and self.vel_y < 0:
                desplazamiento = -dy

            # Actualizar la posición del rectángulo
            self.rect.x += dx
            self.rect.y += dy + desplazamiento

            # Actualizar máscara
            self.mask = pygame.mask.from_surface(self.image)

            # Verificar si el impulso de moneda ha terminado
            if impulso_moneda and time.time() - tiempo_inicio_impulso > DURACION_IMPULSO:
                impulso_moneda = False # Terminar el impulso

            return desplazamiento # Sino retornar el desplazamiento

        def draw(self):
            pantalla.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5)) # Dibujar el jugador en la pantalla



    # Clase Platform para las plataformas
    class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y, ancho, moving):
            pygame.sprite.Sprite.__init__(self) # Inicializar la clase base Sprite
            self.image = pygame.transform.scale(platform_image, (ancho, 19)) # Escalar el alto de imagen de la plataforma
            self.moving = moving # Establecer si la plataforma es móvil
            self.move_counter = random.randint(0, 50) #Contador de movimiento aleatorio
            self.direction = random.choice([-1, 1]) # Dirección de movimiento aleatoria
            self.speed = random.randint(1, 1)  #Velocidad de movimiento aleatoria
            self.rect = self.image.get_rect() # Crear rectángulo de la plataforma
            self.rect.x = x # Posición x de la plataforma
            self.rect.y = y # Posición y de la plataforma

        def update(self, desplazamiento):
            if self.moving: # Si la plataforma es móvil
                self.move_counter += 1 # Incrementar contador de movimiento
                self.rect.x += self.direction * self.speed * velocidad_plataforma #Esto me permite actualizar posición x

            if self.move_counter >= 100 or self.rect.left < 0 or self.rect.right > ANCHO_PANTALLA: # Cambiar de dirección cada 100 movimientos
                self.direction *= -1 # Invertir dirección
                self.move_counter = 0 # Reiniciar contador

            self.rect.y += desplazamiento  #Desplazar la plataforma hacia arriba
            # Eliminar la plataforma si está fuera de la pantalla
            if self.rect.top > ALTO_PANTALLA:
                self.kill() 



    # Clase Coin para las monedas
    class Coin(pygame.sprite.Sprite): 
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self) # Inicializar la clase base Sprite
            self.image = pygame.transform.scale(coin_image, (25, 25)) # Escalar la imagen de la moneda
            self.rect = self.image.get_rect() # Crear hitbox de la moneda
            self.rect.center = (x, y) # Posicionar la moneda

        def update(self, desplazamiento): 
            self.rect.y += desplazamiento # Desplazar la moneda hacia arriba
            # Eliminar la moneda si está fuera de la pantalla
            if self.rect.top > ALTO_PANTALLA:
                self.kill()

    # Crear instancia del jugador
    jumpy = Player(ANCHO_PANTALLA // 2, ALTO_PANTALLA - 150) # Posicionar al jugador en el centro inferior al inicio del juego

    # Crear grupos de sprites para las plataformas y monedas
    grupo_plataformas = pygame.sprite.Group()  # Grupo de plataformas
    coin_group = pygame.sprite.Group()  # Grupo de monedas

    # Crear plataforma inicial
    starting_platform = Platform(ANCHO_PANTALLA // 2 - 50, ALTO_PANTALLA - 50, 100, False)
    grupo_plataformas.add(starting_platform) # Añadir la plataforma al grupo


    
    # Función del juego principal
    def game():
        global score, desplazamiento, desplazamiento_fondo, game_over, contador_final, impulso_moneda, tiempo_inicio_impulso, velocidad_plataforma
        run = True # Estado de ejecución del juego
        
        while run: # Bucle principal del juego
            reloj.tick(FPS) # Esto para controlar la tasa de fotogramas
        
        
            if not game_over: # Si el juego no ha terminado
                desplazamiento = jumpy.mover() # Mover al jugador

                # Cambiar la imagen del jugador si es necesario
                jumpy.cambiar_imagen()

                # Dibujar el fondo
                desplazamiento_fondo += desplazamiento # Actualizar desplazamiento del fondo
                if desplazamiento_fondo >= 600: # Reiniciar desplazamiento del fondo
                    desplazamiento_fondo = 0
                draw_bg(desplazamiento_fondo) # Dibujar el fondo

                # Ajustar el factor de velocidad de la plataforma según la puntuación
                if score >= 3200:
                    velocidad_plataforma = 1.5  # Aumentar velocidad después de 3200 puntos
                else:
                    velocidad_plataforma = 1

                # Generar plataformas
                if len(grupo_plataformas) < MAX_PLATFORMS:
                    p_w = random.randint(40, 60) # Ancho aleatorio de la plataforma
                    p_x = random.randint(0, ANCHO_PANTALLA - p_w) # Posición x aleatoria de la plataforma
                    last_platform_y = min([p.rect.y for p in grupo_plataformas])  # obtener la plataforma más alta
                    p_y = last_platform_y - random.randint(80, 120) # Posición y aleatoria de la plataforma
                    p_moving = random.choice([False, score > 3200]) # Determinar si la plataforma es móvil
                    grupo_plataformas.add(Platform(p_x, p_y, p_w, p_moving)) # Añadir plataforma al grupo

                # Generar monedas
                if random.randint(1, 400) == 1:  # 1% de probabilidad de generar una moneda que he visto que al poner 2 o más se llena todo
                    c_x = random.randint(0, ANCHO_PANTALLA - 25)  # Posición x aleatoria de la moneda
                    c_y = random.randint(-600, 0) # Posición y aleatoria de la moneda
                    coin_group.add(Coin(c_x, c_y)) # Añadir moneda al grupo

                grupo_plataformas.update(desplazamiento) # Actualizar plataformas
                coin_group.update(desplazamiento) # Actualizar monedas

                if desplazamiento > 0:
                    score += desplazamiento # Actualizar puntuación

                pygame.draw.line(pantalla, BLANCO, (0, score - high_score + UMBRAL_DESPLAZAMIENTO), (ANCHO_PANTALLA, score - high_score + UMBRAL_DESPLAZAMIENTO), 3) # Dibujar línea de puntuación
                draw_text('HIGH SCORE', font_small, BLANCO, ANCHO_PANTALLA - 130, score - high_score + UMBRAL_DESPLAZAMIENTO) # Dibujar texto de puntuación alta

                grupo_plataformas.draw(pantalla) # Dibujar plataformas
                coin_group.draw(pantalla) # Dibujar monedas
                jumpy.draw()  # Dibujar al jugador
    
                draw_panel() # Dibujar el panel de información

                # Verificar colisiones con monedas
                if pygame.sprite.spritecollide(jumpy, coin_group, True):
                    impulso_moneda = True # Activar impulso de moneda
                    tiempo_inicio_impulso = time.time() # Registrar tiempo de inicio del impulso

                # Con esto verificar si el jugador se ha caído por malo
                if jumpy.rect.top > ALTO_PANTALLA: 
                    game_over = True  # Terminar el juego
                    pygame.mixer.music.pause() # Pausar la música de fondo
                    game_over_music.play(-1)  #Reproducir música de game over
            else: # Si el juego ha terminado
                if contador_final < ANCHO_PANTALLA:
                    contador_final += 5 # Incrementar contador de desvanecimiento
                    for y in range(0, 6, 2):
                        pygame.draw.rect(pantalla, NEGRO, (0, y * 100, contador_final, 100)) # Dibujar rectángulo de cuando pierdes
                        pygame.draw.rect(pantalla, NEGRO, (ANCHO_PANTALLA - contador_final, (y + 1) * 100, ANCHO_PANTALLA, 100))# Dibujar otros rectángulo de cuando pierdes
                else: 
                    draw_text('GAME OVER, APRENDE A JUGAR!', font_big, BLANCO, 70, 200) # Dibujar texto de game over
                    draw_text('SCORE: ' + str(score), font_big, BLANCO, 160, 250) # Dibujar la puntuación final
                    draw_text('Presiona SPACE para reiniciar el juego', font_big, BLANCO, 40, 300) # Dibujar instrucción para jugar de nuevo
                    update_high_score() # Actualizar la puntuación más alta


                    if pygame.key.get_pressed()[pygame.K_SPACE]: # Si se presiona la tecla espacio
                        game_over = False # Reiniciar el estado del juego
                        score = desplazamiento = contador_final = 0 # Reiniciar variables de puntaje
                        jumpy.rect.center = (ANCHO_PANTALLA // 2, ALTO_PANTALLA - 150) # Reposicionar al jugador al inicio
                        grupo_plataformas.empty() # Vaciar/ resetear el grupo de plataformas
                        coin_group.empty() # Vaciar/ resetear  el grupo de monedas
                        grupo_plataformas.add(Platform(ANCHO_PANTALLA // 2 - 50, ALTO_PANTALLA - 50, 100, False)) # Crear la primera plataforma
                        pygame.mixer.music.unpause() # Reanudar la música de fondo
                        game_over_music.stop() # Detener la música de game over
        
            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    update_high_score() # Si se cierra la ventana
                    run = False # Terminar el bucle principal

            pygame.display.update() # Para actualizar la pantalla

    # Configurar la pantalla para el menú
    pantalla = pygame.display.set_mode((400, 600)) # Crear una ventana de 400x600 píxeles como en movil
    pygame.display.set_caption('Sky Jump Mario') # El título del juego

    # Definir colores
    GRAY = (100, 100, 100) # Definir el color gris con valores RGB

    # Configurar la fuente
    font = pygame.font.Font(None, 74) # Crear las letras de star y exit con tamaño 74

    # Cargar imagen de fondo
    background_image = pygame.image.load('ArchivosSkyjump/Fotomenu.png')

    # Opciones del menú 
    menu_options = ['Start', 'Exit'] # Definir las opciones del menú como una lista

    # Función para dibujar el menú
    def draw_menu(selected_index):
        pantalla.blit(background_image, (0, 0)) # Dibujar la imagen de fondo en la pantalla en la posición (0, 0)
        for index, option in enumerate(menu_options): # Iterar sobre las opciones del menú
            if index == selected_index:
                color = BLANCO # Para resaltar la opción seleccionada con color blanco
            else:
                color = GRAY # Las otras opciones se dibujan en color gris
            label = font.render(option, True, color) # Renderizar el texto de la opción
            ancho = label.get_width() # Obtener el ancho del texto renderizado
            alto = label.get_height() # Obtener la altura del texto renderizado
            pos_x = (pantalla.get_width() - ancho) // 2 # Calcular la posición x centrada
            pos_y = (pantalla.get_height() - alto) // 2 + index * 100 # Calcular la posición y, con un espaciado de 100 píxeles entre opciones
            pantalla.blit(label, (pos_x, pos_y))  # Dibujar el texto en la pantalla en la posición calculada

    # Bucle principal del menú
    def skyjumpmario():
        selected_index = 0  # Inicializar el índice de la opción seleccionada en 0 (primera opción)
        running = True # Variable para mantener el bucle del menú en ejecución

        while running:
            for event in pygame.event.get(): # Iterar sobre los eventos en la cola de eventos
                if event.type == pygame.QUIT: # Si se cierra la ventana
                    pygame.quit() # Salir de Pygame
                    sys.exit() # Salir del programa

                elif event.type == pygame.KEYDOWN:# Si se presiona una tecla
                    if event.key == pygame.K_UP:  # Si la tecla presionada es la flecha hacia arriba
                        selected_index = (selected_index - 1) % len(menu_options) # Mover la selección hacia arriba, con wrap-around
                    elif event.key == pygame.K_DOWN: # Si la tecla presionada es la flecha hacia abajo
                        selected_index = (selected_index + 1) % len(menu_options) # Mover la selección hacia abajo, con wrap-around
                    elif event.key == pygame.K_RETURN: # Si la tecla presionada es Enter
                        if menu_options[selected_index] == 'Start': # Si la opción seleccionada es 'Start'
                            game() # Llamar a la función del juego principal
                        elif menu_options[selected_index] == 'Exit':
                            pygame.quit() # Salir de Pygame
                            sys.exit() # Salir del programa

            draw_menu(selected_index) # Dibujar el menú con la opción actualmente seleccionada
            pygame.display.update() # Actualizar la pantalla para mostrar los cambios
    # Si el script se ejecuta directamente (no importado como módulo)
    skyjumpmario()

def ex7():
    juegomario()