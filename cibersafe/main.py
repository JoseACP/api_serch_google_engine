from flask import Flask, jsonify
import requests
import os
import json

app = Flask(__name__)

@app.route('/buscar_ciberseguridad', methods=['GET'])
def buscar_ciberseguridad():
    # Ruta para obtener la clave de la API
    api_key_file = os.path.join(os.getcwd(), 'C:\\Users\\x1\\Desktop\\cibersafe\\cibersafe\\API_KEY.txt')
    API_KEY = open(api_key_file).read()

    # Ruta para obtener el ID del motor de búsqueda
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

    # Devuelve la cadena JSON como respuesta de la API
    return jsonify(json_string)

if __name__ == '__main__':
    # Ejecuta la aplicación en el puerto 5000 de forma predeterminada
    app.run(debug=True)
