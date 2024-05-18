def app_orientada_objetos():
    # Definimos la clase base Primera_generacion
    class Primera_generacion:
        def __init__(self, nombre, familia):
            # Inicializamos los atributos nombre y familia
            self.nombre = nombre
            self.familia = familia

        def getnombre(self):
            pass
        def getfamilia(self):
            pass

    # Clase Bisabuelo que hereda de Primera_generacion
    class Bisabuelo(Primera_generacion):
        def getnombre(self):
            print("Soy Manolo")

        def getfamilia(self):
            print("Soy tu bisabuelo, soy de la primera generación\n")

    # Clase Bisabuela que hereda de Primera_generacion
    class Bisabuela(Primera_generacion):
        def getnombre(self):
            print("Soy Manoli")

        def getfamilia(self):
            print("Soy tu bisabuela, soy de la primera generación\n")

    # Clase Segunda_generacion que hereda de Primera_generacion
    class Segunda_generacion(Primera_generacion):
        def __init__(self, nombre, familia):
            super().__init__(nombre, familia)

        def getnombre(self):
            pass
        def getfamilia(self):
            pass

    # Clase Abuelo que hereda de Segunda_generacion
    class Abuelo(Segunda_generacion):
        def getnombre(self):
            print("Soy Joaquin")

        def getfamilia(self):
            print("Soy tu abuelo, soy de la segunda generación\n")

    # Clase Abuela que hereda de Segunda_generacion
    class Abuela(Segunda_generacion):
        def getnombre(self):
            print("Soy Pepa")

        def getfamilia(self):
            print("Soy tu abuela, soy de la segunda generación \n")

    # Clase Tercera_generacion que hereda de Segunda_generacion
    class Tercera_generacion(Segunda_generacion):
        def __init__(self, nombre, familia):
            super().__init__(nombre, familia)

        def getnombre(self):
            pass
        def getfamilia(self):
            pass

    # Clase Tio que hereda de Tercera_generacion
    class Tio(Tercera_generacion, Segunda_generacion):
        def __init__(self, nombre, familia):
            super().__init__(nombre, familia)

        def getnombre(self):
            print("Soy Jorge")

        def getfamilia(self):
            print("Soy tu tío, soy de la tercera generación pero como soy mucho más mayor que tu padre me siento de la segunda\n")

    # Clase Padre que hereda de Tercera_generacion
    class Padre(Tercera_generacion):
        def getnombre(self):
            print("Soy Paco")

        def getfamilia(self):
            print("Soy tu padre, soy de la tercera generación, mi hermano es un vejestorio\n")

    # Clase Madre que hereda de Tercera_generacion
    class Madre(Tercera_generacion):
        def getnombre(self):
            print("Soy Sonia")

        def getfamilia(self):
            print("Soy tu madre, soy de la tercera generación \n")

    # Clase Cuarta_generacion que hereda de Tercera_generacion
    class Cuarta_generacion(Tercera_generacion):
        def __init__(self, nombre, familia):
            super().__init__(nombre, familia)

        def getnombre(self):
            pass
        def getfamilia(self):
            pass

    # Clase Hermana que hereda de Cuarta_generacion
    class Hermana(Cuarta_generacion):
        def getnombre(self):
            print("Soy Sara")

        def getfamilia(self):
            print("Soy tu hermana, soy de la cuarta generación, como tú \n")

    # Clase Primo que hereda de Cuarta_generacion
    class Primo(Cuarta_generacion):
        def getnombre(self):
            print("Soy Matias")

        def getfamilia(self):
            print("Soy tu primo, soy de la cuarta generación, como tú")

    # Creación de instancias para prueba

    # Instancia de Bisabuelo
    bisabuelo = Bisabuelo("Manolo", "Familia")
    bisabuelo.getnombre()  
    bisabuelo.getfamilia()  

    # Instancia de Bisabuela
    bisabuela = Bisabuela("Manoli", "Familia")
    bisabuela.getnombre()  
    bisabuela.getfamilia()  

    # Instancia de Abuelo
    abuelo = Abuelo("Joaquin", "Familia")
    abuelo.getnombre()  
    abuelo.getfamilia()  

    # Instancia de Abuela
    abuela = Abuela("Pepa", "Familia")
    abuela.getnombre()  
    abuela.getfamilia()  

    # Instancia de Tio
    tio = Tio("Jorge", "Familia")
    tio.getnombre()  
    tio.getfamilia()  

    # Instancia de Padre
    padre = Padre("Paco", "Familia")
    padre.getnombre()  
    padre.getfamilia()  

    # Instancia de Madre
    madre = Madre("Sonia", "Familia")
    madre.getnombre()  
    madre.getfamilia()  

    # Instancia de Hermana
    hermana = Hermana("Sara", "Familia")
    hermana.getnombre()  
    hermana.getfamilia()  

    # Instancia de Primo
    primo = Primo("Matias", "Familia")
    primo.getnombre()  
    primo.getfamilia()  

# No llamo a la función ya que eso se hace en el programa principal del menu con Apporiobject.app_orientada_objetos() en el case 4