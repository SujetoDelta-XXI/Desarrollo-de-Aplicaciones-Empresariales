from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from .models import Laboratorio
from .google_calendar_utils import obtener_eventos  # Si integras Google Calendar
from django.contrib.auth.decorators import login_required
from .models import Reserva
from .forms import ReservaForm


def lista_laboratorios(request):
    labs = Laboratorio.objects.all()
    return render(request, 'reservas/laboratorios_list.html', {'laboratorios': labs})

def horario_laboratorio(request, lab_id):
    laboratorio = get_object_or_404(Laboratorio, pk=lab_id)
    hoy = datetime.utcnow()
    fin = hoy + timedelta(days=7)
    # Obtiene los eventos del calendario personal. El calendar_id en este caso es una dirección de correo o ID.
    eventos = obtener_eventos(laboratorio.calendar_id, hoy, fin)
    return render(request, 'reservas/horario_laboratorio.html', {
        'laboratorio': laboratorio,
        'eventos': eventos
    })

@login_required
def lista_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user).order_by('fecha_inicio')
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})

@login_required
def crear_reserva(request, lab_id):
    laboratorio = get_object_or_404(Laboratorio, pk=lab_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.laboratorio = laboratorio
            # Aquí podrías validar solapamientos o sincronizar con Google Calendar
            reserva.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/form_reserva.html', {'form': form, 'laboratorio': laboratorio})

@login_required
def actualizar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id, usuario=request.user)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            # Aquí, si usas Google Calendar, actualiza el evento
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/form_reserva.html', {'form': form, 'actualizar': True})

@login_required
def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id, usuario=request.user)
    if request.method == 'POST':
        # Aquí, si es necesario, elimina el evento en Google Calendar
        reserva.delete()
        return redirect('lista_reservas')
    return render(request, 'reservas/confirmar_eliminar.html', {'reserva': reserva})