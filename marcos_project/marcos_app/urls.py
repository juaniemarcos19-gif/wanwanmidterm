from django.urls import path
from . import views

urlpatterns = [
    path('marcos_app/', views.marcos_app, name='marcos_app'),
]