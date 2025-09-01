from django.urls import path
from inicio.views import inicio, crear_aerosol, lista_aerosoles

urlpatterns = [
    path('', inicio, name='inicio'),
    path('aerosoles/crear/', crear_aerosol, name='crear_aerosol'),
    path('aerosoles/', lista_aerosoles, name='lista_aerosoles' ),
]