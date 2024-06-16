import requests # Biblioteca para realizar solicitudes HTTP, en este caso HTTP GET para obtener datos de un servidor.
 
def funscrapping():
    # Hacemos que recorra los 13 idiomas de la página con un for
    for i in range(13):
        # Creamos una URL para cada idioma, incrementando el ID en 1 en cada recorrido
        url = f"https://pokeapi.co/api/v2/language/{i + 1}/"

        # Realizamos una solicitud GET a la URL para solicitar datos de un servidor web
        res = requests.get(url)
        
        # Verificamos si la solicitud fue exitosa comprobando el código de estado
        if res.status_code == 200:

            # Si la solicitud fue exitosa, convertimos la respuesta JSON en un diccionario de Python
            datos = res.json()

            """ Imprimimos los detalles de cada idioma con el ID actual que le corresponde
            Empleo f-string, ya que,contiene variables y expresiones entre llaves "{}" que se sustituyen directamente por su valor."""

            print(f"\n┗━━━━━༻  Detalles del idioma ID {i + 1}༺━━━━━┛ :") # Aclaro que añado el {i + 1} para que ajuste estos valores para que vayan desde 1 hasta 13
            print(f"ID: {datos['id']}")      
            print(f"Abreviación de idioma en ISO: {datos['name']}")
            print(f"Oficial: {datos['official']}")
            print(f"Código ISO 639: {datos['iso639']}")
            print(f"Código ISO 3166: {datos['iso3166']}\n")
            print("El nombre del idioma id en otros idiomas que tiene:")
            
            # Hacemos un recorrido sobre los nombres en otros idiomas y los imprimimos
            for name in datos["names"]:
                print(f"{name['name']} (Idioma: {name['language']['name']})")
            
            # Imprimimos también el URL del idioma correspondiente para completar el apartado
            print(f"El URL del idioma: {url}")
        else:
            # Con el else en el caso de que la solicitud no funcione, imprimimos un mensaje de error
            print(f"No se pudieron obtener los datos del idioma con ID {i + 1}.")
