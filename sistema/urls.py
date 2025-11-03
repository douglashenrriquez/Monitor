from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/system-info/', views.api_system_info, name='api_system_info'),
]