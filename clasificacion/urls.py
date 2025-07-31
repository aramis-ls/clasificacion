from django.urls import path

from clasificacion import views

app_name = 'clasificacion'
urlpatterns = [
    path('',views.clasificacion_excel, name= 'Clasificacion'),
    path('clasificado/clasificar', views.clasificar_excel, name='Clasificar')
]