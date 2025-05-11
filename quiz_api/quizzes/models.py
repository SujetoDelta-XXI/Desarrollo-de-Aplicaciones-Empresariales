from django.db import models
# from django.contrib.postgres.fields import ArrayField # Si usas PostgreSQL

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # --- ESTOS SON LOS CAMPOS IMPORTANTES EN EL MODELO QUIZ ---
    category_id_external = models.IntegerField(
        null=True,
        blank=True,
        help_text="ID de la Categoría desde el servicio externo"
    )

    # Opción 1: ArrayField (PostgreSQL)
    # tag_ids_external = ArrayField(
    #     models.IntegerField(),
    #     blank=True,
    #     default=list,
    #     help_text="Lista de IDs de Etiquetas desde el servicio externo"
    # )

    # Opción 2: CharField (para otras DBs o si prefieres string)
    tag_ids_external = models.CharField(
        max_length=500, # Ajusta según necesidad
        blank=True,
        default="", # O null=True, default=None
        help_text="Lista de IDs de Etiquetas (separados por comas) desde el servicio externo"
    )
    # --- FIN DE LOS CAMPOS IMPORTANTES ---

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text[:50]} - {self.text[:50]}"