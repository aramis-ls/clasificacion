from django.urls import path

from productos import views

app_name ='productos'
urlpatterns = [
    path('',views.productos, name= 'Productos'),
]