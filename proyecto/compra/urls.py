from django.urls import path
from . import views


urlpatterns = [
    path('',views.compra, name="Comprar"),
]

