import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

CATEGORY_TAGS_API_BASE_URL = settings.CATEGORY_TAGS_BASE_URL

def _make_category_tags_api_request(method, endpoint, params=None, json_data=None, expected_status_code=None):
    url = f"{CATEGORY_TAGS_API_BASE_URL}{endpoint}"
    try:
        response = requests.request(method, url, params=params, json=json_data, timeout=5)

        if expected_status_code: # Usado para validaciones de existencia simples
            return response.status_code == expected_status_code

        response.raise_for_status() # Lanza HTTPError para respuestas 4xx/5xx en otros casos
        if response.status_code == 204:
            return None
        return response.json()

    except requests.exceptions.HTTPError as e:
        error_message = f"Error HTTP al llamar a API de Category/Tags {method.upper()} {url}: {e.response.status_code}"
        error_detail = e.response.text
        logger.error(f"{error_message} - {error_detail}")
        try:
            error_data = e.response.json()
            if isinstance(error_data, dict):
                error_data['status_code'] = e.response.status_code
            return error_data
        except requests.exceptions.JSONDecodeError:
            return {"error": "HTTP error", "status_code": e.response.status_code, "detail": error_detail}
    except requests.exceptions.RequestException as e:
        logger.error(f"Error de conexión al llamar a API de Category/Tags {method.upper()} {url}: {e}")
        return {"error": "Connection error", "detail": str(e), "status_code": 503}
    except requests.exceptions.JSONDecodeError as e:
        logger.error(f"Error al decodificar JSON de API de Category/Tags {method.upper()} {url}: {e.msg} - Respuesta: {e.doc}")
        return {"error": "Invalid JSON response", "detail": str(e), "status_code": 500}


def category_exists_in_category_tags_api(category_id):
    if not category_id:
        return False # O True si es opcional y null es válido
    return _make_category_tags_api_request("get", f"categories/{category_id}/", expected_status_code=200)

def tags_exist_in_category_tags_api(tag_ids):
    if not tag_ids:
        return True
    if not isinstance(tag_ids, list) or not all(isinstance(tid, int) for tid in tag_ids):
        logger.warning("tag_ids_external no es una lista válida de enteros.")
        return False
    for tag_id in tag_ids: # Validación individual (mejorar si es posible con endpoint masivo)
        if not _make_category_tags_api_request("get", f"tags/{tag_id}/", expected_status_code=200):
            logger.warning(f"Tag ID {tag_id} no encontrado en API de Category/Tags.")
            return False
    return True

# --- NUEVAS FUNCIONES PARA OBTENER CHOICES ---
def get_all_categories_for_choices():
    """
    Obtiene todas las categorías de la API de category_tags para usarlas como choices.
    Retorna una lista de tuplas [(id, name), ...].
    """
    # Asumimos que el endpoint /categories/ devuelve una lista de objetos
    # o un objeto paginado con una clave 'results'.
    # Para choices, idealmente querrías todos los items, así que la API
    # de category_tags debería soportar un parámetro como ?page_size=all o similar,
    # o este cliente debería manejar la paginación para obtener todos los resultados.
    # Por simplicidad, asumimos que obtenemos una lista manejable.
    data = _make_category_tags_api_request("get", "categories/?page_size=1000") # Pide muchos para evitar paginación simple
    choices = []
    if isinstance(data, list): # Si la respuesta es directamente una lista
        choices = [(item['id'], item['name']) for item in data if 'id' in item and 'name' in item]
    elif isinstance(data, dict) and 'results' in data and isinstance(data['results'], list): # Si es paginado por DRF
        choices = [(item['id'], item['name']) for item in data['results'] if 'id' in item and 'name' in item]
    else:
        logger.error("No se pudieron obtener las categorías para los choices o el formato es inesperado.")

    if not choices: # Si está vacío después de intentar, añade una opción de error o indicación
        return [('', '--------- (No se pudieron cargar categorías) ---------')]
    return [('', '---------')] + choices # Añadir opción vacía para campos no requeridos

def get_all_tags_for_choices():
    """
    Obtiene todos los tags de la API de category_tags para usarlos como choices.
    Retorna una lista de tuplas [(id, name), ...].
    """
    data = _make_category_tags_api_request("get", "tags/?page_size=1000") # Pide muchos
    choices = []
    if isinstance(data, list):
        choices = [(item['id'], item['name']) for item in data if 'id' in item and 'name' in item]
    elif isinstance(data, dict) and 'results' in data and isinstance(data['results'], list):
        choices = [(item['id'], item['name']) for item in data['results'] if 'id' in item and 'name' in item]
    else:
        logger.error("No se pudieron obtener los tags para los choices o el formato es inesperado.")

    if not choices:
        return [('', '--------- (No se pudieron cargar etiquetas) ---------')]
    # Para MultipleChoiceField, no necesitas una opción vacía explícita si `required=False`.
    return choices

def get_category_by_id(category_id):
    if not category_id:
        return None
    logger.debug(f"API Client: Attempting to get category by ID: {category_id}")
    # Asegúrate que el endpoint 'categories/<id>/' exista
    data = _make_category_tags_api_request("get", f"categories/{category_id}/")

    if data and isinstance(data, dict) and not data.get("error"):
        if 'id' in data and 'name' in data:
            logger.debug(f"API Client: Successfully fetched category: {data['name']}")
            return data # Devuelve el objeto completo de la categoría
        else:
            logger.warning(f"API Client: Category data for ID {category_id} is missing 'id' or 'name'. Data: {data}")
            return None
    elif data and data.get("error"):
        logger.error(f"API Client: Error fetching category ID {category_id}: {data.get('detail', data['error'])}")
        return None
    else:
        logger.error(f"API Client: Unexpected response or no data for category ID {category_id}. Data: {data}")
        return None

def get_tags_by_ids(tag_ids_list):
    if not tag_ids_list:
        return []
    
    # Convertir todos los IDs a string para la URL, si no lo son ya
    tag_ids_str_list = [str(tid) for tid in tag_ids_list]

    logger.debug(f"API Client: Attempting to get tags by IDs: {tag_ids_str_list}")
    
    params = {"id__in": ",".join(tag_ids_str_list)}
    data = _make_category_tags_api_request("get", "tags/", params=params)
    tags = []
    if data and isinstance(data, dict) and 'results' in data and isinstance(data['results'], list):
         for item in data['results']:
             if isinstance(item, dict) and 'id' in item and 'name' in item:
                 tags.append(item)
    elif data and isinstance(data, list): # Si no es paginado pero devuelve una lista
          for item in data:
             if isinstance(item, dict) and 'id' in item and 'name' in item:
                 tags.append(item)
    else:
         logger.error(f"API Client: Could not fetch tags by IDs {tag_ids_str_list} or format unexpected. Data: {data}")
    return tags