from django.urls import path
from . import views

urlpatterns = [
    # Operaciones relacionadas a laboratorios y reservaciones
    path('laboratorios/', views.lista_laboratorios, name='lista_laboratorios'),
    path('laboratorios/<int:lab_id>/', views.horario_laboratorio, name='horario_laboratorio'),
    path('laboratorios/<int:lab_id>/reservar/', views.crear_reserva, name='crear_reserva'),
    
    # CRUD para las reservaciones propias
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/<int:reserva_id>/editar/', views.actualizar_reserva, name='actualizar_reserva'),
    path('reservas/<int:reserva_id>/eliminar/', views.eliminar_reserva, name='eliminar_reserva'),
]
