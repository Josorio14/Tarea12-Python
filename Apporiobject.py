def app_orientada_objetos():
    class Primera_generacion:
        def __init__(self, nombre, familia):
            self.nombre = nombre
            self.familia = familia

        def getnombre(self):
            pass

        def getfamilia(self):
            pass

    class Bisabuelo(Primera_generacion):
        def getnombre(self):
            print("Soy Manolo")

        def getfamilia(self):
            print("Soy tu bisabuelo, soy de la primera generación")

    class Bisabuela(Primera_generacion):
        def getnombre(self):
            print("Soy Manoli")

        def getfamilia(self):
            print("Soy tu bisabuela, soy de la primera generación")

    class Segunda_generacion(Primera_generacion):
        def __init__(self, nombre, familia):
            super().__init__(nombre, familia)

        def getnombre(self):
            pass

        def getfamilia(self):
            pass

    class Abuelo(Segunda_generacion):
        def getnombre(self):
            print("Soy Joaquin")

        def getfamilia(self):
            print("Soy tu abuelo, soy de la segunda generación")

    class Abuela(Segunda_generacion):
        def getnombre(self):
            print("Soy Pepa")

        def getfamilia(self):
            print("Soy tu abuela, soy de la segunda generación")

    class Tercera_generacion(Segunda_generacion):
        def __init__(self, nombre, familia):
            super().__init__(nombre, familia)

        def getnombre(self):
            pass

        def getfamilia(self):
            pass

    class Tio(Tercera_generacion):
        def __init__(self, nombre, familia):
            super().__init__(nombre, familia)

        def getnombre(self):
            print("Soy Jorge")

        def getfamilia(self):
            print("Soy tu tío, soy de la tercera generación pero como soy mucho más mayor que tu padre me siento de la segunda")

    class Padre(Tercera_generacion):
        def getnombre(self):
            print("Soy Paco")

        def getfamilia(self):
            print("Soy tu padre, soy de la tercera generación, mi hermano es un vejestorio")

    class Madre(Tercera_generacion):
        def getnombre(self):
            print("Soy Sonia")

        def getfamilia(self):
            print("Soy tu madre, soy de la tercera generación")

    class Cuarta_generacion(Tercera_generacion):
        def __init__(self, nombre, familia):
            super().__init__(nombre, familia)

        def getnombre(self):
            pass

        def getfamilia(self):
            pass

    class Hermana(Cuarta_generacion):
        def getnombre(self):
            print("Soy Sara")

        def getfamilia(self):
            print("Soy tu hermana, soy de la cuarta generación, como tú")

    class Primo(Cuarta_generacion):
        def getnombre(self):
            print("Soy Matias")

        def getfamilia(self):
            print("Soy tu primo, soy de la cuarta generación, como tú")

    # Creación de instancias para prueba
    bisabuelo = Bisabuelo("Manolo", "Familia")
    bisabuelo.getnombre()
    bisabuelo.getfamilia()

    bisabuela = Bisabuela("Manoli", "Familia")
    bisabuela.getnombre()
    bisabuela.getfamilia()

    abuelo = Abuelo("Joaquin", "Familia")
    abuelo.getnombre()
    abuelo.getfamilia()

    abuela = Abuela("Pepa", "Familia")
    abuela.getnombre()
    abuela.getfamilia()

    tio = Tio("Jorge", "Familia")
    tio.getnombre()
    tio.getfamilia()

    padre = Padre("Paco", "Familia")
    padre.getnombre()
    padre.getfamilia()

    madre = Madre("Sonia", "Familia")
    madre.getnombre()
    madre.getfamilia()

    hermana = Hermana("Sara", "Familia")
    hermana.getnombre()
    hermana.getfamilia()

    primo = Primo("Matias", "Familia")
    primo.getnombre()
    primo.getfamilia()

app_orientada_objetos()
