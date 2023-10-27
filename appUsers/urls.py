from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from appUsers import views

router = routers.DefaultRouter()
router.register(r'usuarioadmin', views.UsuarioAdminView, 'usuarioadmin')
router.register(r'usuarioregular', views.UsuarioRegularView, 'usuarioregular')


urlpatterns = [
    path("api/", include(router.urls)),
    path("docs/", include_docs_urls(title="App API")),
]
