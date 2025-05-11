# category_tags/quizzes_api_client.py
import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

# Esta URL base DEBE apuntar a la API original de quizzes (API 1)
QUIZZES_API_BASE_URL = settings.QUIZZES_API_BASE_URL # Asumiendo que QUIZZES_API_BASE_URL apunta a la API de quizzes

def _make_quizzes_api_request(method, endpoint, params=None, json_data=None):
    url = f"{QUIZZES_API_BASE_URL}{endpoint}"
    try:
        response = requests.request(method, url, params=params, json=json_data, timeout=5)
        response.raise_for_status()
        if response.status_code == 204:
            return None
        return response.json()
    except requests.exceptions.HTTPError as e:
        error_message = f"Error HTTP al llamar a API de Quizzes {method.upper()} {url}: {e.response.status_code}"
        error_detail = e.response.text
        logger.error(f"{error_message} - {error_detail}")
        try:
            return e.response.json()
        except requests.exceptions.JSONDecodeError:
            return {"error": "HTTP error", "status_code": e.response.status_code, "detail": error_detail}
    except requests.exceptions.RequestException as e:
        logger.error(f"Error de conexión al llamar a API de Quizzes {method.upper()} {url}: {e}")
        return {"error": "Connection error", "detail": str(e)}
    except requests.exceptions.JSONDecodeError as e:
        logger.error(f"Error al decodificar JSON de API de Quizzes {method.upper()} {url}: {e.msg} - Respuesta: {e.doc}")
        return {"error": "Invalid JSON response", "detail": str(e)}

def get_quizzes_from_quizzes_api(params=None):
    return _make_quizzes_api_request("get", "quizzes/", params=params)

def get_quiz_detail_from_quizzes_api(quiz_id):
    return _make_quizzes_api_request("get", f"quizzes/{quiz_id}/")

def submit_quiz_answers_to_quizzes_api(quiz_id, answers_payload):
    return _make_quizzes_api_request("post", f"quizzes/{quiz_id}/validate/", json_data={"answers": answers_payload})