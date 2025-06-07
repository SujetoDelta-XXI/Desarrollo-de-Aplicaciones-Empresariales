from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action # Asegúrate de que esta línea esté si usas @action
from . import quizzes_api_client # Cliente para llamar a la API de quizzes

from .models import Category, Tag # Modelos locales
from .serializers import CategorySerializer, TagSerializer # Serializadores locales

# Nuevos ViewSets para Category y Tag (gestionados por esta app)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Aquí puedes añadir permisos, filtros, etc., específicos para categorías

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # Aquí puedes añadir permisos, filtros, etc., específicos para tags

# El ProxiedQuizViewSet para interactuar con la API de quizzes
class ProxiedQuizViewSet(viewsets.ViewSet):
    """
    Un ViewSet que actúa como proxy para la API de Quizzes original.
    """
    def list(self, request: Request):
        # Recolectar parámetros de la query
        query_params = {}
        category_id_ext = request.query_params.get('category_id_external')
        search_term = request.query_params.get('search')
        page = request.query_params.get('page')
        # Añade otros parámetros que tu API de quizzes pueda esperar
        # como 'ordering', 'tag_ids_external' (si lo implementas)

        if category_id_ext:
            # El cliente espera 'category_id' como nombre del parámetro para la API de quizzes
            # Si la API de quizzes espera 'category_id_external', usa ese nombre aquí.
            # Vamos a asumir que la API de quizzes espera 'category_id_external' para filtrar.
            query_params['category_id_external'] = category_id_ext
        if search_term:
            query_params['search'] = search_term
        if page:
            query_params['page'] = page
        # Ejemplo si quieres pasar tags (la API de quizzes debe soportar esto):
        # tag_ids_ext = request.query_params.getlist('tag_ids_external') # .getlist para múltiples valores
        # if tag_ids_ext:
        #     query_params['tag_ids_external'] = ','.join(tag_ids_ext) # o como la API de quizzes lo espere

        # Llamada al api_client que apunta a la API de quizzes
        # CORRECCIÓN DEL NOMBRE DE LA FUNCIÓN y paso de parámetros
        data = quizzes_api_client.get_quizzes_from_quizzes_api(params=query_params)

        if data and 'error' not in data:
            return Response(data)
        status_code = data.get('status_code', status.HTTP_502_BAD_GATEWAY) if data else status.HTTP_502_BAD_GATEWAY
        return Response(data or {"error": "No se pudo obtener datos de la API de quizzes"}, status=status_code)

    def retrieve(self, request: Request, pk=None):
        # CORRECCIÓN DEL NOMBRE DE LA FUNCIÓN
        data = quizzes_api_client.get_quiz_detail_from_quizzes_api(quiz_id=pk)

        if data and 'error' not in data:
            return Response(data)
        status_code = data.get('status_code', status.HTTP_404_NOT_FOUND) if data else status.HTTP_404_NOT_FOUND
        return Response(data or {"error": "Quiz no encontrado en la API de quizzes"}, status=status_code)

    @action(detail=True, methods=['post'], url_path='validate-answers')
    def validate_answers(self, request: Request, pk=None):
        answers_payload = request.data.get("answers")
        if answers_payload is None:
            return Response({"error": "El campo 'answers' es requerido."}, status=status.HTTP_400_BAD_REQUEST)

        # CORRECCIÓN DEL NOMBRE DE LA FUNCIÓN
        data = quizzes_api_client.submit_quiz_answers_to_quizzes_api(quiz_id=pk, answers_payload=answers_payload)

        if data and 'error' not in data:
            return Response(data)
        status_code = data.get('status_code', status.HTTP_502_BAD_GATEWAY) if data else status.HTTP_502_BAD_GATEWAY
        return Response(data or {"error": "No se pudo procesar la validación con la API de quizzes"}, status=status_code)