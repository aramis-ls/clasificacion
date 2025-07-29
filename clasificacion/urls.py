from django.urls import path

from clasificacion import views

app_name = 'clasificacion'
urlpatterns = [
    path('',views.clasificacion, name= 'Clasificacion'),
]