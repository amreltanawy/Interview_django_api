"""MLWrapper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

API_INFO = openapi.Info(
    title="genify Task Api",
    default_version='v1.1.3',
    description="Interview Task Api",
)
SchemaView = get_schema_view(API_INFO, public=True)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', SchemaView.without_ui(cache_timeout=0)),
    path('swagger/', login_required(SchemaView.with_ui('swagger', cache_timeout=1))),
    path('redoc/', login_required(SchemaView.with_ui('redoc', cache_timeout=1))),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),   
    path('', include('django.contrib.auth.urls')),
]
