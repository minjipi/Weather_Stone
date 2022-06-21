from django.urls import path
from . import views

urlpatterns = [
    path('', views.control),
    path('pub', views.pub),
]