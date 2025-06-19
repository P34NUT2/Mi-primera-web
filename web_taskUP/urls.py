"""
URL configuration for web_taskUP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings#para servir archivos media en desarrollo

urlpatterns = [
    #paths de la app core 
    path('', include('core.urls')),
    #path para la app task 
    path('tasks/', include('tasks.urls')),
    #path del modelo offer
    path('offers/', include('offers.urls')),
    #path de la aplicacion offer
    path('offers/', include('offers.urls')),
    #path del admin
    path('admin/', admin.site.urls),
    #path de la ap registration
    path('registrations/', include('registration.urls')),
    #path de las accounts django por defecto ya la maneja
    path('accounts/', include('django.contrib.auth.urls')),  # Incluye login/logout
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''Ahorita poner y arreglar la task list con el pk y slugliferalo bien'''