from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils import timezone
from contratos.models import Contrato, HistorialContrato
from datetime import timedelta

@login_required
def dashboard(request):
    # Estadísticas generales
    total_contratos = Contrato.objects.count()
    contratos_vigentes = Contrato.objects.filter(
        fecha_inicio__lte=timezone.now().date(),
        fecha_fin__gte=timezone.now().date()
    ).count()
    
    # Contratos por vencer (próximos 30 días)
    fecha_limite = timezone.now().date() + timedelta(days=30)
    contratos_por_vencer = Contrato.objects.filter(
        fecha_fin__gt=timezone.now().date(),
        fecha_fin__lte=fecha_limite
    ).order_by('fecha_fin')
    
    # Contratos por tipo
    contratos_por_tipo = Contrato.objects.values('tipo').annotate(
        total=Count('id')
    ).order_by('tipo')
    
    # Actividad reciente
    actividad_reciente = HistorialContrato.objects.all().order_by('-fecha')[:10]
    
    # Contratos recientes
    contratos_recientes = Contrato.objects.all().order_by('-fecha_creacion')[:5]
    
    context = {
        'total_contratos': total_contratos,
        'contratos_vigentes': contratos_vigentes,
        'contratos_por_vencer': contratos_por_vencer,
        'contratos_por_tipo': contratos_por_tipo,
        'actividad_reciente': actividad_reciente,
        'contratos_recientes': contratos_recientes,
    }
    
    return render(request, 'dashboard/index.html', context)