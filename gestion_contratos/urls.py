from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from usuarios.views import login_view, registro_usuario, lista_usuarios
from dashboard.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    
    # Autenticación
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # Usuarios
    path('usuarios/', include([
        path('', lista_usuarios, name='lista_usuarios'),
        path('nuevo/', registro_usuario, name='registro_usuario'),
    ])),
    
    # Contratos
    path('contratos/', include('contratos.urls')),
]

# Servir archivos media durante desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)