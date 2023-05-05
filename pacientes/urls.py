from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.registrar, name="registro"),
    path('list', views.listado, name="listado"),


]
