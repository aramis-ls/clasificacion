from django.urls import path

from fracciones import views

app_name='fracciones'
urlpatterns = [
    path('',views.lista_fracciones, name= 'Fracciones'),
]