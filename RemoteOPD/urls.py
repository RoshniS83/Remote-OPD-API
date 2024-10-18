"""
URL configuration for RemoteOPD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
          openapi.Info(
                    title='Remote OPD API',
                    default_version='',
                    description='',
          ),
          public=True,
          permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
          path('admin/', admin.site.urls),
          path('api/patient/', include('Patient.urls')),
          path('api/user/', include('User.urls')),
          path('api/disease/', include('disease.urls')),
          path('api/villages/', include('villages.urls')),
          path('api/medicines/', include('medicines.urls')),
          path('api/camps/', include('camps.urls')),
          path('api/hbcamp/', include('hbcamp.urls')),
          path('api/eyecamp/', include('eyecamp.urls')),
          path('api/client/', include('Client.urls')),
          path('api/adcamp/', include('adcamp.urls')),
          path('api/megacamp/', include('megacamp.urls')),
          path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
          urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
