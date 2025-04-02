from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from .models import Usuarios
from .forms import UsuariosForm

def usuarios_list(request):
    usuarios = Usuarios.objects.all()
    
    # Handle filtering
    estado_filter = request.GET.get('estado')
    
    if estado_filter and estado_filter != 'all':
        usuarios = usuarios.filter(estado=estado_filter)
    
    context = {
        'usuarios': usuarios,
        'estado_filter': estado_filter,
    }
    
    return render(request, 'usuarios/usuario_list.html', context)

def usuario_create(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario created successfully!')
            return redirect('usuario_list')
    else:
        form = UsuariosForm()
    
    return render(request, 'usuarios/usuario_form.html', {'form': form})

def usuario_update(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    
    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario updated successfully!')
            return redirect('usuario_list')
    else:
        form = UsuariosForm(instance=usuario)
    
    return render(request, 'usuarios/usuario_form.html', {'form': form})

def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario deleted successfully!')
        return redirect('usuario_list')
    
    return render(request, 'usuarios/usuario_confirm_delete.html', {'usuario': usuario})