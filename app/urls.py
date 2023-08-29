from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('converter/', views.converter, name='converter')
]
