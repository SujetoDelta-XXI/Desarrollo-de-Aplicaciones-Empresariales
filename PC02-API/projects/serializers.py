# serializers.py
from rest_framework import serializers
from .models import Evento, Ubicacion, Registro

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer(read_only=True)
    ubicacion_id = serializers.PrimaryKeyRelatedField(
        queryset=Ubicacion.objects.all(), source='ubicacion', write_only=True
    )

    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'descripcion', 'fecha', 'precio', 'ubicacion', 'ubicacion_id']

class RegistroSerializer(serializers.ModelSerializer):
    evento = EventoSerializer(read_only=True)
    evento_id = serializers.PrimaryKeyRelatedField(
        queryset=Evento.objects.all(), source='evento', write_only=True
    )

    class Meta:
        model = Registro
        fields = ['id', 'nombre_participante', 'correo', 'asistencia_confirmada', 'evento', 'evento_id']
