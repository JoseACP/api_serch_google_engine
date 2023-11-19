import requests
import os
import json

# Leer la clave de la API desde un archivo
api_key_file = os.path.join(os.getcwd(), 'C:\\Users\\x1\\Desktop\\cibersafe\\cibersafe\\API_KEY.txt')
API_KEY = open(api_key_file).read()

# Leer el ID del motor de búsqueda desde un archivo
search_engine_id_file = os.path.join(os.getcwd(), 'C:\\Users\\x1\\Desktop\\cibersafe\\cibersafe\\SEARCH_ENGINE_ID.txt')
SEARCH_ENGINE_ID = open(search_engine_id_file).read()

# Términos de búsqueda
search_query = 'ciberseguridad'

# URL de la API de búsqueda personalizada de Google
url = 'https://customsearch.googleapis.com/customsearch/v1'

# Parámetros de la solicitud HTTP
params = {
    'q': search_query,
    'key': API_KEY,
    'cx': SEARCH_ENGINE_ID,
}

# Realizar la solicitud HTTP
response = requests.get(url, params=params)

# Obtener los resultados en formato JSON
results = response.json()

# Estructura de datos para almacenar los resultados en formato JSON
json_data = {"results": []}

# Verificar si hay resultados en la respuesta JSON
if 'items' in results:
    # Iterar sobre los primeros tres resultados
    for i, result in enumerate(results['items'][:3], 1):
        title = result['title']
        snippet = result['snippet']
        link = result['link']

        # Crear un diccionario para cada resultado
        result_data = {
            "Resultado": i,
            "Título": title,
            "Enlace": link,
            "Texto relacionado con el tema": snippet
        }

        # Agregar el diccionario al listado de resultados
        json_data["results"].append(result_data)

# Convertir el diccionario a una cadena JSON con formato y sin caracteres ASCII
json_string = json.dumps(json_data, indent=4, ensure_ascii=False)

# Imprimir la cadena JSON resultante
print(json_string)
