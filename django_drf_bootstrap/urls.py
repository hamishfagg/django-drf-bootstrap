"""
URL configuration for django_drf_bootstrap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django_drf_bootstrap.user.api import router as user_router
from django_drf_bootstrap.note.api import router as note_router

urlpatterns = [
    # API Docs
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api-docs/",
        SpectacularSwaggerView.as_view(
             url_name="schema"
        ),
        name="",
    ),

    path("admin/", admin.site.urls),
    path("auth/", include('djoser.urls.authtoken')),
    path('', include(user_router.urls)),  # Our user endpoint(s) via Djoser
    path('notes/', include(note_router.urls))
]