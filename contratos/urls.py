from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contratos, name='lista_contratos'),
    path('nuevo/', views.nuevo_contrato, name='nuevo_contrato'),
    path('<int:pk>/', views.detalle_contrato, name='detalle_contrato'),
    path('<int:pk>/editar/', views.editar_contrato, name='editar_contrato'),
    path('<int:contrato_pk>/adjunto/nuevo/', views.agregar_adjunto, name='agregar_adjunto'),
]