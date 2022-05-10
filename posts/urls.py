from django.urls import path
from . import views

urlpatterns = [
    path('', views.listpost),
    path('<int:id>/', views.detailpost),
]
