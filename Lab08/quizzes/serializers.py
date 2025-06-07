from rest_framework import serializers
from .models import Quiz, Question, Choice # Asegúrate que Question y Choice estén definidos en models.py
from . import category_tags_api_client as ct_api_client
import logging

logger = logging.getLogger(__name__)

# --- Serializers para Question y Choice (sin cambios respecto a tu versión) ---
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "question", "text", "is_correct")


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("id", "quiz", "text", "choices")


class QuestionDetailSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("id", "quiz", "text", "choices")

# --- Serializer para Quiz (con lógica para nombres de categoría/etiquetas) ---
class QuizSerializer(serializers.ModelSerializer):
    # --- Campos para ENTRADA de IDs (usados en formularios/creación) ---
    category_id_external_input = serializers.ChoiceField(
        choices=[], # Se poblará en __init__
        required=False,
        allow_null=True,
        allow_blank=True,
        help_text="Selecciona una Categoría (desde el servicio externo).",
        write_only=True, # Solo para entrada, no se muestra en la salida JSON
        source='category_id_external' # Mapea al campo del modelo 'category_id_external'
    )
    tag_ids_external_input = serializers.MultipleChoiceField(
        choices=[], # Se poblará en __init__
        required=False,
        allow_empty=True,
        help_text="Selecciona una o más Etiquetas (desde el servicio externo).",
        write_only=True, # Solo para entrada, no se muestra en la salida JSON
        source='tag_ids_external' # Mapea al campo del modelo 'tag_ids_external'
    )

    # --- Campos para SALIDA (mostrar nombres en JSON) ---
    category_name = serializers.SerializerMethodField(read_only=True)
    tag_names = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Quiz
        fields = [
            'id',
            'title',
            'description',
            # Campos de entrada (no se mostrarán en la salida por write_only=True)
            'category_id_external_input',
            'tag_ids_external_input',
            # Campos de salida con nombres
            'category_name',
            'tag_names',
            # Opcional: Si aún quieres mostrar los IDs en la salida, descomenta/añade:
            # 'category_id_external',
            # 'tag_ids_external',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view = self.context.get('view', None)
        load_choices_for_input_fields = False
        if view and hasattr(view, 'action'):
            if view.action in ['create', 'update', 'partial_update', 'metadata']:
                load_choices_for_input_fields = True
        elif 'request' in self.context and self.context['request'].method == 'OPTIONS':
             load_choices_for_input_fields = True

        if load_choices_for_input_fields:
            try:
                category_choices = ct_api_client.get_all_categories_for_choices()
                self.fields['category_id_external_input'].choices = category_choices
            except Exception as e:
                logger.error(f"Error al poblar category_id_external_input choices: {e}")
                self.fields['category_id_external_input'].choices = [('', 'Error al cargar categorías')]

            try:
                tag_choices = ct_api_client.get_all_tags_for_choices()
                self.fields['tag_ids_external_input'].choices = tag_choices
            except Exception as e:
                logger.error(f"Error al poblar tag_ids_external_input choices: {e}")
                self.fields['tag_ids_external_input'].choices = []

    # --- Métodos para SerializerMethodField (obtener nombres) ---
    def get_category_name(self, obj):
        """Obtiene el nombre de la categoría desde la API externa."""
        if obj.category_id_external: # obj es la instancia de Quiz
            category_data = ct_api_client.get_category_by_id(obj.category_id_external)
            if category_data and isinstance(category_data, dict) and 'name' in category_data:
                return category_data['name']
            logger.warning(f"No se pudo obtener el nombre para category_id_external: {obj.category_id_external} para Quiz ID {obj.id}")
            # Podrías devolver el ID o un mensaje si no se encuentra el nombre
            return f"ID: {obj.category_id_external} (Nombre no encontrado)"
        return None

    def get_tag_names(self, obj):
        """Obtiene los nombres de las etiquetas desde la API externa."""
        tag_ids_to_fetch = []
        # Asumiendo que obj.tag_ids_external es un string de IDs separados por comas (CharField)
        if isinstance(obj.tag_ids_external, str) and obj.tag_ids_external:
            try:
                tag_ids_to_fetch = [int(tid) for tid in obj.tag_ids_external.split(',') if tid.strip()]
            except ValueError:
                logger.error(f"Error al parsear tag_ids_external '{obj.tag_ids_external}' para Quiz ID {obj.id}")
                return ["Error al parsear IDs de etiquetas"]
        # Si fuera ArrayField en el modelo:
        # elif isinstance(obj.tag_ids_external, list):
        #     tag_ids_to_fetch = [int(tid) for tid in obj.tag_ids_external]

        if not tag_ids_to_fetch:
            return []

        tags_data_list = ct_api_client.get_tags_by_ids(tag_ids_to_fetch)
        if tags_data_list:
            names = [tag['name'] for tag in tags_data_list if isinstance(tag, dict) and 'name' in tag]
            if len(names) == len(tag_ids_to_fetch):
                return names
            else: # Si algunos nombres no se encontraron
                logger.warning(f"No se encontraron nombres para todos los tag_ids: {tag_ids_to_fetch} para Quiz ID {obj.id}")
                # Devolver una mezcla o solo los encontrados
                found_names_map = {tag['id']: tag['name'] for tag in tags_data_list if isinstance(tag, dict) and 'id' in tag and 'name' in tag}
                return [found_names_map.get(tid, f"ID: {tid} (Nombre no encontrado)") for tid in tag_ids_to_fetch]

        logger.warning(f"No se pudieron obtener nombres para tag_ids_external: {tag_ids_to_fetch} para Quiz ID {obj.id}")
        return [f"ID: {tid} (Nombre no encontrado)" for tid in tag_ids_to_fetch]


    # --- Validación para los campos _input ---
    def validate_category_id_external_input(self, value):
        """Valida el ID de categoría del input."""
        if value == '' or value is None:
            return None # Permite nulo si el campo del modelo lo permite
        try:
            category_id = int(value)
        except (ValueError, TypeError):
            raise serializers.ValidationError("El ID de categoría debe ser un número.")

        if not ct_api_client.category_exists_in_category_tags_api(category_id):
            raise serializers.ValidationError(f"La categoría con ID {category_id} no existe o no es válida.")
        return category_id # Devuelve el ID como entero

    def validate_tag_ids_external_input(self, value):
        """Valida los IDs de etiquetas del input."""
        if not value: # Lista vacía
            return []
        try:
            tag_ids = [int(tid) for tid in value] # Convertir a lista de enteros
        except (ValueError, TypeError):
            raise serializers.ValidationError("Todos los IDs de etiquetas deben ser numéricos.")

        if not ct_api_client.tags_exist_in_category_tags_api(tag_ids):
            raise serializers.ValidationError("Una o más etiquetas seleccionadas no existen o no son válidas.")
        return tag_ids # Devolver lista de enteros


    # --- Lógica de guardado (create/update) ---
    def _prepare_tag_ids_for_model(self, tag_ids_list_of_ints):
        """
        Prepara la lista de IDs de etiquetas (enteros) para guardarla en el modelo.
        Si el campo del modelo es CharField, convierte la lista a string.
        """
        # Asumiendo que el campo del modelo 'tag_ids_external' es CharField
        if isinstance(tag_ids_list_of_ints, list):
            return ",".join(map(str, tag_ids_list_of_ints))
        return ""

    def create(self, validated_data):
        # 'validated_data' contendrá 'category_id_external' y 'tag_ids_external'
        # gracias al atributo 'source' en los campos _input.
        # 'category_id_external' ya será un int (o None).
        # 'tag_ids_external' será una lista de ints.

        tag_ids_list = validated_data.get('tag_ids_external', [])
        # Convertir la lista de tag_ids (enteros) a string si el modelo usa CharField
        validated_data['tag_ids_external'] = self._prepare_tag_ids_for_model(tag_ids_list)

        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Similar a create, 'validated_data' tendrá los IDs de los campos _input
        # gracias a 'source'.
        if 'tag_ids_external' in validated_data:
            tag_ids_list = validated_data.get('tag_ids_external') # Será una lista de ints
            validated_data['tag_ids_external'] = self._prepare_tag_ids_for_model(tag_ids_list)

        return super().update(instance, validated_data)

# --- Serializer para Detalle de Quiz (hereda y añade preguntas) ---
class QuizDetailSerializer(QuizSerializer): # Hereda la lógica de QuizSerializer (incluyendo los nombres)
    questions = QuestionDetailSerializer(many=True, read_only=True)

    class Meta(QuizSerializer.Meta): # Hereda fields y read_only_fields del padre
        # Asegúrate de que los campos de QuizSerializer.Meta.fields sean los que quieres
        # para el detalle. Si quieres algo diferente, redefine 'fields' aquí.
        current_fields = list(QuizSerializer.Meta.fields)
        # Quitar los campos _input si están, ya que son write_only
        current_fields = [f for f in current_fields if not f.endswith('_input')]
        fields = current_fields + ['questions']


# --- Serializer para Respuestas (sin cambios) ---
class AnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()