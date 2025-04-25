from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import Contrato, ArchivoAdjunto, HistorialContrato
from .forms import ContratoForm, ArchivoAdjuntoForm

@login_required
def lista_contratos(request):
    contratos = Contrato.objects.all().order_by('-fecha_creacion')
    return render(request, 'contratos/lista_contratos.html', {'contratos': contratos})

@login_required
def detalle_contrato(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    adjuntos = contrato.adjuntos.all()
    historial = contrato.historial.all()
    return render(request, 'contratos/detalle_contrato.html', {
        'contrato': contrato,
        'adjuntos': adjuntos,
        'historial': historial
    })

@login_required
def nuevo_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            contrato = form.save(commit=False)
            contrato.creado_por = request.user
            contrato.save()
            
            # Registrar en historial
            HistorialContrato.objects.create(
                contrato=contrato,
                usuario=request.user,
                descripcion_cambio="Creación del contrato"
            )
            
            return redirect('detalle_contrato', pk=contrato.pk)
    else:
        form = ContratoForm()
    
    return render(request, 'contratos/form_contrato.html', {'form': form, 'accion': 'Nuevo'})

@login_required
def editar_contrato(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    
    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            # Guardar los valores anteriores para el historial
            cambios = []
            for campo in form.changed_data:
                valor_anterior = getattr(contrato, campo)
                valor_nuevo = form.cleaned_data[campo]
                cambios.append(f"{campo}: {valor_anterior} → {valor_nuevo}")
            
            contrato = form.save()
            contrato.actualizar_estado()
            
            # Registrar en historial si hubo cambios
            if cambios:
                HistorialContrato.objects.create(
                    contrato=contrato,
                    usuario=request.user,
                    descripcion_cambio="Modificación: " + ", ".join(cambios)
                )
            
            return redirect('detalle_contrato', pk=contrato.pk)
    else:
        form = ContratoForm(instance=contrato)
    
    return render(request, 'contratos/form_contrato.html', {'form': form, 'contrato': contrato, 'accion': 'Editar'})

@login_required
def agregar_adjunto(request, contrato_pk):
    contrato = get_object_or_404(Contrato, pk=contrato_pk)
    
    if request.method == 'POST':
        form = ArchivoAdjuntoForm(request.POST, request.FILES)
        if form.is_valid():
            adjunto = form.save(commit=False)
            adjunto.contrato = contrato
            adjunto.save()
            
            # Registrar en historial
            HistorialContrato.objects.create(
                contrato=contrato,
                usuario=request.user,
                descripcion_cambio=f"Archivo adjunto añadido: {adjunto.nombre}"
            )
            
            return redirect('detalle_contrato', pk=contrato.pk)
    else:
        form = ArchivoAdjuntoForm()
    
    return render(request, 'contratos/form_adjunto.html', {'form': form, 'contrato': contrato})